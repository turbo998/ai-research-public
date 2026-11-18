# Azure AI Agent Infrastructure Playbook: 6-Runtime & 12-Scenario Architecture Benchmark Report (7-Card 4:5 Edition)

> 🌐 **Language / 语言切换**: **[🇬🇧 English Report (test-report.en.md)](test-report.en.md)** | **[🇨🇳 中文评测报告 (test-report.md)](test-report.md)** | **[📊 7-Card HTML (`cards.html`)](cards.html)** | **[📘 Playbook (EN)](README.en.md)**

**Provenance**: `anonymized_reported + deterministic_architecture_verifier (independently_reproduced=false)`, synthesized from de-identified Microsoft Azure AI Infrastructure field architecture specs (`Agent Runtime Pitch`, `AKSClaw Multi-Tenant Kubernetes`, `Agent Infra Playbook`, `E2B on Azure CheckRide v2`) and verified by [`simulator/agent_infra_sizer.py`](simulator/agent_infra_sizer.py).

Artifacts:
- [CSP-Locked 7-Card 4:5 HTML Deck (`cards.html`)](cards.html) · [`test-report-cards.html`](test-report-cards.html)
- [Structured Benchmark Telemetry (`report.json`)](report.json)
- [12-Scenario Matrix CSV (`evidence/test-scenarios.csv`)](evidence/test-scenarios.csv) · [Robustness CSV (`evidence/test-robustness.csv`)](evidence/test-robustness.csv) · [Startup Latency CSV (`evidence/test-batch-latency.csv`)](evidence/test-batch-latency.csv)

---

## Card 1 (`1 / 7` · `HANDS-ON · AZURE AI AGENT INFRASTRUCTURE BENCHMARK`) — Overview & Workbench

**Headline Finding**: **6 Azure Agent Runtimes, 108ms MicroVM restore** — complementary 6-tier runtime spectrum with measured `108 ms` Base / `132 ms` Code-Interpreter V1 restore on `Standard_D96as_v7` (5th-Gen AMD EPYC Turin + Azure Boost).

| Workbench Decision | Type | Evaluation Question | Verdict | Confidence | Action Tier | Distribution Summary |
|---|---|---|---|---:|---|---|
| `e2b_turin_v7_speedup` | `choice` | Does `Standard_D96as_v7` (AMD Turin + Azure Boost) outperform `D96s_v6` and `D96as_v6` on E2B sandbox restore? | `108 ms Base / 132 ms Code-Interpreter V1` | `0.926` (`92.6%`) | `Act automatically` | `D96as_v7`: 108/132 ms; `D96s_v6`: 116/159 ms; `D96as_v6`: 239/255 ms |
| `aksclaw_security_enforcement` | `choice` | Are all 5 `AKSClaw` multi-tenant security boundaries enforced by the platform rather than prompt rules? | `5 / 5 platform hard boundaries (100.0%)` | `1.000` (`100.0%`) | `Act automatically` | IMDS block, egress allowlist, keyless proxy, Entra Agent ID, Unified AI Gateway |
| `playbook_delivery_gate` | `score` | When deep infra control is required without an internal ops team, can SA default back to Foundry Hosted Agents? | `0% shortcut allowed (Hold for CSU / Partner)` | `0.750` (`75.0%`) | `Send to a human` | 9/12 positive matches, 3/12 anti-patterns intercepted |

---

## Card 2 (`2 / 7` · `SCENARIO: MANUS × E2B 100K+ VIRTUAL COMPUTERS & AKSCLAW FLEET`) — Deep Dive

**Headline Finding**: **261 D96as_v7 nodes serve 100K sandboxes at 108ms** within a single Azure VMSS Flexible scale set (`26.1%` of the 1,000-VM ceiling).

| Decision Field | Type | Question | Result | Confidence | Action Tier | Basis |
|---|---|---|---|---:|---|---|
| `vmss_100k_capacity_fit` | `choice` | Can 100,000 concurrent 512 MiB E2B sandboxes run inside a single Azure VMSS Flexible scale set (1,000-VM limit)? | `Yes · 261 Client Nodes (26.1% of limit)` | `0.850` | `Act automatically` | 384 GiB × 85% HugePages × 60% headroom = 384 steady-state sandboxes/node |
| `apim_appgw_dual_hop_isolation` | `noul` | Does `AppGW WAF v2` + `APIM rate-limit-by-key` isolate 100K+ dynamic sandbox subdomains with WebSocket pass-through? | `Yes (100% per-Host isolation)` | `P(true) = 1.0` | `Act automatically` | Keyed on `@(context.Request.Headers.GetValueOrDefault("Host"))` |
| `upstream_e2b_production_readiness` | `score` | Is stock upstream E2B API server horizontally scalable and reboot-resilient out of the box? | `1 / 4 HA criteria met (25.0%)` | `0.250` | `Confirm` | Single-process in-memory node state requires external state & orphan GC hardening |

