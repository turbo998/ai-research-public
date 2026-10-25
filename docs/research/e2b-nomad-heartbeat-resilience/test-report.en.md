# 7-Card 4:5 Benchmark & Verification Report: E2B Sandbox Cluster Resilience Under Single Non-Leader Nomad Server Failure

> **Language / 语言**: [中文 (`test-report.md`)](test-report.md) | **English (Current)**  
> **Companion Artifacts**: [7-Card 4:5 Visual HTML Deck (`test-report-cards.html`)](test-report-cards.html) · [Sealed Data (`report.json`)](report.json) · [Provenance Ledger (`evidence.json`)](evidence.json) · [Study Notes (`README.en.md`)](README.en.md)

---

## Card 1 (`1 / 7` · `HANDS-ON · CLOUD ARCHITECTURE & AI SANDBOX INFRASTRUCTURE RESILIENCE`) — Overview & Workbench

### Headline Finding
**1 Stopped Nomad Server Replaced 35% of Healthy E2B Orchestrators — `disconnect (50s)` & `heartbeat_grace (50s)` Achieve 100% Retention**

### Workbench Summary (3 Nomad Servers · 20 Sandbox Hosts)
- **Cluster Topology Under Test**: 3 Nomad Servers (1 Leader + 2 Followers, maintaining 2/3 Raft quorum) and 20 Nomad Client sandbox hosts running `20` `Orchestrator` allocations, `20` `session-proxy` allocations, `3` `client-proxy` allocations, and the E2B `API` service.
- **Top Metric Pills**:
  - `Baseline: 7/20 Orch & 2/3 Proxy Replaced` (Default `heartbeat_grace = 10s`, no `disconnect`, 11-minute observation window)
  - `disconnect=50s: 10/10 Sandboxes · 23/23 Streams` (100% survival of running sandboxes and active HTTP NDJSON long streams)
  - `Short Requests: 12,581 / 12,581 (0 Errors)` (100% success across high-frequency short requests during Server failover)
  - `heartbeat_grace=50s: 20/20 Ready (2 Rounds)` (All 20 surviving Clients remained `ready` across 2 consecutive fault-injection rounds)

---

## Card 2 (`2 / 7` · `SCENARIO: SINGLE NON-LEADER NOMAD SERVER FAILURE`) — Single-Case Deep Dive

### Quantified Headline
**Why tasks died at $t \approx 39\text{s}$ AFTER heartbeats recovered at $t \approx 21\text{s}$ — and how two distinct `50s` windows fixed it.**

> **Observed Log Quote**: At `~21s` after the cloud platform confirmed the non-Leader Server VM stopped, the Client logged a successful heartbeat to a healthy Server. Yet at `~39s` the original task began `Killing`, and at `~44s` the active HTTP NDJSON stream closed.

| Decision Dimension | Badge | Core Finding | Confidence | Action Gate | Key Distribution Metrics |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **`baseline_paradox_root_cause`** | `choice` | `yamux` Keepalive (`30s` interval + `10s` Pong = `10–40s`) lost the race against the Leader timer (`10–20s TTL + 10s grace = 20–30s`); reconnecting pulled the already-issued `stop` plan | `100%` | `Send to a human` | `client-proxy` replaced `66.7%` (2/3) · `Orchestrator` replaced `35.0%` (7/20) · `session-proxy` replaced `35.0%` (7/20) |
| **`solution_1_disconnect_validation`** | `score` | With `lost_after = "50s"`, `replace = false`, `reconcile = "keep_original"`, allocations entered `unknown` for `1.7s–31.6s` and reconciled cleanly to `running` | `100%` | `Act automatically` | Sandbox preservation `100%` (10/10) · NDJSON long streams `100%` (23/23) · Max `unknown` vs window `63.2%` (31.6s/50s) |
| **`solution_2_grace_vs_capacity`** | `score` | With `server { heartbeat_grace = "50s" }`, the `60s–70s` Leader budget absorbed `yamux` failover; `20/20` Clients stayed `ready` across 2 rounds | `98%` | `Act automatically` | Surviving Clients `ready` `100%` (20/20) · E2B API ready pool `100%` (20/20) · Max `yamux` switch vs budget `61.5%` (40s/65s) |

---

## Card 3 (`3 / 7` · `WHAT I TESTED`) — 9-Scenario Evaluation Matrix (Scorecard)

