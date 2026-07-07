# pr_docs_triage_top_candidates.md

Source: `pr_docs_triage_top_candidates.txt`

```text
PRs from pr_numbers_no_docs.txt most likely to need docs updates
Sorted by descending heuristic score

#2199 score=14 needs_docs=yes confidence=high
  feat(api): Introduce VPC prefix lifecycle
  https://github.com/NVIDIA/infra-controller/pull/2199
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:8|weak-keywords:2|negative-keywords:1

#2216 score=14 needs_docs=yes confidence=high
  feat: Initial changes for Astra support
  https://github.com/NVIDIA/infra-controller/pull/2216
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2272 score=14 needs_docs=yes confidence=high
  change(rest-api): Align REST API with new VpcPrefix lifecycle
  https://github.com/NVIDIA/infra-controller/pull/2272
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2288 score=14 needs_docs=yes confidence=high
  feat: Surface Flow task report on Task API
  https://github.com/NVIDIA/infra-controller/pull/2288
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2534 score=14 needs_docs=yes confidence=high
  feat: Surface Flow component status, leak status, and override-readiness in REST
  https://github.com/NVIDIA/infra-controller/pull/2534
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:6|weak-keywords:2|negative-keywords:1

#2867 score=14 needs_docs=yes confidence=high
  feat(rest-api): Enhance get all VPC Peering filtering and peer Tenant visibility
  https://github.com/NVIDIA/infra-controller/pull/2867
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|strong-keywords:6|weak-keywords:1|negative-keywords:1

#2877 score=14 needs_docs=yes confidence=high
  fix(dhcp): Guard DHCP lease expiry handling with a feature flag.
  https://github.com/NVIDIA/infra-controller/pull/2877
  signals: high-signal-path|ops/config-path|proto-change|strong-keywords:8|weak-keywords:2|negative-keywords:1

#2967 score=14 needs_docs=yes confidence=high
  Upsert firmware config api
  https://github.com/NVIDIA/infra-controller/pull/2967
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|strong-keywords:9|weak-keywords:1|negative-keywords:1

#2037 score=13 needs_docs=yes confidence=high
  feat: Expose last seen scout version for a machine
  https://github.com/NVIDIA/infra-controller/pull/2037
  signals: high-signal-path|proto-change|config-or-schema-file|strong-keywords:7|weak-keywords:2|negative-keywords:1

#2264 score=13 needs_docs=yes confidence=high
  feat: Add ComponentStatus model in Flow — derive, persist, and surface per-component readiness
  https://github.com/NVIDIA/infra-controller/pull/2264
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2479 score=13 needs_docs=yes confidence=high
  feat: Add operation run foundation
  https://github.com/NVIDIA/infra-controller/pull/2479
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:8|weak-keywords:1|negative-keywords:1

#2500 score=13 needs_docs=yes confidence=high
  feat(librms): `v0.9.0-rc1` for hardware type-specific support
  https://github.com/NVIDIA/infra-controller/pull/2500
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:10|weak-keywords:1|negative-keywords:1

#2666 score=13 needs_docs=yes confidence=high
  feat(zero-dpu): Allow flat VPC's to not belong to a network segment
  https://github.com/NVIDIA/infra-controller/pull/2666
  signals: high-signal-path|proto-change|config-or-schema-file|strong-keywords:6|weak-keywords:3|negative-keywords:1

#2829 score=13 needs_docs=yes confidence=high
  feat(rest-api): Support for adding Tenant information when reported Issue for Delete Instance
  https://github.com/NVIDIA/infra-controller/pull/2829
  signals: high-signal-path|ops/config-path|proto-change|strong-keywords:6|weak-keywords:1|negative-keywords:1

#2844 score=13 needs_docs=yes confidence=high
  feat: Add operation run planning and create RPC
  https://github.com/NVIDIA/infra-controller/pull/2844
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:8|weak-keywords:1|negative-keywords:1

#2861 score=13 needs_docs=yes confidence=high
  feat(zero-dpu): Pass VPC ID to AllocateInstance from REST API
  https://github.com/NVIDIA/infra-controller/pull/2861
  signals: high-signal-path|ops/config-path|proto-change|strong-keywords:6|weak-keywords:1|negative-keywords:1

#2904 score=13 needs_docs=yes confidence=high
  feat: Carbide side changes to support Astra
  https://github.com/NVIDIA/infra-controller/pull/2904
  signals: high-signal-path|ops/config-path|proto-change|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2991 score=13 needs_docs=yes confidence=high
  feat(credential-rotation): stage site-wide credential rotations
  https://github.com/NVIDIA/infra-controller/pull/2991
  signals: high-signal-path|ops/config-path|proto-change|strong-keywords:6|weak-keywords:1|negative-keywords:1

#3018 score=13 needs_docs=yes confidence=high
  feat(api): add host firmware config delete endpoint
  https://github.com/NVIDIA/infra-controller/pull/3018
  signals: high-signal-path|ops/config-path|proto-change|strong-keywords:8|weak-keywords:1|negative-keywords:1

#1803 score=12 needs_docs=yes confidence=high
  feat: add a bypass-state-controller flag to the component management API
  https://github.com/NVIDIA/infra-controller/pull/1803
  signals: high-signal-path|proto-change|strong-keywords:7|weak-keywords:2|negative-keywords:1

#1854 score=12 needs_docs=yes confidence=high
  feat(health): add API support for NVL domain health records
  https://github.com/NVIDIA/infra-controller/pull/1854
  signals: high-signal-path|proto-change|config-or-schema-file|strong-keywords:8|weak-keywords:1|negative-keywords:1

#2043 score=12 needs_docs=yes confidence=high
  feat(api): add admin force-delete for racks
  https://github.com/NVIDIA/infra-controller/pull/2043
  signals: high-signal-path|proto-change|strong-keywords:10|weak-keywords:2|negative-keywords:1

#2133 score=12 needs_docs=yes confidence=high
  feat(dns): cache all negative DNS responses, switch to LRU
  https://github.com/NVIDIA/infra-controller/pull/2133
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:8|weak-keywords:1|negative-keywords:1|high-signal-label

#2151 score=12 needs_docs=yes confidence=high
  Fixes to facilitate move from dpf to non-dpf and vice versa
  https://github.com/NVIDIA/infra-controller/pull/2151
  signals: high-signal-path|proto-change|strong-keywords:6|weak-keywords:3|negative-keywords:1

#2234 score=12 needs_docs=yes confidence=high
  feat(api): Include additional state details in DpuInfo
  https://github.com/NVIDIA/infra-controller/pull/2234
  signals: high-signal-path|proto-change|strong-keywords:7|weak-keywords:2|negative-keywords:1

#2255 score=12 needs_docs=yes confidence=high
  fix: Remove requirement for access token for rms fw update
  https://github.com/NVIDIA/infra-controller/pull/2255
  signals: high-signal-path|proto-change|strong-keywords:8|weak-keywords:2|negative-keywords:1

#2259 score=12 needs_docs=yes confidence=high
  chore(rest-api): Snapshot Core proto, update Machine health override/Rack profile ID refs
  https://github.com/NVIDIA/infra-controller/pull/2259
  signals: high-signal-path|ops/config-path|proto-change|strong-keywords:2|weak-keywords:2|negative-keywords:1

#2610 score=12 needs_docs=yes confidence=high
  feat: Set NTP servers from site config
  https://github.com/NVIDIA/infra-controller/pull/2610
  signals: high-signal-path|proto-change|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:9|weak-keywords:3|negative-keywords:1

#2613 score=12 needs_docs=yes confidence=high
  refactor(vpc): separate Vpc fields into config/status
  https://github.com/NVIDIA/infra-controller/pull/2613
  signals: high-signal-path|proto-change|strong-keywords:9|weak-keywords:2|negative-keywords:1

#2665 score=12 needs_docs=yes confidence=high
  feat: support storing secrets/credentials in Postgres
  https://github.com/NVIDIA/infra-controller/pull/2665
  signals: high-signal-path|proto-change|config-or-schema-file|strong-keywords:11|weak-keywords:1|negative-keywords:1

#2751 score=12 needs_docs=yes confidence=high
  change(api): add dual-stack FNN allocation and IPv6 static-assignment support
  https://github.com/NVIDIA/infra-controller/pull/2751
  signals: high-signal-path|proto-change|config-or-schema-file|strong-keywords:8|weak-keywords:1|negative-keywords:1

#2865 score=12 needs_docs=yes confidence=high
  feat(admin-cli): inspect a machine's MachineBootInterface across its lifecycle
  https://github.com/NVIDIA/infra-controller/pull/2865
  signals: high-signal-path|proto-change|strong-keywords:4|weak-keywords:1

#3022 score=12 needs_docs=yes confidence=high
  feat(rest-api): Add Machine power control endpoint for Provider
  https://github.com/NVIDIA/infra-controller/pull/3022
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:3

#2175 score=11 needs_docs=yes confidence=high
  refactor(rms-client)!: migrate to updated RMS proto
  https://github.com/NVIDIA/infra-controller/pull/2175
  signals: high-signal-path|proto-change|config-or-schema-file|strong-keywords:7|weak-keywords:1|negative-keywords:2

#2286 score=11 needs_docs=yes confidence=high
  feat: Add Task Rule REST APIs for Flow Operation Rule Management
  https://github.com/NVIDIA/infra-controller/pull/2286
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:10|weak-keywords:2|negative-keywords:1

#2314 score=11 needs_docs=yes confidence=high
  feat: make any host interface the primary, not just a DPU
  https://github.com/NVIDIA/infra-controller/pull/2314
  signals: high-signal-path|proto-change|strong-keywords:9|weak-keywords:2|negative-keywords:2

#2440 score=11 needs_docs=yes confidence=high
  feat: Mirror Core expected inventory into Flow tables
  https://github.com/NVIDIA/infra-controller/pull/2440
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:8|weak-keywords:2|negative-keywords:1

#2447 score=11 needs_docs=yes confidence=high
  fix(api): Add a tenant_state field to VpcPrefix message
  https://github.com/NVIDIA/infra-controller/pull/2447
  signals: high-signal-path|proto-change|strong-keywords:8|weak-keywords:1|negative-keywords:1

#2461 score=11 needs_docs=yes confidence=high
  Chore: Connect Flow ReadinessGate to Component Status
  https://github.com/NVIDIA/infra-controller/pull/2461
  signals: high-signal-path|ops/config-path|proto-change|non-doc-markdown-only-hint|strong-keywords:7|weak-keywords:1|negative-keywords:2

#2470 score=11 needs_docs=yes confidence=high
  feat: support attaching HostInband segments to VPCs
  https://github.com/NVIDIA/infra-controller/pull/2470
  signals: high-signal-path|proto-change|strong-keywords:6|weak-keywords:1|negative-keywords:1

#2481 score=11 needs_docs=yes confidence=high
  feat: add a separate site-wide credential for the SuperNIC Lockdown
  https://github.com/NVIDIA/infra-controller/pull/2481
  signals: high-signal-path|proto-change|strong-keywords:6|weak-keywords:1|negative-keywords:1

#2539 score=11 needs_docs=yes confidence=high
  feat(rest-api): Add DPU machine retrieval endpoint
  https://github.com/NVIDIA/infra-controller/pull/2539
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:6|weak-keywords:1

#2544 score=11 needs_docs=yes confidence=high
  feat(rest-api): Remove firmware_version from expected inventory APIs
  https://github.com/NVIDIA/infra-controller/pull/2544
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:7|weak-keywords:2|negative-keywords:1

#2586 score=11 needs_docs=yes confidence=high
  feat(errors): add operator error schema
  https://github.com/NVIDIA/infra-controller/pull/2586
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:9|weak-keywords:1|negative-keywords:3

#2590 score=11 needs_docs=yes confidence=high
  feat: dpf: Display DPF disabled warning.
  https://github.com/NVIDIA/infra-controller/pull/2590
  signals: high-signal-path|proto-change|strong-keywords:8|weak-keywords:1|negative-keywords:1

#2619 score=11 needs_docs=yes confidence=high
  fix: Record null status observations when connectivity to NMX-C canno…
  https://github.com/NVIDIA/infra-controller/pull/2619
  signals: high-signal-path|proto-change|strong-keywords:8|weak-keywords:1|negative-keywords:1

#2651 score=11 needs_docs=yes confidence=high
  feat(machine-validation): M1: Add machine validation execution tracking foundation
  https://github.com/NVIDIA/infra-controller/pull/2651
  signals: high-signal-path|proto-change|config-or-schema-file|strong-keywords:10|weak-keywords:1|negative-keywords:2

#2672 score=11 needs_docs=yes confidence=high
  change(api,dhcp): new proto types, migrations & dual-stack NetworkDef…
  https://github.com/NVIDIA/infra-controller/pull/2672
  signals: high-signal-path|proto-change|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:9|weak-keywords:1|negative-keywords:1

#2747 score=11 needs_docs=yes confidence=high
  feat: declare a host NIC's network segment type directly
  https://github.com/NVIDIA/infra-controller/pull/2747
  signals: high-signal-path|proto-change|strong-keywords:4|weak-keywords:1|negative-keywords:1

#2757 score=11 needs_docs=yes confidence=high
  feat(site-explorer): report Mellanox firmware from explored data
  https://github.com/NVIDIA/infra-controller/pull/2757
  signals: high-signal-path|proto-change|strong-keywords:4

#2813 score=11 needs_docs=yes confidence=high
  fix(helm): correct boot-artifacts mount path and remove readOnly
  https://github.com/NVIDIA/infra-controller/pull/2813
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:5|weak-keywords:2|negative-keywords:1

#2838 score=11 needs_docs=yes confidence=high
  feat(machine-validation): Implement M2 machine validation heartbeat recovery
  https://github.com/NVIDIA/infra-controller/pull/2838
  signals: high-signal-path|proto-change|config-or-schema-file|strong-keywords:11|weak-keywords:1|negative-keywords:2

#2905 score=11 needs_docs=yes confidence=high
  fix(rest-api): Allow correct indices for Interface virtual function ID
  https://github.com/NVIDIA/infra-controller/pull/2905
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:3|weak-keywords:2

#2993 score=11 needs_docs=yes confidence=high
  feat(rest-api): Allow users to specify UUID when creating Network Security Group
  https://github.com/NVIDIA/infra-controller/pull/2993
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:8|weak-keywords:2|negative-keywords:1

#3002 score=11 needs_docs=yes confidence=high
  feat(rest-api): Add API model, endpoints for host firmware config management
  https://github.com/NVIDIA/infra-controller/pull/3002
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:8|weak-keywords:2|negative-keywords:1

#2141 score=10 needs_docs=yes confidence=high
  chore(rest-api): Update Go module path to match unified repo path
  https://github.com/NVIDIA/infra-controller/pull/2141
  signals: high-signal-path|ops/config-path|proto-change|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:1|weak-keywords:2|negative-keywords:2

#2150 score=10 needs_docs=yes confidence=high
  fix(rest-api): Populate RoutingProfileType directly from the controller value
  https://github.com/NVIDIA/infra-controller/pull/2150
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:2|negative-keywords:1

#2249 score=10 needs_docs=yes confidence=high
  feat(helm): add opt-in legacy carbide/forge name aliases for nico-api…
  https://github.com/NVIDIA/infra-controller/pull/2249
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:6|weak-keywords:1|negative-keywords:1

#2342 score=10 needs_docs=yes confidence=high
  fix(rest-api): Treat instance status consistently across reporting, filtering, and statistics
  https://github.com/NVIDIA/infra-controller/pull/2342
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2467 score=10 needs_docs=yes confidence=high
  feat(rest-api): Add DPU target for Tray firmware update API
  https://github.com/NVIDIA/infra-controller/pull/2467
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:9|weak-keywords:2|negative-keywords:2

#2491 score=10 needs_docs=yes confidence=high
  feat: Set component leak_status from leak-detection loop in Flow
  https://github.com/NVIDIA/infra-controller/pull/2491
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:6|weak-keywords:1|negative-keywords:1

#2548 score=10 needs_docs=yes confidence=high
  [#2060] fix: rename forge.local to nico.local
  https://github.com/NVIDIA/infra-controller/pull/2548
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:9|weak-keywords:1|negative-keywords:1

#2591 score=10 needs_docs=yes confidence=high
  feat: Add Site Explorer run status to admin UI
  https://github.com/NVIDIA/infra-controller/pull/2591
  signals: high-signal-path|proto-change|config-or-schema-file|strong-keywords:9|weak-keywords:1|negative-keywords:3

#2701 score=10 needs_docs=yes confidence=high
  feat(rest-api): return valid JSON from DELETE endpoints
  https://github.com/NVIDIA/infra-controller/pull/2701
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:6|weak-keywords:2|negative-keywords:2

#2840 score=10 needs_docs=yes confidence=high
  fix(site-agent): mount Core-gRPC certs where the binary reads them + …
  https://github.com/NVIDIA/infra-controller/pull/2840
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:8|weak-keywords:1|negative-keywords:1

#2860 score=10 needs_docs=yes confidence=high
  Adding decline-probation-period to kea config
  https://github.com/NVIDIA/infra-controller/pull/2860
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2894 score=10 needs_docs=yes confidence=high
  fix(rest-api): Add soft-deletion tag for DPU Extension Service deleted timestamp
  https://github.com/NVIDIA/infra-controller/pull/2894
  signals: high-signal-path|ops/config-path|strong-keywords:4|weak-keywords:1

#2942 score=10 needs_docs=yes confidence=high
  fix(site-agent): use mTLS for Flow gRPC and protect temporal-certs secret
  https://github.com/NVIDIA/infra-controller/pull/2942
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:8|weak-keywords:1|negative-keywords:1

#2139 score=9 needs_docs=yes confidence=high
  chore(rest-api): Apply our new FromProto/ToProto modeling to Machine
  https://github.com/NVIDIA/infra-controller/pull/2139
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:2|negative-keywords:2

#2140 score=9 needs_docs=yes confidence=high
  chore(rest-api): Apply our FromProto/ToProto modeling to the Instance delete flow
  https://github.com/NVIDIA/infra-controller/pull/2140
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:2|negative-keywords:2

#2142 score=9 needs_docs=yes confidence=high
  feat: Add core component manager integration for compute tray in Flow
  https://github.com/NVIDIA/infra-controller/pull/2142
  signals: high-signal-path|ops/config-path|non-doc-markdown-only-hint|strong-keywords:7|weak-keywords:3|negative-keywords:1

#2157 score=9 needs_docs=yes confidence=high
  feat(switch-controller): add power control on/off/reset …
  https://github.com/NVIDIA/infra-controller/pull/2157
  signals: high-signal-path|config-or-schema-file|strong-keywords:7|weak-keywords:2|negative-keywords:1

#2162 score=9 needs_docs=yes confidence=high
  feat: Add shared rule validation framework
  https://github.com/NVIDIA/infra-controller/pull/2162
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2170 score=9 needs_docs=yes confidence=high
  fix(rest-api): Include NVLink/DPU Ext. Deployments when updating Instance metadata
  https://github.com/NVIDIA/infra-controller/pull/2170
  signals: high-signal-path|ops/config-path|strong-keywords:3|weak-keywords:1

#2171 score=9 needs_docs=yes confidence=high
  refactor(rest-api): Use our generic cdb.GetPtr instead of per-type GetXPtr helpers
  https://github.com/NVIDIA/infra-controller/pull/2171
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2173 score=9 needs_docs=yes confidence=high
  chore(rest-api): Apply the new FromProto/ToProto modeling to SKU
  https://github.com/NVIDIA/infra-controller/pull/2173
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:2|negative-keywords:2

#2177 score=9 needs_docs=yes confidence=high
  chore(rest-api): Apply the new FromProto/ToProto modeling to SSHKeyGroup
  https://github.com/NVIDIA/infra-controller/pull/2177
  signals: high-signal-path|ops/config-path|strong-keywords:8|weak-keywords:2|negative-keywords:2

#2178 score=9 needs_docs=yes confidence=high
  chore(rest-api): Apply the FromProto/ToProto modeling to OperatingSystem
  https://github.com/NVIDIA/infra-controller/pull/2178
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:2|negative-keywords:2

#2180 score=9 needs_docs=yes confidence=high
  chore(rest-api): Apply FromProto/ToProto modeling to Subnet
  https://github.com/NVIDIA/infra-controller/pull/2180
  signals: high-signal-path|ops/config-path|strong-keywords:8|weak-keywords:2|negative-keywords:2

#2183 score=9 needs_docs=yes confidence=high
  chore(rest-api): Apply FromProto/ToProto modeling to VpcPeering
  https://github.com/NVIDIA/infra-controller/pull/2183
  signals: high-signal-path|ops/config-path|strong-keywords:8|weak-keywords:2|negative-keywords:2

#2184 score=9 needs_docs=yes confidence=high
  chore(rest-api): Apply FromProto/ToProto modeling to DpuExtensionService
  https://github.com/NVIDIA/infra-controller/pull/2184
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:2|negative-keywords:2

#2185 score=9 needs_docs=yes confidence=high
  chore(rest-api): Apply FromProto/ToProto modeling to NetworkSecurityGroup
  https://github.com/NVIDIA/infra-controller/pull/2185
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:2|negative-keywords:2

#2187 score=9 needs_docs=yes confidence=high
  chore(rest-api): Apply FromProto/ToProto modeling to VpcPrefix
  https://github.com/NVIDIA/infra-controller/pull/2187
  signals: high-signal-path|ops/config-path|strong-keywords:8|weak-keywords:2|negative-keywords:2

#2208 score=9 needs_docs=yes confidence=high
  chore(rest-api): Inline basic deletion-request protos in handlers
  https://github.com/NVIDIA/infra-controller/pull/2208
  signals: high-signal-path|ops/config-path|strong-keywords:6|weak-keywords:2|negative-keywords:2

#2217 score=9 needs_docs=yes confidence=high
  fix: drop NICO_REST_REPO / NICO_REPO env vars
  https://github.com/NVIDIA/infra-controller/pull/2217
  signals: high-signal-path|ops/config-path|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2220 score=9 needs_docs=yes confidence=high
  feat(rest-api): Infer Provider/Tenant from caller's org 
  https://github.com/NVIDIA/infra-controller/pull/2220
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:2|weak-keywords:1

#2270 score=9 needs_docs=yes confidence=high
  fix(nico-dhcp): dual-name kea hook params + require operator IPs
  https://github.com/NVIDIA/infra-controller/pull/2270
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:9|weak-keywords:1|negative-keywords:2

#2276 score=9 needs_docs=yes confidence=high
  feat: Log every gRPC call on server and client paths in Flow
  https://github.com/NVIDIA/infra-controller/pull/2276
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2285 score=9 needs_docs=yes confidence=high
  feat: and now enhance machine_interfaces with a full MachineBootInterface
  https://github.com/NVIDIA/infra-controller/pull/2285
  signals: high-signal-path|config-or-schema-file|strong-keywords:9|weak-keywords:3|negative-keywords:1

#2289 score=9 needs_docs=yes confidence=high
  feat(rest-api): Support selective hot-loading for API config, enable for phone home URL
  https://github.com/NVIDIA/infra-controller/pull/2289
  signals: high-signal-path|ops/config-path|strong-keywords:10|weak-keywords:1|negative-keywords:1

#2310 score=9 needs_docs=yes confidence=high
  feat(rest-api): write all expected-inventory device metadata to Core
  https://github.com/NVIDIA/infra-controller/pull/2310
  signals: high-signal-path|ops/config-path|strong-keywords:8|weak-keywords:1|negative-keywords:1

#2416 score=9 needs_docs=yes confidence=high
  Allow seeding carbide-api-config with VPCs
  https://github.com/NVIDIA/infra-controller/pull/2416
  signals: high-signal-path|config-or-schema-file|strong-keywords:7|weak-keywords:2|negative-keywords:1

#2436 score=9 needs_docs=yes confidence=high
  NICo infra fixes + blank site templates
  https://github.com/NVIDIA/infra-controller/pull/2436
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:3

#2460 score=9 needs_docs=yes confidence=high
  fix(rest-api): share SQL IP address typing between nvswitch and powershelf
  https://github.com/NVIDIA/infra-controller/pull/2460
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2477 score=9 needs_docs=yes confidence=high
  feat: Add generic Core gRPC proxy and BMC credential endpoints
  https://github.com/NVIDIA/infra-controller/pull/2477
  signals: high-signal-path|ops/config-path|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:6

#2480 score=9 needs_docs=yes confidence=high
  fix(rest-api): Validate MAC if provided in Expected Machine update request
  https://github.com/NVIDIA/infra-controller/pull/2480
  signals: high-signal-path|ops/config-path|strong-keywords:2|weak-keywords:2

#2489 score=9 needs_docs=yes confidence=high
  fix: Keep Flow mirror off in actual-sync inventory tests
  https://github.com/NVIDIA/infra-controller/pull/2489
  signals: high-signal-path|ops/config-path|strong-keywords:6|weak-keywords:1|negative-keywords:1

#2521 score=9 needs_docs=yes confidence=high
  feat: Include switch NVOS IP in Flow component/tray description
  https://github.com/NVIDIA/infra-controller/pull/2521
  signals: high-signal-path|ops/config-path|strong-keywords:6|weak-keywords:1|negative-keywords:1

#2537 score=9 needs_docs=yes confidence=high
  fix: Drop firmware_version from expected-inventory metadata
  https://github.com/NVIDIA/infra-controller/pull/2537
  signals: high-signal-path|ops/config-path|strong-keywords:6|weak-keywords:1|negative-keywords:1

#2542 score=9 needs_docs=yes confidence=high
  chore(rest-api): Migrate SSH key association DAOs to param structs
  https://github.com/NVIDIA/infra-controller/pull/2542
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:2|negative-keywords:2

#2655 score=9 needs_docs=yes confidence=high
  fix: turn on FNN in struct used during site creation
  https://github.com/NVIDIA/infra-controller/pull/2655
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2756 score=9 needs_docs=yes confidence=high
  feat: resolve scout firmware upgrade scripts from static assets
  https://github.com/NVIDIA/infra-controller/pull/2756
  signals: high-signal-path|ops/config-path|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:7|weak-keywords:1|negative-keywords:1

#2759 score=9 needs_docs=yes confidence=high
  chore(rest-api): Migrate Provider and Status Details DAOs to use struct params
  https://github.com/NVIDIA/infra-controller/pull/2759
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:2|negative-keywords:2

#2781 score=9 needs_docs=yes confidence=high
  docs(helm): document required resource pools in site config
  https://github.com/NVIDIA/infra-controller/pull/2781
  signals: high-signal-path|ops/config-path|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:9|weak-keywords:1|negative-keywords:1

#2825 score=9 needs_docs=yes confidence=high
  fix(nico-api): add carbide-api.forge to default cert SANs (DPU heartbeat during carbide→nico rename)
  https://github.com/NVIDIA/infra-controller/pull/2825
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:3

#2833 score=9 needs_docs=yes confidence=high
  refactor(site-explorer): paginate the explored Mellanox device RPC
  https://github.com/NVIDIA/infra-controller/pull/2833
  signals: high-signal-path|proto-change|strong-keywords:3|negative-keywords:1

#2956 score=9 needs_docs=yes confidence=high
  fix(ssh-console): add opt-in IPMI SOL conflict recovery
  https://github.com/NVIDIA/infra-controller/pull/2956
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:9|weak-keywords:2|negative-keywords:3

#2961 score=9 needs_docs=yes confidence=high
  feat(rest-api): Expose isDpfEnabled for Expected Machine endpoints
  https://github.com/NVIDIA/infra-controller/pull/2961
  signals: high-signal-path|ops/config-path|config-or-schema-file|strong-keywords:2|weak-keywords:3|negative-keywords:1

#2116 score=8 needs_docs=yes confidence=high
  chore(rest-api): Apply our FromProto/ToProto modeling to InfiniBandPartition
  https://github.com/NVIDIA/infra-controller/pull/2116
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:2|negative-keywords:3

#2122 score=8 needs_docs=yes confidence=high
  chore(rest-api): Apply our FromProto/ToProto modeling to NVLinkLogicalPartition
  https://github.com/NVIDIA/infra-controller/pull/2122
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:2|negative-keywords:3

#2191 score=8 needs_docs=yes confidence=high
  Support for setting multicast group limits on nvlink partitions
  https://github.com/NVIDIA/infra-controller/pull/2191
  signals: high-signal-path|config-or-schema-file|strong-keywords:9|weak-keywords:1|negative-keywords:1

#2194 score=8 needs_docs=yes confidence=high
  feat: Add MCP read-only server mode
  https://github.com/NVIDIA/infra-controller/pull/2194
  signals: high-signal-path|ops/config-path|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:3

#2195 score=8 needs_docs=yes confidence=high
  feat(rpc): gate prost builders behind test-support
  https://github.com/NVIDIA/infra-controller/pull/2195
  signals: high-signal-path|config-or-schema-file|strong-keywords:9|weak-keywords:2|negative-keywords:2

#2206 score=8 needs_docs=yes confidence=high
  Add `--zero-dpu` flag to admin-cli
  https://github.com/NVIDIA/infra-controller/pull/2206
  signals: high-signal-path|strong-keywords:5|weak-keywords:2|negative-keywords:1

#2221 score=8 needs_docs=yes confidence=high
  feat(admin-cli): add usage examples to all commands; restructure browse
  https://github.com/NVIDIA/infra-controller/pull/2221
  signals: high-signal-path|ops/config-path|config-or-schema-file|non-doc-markdown-only-hint|strong-keywords:7|weak-keywords:1|negative-keywords:2

#2257 score=8 needs_docs=yes confidence=high
  nvue-client: Use slightly stronger types for NvueConfig
  https://github.com/NVIDIA/infra-controller/pull/2257
  signals: high-signal-path|config-or-schema-file|strong-keywords:9|weak-keywords:1|negative-keywords:1

#2261 score=8 needs_docs=yes confidence=high
  feat: store the full boot interface for boot-device management
  https://github.com/NVIDIA/infra-controller/pull/2261
  signals: high-signal-path|config-or-schema-file|strong-keywords:6|weak-keywords:1|negative-keywords:1

#2265 score=8 needs_docs=yes confidence=high
  chore(rest-api): Set default phone home URL to use dedicated IP
  https://github.com/NVIDIA/infra-controller/pull/2265
  signals: high-signal-path|ops/config-path|strong-keywords:8|weak-keywords:1|negative-keywords:2

#2308 score=8 needs_docs=yes confidence=high
  chore(rest-api): Migrate Tenant and Fabric DAOs to use param structs
  https://github.com/NVIDIA/infra-controller/pull/2308
  signals: high-signal-path|ops/config-path|strong-keywords:7|weak-keywords:1|negative-keywords:2

#2313 score=8 needs_docs=yes confidence=high
  fix(rest-api): Allow privileged Tenants to retrieve Expected Machines without specifying Site ID
  https://github.com/NVIDIA/infra-controller/pull/2313
  signals: high-signal-path|ops/config-path|strong-keywords:2|weak-keywords:2|negative-keywords:1
```
