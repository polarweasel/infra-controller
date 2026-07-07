# Most-Likely Missing Docs PRs

Second-pass heuristic with a rebalanced split.

- Total: `47`
- Operator Docs likely: `7`
- API/Reference Docs likely: `40`

## Operator Docs Likely

- **PR [#2216](https://github.com/NVIDIA/infra-controller/pull/2216)** (`op_score=17`, `api_score=17`)
  - Title: `feat: Initial changes for Astra support`
  - Reasons: `admin tooling surface`, `infra operations subsystem`, `configuration impact`, `also_api:proto contract changes`

- **PR [#2199](https://github.com/NVIDIA/infra-controller/pull/2199)** (`op_score=24`, `api_score=22`)
  - Title: `feat(api): Introduce VPC prefix lifecycle`
  - Reasons: `deploy/helm changes`, `dev/scripts operational changes`, `admin tooling surface`, `also_api:proto contract changes`

- **PR [#2470](https://github.com/NVIDIA/infra-controller/pull/2470)** (`op_score=10`, `api_score=13`)
  - Title: `feat: support attaching HostInband segments to VPCs`
  - Reasons: `admin tooling surface`, `operator-oriented language`, `also_api:proto contract changes`

- **PR [#2481](https://github.com/NVIDIA/infra-controller/pull/2481)** (`op_score=10`, `api_score=13`)
  - Title: `feat: add a separate site-wide credential for the SuperNIC Lockdown`
  - Reasons: `admin tooling surface`, `operator-oriented language`, `also_api:proto contract changes`

- **PR [#2991](https://github.com/NVIDIA/infra-controller/pull/2991)** (`op_score=10`, `api_score=13`)
  - Title: `feat(credential-rotation): stage site-wide credential rotations`
  - Reasons: `admin tooling surface`, `operator-oriented language`, `also_api:proto contract changes`

- **PR [#2261](https://github.com/NVIDIA/infra-controller/pull/2261)** (`op_score=12`, `api_score=9`)
  - Title: `feat: store the full boot interface for boot-device management`
  - Reasons: `admin tooling surface`, `configuration impact`, `operator-oriented language`, `also_api:public API code surface`

- **PR [#3033](https://github.com/NVIDIA/infra-controller/pull/3033)** (`op_score=10`, `api_score=13`)
  - Title: `feat(api): link switches and power shelves to their BMC via machine_interfaces`
  - Reasons: `admin tooling surface`, `operator-oriented language`, `also_api:public API code surface`

## API/Reference Docs Likely

- **PR [#1854](https://github.com/NVIDIA/infra-controller/pull/1854)** (`op_score=4`, `api_score=21`)
  - Title: `feat(health): add API support for NVL domain health records`
  - Reasons: `proto contract changes`, `public API code surface`, `schema migration impact`, `also_operator:admin tooling surface`

- **PR [#2591](https://github.com/NVIDIA/infra-controller/pull/2591)** (`op_score=2`, `api_score=19`)
  - Title: `feat: Add Site Explorer run status to admin UI`
  - Reasons: `proto contract changes`, `public API code surface`, `schema migration impact`, `also_operator:admin tooling surface`

- **PR [#2665](https://github.com/NVIDIA/infra-controller/pull/2665)** (`op_score=12`, `api_score=22`)
  - Title: `feat: support storing secrets/credentials in Postgres`
  - Reasons: `proto contract changes`, `public API code surface`, `schema migration impact`, `also_operator:admin tooling surface`

- **PR [#2666](https://github.com/NVIDIA/infra-controller/pull/2666)** (`op_score=4`, `api_score=21`)
  - Title: `feat(zero-dpu): Allow flat VPC's to not belong to a network segment`
  - Reasons: `proto contract changes`, `public API code surface`, `schema migration impact`, `also_operator:admin tooling surface`

- **PR [#2865](https://github.com/NVIDIA/infra-controller/pull/2865)** (`op_score=4`, `api_score=18`)
  - Title: `feat(admin-cli): inspect a machine's MachineBootInterface across its lifecycle`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2037](https://github.com/NVIDIA/infra-controller/pull/2037)** (`op_score=6`, `api_score=21`)
  - Title: `feat: Expose last seen scout version for a machine`
  - Reasons: `proto contract changes`, `public API code surface`, `schema migration impact`, `also_operator:operator-oriented language`

- **PR [#2651](https://github.com/NVIDIA/infra-controller/pull/2651)** (`op_score=4`, `api_score=19`)
  - Title: `feat(machine-validation): M1: Add machine validation execution tracking foundation`
  - Reasons: `proto contract changes`, `public API code surface`, `schema migration impact`, `also_operator:operator-oriented language`

- **PR [#2751](https://github.com/NVIDIA/infra-controller/pull/2751)** (`op_score=6`, `api_score=21`)
  - Title: `change(api): add dual-stack FNN allocation and IPv6 static-assignment support`
  - Reasons: `proto contract changes`, `public API code surface`, `schema migration impact`, `also_operator:operator-oriented language`

- **PR [#2838](https://github.com/NVIDIA/infra-controller/pull/2838)** (`op_score=4`, `api_score=19`)
  - Title: `feat(machine-validation): Implement M2 machine validation heartbeat recovery`
  - Reasons: `proto contract changes`, `public API code surface`, `schema migration impact`, `also_operator:operator-oriented language`

- **PR [#2967](https://github.com/NVIDIA/infra-controller/pull/2967)** (`op_score=6`, `api_score=21`)
  - Title: `Upsert firmware config api`
  - Reasons: `proto contract changes`, `public API code surface`, `schema migration impact`, `also_operator:operator-oriented language`

- **PR [#1803](https://github.com/NVIDIA/infra-controller/pull/1803)** (`op_score=10`, `api_score=18`)
  - Title: `feat: add a bypass-state-controller flag to the component management API`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2043](https://github.com/NVIDIA/infra-controller/pull/2043)** (`op_score=10`, `api_score=18`)
  - Title: `feat(api): add admin force-delete for racks`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2151](https://github.com/NVIDIA/infra-controller/pull/2151)** (`op_score=4`, `api_score=13`)
  - Title: `Fixes to facilitate move from dpf to non-dpf and vice versa`
  - Reasons: `proto contract changes`, `public API code surface`, `also_operator:admin tooling surface`

- **PR [#2175](https://github.com/NVIDIA/infra-controller/pull/2175)** (`op_score=4`, `api_score=17`)
  - Title: `refactor(rms-client)!: migrate to updated RMS proto`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2255](https://github.com/NVIDIA/infra-controller/pull/2255)** (`op_score=10`, `api_score=18`)
  - Title: `fix: Remove requirement for access token for rms fw update`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2314](https://github.com/NVIDIA/infra-controller/pull/2314)** (`op_score=8`, `api_score=16`)
  - Title: `feat: make any host interface the primary, not just a DPU`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2590](https://github.com/NVIDIA/infra-controller/pull/2590)** (`op_score=10`, `api_score=18`)
  - Title: `feat: dpf: Display DPF disabled warning.`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2613](https://github.com/NVIDIA/infra-controller/pull/2613)** (`op_score=10`, `api_score=18`)
  - Title: `refactor(vpc): separate Vpc fields into config/status`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2619](https://github.com/NVIDIA/infra-controller/pull/2619)** (`op_score=10`, `api_score=18`)
  - Title: `fix: Record null status observations when connectivity to NMX-C canno…`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2747](https://github.com/NVIDIA/infra-controller/pull/2747)** (`op_score=8`, `api_score=16`)
  - Title: `feat: declare a host NIC's network segment type directly`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2757](https://github.com/NVIDIA/infra-controller/pull/2757)** (`op_score=10`, `api_score=18`)
  - Title: `feat(site-explorer): report Mellanox firmware from explored data`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2141](https://github.com/NVIDIA/infra-controller/pull/2141)** (`op_score=6`, `api_score=25`)
  - Title: `chore(rest-api): Update Go module path to match unified repo path`
  - Reasons: `proto contract changes`, `openapi changes`, `public API code surface`, `also_operator:configuration impact`

- **PR [#2234](https://github.com/NVIDIA/infra-controller/pull/2234)** (`op_score=6`, `api_score=18`)
  - Title: `feat(api): Include additional state details in DpuInfo`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:operator-oriented language`

- **PR [#2259](https://github.com/NVIDIA/infra-controller/pull/2259)** (`op_score=-2`, `api_score=16`)
  - Title: `chore(rest-api): Snapshot Core proto, update Machine health override/Rack profile ID refs`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`

- **PR [#2272](https://github.com/NVIDIA/infra-controller/pull/2272)** (`op_score=8`, `api_score=27`)
  - Title: `change(rest-api): Align REST API with new VpcPrefix lifecycle`
  - Reasons: `proto contract changes`, `openapi changes`, `public API code surface`, `also_operator:configuration impact`

- **PR [#2288](https://github.com/NVIDIA/infra-controller/pull/2288)** (`op_score=8`, `api_score=27`)
  - Title: `feat: Surface Flow task report on Task API`
  - Reasons: `proto contract changes`, `openapi changes`, `public API code surface`, `also_operator:configuration impact`

- **PR [#2447](https://github.com/NVIDIA/infra-controller/pull/2447)** (`op_score=6`, `api_score=18`)
  - Title: `fix(api): Add a tenant_state field to VpcPrefix message`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:operator-oriented language`

- **PR [#2534](https://github.com/NVIDIA/infra-controller/pull/2534)** (`op_score=8`, `api_score=27`)
  - Title: `feat: Surface Flow component status, leak status, and override-readiness in REST`
  - Reasons: `proto contract changes`, `openapi changes`, `public API code surface`, `also_operator:configuration impact`

- **PR [#2829](https://github.com/NVIDIA/infra-controller/pull/2829)** (`op_score=2`, `api_score=16`)
  - Title: `feat(rest-api): Support for adding Tenant information when reported Issue for Delete Instance`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2833](https://github.com/NVIDIA/infra-controller/pull/2833)** (`op_score=4`, `api_score=18`)
  - Title: `refactor(site-explorer): paginate the explored Mellanox device RPC`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:admin tooling surface`

- **PR [#2861](https://github.com/NVIDIA/infra-controller/pull/2861)** (`op_score=0`, `api_score=18`)
  - Title: `feat(zero-dpu): Pass VPC ID to AllocateInstance from REST API`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`

- **PR [#2877](https://github.com/NVIDIA/infra-controller/pull/2877)** (`op_score=11`, `api_score=18`)
  - Title: `fix(dhcp): Guard DHCP lease expiry handling with a feature flag.`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:infra operations subsystem`

- **PR [#2904](https://github.com/NVIDIA/infra-controller/pull/2904)** (`op_score=6`, `api_score=13`)
  - Title: `feat: Carbide side changes to support Astra`
  - Reasons: `proto contract changes`, `public API code surface`, `also_operator:operator-oriented language`

- **PR [#3018](https://github.com/NVIDIA/infra-controller/pull/3018)** (`op_score=6`, `api_score=18`)
  - Title: `feat(api): add host firmware config delete endpoint`
  - Reasons: `proto contract changes`, `public API code surface`, `api/reference language`, `also_operator:operator-oriented language`

- **PR [#3022](https://github.com/NVIDIA/infra-controller/pull/3022)** (`op_score=8`, `api_score=27`)
  - Title: `feat(rest-api): Add Machine power control endpoint for Provider`
  - Reasons: `proto contract changes`, `openapi changes`, `public API code surface`, `also_operator:configuration impact`

- **PR [#2157](https://github.com/NVIDIA/infra-controller/pull/2157)** (`op_score=6`, `api_score=8`)
  - Title: `feat(switch-controller): add power control on/off/reset …`
  - Reasons: `public API code surface`, `schema migration impact`, `also_operator:operator-oriented language`

- **PR [#2285](https://github.com/NVIDIA/infra-controller/pull/2285)** (`op_score=6`, `api_score=13`)
  - Title: `feat: and now enhance machine_interfaces with a full MachineBootInterface`
  - Reasons: `public API code surface`, `schema migration impact`, `api/reference language`, `also_operator:operator-oriented language`

- **PR [#2672](https://github.com/NVIDIA/infra-controller/pull/2672)** (`op_score=11`, `api_score=21`)
  - Title: `change(api,dhcp): new proto types, migrations & dual-stack NetworkDef…`
  - Reasons: `proto contract changes`, `public API code surface`, `schema migration impact`, `also_operator:infra operations subsystem`

- **PR [#2827](https://github.com/NVIDIA/infra-controller/pull/2827)** (`op_score=6`, `api_score=8`)
  - Title: `fix: Allow extension service reuse after soft delete`
  - Reasons: `public API code surface`, `schema migration impact`, `also_operator:operator-oriented language`

- **PR [#2846](https://github.com/NVIDIA/infra-controller/pull/2846)** (`op_score=8`, `api_score=14`)
  - Title: `feat: track per-device credential rotation convergence`
  - Reasons: `public API code surface`, `schema migration impact`, `api/reference language`, `also_operator:configuration impact`