| SCENARIO | QUESTION / TASK | MODEL / SYSTEM ANSWER | PROB / SCORE | PASS | ACTION |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Baseline · Default Control Plane (`grace=10s`)** | `Orchestrator` task group (20 Nomad Clients, 1 of 3 Servers stopped, 11m window) | `13/20` retained \| **`7/20` (`35.0%`) replaced** despite healthy Client hosts | `65%` | ✕ | `Human` |
| **Baseline · Default Control Plane (`grace=10s`)** | `session-proxy` task group (20 Nomad Clients, 1 of 3 Servers stopped, 11m window) | `13/20` retained \| **`7/20` (`35.0%`) replaced** after Client reconnected at $t \approx 21\text{s}$ | `65%` | ✕ | `Human` |
| **Baseline · Default Control Plane (`grace=10s`)** | `client-proxy` shared ingress (3 allocations, 1 of 3 Servers stopped, 11m window) | `1/3` retained \| **`2/3` (`66.7%`) replaced**, breaking active user streams at $t \approx 44\text{s}$ | `33%` | ✕ | `Human` |
| **Solution 1 · `disconnect` (`lost_after=50s`, `replace=false`)** | `Orchestrator` + `session-proxy` + `client-proxy` allocation retention (`unknown` `1.7–31.6s`) | **`43/43` (`100%`) allocations preserved**; `0` task restarts on reconnect | `100%` | ✓ | `Auto` |
| **Solution 1 · `disconnect` (`lost_after=50s`, `replace=false`)** | Running Firecracker sandbox state (process PIDs, memory pages & files) | **`10/10` (`100%`) sandboxes preserved** across independent post-fault checks | `100%` | ✓ | `Auto` |
| **Solution 1 · `disconnect` (`lost_after=50s`, `replace=false`)** | Active user traffic (`23` HTTP NDJSON long streams + `12,581` short requests) | **`23/23` (`100%`) NDJSON streams held \| `12,581/12,581` short requests (`0` errors)** | `100%` | ✓ | `Auto` |
| **Solution 1 · Creation Capacity Blast Radius** | E2B API placement pool (`Filter: Status == 'ready'` / `ClientStatus == 'running'`) | **`13/20` (`65.0%`) ready nodes**; 7 disconnected nodes temporarily dropped (`+53.8%` load) | `65%` | ✕ | `Confirm` |
| **Solution 2 · Server `heartbeat_grace = 50s`** | 20 surviving Nomad Clients across 2 full fault-injection test rounds (`60–70s` budget) | **`20/20` (`100%`) Clients stay `ready`** (`0` down/disconnected, `0` replacements) | `100%` | ✓ | `Auto` |
| **Solution 2 · Real Host Crash Trade-Off** | Nomad heartbeat-layer detection latency when a physical Client host genuinely crashes | Delayed from `20–30s` to **`60–70s` (`+40s`)**; requires gRPC app health checks to fence | `57%` | ✕ | `Confirm` |

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`) — Source Call Chain & Protocol Verification

### Pinned Upstream Code Contracts (`hashicorp/nomad@bf24b0dd` · `hashicorp/yamux@v0.1.2` · `e2b-dev/runtime@afaaeaef`)

```json
{
  "nomad_heartbeat_and_reconciler_contract": {
    "client_heartbeat_rpc": "client/client.go#L2236: c.RPC('Node.UpdateStatus', {NodeID, Status: 'ready'}) -> resp.HeartbeatTTL",
    "client_failover_wait": "client/rpc.go#L83 + yamux@v0.1.2/session.go#L327: 30s Keepalive + 10s Pong -> 10-40s silent drop wait",
    "leader_timer_formula": "nomad/heartbeat.go#L93: resetHeartbeatTimerLocked(id, ttl + HeartbeatGrace)",
    "leader_expiry_branch": "nomad/heartbeat.go#L137: Status = Down; if canDisconnect && hasPendingReconnects -> Disconnected",
    "disconnect_expiry": "nomad/structs/alloc.go#L756: lastUnknown.Add(tg.GetDisconnectLostAfter())",
    "reconciler_guard": "scheduler/reconciler/filters.go#L527: if isDisconnecting && !alloc.ReplaceOnDisconnect() { return }",
    "reconnect_kill_trigger": "client/allocrunner/alloc_runner.go#L1078: if !ar.Alloc().TerminalStatus() && update.TerminalStatus() -> killTasks()"
  }
}
```

`↓ Tuned HCL Configuration + E2B Upper-Layer Placement Filter Interaction`

```hcl
# 1. Nomad Server Config (extend pre-disconnect switch budget from 20-30s to 60-70s)
server {
  heartbeat_grace = "50s"
}

# 2. Nomad Job Task Group Config (apply to orchestrator, session-proxy, AND client-proxy)
group "orchestrator" {
  disconnect {
    lost_after = "50s"           # Window starts at tU (when alloc enters unknown ~25s), expires at tU+50s (~75s+)
    replace    = false           # Do not spawn replacement allocation while disconnecting
    reconcile  = "keep_original" # Retain original running allocation upon reconnection
  }
}
```

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`) — Policy Perturbation & Trade-Off Matrix

