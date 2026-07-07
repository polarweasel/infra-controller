# PR Docs Triage Script

`pr_docs_triage.py` scores PRs from `pr_numbers_no_docs.txt` to estimate which PRs likely should have included documentation updates.

## Prerequisites

- `python3`
- GitHub CLI (`gh`) authenticated with access to `NVIDIA/infra-controller`

## Input

- `pr_numbers_no_docs.txt` at repo root
  - One PR number per line

## Run

From repo root:

```bash
python3 scripts/pr_docs_triage.py
```

## Outputs

Written at repo root:

- `pr_docs_triage.csv`
  - One row per PR with metadata, heuristic `score`, `needs_docs` (`yes`/`maybe`/`no`), `confidence`, and `signals`
- `pr_docs_triage_top_candidates.txt`
  - Human-readable shortlist of the top `yes`/`maybe` candidates

## Notes

- This is a heuristic triage tool, not a definitive policy check.
- Scoring is based on changed file paths, PR title/body keywords, labels, and basic noise filtering.
