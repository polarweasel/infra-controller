#!/usr/bin/env python3

import csv
import json
import re
import subprocess
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

repo = "NVIDIA/infra-controller"
root = Path("/Users/aball/devel/NICo/pw-infra-controller")
input_file = root / "pr_numbers_no_docs.txt"
out_csv = root / "pr_docs_triage.csv"
out_top = root / "pr_docs_triage_top_candidates.txt"

pr_numbers = [int(line.strip()) for line in input_file.read_text().splitlines() if line.strip()]

token = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
HEADERS = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "nico-docs-triage",
}

high_signal_prefixes = [
    "crates/api/",
    "crates/api-model/",
    "crates/rpc/",
    "rest-api/",
    "helm/",
    "deploy/",
    "crates/admin-cli/",
    "crates/admin/",
    "crates/config/",
    "crates/agent/",
    "fern/",
    "book/",
]
ops_signal_prefixes = [
    "deploy/",
    "helm/",
    "helm-prereqs/",
    "dev/",
    "scripts/",
    "rest-api/",
]
noise_prefixes = [
    ".github/",
    "lints/",
    "tests/",
    "test/",
    "dev/",
]

strong_keywords = [
    "add",
    "added",
    "introduce",
    "support",
    "implement",
    "new",
    "enable",
    "feature",
    "endpoint",
    "api",
    "rpc",
    "schema",
    "migration",
    "config",
    "configuration",
    "permission",
    "rbac",
    "security",
    "auth",
    "encryption",
    "default",
    "deprecate",
    "remove",
]
weak_keywords = [
    "update",
    "change",
    "improve",
    "extend",
    "expose",
    "allow",
    "option",
    "toggle",
    "flag",
]
negative_keywords = [
    "test",
    "ci",
    "flake",
    "lint",
    "refactor",
    "cleanup",
    "chore",
    "typo",
    "format",
    "rename only",
]


def get_json(url: str, retries: int = 4):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=35) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="ignore")
            if e.code in (403, 429):
                sleep_for = min(8 * (attempt + 1), 30)
                time.sleep(sleep_for)
                continue
            if e.code == 404:
                return None
            if attempt == retries - 1:
                raise RuntimeError(f"HTTP {e.code}: {body[:200]}")
            time.sleep(2 * (attempt + 1))
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))
    return None


def fetch_pr(pr_number: int):
    pr_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    pr = get_json(pr_url)
    if pr is None:
        return {"pr_number": pr_number, "error": "PR not found"}

    files = []
    page = 1
    while True:
        files_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/files?per_page=100&page={page}"
        batch = get_json(files_url)
        if batch is None:
            break
        if not batch:
            break
        files.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    return {"pr": pr, "files": files}