| QUESTION / DIMENSION | SELECTED COMPARISON | ORIGINAL (%) | TUNED (%) | CHANGE (PTS) | HELD / IMPROVED |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **`Orchestrator` Retention** | Baseline (no `disconnect`) $\rightarrow$ Solution 1 (`disconnect 50s`) | `65.0%` | `100.0%` | **`+35.0`** | ✓ |
| **`session-proxy` Retention** | Baseline (no `disconnect`) $\rightarrow$ Solution 1 (`disconnect 50s`) | `65.0%` | `100.0%` | **`+35.0`** | ✓ |
| **`client-proxy` Ingress Retention** | Baseline (no `disconnect`) $\rightarrow$ Solution 1 (`disconnect 50s`) | `33.3%` | `100.0%` | **`+66.7`** | ✓ |
| **New Sandbox Placement Pool** | Solution 1 (`grace=10s`) $\rightarrow$ Solution 2 (`grace=50s`) | `65.0%` | `100.0%` | **`+35.0`** | ✓ |
| **Real Client Crash Fencing Speed** | Default (`grace=10s`, $\le 30\text{s}$) $\rightarrow$ Extended (`grace=50s`, $\le 70\text{s}$) | `100.0%` | `42.9%` | **`-57.1`** | ✕ (Trade-off) |

---

## Card 6 (`6 / 7` · `LATENCY`) — Control-Plane Timing Windows: Lower/Before vs. Upper/After Bounds (ms)

| Row (`#`) | Timing Window Comparison | Lower / Before (`ms`) | Upper / After (`ms`) | Architectural Meaning |
| :---: | :--- | :---: | :---: | :--- |
| **`#1`** | Dynamic Heartbeat `TTL` (`15s` illustrative) vs. Default Leader Budget (`TTL + 10s grace = 25s`) | `15,000 ms` | `25,000 ms` | Default configuration leaves only `10,000 ms` grace margin |
| **`#2`** | `yamux` Silent Drop Min Detection (`10s` Pong) vs. Max Detection (`30s` Ping + `10s` Pong = `40s`) | `10,000 ms` | `40,000 ms` | Upper half (`25,000–40,000 ms`) exceeds `#1`'s default Leader budget |
| **`#3`** | Observed Log Heartbeat Recovery ($t \approx 21\text{s}$) vs. Local Task `Killing` ($t \approx 39\text{s}$) | `21,000 ms` | `39,000 ms` | Client pulls and executes the `stop` plan `18,000 ms` after reconnecting |
| **`#4`** | Max Observed `unknown` Duration (`31.6s`) vs. Configured `lost_after` Limit (`50.0s`) | `31,600 ms` | `50,000 ms` | Leaves `18,400 ms` (`36.8%`) safety margin, achieving `0` replacements |
| **`#5`** | Default Leader Illustrative Budget (`25s`) vs. `heartbeat_grace = 50s` Budget (`65s`) | `25,000 ms` | `65,000 ms` | `65,000 ms` budget fully absorbs `#2`'s `40,000 ms` max `yamux` failover |
| **`#6`** | Real Host Crash Max Detection under Default (`30s`) vs. `grace = 50s` (`70s`) | `30,000 ms` | `70,000 ms` | `grace = 50s` adds `+40,000 ms` heartbeat delay for true host crashes |

---

## Card 7 (`7 / 7` · `MY TAKE`) — Good Fit vs. Not For & Production Readiness

### ✅ Good Fit
- **Defense-in-Depth Pairing**: Combine a moderate Server `heartbeat_grace` with task-group `disconnect { lost_after = "50s", replace = false, reconcile = "keep_original" }`.
- **Full Access-Path Coverage**: Apply `disconnect` policies to `Orchestrator`, `session-proxy`, AND `client-proxy` task groups.
- **Dual-Layer Health Fencing**: Use active `Orchestrator` gRPC application health checks (not just Nomad node status) to fence genuinely dead hosts within seconds.
- **Capacity Headroom Sizing**: Reserve $\ge 35\%$ N+1 creation headroom if relying on short `heartbeat_grace` + `disconnect` during Server maintenance.

### ⛔ Not For
- Running stateful Firecracker `Orchestrator` instances under Nomad's default disconnect behavior (immediate `stop`/`lost` on a `20–30s` heartbeat timeout).
- Protecting only `Orchestrator` while leaving `client-proxy` (`2/3` replaced in baseline) or `session-proxy` (`7/20` replaced) on default replacement rules.
- Confusing `lost_after = "50s"` (starts when the allocation enters `unknown` at $t_U \approx 25\text{s}$) with `heartbeat_grace = "50s"` (extends the pre-disconnect timer).
- Setting extreme `heartbeat_grace` values without an independent fast health check to stop routing new sandboxes to genuinely crashed hosts.

### Provenance & Verification
- **Provenance**: `anonymized_reported` + `static_source_verified` (`independently_reproduced = false`; derived from the published fault-injection case study and verified line-by-line against pinned upstream commits, with `6/6` deterministic unit tests passing).
- **Pinned Sources**: `hashicorp/nomad@bf24b0dd97430d3b364b68b1f7375e85e585778f` · `hashicorp/yamux@v0.1.2` · `e2b-dev/runtime@afaaeaef96aae86f65ce60bf38fe083e7638a28e` · `hashicorp/nomad#17974`.
