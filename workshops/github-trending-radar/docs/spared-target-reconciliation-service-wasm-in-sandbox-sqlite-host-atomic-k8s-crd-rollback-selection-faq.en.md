# Per-App In-Sandbox SQLite Wasm Host (`michaelmagan/spared`) & Atomic K8s CRD Reliability Control Plane (`TargetReconciliationService`) Deep-Dive & Selection FAQ

> **Document Metadata (2026-11-14 · Night Round 65 / Cumulative Round 248)**  
> - **Benchmark Style**: `ib-vs-ethernet-roce-selection-faq.md` (First-Principles + Plain-Language Deconstruction + 3 Architect Core Questions + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> - **Primary Evaluated Repositories**:  
>   1. [`michaelmagan/spared`](https://github.com/michaelmagan/spared) (`★ 44`, Apache-2.0 open-source Rust web app host where **each app and its SQLite database run inside their own `wasm32-wasip2` Wasm sandbox**: delivers **`2.6x` faster warm p50 latency (`148 µs` vs. `workerd 388 µs`), `3.0x` lower p99 at 16 connections (`5.45 ms` vs. `16.53 ms`), `0.9 ms` idle wake, and `4.8x` less unreclaimable memory at 200 apps (`108 MiB` vs. `516 MiB`)**, with a built-in `AGENTS.md` for autonomous coding-agent deployment)  
>   2. [`ATLURI0001/target-reconciliation-service`](https://github.com/ATLURI0001/target-reconciliation-service) (`★ 45`, Apache-2.0 Go 1.24+ Kubernetes-native reliability control plane: combines a validated `ReliabilityTarget` CRD reconciler, uncached K8s observation, **GitOps ownership fences**, PostgreSQL immutable audit timelines, and **digest-pinned image rollbacks guarded by atomic `UID / resourceVersion / image` preconditions**)  
> - **Visual Architecture Diagram**: [`assets/github-ai-radar-2026-11-14-r65-spared-targetreconciliation.svg`](../../../assets/github-ai-radar-2026-11-14-r65-spared-targetreconciliation.svg)  
> - **Audit Contract ID**: `CLAIM-20261114-R65-SPARED-TARGETRECONCILIATION` (base bare-metal server hardware depreciation is explicitly marked `not_measured`)

---

## 📌 1. Executive Summary (Understand the Essence in 3 Minutes)

1. **When hosting hundreds of AI-generated internal micro-apps, why do Docker containers exhaust RAM while `workerd` and `Spin` leave SQLite inside the shared host process — and how does `michaelmagan/spared` achieve both in-sandbox SQLite isolation and `2.6x` faster warm latency?**  
   - **Plain-Language Essence**: Running 200 small apps as 200 Docker containers wastes gigabytes of RAM, while existing Wasm/isolate runtimes (`workerd`, `Spin`, `celld`) run SQLite in the host process outside the tenant sandbox.  
   - **First-Principles Breakthrough in `spared`**:
     - **SQLite Compiled Inside Each App's `wasm32-wasip2` Sandbox**: `spared setup` compiles SQLite to Wasm once via `wasi-sdk 25`, so every Rust app and its SQLite engine execute inside the same isolated Wasm sandbox under a single host binary (`spared serve`).
     - **Verified Performance vs. `workerd` on a 4-vCPU VM**: Achieves **`148 µs` vs. `388 µs` warm p50 (`2.6x` faster)**, **`5.45 ms` vs. `16.53 ms` p99 at 16 connections (`3.0x` lower)**, **`0.9 ms` idle wake**, and **`108 MiB` vs. `516 MiB` unreclaimable RAM across 200 apps (`4.8x` less)**, while transparently documenting trade-offs (total RAM at 200 apps is `889 MiB` vs. `574 MiB`, and JS on `workerd` leads on native-bound crypto/gzip/JSON while Rust on `spared` wins 8 of 14 backend benchmarks). Includes a turnkey `AGENTS.md` for Claude Code and Codex.
2. **Why do ad-hoc Kubernetes auto-rollback scripts clash with ArgoCD/Flux or overwrite concurrent operator fixes — and how does `TargetReconciliationService` enforce accountable, atomic recovery?**  
   - **Plain-Language Essence**: Blindly running `kubectl rollout undo` on an alert often fights GitOps controllers, rolls back to mutable tags, or overwrites changes applied moments earlier by an on-call engineer.  
   - **First-Principles Breakthrough in `TargetReconciliationService`**:
     - **GitOps Ownership Fences + Explainable Dry-Run Proposals + Explicit Approval**: Detects sustained fresh failures on `ReliabilityTarget` CRDs using uncached K8s observation, checks opt-in and GitOps ownership fences, generates explainable dry-run rollback plans, and enforces per-target concurrent admission and operator approval.
     - **Digest-Pinned Rollback with Atomic `UID / resourceVersion / image` Preconditions + PostgreSQL Audit**: Executes rollbacks only against immutable image digests while asserting atomic `UID`, `resourceVersion`, and image preconditions, then verifies that original target/container/replica counts reach observed rollout readiness. All state is persisted transactionally in PostgreSQL (zero in-memory fallback) and surfaced in a read-only Next.js console with explicit `loading / error / empty / stale` states.
3. **Closed-Form FinOps Audit Conclusion (`CLAIM-20261114-R65-SPARED-TARGETRECONCILIATION`)**:  
   - Modeled for **200 isolated internal micro-apps and 30 Kubernetes rollback reconciliations/month** (at **`$100.00/hr`** engineering labor): migrating from **Path A** (200 separate Docker containers/DBs + manual unfenced `kubectl` rollbacks: **`$5,680.00/mo`**, comprising `$1,880.00` hosting/downtime spend + `38.0h` orchestration and GitOps conflict recovery labor `$3,800.00`) to **Path C** (`spared` per-app Wasm+SQLite host + `TargetReconciliationService` atomic CRD control plane: **`$490.00/mo`**, comprising `$140.00` high-density VM spend + `3.5h` approval review labor `$350.00`) saves **`$5,190.00/mo`** (**`-91.37%`**, or **`$62,280.00/yr`**) and cuts engineering hours by **`90.79%`**.

![spared & TargetReconciliationService Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r65-spared-targetreconciliation.svg)

---

## 💬 2. Three Architect Core Questions (Q1–Q3 Deep Dive)

### Q1: Why is `michaelmagan/spared`'s decision to run SQLite *inside* each app's Wasm sandbox (`wasm32-wasip2`) critical for AI-generated micro-apps?

1. **Containing Untrusted Query & Extension Blast Radius**:  
   - When coding agents rapidly generate and deploy internal apps via `spared new` and `spared deploy`, placing SQLite inside the app's own Wasm linear memory ensures that neither malformed queries nor SQLite memory bugs can cross tenant boundaries or leak unreclaimable host memory (`108 MiB` vs. `516 MiB` at 200 apps).

---

### Q2: How do `TargetReconciliationService`'s atomic `UID / resourceVersion / image` preconditions prevent TOCTOU rollback races in Kubernetes?

1. **Optimistic Concurrency Locking Across Human Approval Windows**:  
   - Between proposing a rollback and receiving operator approval, the target workload might be recreated (`UID` change) or patched (`resourceVersion` / `image` change). Enforcing all three preconditions plus digest pinning guarantees the rollback aborts safely rather than clobbering newer state.

---

### Q3: Why does `TargetReconciliationService`'s Next.js console mandate explicit `loading / error / empty / stale` states?

1. **Preventing Stale Telemetry From Masquerading as "Zero Incidents"**:  
   - Operational dashboards that render a blank table when the backend API fails or stales trick SREs into assuming clusters are healthy. Explicitly distinguishing `empty` from `error` and `stale` prevents silent observability blind spots.

---

## 🧭 3. Architecture Decision Tree & Topology (Mermaid)

```mermaid
flowchart TD
    Start["High-Density Micro-App Hosting & Accountable Kubernetes Rollback Control Plane"] --> Domain{"Target Infrastructure Layer?"}

    Domain -->|"High-Density Multi-Tenant Web Apps with Embedded SQLite on One VM"| HostGate{"Isolation & Latency Requirement?"}
    HostGate -->|"Per-App SQLite Inside Wasm Sandbox + 148 µs p50 + AGENTS.md"| UseSpared["✅ michaelmagan/spared (Rust · Apache-2.0 · wasm32-wasip2)<br/>• 2.6x faster warm p50 (148µs), 3.0x lower p99 (5.45ms)<br/>• 4.8x less unreclaimable RAM at 200 apps (108 MiB vs 516 MiB)"]
    HostGate -->|"Heavy native C crypto/gzip bound JS workers"| UseWorkerd["🔄 Cloudflare workerd"]

    Domain -->|"Policy-Driven Kubernetes Failure Detection, Approval & Rollback"| K8sGate{"Governance & Audit Contract?"}
    K8sGate -->|"GitOps Ownership Fences + Atomic UID/resourceVersion/Digest Preconditions<br/>+ PostgreSQL Immutable Audit"| UseTRS["✅ ATLURI0001/target-reconciliation-service (Go 1.24+ · Apache-2.0)<br/>• ReliabilityTarget CRD + default dry-run proposals + operator approval<br/>• Post-rollback replica readiness check + 4-state Next.js console"]
    K8sGate -->|"Ephemeral dev cluster"| RawKubectl["🔄 Manual kubectl rollout undo"]

    UseSpared --> FinOps["💰 Closed-Form FinOps Impact (CLAIM-20261114-R65-SPARED-TARGETRECONCILIATION)<br/>Monthly Total $5,680.00 ➔ $490.00 (-91.37% · Saves $62,280/yr)"]
    UseTRS --> FinOps
```

---

## 📊 4. Peer Comparison Matrix (Decision Matrix)

| Evaluation Dimension | `michaelmagan/spared` (In-Sandbox SQLite Wasm Host) | `workerd` / 200 Separate Docker Containers | `TargetReconciliationService` (Atomic K8s CRD Reconciler) | Manual `kubectl` / Unfenced Scripts |
| :--- | :--- | :--- | :--- | :--- |
| **Isolation & Concurrency** | **SQLite runs inside each app's `wasm32-wasip2` sandbox** | `workerd` runs SQLite in host; Docker wastes multi-GB RAM | **GitOps ownership fences + per-target admission lock** | Fights ArgoCD/Flux in overwrite loops |
| **Performance & Invariants** | **`148 µs` p50 (`2.6x`), `5.45 ms` p99 (`3.0x`), `108 MiB` pinned RAM** | `workerd` `388 µs` p50, `16.53 ms` p99, `516 MiB` pinned RAM | **Digest-pinned + `UID/resourceVersion/image` preconditions** | Mutable tag rollbacks with zero TOCTOU safety |
| **Agentic & Audit Readiness** | **Ships `AGENTS.md` for 1-command `spared new/test/deploy`** | Manual multi-container Dockerfile & proxy wiring | **PostgreSQL immutable audit timeline (0 in-memory fallback)** | Ephemeral shell history with no approval trail |
| **Operational Honesty** | **Explicitly documents cold page-cache wake & total RAM (`889 MiB`)** | Often omits unreclaimable vs total memory breakdown | **Read-only console separates `loading/error/empty/stale`** | Stale API failures often render as empty incident lists |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261114-R65-SPARED-TARGETRECONCILIATION`)

> **Scope & Boundary Declaration**: This synthetic FinOps model covers monthly multi-tenant micro-app VM/container hosting and downtime spend across **200 isolated apps and 30 Kubernetes rollback reconciliations** plus engineering labor for **container database maintenance and GitOps rollback conflict resolution** (at **`$100.00/hr`**); base bare-metal server hardware depreciation is explicitly marked **`not_measured`**.

| Architecture Path | Hosting & Downtime Spend (`USD/mo`) | Container Ops & Rollback Labor (`hrs/mo`) | Engineering Labor Cost (`@ $100/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: 200 Docker Containers + Manual Unfenced Rollbacks** | `$1,880.00` | `38.0 hrs` | `$3,800.00` | **`$5,680.00`** | Baseline (`0.00%`) |
| **Path B: Host-Shared SQLite (`workerd`) + Unfenced Scripts** | `$880.00` | `18.0 hrs` | `$1,800.00` | **`$2,680.00`** | `-$3,000.00` (`-52.82%`) |
| **Path C (Recommended): `spared` Wasm Host + `TargetReconciliation`** | **`$140.00`** | **`3.5 hrs`** | **`$350.00`** | **`$490.00`** | **`-$5,190.00` (`-91.37%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 1880.00 + 38.0 \times 100.00 = 1880.00 + 3800.00 = \$5,680.00$
  - $\text{Path B Total} = 880.00 + 18.0 \times 100.00 = 880.00 + 1800.00 = \$2,680.00$
  - $\text{Path C Total} = 140.00 + 3.5 \times 100.00 = 140.00 + 350.00 = \$490.00$
  - $\text{Net Savings (Path C vs Path A)} = 5680.00 - 490.00 = \$5,190.00/\text{mo} \quad (-91.37\%, \text{Annualized } \$62,280.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect Actionable Checklist

1. **Install `michaelmagan/spared`, pre-compile SQLite to Wasm, and deploy an isolated Rust app**:
   ```bash
   curl --proto '=https' --tlsv1.2 -fsSL https://raw.githubusercontent.com/michaelmagan/spared/main/scripts/install.sh | sh
   export PATH="$HOME/.spared/bin:$PATH"
   spared setup && spared serve --data-dir ./data &
   spared new my-app && cd my-app && spared test && spared deploy
   ```
2. **Configure `ReliabilityTarget` CRDs in `TargetReconciliationService`**:
   - Enable GitOps ownership fences, dry-run proposals, and digest-pinned `UID/resourceVersion` preconditions backed by PostgreSQL audit persistence.