def score_pr(pr_data):
    pr = pr_data["pr"]
    files = pr_data["files"]
    pr_number = pr["number"]

    title = (pr.get("title") or "").lower()
    body = (pr.get("body") or "").lower()
    merged = pr.get("merged_at") is not None
    labels = [lbl.get("name", "") for lbl in pr.get("labels", [])]
    labels_l = [l.lower() for l in labels]
    filenames = [f.get("filename", "") for f in files]

    score = 0
    signals = []

    # Path-based signals
    if any(name.startswith(tuple(high_signal_prefixes)) for name in filenames):
        score += 3
        signals.append("high-signal-path")
    if any(name.startswith(tuple(ops_signal_prefixes)) for name in filenames):
        score += 2
        signals.append("ops/config-path")
    if any(name.endswith(".proto") for name in filenames):
        score += 4
        signals.append("proto-change")
    if any(name.endswith((".sql", ".toml", ".yaml", ".yml", ".json")) for name in filenames):
        score += 1
        signals.append("config-or-schema-file")
    if any(name.endswith((".md", ".rst")) for name in filenames):
        score -= 1
        signals.append("non-doc-markdown-only-hint")

    # PR text signals
    text_blob = f"{title} {body}"
    strong_hits = sum(1 for k in strong_keywords if re.search(rf"\b{re.escape(k)}\b", text_blob))
    weak_hits = sum(1 for k in weak_keywords if re.search(rf"\b{re.escape(k)}\b", text_blob))
    negative_hits = sum(1 for k in negative_keywords if re.search(rf"\b{re.escape(k)}\b", text_blob))

    if strong_hits:
        add = min(4, strong_hits)
        score += add
        signals.append(f"strong-keywords:{strong_hits}")
    if weak_hits:
        add = min(2, weak_hits)
        score += add
        signals.append(f"weak-keywords:{weak_hits}")
    if negative_hits:
        sub = min(4, negative_hits)
        score -= sub
        signals.append(f"negative-keywords:{negative_hits}")

    # Label signals
    if any(x in labels_l for x in ["feature", "enhancement", "api", "breaking", "security", "bug"]):
        score += 2
        signals.append("high-signal-label")
    if any(x in labels_l for x in ["ci", "test", "chore", "cleanup", "refactor"]):
        score -= 2
        signals.append("low-signal-label")

    # File mix signal
    non_noise = [
        name
        for name in filenames
        if not name.startswith(tuple(noise_prefixes)) and "/test" not in name and name != "Cargo.lock"
    ]
    if len(non_noise) == 0:
        score -= 2
        signals.append("mostly-ci-test-noise")

    if not merged:
        score -= 1
        signals.append("not-merged")

    needs_docs = "yes" if score >= 6 else ("maybe" if score >= 3 else "no")
    confidence = "high" if score >= 8 or score <= 0 else ("medium" if score >= 4 else "low")

    return {
        "pr_number": pr_number,
        "url": pr.get("html_url", ""),
        "title": pr.get("title", ""),
        "state": pr.get("state", ""),
        "merged": merged,
        "author": (pr.get("user") or {}).get("login", ""),
        "created_at": pr.get("created_at", ""),
        "merged_at": pr.get("merged_at", ""),
        "labels": "|".join(labels),
        "files_changed": len(filenames),
        "additions": pr.get("additions", 0),
        "deletions": pr.get("deletions", 0),
        "changed_files_sample": "|".join(filenames[:8]),
        "score": score,
        "needs_docs": needs_docs,
        "confidence": confidence,
        "signals": "|".join(signals),
    }


rows = []
errors = []
with ThreadPoolExecutor(max_workers=10) as ex:
    futures = {ex.submit(fetch_pr, n): n for n in pr_numbers}
    for _, fut in enumerate(as_completed(futures), 1):
        n = futures[fut]
        try:
            data = fut.result()
            if "error" in data:
                errors.append((n, data["error"]))
                continue
            rows.append(score_pr(data))
        except Exception as e:
            errors.append((n, str(e)))

rows.sort(key=lambda r: (-r["score"], r["pr_number"]))

fieldnames = [
    "pr_number",
    "url",
    "title",
    "state",
    "merged",
    "author",
    "created_at",
    "merged_at",
    "labels",
    "files_changed",
    "additions",
    "deletions",
    "changed_files_sample",
    "score",
    "needs_docs",
    "confidence",
    "signals",
]

with out_csv.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

candidates = [r for r in rows if r["needs_docs"] in ("yes", "maybe")]
with out_top.open("w") as f:
    f.write("PRs from pr_numbers_no_docs.txt most likely to need docs updates\n")
    f.write("Sorted by descending heuristic score\n\n")
    for r in candidates[:120]:
        f.write(f"#{r['pr_number']} score={r['score']} needs_docs={r['needs_docs']} confidence={r['confidence']}\n")
        f.write(f"  {r['title']}\n")
        f.write(f"  {r['url']}\n")
        f.write(f"  signals: {r['signals']}\n\n")

count_yes = sum(1 for r in rows if r["needs_docs"] == "yes")
count_maybe = sum(1 for r in rows if r["needs_docs"] == "maybe")
count_no = sum(1 for r in rows if r["needs_docs"] == "no")

print(f"INPUT_PRS={len(pr_numbers)}")
print(f"OUTPUT_ROWS={len(rows)}")
print(f"NEEDS_DOCS_YES={count_yes}")
print(f"NEEDS_DOCS_MAYBE={count_maybe}")
print(f"NEEDS_DOCS_NO={count_no}")
print(f"ERRORS={len(errors)}")
print(f"WROTE_CSV={out_csv}")
print(f"WROTE_TOP={out_top}")
if errors:
    print("FIRST_ERRORS=", errors[:10])
