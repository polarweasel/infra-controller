# pr_docs_most_likely_missing_from_txt.md

Source: `pr_docs_most_likely_missing.txt`

```text
Most-likely missing docs PRs (second-pass heuristic, rebalanced split)
Split into Operator Docs likely and API/Reference Docs likely
Total: 47 | Operator: 7 | API/Reference: 40

## Operator Docs Likely

#2216 (op_score=17, api_score=17)
  feat: Initial changes for Astra support
  https://github.com/NVIDIA/infra-controller/pull/2216
  reasons: admin tooling surface|infra operations subsystem|configuration impact|also_api:proto contract changes

#2199 (op_score=24, api_score=22)
  feat(api): Introduce VPC prefix lifecycle
  https://github.com/NVIDIA/infra-controller/pull/2199
  reasons: deploy/helm changes|dev/scripts operational changes|admin tooling surface|also_api:proto contract changes

#2470 (op_score=10, api_score=13)
  feat: support attaching HostInband segments to VPCs
  https://github.com/NVIDIA/infra-controller/pull/2470
  reasons: admin tooling surface|operator-oriented language|also_api:proto contract changes

#2481 (op_score=10, api_score=13)
  feat: add a separate site-wide credential for the SuperNIC Lockdown
  https://github.com/NVIDIA/infra-controller/pull/2481
  reasons: admin tooling surface|operator-oriented language|also_api:proto contract changes

#2991 (op_score=10, api_score=13)
  feat(credential-rotation): stage site-wide credential rotations
  https://github.com/NVIDIA/infra-controller/pull/2991
  reasons: admin tooling surface|operator-oriented language|also_api:proto contract changes

#2261 (op_score=12, api_score=9)
  feat: store the full boot interface for boot-device management
  https://github.com/NVIDIA/infra-controller/pull/2261
  reasons: admin tooling surface|configuration impact|operator-oriented language|also_api:public API code surface

#3033 (op_score=10, api_score=13)
  feat(api): link switches and power shelves to their BMC via machine_interfaces
  https://github.com/NVIDIA/infra-controller/pull/3033
  reasons: admin tooling surface|operator-oriented language|also_api:public API code surface

## API/Reference Docs Likely

#1854 (op_score=4, api_score=21)
  feat(health): add API support for NVL domain health records
  https://github.com/NVIDIA/infra-controller/pull/1854
  reasons: proto contract changes|public API code surface|schema migration impact|also_operator:admin tooling surface

#2591 (op_score=2, api_score=19)
  feat: Add Site Explorer run status to admin UI
  https://github.com/NVIDIA/infra-controller/pull/2591
  reasons: proto contract changes|public API code surface|schema migration impact|also_operator:admin tooling surface

#2665 (op_score=12, api_score=22)
  feat: support storing secrets/credentials in Postgres
  https://github.com/NVIDIA/infra-controller/pull/2665
  reasons: proto contract changes|public API code surface|schema migration impact|also_operator:admin tooling surface

#2666 (op_score=4, api_score=21)
  feat(zero-dpu): Allow flat VPC's to not belong to a network segment
  https://github.com/NVIDIA/infra-controller/pull/2666
  reasons: proto contract changes|public API code surface|schema migration impact|also_operator:admin tooling surface

#2865 (op_score=4, api_score=18)
  feat(admin-cli): inspect a machine's MachineBootInterface across its lifecycle
  https://github.com/NVIDIA/infra-controller/pull/2865
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2037 (op_score=6, api_score=21)
  feat: Expose last seen scout version for a machine
  https://github.com/NVIDIA/infra-controller/pull/2037
  reasons: proto contract changes|public API code surface|schema migration impact|also_operator:operator-oriented language

#2651 (op_score=4, api_score=19)
  feat(machine-validation): M1: Add machine validation execution tracking foundation
  https://github.com/NVIDIA/infra-controller/pull/2651
  reasons: proto contract changes|public API code surface|schema migration impact|also_operator:operator-oriented language

#2751 (op_score=6, api_score=21)
  change(api): add dual-stack FNN allocation and IPv6 static-assignment support
  https://github.com/NVIDIA/infra-controller/pull/2751
  reasons: proto contract changes|public API code surface|schema migration impact|also_operator:operator-oriented language

#2838 (op_score=4, api_score=19)
  feat(machine-validation): Implement M2 machine validation heartbeat recovery
  https://github.com/NVIDIA/infra-controller/pull/2838
  reasons: proto contract changes|public API code surface|schema migration impact|also_operator:operator-oriented language

#2967 (op_score=6, api_score=21)
  Upsert firmware config api
  https://github.com/NVIDIA/infra-controller/pull/2967
  reasons: proto contract changes|public API code surface|schema migration impact|also_operator:operator-oriented language

#1803 (op_score=10, api_score=18)
  feat: add a bypass-state-controller flag to the component management API
  https://github.com/NVIDIA/infra-controller/pull/1803
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2043 (op_score=10, api_score=18)
  feat(api): add admin force-delete for racks
  https://github.com/NVIDIA/infra-controller/pull/2043
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2151 (op_score=4, api_score=13)
  Fixes to facilitate move from dpf to non-dpf and vice versa
  https://github.com/NVIDIA/infra-controller/pull/2151
  reasons: proto contract changes|public API code surface|also_operator:admin tooling surface

#2175 (op_score=4, api_score=17)
  refactor(rms-client)!: migrate to updated RMS proto
  https://github.com/NVIDIA/infra-controller/pull/2175
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2255 (op_score=10, api_score=18)
  fix: Remove requirement for access token for rms fw update
  https://github.com/NVIDIA/infra-controller/pull/2255
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2314 (op_score=8, api_score=16)
  feat: make any host interface the primary, not just a DPU
  https://github.com/NVIDIA/infra-controller/pull/2314
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2590 (op_score=10, api_score=18)
  feat: dpf: Display DPF disabled warning.
  https://github.com/NVIDIA/infra-controller/pull/2590
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2613 (op_score=10, api_score=18)
  refactor(vpc): separate Vpc fields into config/status
  https://github.com/NVIDIA/infra-controller/pull/2613
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2619 (op_score=10, api_score=18)
  fix: Record null status observations when connectivity to NMX-C canno…
  https://github.com/NVIDIA/infra-controller/pull/2619
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2747 (op_score=8, api_score=16)
  feat: declare a host NIC's network segment type directly
  https://github.com/NVIDIA/infra-controller/pull/2747
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2757 (op_score=10, api_score=18)
  feat(site-explorer): report Mellanox firmware from explored data
  https://github.com/NVIDIA/infra-controller/pull/2757
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2141 (op_score=6, api_score=25)
  chore(rest-api): Update Go module path to match unified repo path
  https://github.com/NVIDIA/infra-controller/pull/2141
  reasons: proto contract changes|openapi changes|public API code surface|also_operator:configuration impact

#2234 (op_score=6, api_score=18)
  feat(api): Include additional state details in DpuInfo
  https://github.com/NVIDIA/infra-controller/pull/2234
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:operator-oriented language

#2259 (op_score=-2, api_score=16)
  chore(rest-api): Snapshot Core proto, update Machine health override/Rack profile ID refs
  https://github.com/NVIDIA/infra-controller/pull/2259
  reasons: proto contract changes|public API code surface|api/reference language

#2272 (op_score=8, api_score=27)
  change(rest-api): Align REST API with new VpcPrefix lifecycle
  https://github.com/NVIDIA/infra-controller/pull/2272
  reasons: proto contract changes|openapi changes|public API code surface|also_operator:configuration impact

#2288 (op_score=8, api_score=27)
  feat: Surface Flow task report on Task API
  https://github.com/NVIDIA/infra-controller/pull/2288
  reasons: proto contract changes|openapi changes|public API code surface|also_operator:configuration impact

#2447 (op_score=6, api_score=18)
  fix(api): Add a tenant_state field to VpcPrefix message
  https://github.com/NVIDIA/infra-controller/pull/2447
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:operator-oriented language

#2534 (op_score=8, api_score=27)
  feat: Surface Flow component status, leak status, and override-readiness in REST
  https://github.com/NVIDIA/infra-controller/pull/2534
  reasons: proto contract changes|openapi changes|public API code surface|also_operator:configuration impact

#2829 (op_score=2, api_score=16)
  feat(rest-api): Support for adding Tenant information when reported Issue for Delete Instance
  https://github.com/NVIDIA/infra-controller/pull/2829
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2833 (op_score=4, api_score=18)
  refactor(site-explorer): paginate the explored Mellanox device RPC
  https://github.com/NVIDIA/infra-controller/pull/2833
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:admin tooling surface

#2861 (op_score=0, api_score=18)
  feat(zero-dpu): Pass VPC ID to AllocateInstance from REST API
  https://github.com/NVIDIA/infra-controller/pull/2861
  reasons: proto contract changes|public API code surface|api/reference language

#2877 (op_score=11, api_score=18)
  fix(dhcp): Guard DHCP lease expiry handling with a feature flag.
  https://github.com/NVIDIA/infra-controller/pull/2877
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:infra operations subsystem

#2904 (op_score=6, api_score=13)
  feat: Carbide side changes to support Astra
  https://github.com/NVIDIA/infra-controller/pull/2904
  reasons: proto contract changes|public API code surface|also_operator:operator-oriented language

#3018 (op_score=6, api_score=18)
  feat(api): add host firmware config delete endpoint
  https://github.com/NVIDIA/infra-controller/pull/3018
  reasons: proto contract changes|public API code surface|api/reference language|also_operator:operator-oriented language

#3022 (op_score=8, api_score=27)
  feat(rest-api): Add Machine power control endpoint for Provider
  https://github.com/NVIDIA/infra-controller/pull/3022
  reasons: proto contract changes|openapi changes|public API code surface|also_operator:configuration impact

#2157 (op_score=6, api_score=8)
  feat(switch-controller): add power control on/off/reset …
  https://github.com/NVIDIA/infra-controller/pull/2157
  reasons: public API code surface|schema migration impact|also_operator:operator-oriented language

#2285 (op_score=6, api_score=13)
  feat: and now enhance machine_interfaces with a full MachineBootInterface
  https://github.com/NVIDIA/infra-controller/pull/2285
  reasons: public API code surface|schema migration impact|api/reference language|also_operator:operator-oriented language

#2672 (op_score=11, api_score=21)
  change(api,dhcp): new proto types, migrations & dual-stack NetworkDef…
  https://github.com/NVIDIA/infra-controller/pull/2672
  reasons: proto contract changes|public API code surface|schema migration impact|also_operator:infra operations subsystem

#2827 (op_score=6, api_score=8)
  fix: Allow extension service reuse after soft delete
  https://github.com/NVIDIA/infra-controller/pull/2827
  reasons: public API code surface|schema migration impact|also_operator:operator-oriented language

#2846 (op_score=8, api_score=14)
  feat: track per-device credential rotation convergence
  https://github.com/NVIDIA/infra-controller/pull/2846
  reasons: public API code surface|schema migration impact|api/reference language|also_operator:configuration impact
```