---

## Card 3 (`3 / 7` · `WHAT I TESTED`) — 12-Scenario Evaluation Matrix

| Scenario | Workload & Governance Requirement | Evaluated Architecture | Pass | Action |
|---|---|---|---:|---|
| `S01 · Customer-Facing Agent` | 30K+ monthly sessions, ~75% autonomous resolution over banking APIs | `Foundry + ACA/AKS + Cosmos DB (100%)` | Yes | `Auto` |
| `S02 · Customer-Facing Agent` | Burst execution of untrusted LLM-generated Python scripts & file parsing | `ACA Apps + Dynamic Sessions (100%)` | Yes | `Auto` |
| `S03 · Digital-Native AI Product` | Custom OCI image, persistent workspace files, explicit pause/resume | `ACA Sandboxes Preview + HorizonDB (92%)` | Yes | `Confirm` |
| `S04 · Digital-Native AI Product` | `<150 ms` Firecracker MicroVM restore, per-Host rate limit, WebSocket desktop | `E2B on VMSS D96as_v7 108ms/132ms (100%)` | Yes | `Auto` |
| `S05 · Enterprise Agent Platform` | Per-engineer persistent agent, BYO harness, autonomous SRE triage | `AKSClaw 5-Boundary Runtime on AKS (100%)` | Yes | `Auto` |
| `S06 · Multi-Agent Workflow` | Multi-agent review + mandatory human approval wait + deterministic replay | `Durable Functions + ACA Apps + DB (100%)` | Yes | `Auto` |
| `S07 · Multi-Agent Workflow` | LangGraph triage -> GitHub Copilot SDK coding agent -> Foundry compliance | `MAF + GH Copilot SDK + Foundry (100%)` | Yes | `Auto` |
| `S08 · Agent Factory` | Internal B2E copilots needing SAP/Salesforce/M365 MCP connectors with low ops | `Foundry Hosted Agents + MCP Toolboxes (100%)` | Yes | `Auto` |
| `S09 · Regulated Industry Agent` | Deep infra control required, but customer has NO engineering/ops team | `Direct Foundry fallback rejected; CSU/Partner gate (0%)` `✕` | No | `Human` |
| `S10 · Enterprise Agent Platform` | Stock open-source E2B API server multi-node failover without state externalization | `In-memory node state lost on reboot (25%)` `✕` | No | `Confirm` |
| `S11 · Regulated Industry Agent` | Assuming raw ACA/AKS container deployment automatically enables Entra Agent ID | `Requires explicit Agent ID + Gateway key custody (33%)` `✕` | No | `Confirm` |
| `S12 · Agent Factory` | Account below `$10,000/mo` model spend evaluated via non-model foundation readiness | `Qualifies via Specific or General+3 Foundations (100%)` | Yes | `Auto` |

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`) — APIM Per-Host Rate Limiting & AKSClaw Hard Boundaries

```xml
<!-- 1. E2B on Azure: APIM Per-Sandbox Dynamic Subdomain Rate Limit (<port>-<sandboxId>.domain.com) -->
<inbound>
  <base />
  <rate-limit-by-key calls="300" renewal-period="60"
    counter-key="@(context.Request.Headers.GetValueOrDefault(&quot;Host&quot;, &quot;unknown&quot;))"
    increment-condition="@(context.Response.StatusCode &gt;= 200 &amp;&amp; context.Response.StatusCode &lt; 400)" />
  <set-backend-service base-url="http://10.240.0.10:8080" />
</inbound>
```

` ↓ Combined with AKSClaw Kata Pod VM + Entra Agent ID + Keyless AI Gateway ↓ `

```yaml
# 2. AKSClaw Kata Pod VM + Zero-Key AI Gateway Contract
runtimeClassName: kata-mshv-vm-isolation
serviceAccountName: entra-agent-id-alice
env:
  - name: OPENAI_BASE_URL
    value: "http://ai-gateway.platform.svc.cluster.local/v1"
# Zero LLM API keys in container; NetworkPolicy blocks 169.254.169.254 IMDS -> <answer>
```

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`) — Silicon Generation & Control-Boundary Perturbations

| Dimension | Comparison (`Baseline` vs. `Upgraded / Hardened`) | Baseline % | Hardened % | Delta (pts) | Invariant Holds |
|---|---|---:|---:|---:|---|
| `E2B Code-Interpreter V1: Intel v6 vs AMD Turin v7` | `D96s_v6` (159 ms -> `62.9%` index) vs `D96as_v7` (132 ms -> `75.8%` index) | `62.9` | `75.8` | `+12.9` | Yes |
| `E2B Base MicroVM: AMD Genoa v6 vs AMD Turin v7` | `D96as_v6` (239 ms -> `41.8%` index) vs `D96as_v7` (108 ms -> `92.6%` index) | `41.8` | `92.6` | `+50.8` | Yes |
| `Workspace Persistence Across Idle Reclamation` | ACA Dynamic Sessions (`0%` local disk kept) vs ACA Sandboxes + HorizonDB (`100%`) | `0.0` | `100.0` | `+100.0` | Yes |
| `Prompt Injection / --yolo Resistance` | In-agent soft rules (`0%` hard immunity) vs AKSClaw 5 platform boundaries (`100%`) | `0.0` | `100.0` | `+100.0` | Yes |
| `VMSS Autoscaling Asymmetry` | CPU scale-out (`60%`) vs HugePages drain-gated scale-in (`100%` safe drain) | `100.0` | `100.0` | `0.0` | Yes |

---

## Card 6 (`6 / 7` · `LATENCY & STARTUP SCALING`) — Sandbox Allocation & Restore Latency

| Tier | Optimized Path (`#3B82F6`) | Baseline Path (`#CBD5E1`) | Source |
|---|---|---|---|
| `E2B Base Sandbox (Turin v7 vs Genoa v6)` | **108 ms (`D96as_v7` + `UFFD`)** | 239 ms (`D96as_v6`) | Measured (`CheckRide v2` Slide 19) |
| `E2B Base Sandbox (Turin v7 vs Intel v6)` | **108 ms (`D96as_v7`)** | 116 ms (`D96s_v6`) | Measured (`CheckRide v2` Slide 19) |
| `E2B Code-Interpreter V1 (Turin v7 vs Genoa v6)` | **132 ms (`D96as_v7` + Jupyter)** | 255 ms (`D96as_v6`) | Measured (`CheckRide v2` Slide 19) |
| `E2B Code-Interpreter V1 (Turin v7 vs Intel v6)` | **132 ms (`D96as_v7`)** | 159 ms (`D96s_v6`) | Measured (`CheckRide v2` Slide 19) |
| `ACA Dynamic Sessions (Warm Pool vs Cold)` | **~210 ms (Pre-Warmed Hyper-V)** | ~2,200 ms (Cold Container) | Architecture reference model |
| `ACA Sandboxes (Snapshot Resume vs Cold Rebuild)` | **~320 ms (Snapshot Resume)** | ~1,650 ms (Cold OCI + Volume) | Architecture reference model |

---

## Card 7 (`7 / 7` · `MY TAKE`) — Good Fit vs. Not For

- **✅ Good Fit**:
  - **Foundry Hosted Agents** for governed enterprise B2E/B2B copilots over M365/SAP/Salesforce MCP connectors with minimal ops overhead.
  - **Durable Functions** for multi-day human approvals and event-driven transactional sagas.
  - **ACA Dynamic Sessions / Sandboxes** for burst untrusted Python execution (`~210 ms`) or snapshot-resumable developer workspaces.
  - **AKS + Kata (`AKSClaw`)** for multi-tenant enterprise agent factories with 5 hard platform security boundaries.
  - **E2B on Azure VMSS (`D96as_v7`)** for 10K–100K+ sub-150ms cloud virtual computers.
- **⛔ Not For**:
  - Do **not** route deep-control workloads without an engineering team into Foundry Hosted Agents as a shortcut—require CSU/Partner delivery ownership.
  - Do **not** store durable state on ACA Dynamic Sessions local disk or embed LLM API keys inside agent containers.
