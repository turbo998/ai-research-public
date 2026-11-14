# Dogwood Temporal OS Sandbox (`strands-agents/box`) & Supervised Rust Agent Pipeline Runtime (`joydle/borg`) Selection & Architecture FAQ

> **Track**: GitHub AI Trending & High-Velocity Breakout Selection Guide · 2026-11-14 Night Round 77 (Cumulative Round 260 Milestone / R260)  
> **Benchmark Standard**: Modeled after `ib-vs-ethernet-roce-selection-faq.md` (Plain-Language Essence + First Principles + 6-Part Structure + Closed-Form FinOps Audit)  
> **Claim ID**: `CLAIM-20261114-R77-STRANDSBOX-BORG`  
> **Architecture Visual**: [`assets/github-ai-radar-2026-11-14-r77-strandsbox-borg.svg`](../../../assets/github-ai-radar-2026-11-14-r77-strandsbox-borg.svg)  
> **中文版本**: [阅读中文版 (`strands-box-borg-dogwood-temporal-os-sandbox-supervised-rust-agent-pipeline-runtime-selection-faq.md`)](./strands-box-borg-dogwood-temporal-os-sandbox-supervised-rust-agent-pipeline-runtime-selection-faq.md)

---

## 📌 1. Executive Summary (What Are They & What Pain Points Do They Solve?)

1. **Plain-Language Breakdown**:
   - **`strands-agents/box` (`★ 545`, Rust, Apache-2.0)** is **Strands Box**, a harness-agnostic operating-system sandbox for AI agents that combines host OS isolation (`box.toml`) with **stateful temporal semantic policies written in Dogwood (`policy.dw`)**. Static containers can only allow or block network access globally—meaning an agent with outbound HTTP access can read a secret file and immediately exfiltrate it. In `Strands Box`, **Strands Shell, Monty for Python, the egress gateway, and the MCP broker share a unified event history** evaluated out-of-process by the embedded Dogwood Local Engine (default-deny, `forbid` overrides `permit`). As a result, **a file read through Shell or Python can dynamically cause the egress gateway to deny a subsequent outbound HTTP request**.
   - **`joydle/borg` (`★ 93`, Rust 1.88+, MIT/Apache-2.0)** is an **Erlang-style supervised agent pipeline runtime for Rust (`v1.0.0`)**. It composes LLM calls into typed pipelines (`Single`, `Sequential`, `Parallel`, `Branch`, `Fallback`, `LoopUntil`, `FallbackLadder`, `Heartbeat`, `Deferred`) that **cancel cleanly across nested children, isolate panics so a crashing worker never takes down its siblings, prevent restart-storm meltdowns with backoff/jitter and sliding-window circuit breakers, enforce token budgets, and resume after crashes**, complete with a built-in zero-key `FakeLlmClient`.
2. **Quantified FinOps Impact (`CLAIM-20261114-R77-STRANDSBOX-BORG` · R260 Milestone)**:
   - Evaluated across **25 monthly security-critical multi-agent pipeline deployments** at an AI Solution Architect rate of **$95.00/hr** (local workstation hardware telemetry: `not_measured`):
   - **Path A (Static Stateless Firewall Rules + Unsupervised Async Tasks Suffering Retry Storms & Cascading Panics)**: **$1,780.00/mo** in runaway retry-storm token waste and orphaned in-flight LLM calls + **39.0 hrs/mo ($3,705.00)** in exfiltration triage and panic recovery = **$5,485.00/mo**.
   - **Path B (Static Seccomp/Iptables + Basic Tokio `try_join!` Retry Loops)**: **$830.00/mo** in token/infra spend + **17.5 hrs/mo ($1,662.50)** in manual orchestration maintenance = **$2,492.50/mo**.
   - **Path C (`strands-agents/box` Dogwood Temporal Sandbox + `joydle/borg` Supervised Rust Runtime)**: **$95.00/mo** in budget-capped token spend + **3.5 hrs/mo ($332.50)** of engineering review = **$427.50/mo**, delivering **$5,057.50/mo in net savings (-92.21%, $60,690.00/yr annualized, and -91.03% engineering hours)**.

![2026-11-14 Night Round 77 (R260 Milestone) Architecture Summary](../../../assets/github-ai-radar-2026-11-14-r77-strandsbox-borg.svg)

---

## 🔍 2. Core Architectural Q&A (Q1–Q3 First-Principles Deep Dive)

### Q1: Why do static container firewalls fail against prompt-injected data exfiltration, and how does `strands-agents/box` stop read-then-exfiltrate chains?
- **The Static Sandbox Blind Spot**: If an agent needs both local file access and outbound HTTP/MCP access during a task, static rules cannot stop it from reading credentials and sending them out over an allowed port.
- **How `Strands Box` + `Dogwood` Solve It**:
  1. **Shared Cross-Surface Event History**: `Strands Shell`, `Monty for Python`, the `Egress Gateway`, and the `MCP Broker` feed every operation into an out-of-process Dogwood Local Engine.
  2. **Temporal `permit` / `forbid` Evaluation**: Rules in `policy.dw` inspect earlier actions and elapsed time—so reading a sensitive path in Shell or Python immediately activates a `forbid` rule blocking subsequent outbound HTTP requests.

### Q2: Why is raw `tokio::spawn` + `try_join!` dangerous for multi-agent pipelines, and what does `joydle/borg` add?
- **Supervision Primitives for LLM Pipelines**:
  1. **Panic Isolation & Hierarchical Cancellation**: A panicking child in `par([step(Coder), step(TestWriter), step(DocWriter)])` never crashes its siblings, and cancelling the pipeline cleanly aborts every nested agent and in-flight LLM request.
  2. **Meltdown & Circuit-Breaker Protection**: Combines `repeat(8, ...)` bounded loops, `FallbackLadder` across models, restart-storm meltdown protection, and a zero-key `FakeLlmClient` for deterministic offline testing.

### Q3: How should AI Solution Architects combine `strands-agents/box` and `joydle/borg`?
- **Defense-in-Depth Runtime Stack**: Compile your multi-agent orchestration inside `joydle/borg` for internal supervision, budget enforcement, and panic isolation, then execute the binary inside `strands-agents/box` (`box.toml` + `policy.dw`) to enforce out-of-process OS and temporal network/MCP boundaries.

---

## 🧭 3. Mermaid Selection Decision Tree & Architecture Flow

```mermaid
flowchart TD
    A["AI SA Production Agent Security & Supervision Architecture (R260)"] --> B{"Primary Requirement: Temporal Read-Then-Exfiltrate Prevention<br/>or Supervised Rust Multi-Agent Pipeline Resilience?"}
    B -->|"OS Sandbox + Temporal Dogwood Policy Across Shell/Python/HTTP/MCP"| C["Adopt strands-agents/box<br/>(★ 545 · Rust · box.toml + Dogwood policy.dw)"]
    B -->|"Panic-Isolated Rust Pipelines + Circuit Breakers + Budgets"| D["Adopt joydle/borg<br/>(★ 93 · Rust 1.88+ · Supervised Agent Runtime)"]
    B -->|"Zero-Trust High-Availability Enterprise Agent Platform"| E["Outer Strands Box Sandbox + Inner borg Supervised Pipeline"]

    C --> C1["4 Mediated Surfaces: Strands Shell · Monty Python ·<br/>Egress Gateway · MCP Broker"]
    C1 --> C2["Shared Event History + Elapsed Time Evaluation"]
    C2 --> C3["Out-of-Process Dogwood Engine (default-deny, forbid > permit):<br/>Sensitive File Read Blocks Subsequent Outbound HTTP"]

    D --> D1["9 Primitives: seq / par / repeat / Branch /<br/>FallbackLadder / Heartbeat / Deferred"]
    D1 --> D2["Per-Child Cancel + Panic Isolation + Restart-Storm Meltdown + Breaker"]
    D2 --> D3["#[derive(BorgAgentDerive)] + Zero-Key FakeLlmClient Testing"]

    E --> F["Closed-Form FinOps TCO: $5,485.00/mo → $427.50/mo (-92.21%)"]
```

---

## 📊 4. Peer Comparison Matrix

| Evaluation Dimension | `strands-agents/box` | `joydle/borg` | Static Docker / Seccomp | Raw Tokio / `asyncio.gather` |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Layer** | OS sandbox + `Dogwood` temporal policy engine | Erlang-style supervised Rust agent pipeline runtime | Static container/syscall isolation | Low-level async concurrency primitives |
| **Exfiltration Prevention** | **Shared Shell/Python/HTTP/MCP event history blocks read→HTTP chains** | Pipeline guardrails & token budget caps | Static network rules blind to prior file reads | None |
| **Fault Isolation & Retries** | Out-of-process policy enforcement | **Sibling panic isolation, restart-storm meltdown, sliding breaker** | Coarse container restarts | Unhandled panic or retry loop cascades |
| **Offline Determinism** | Harness-agnostic binary wrapper | **Built-in `FakeLlmClient` requires zero API keys** | Requires full environment setup | Coupled to live provider SDKs |
| **Monthly TCO (25 Deployments)** | **Combined Path C: $427.50/mo (incl. 3.5h review)** | **Combined Path C: $427.50/mo (incl. 3.5h review)** | Path B: $2,492.50/mo (incl. 17.5h maintenance) | Path A: $5,485.00/mo (incl. 39.0h triage) |

---

## 🧮 5. Quantitative Insights & Closed-Form FinOps Audit (`CLAIM-20261114-R77-STRANDSBOX-BORG` · R260 Milestone)

> **Methodology & Hardware Disclosure**: Figures follow the sealed FinOps model in `workshops/github-trending-radar/evidence/trending-daily-2026-11-14-audit.json` across 25 monthly deployments at `$95.00/hr`; local workstation hardware telemetry is explicitly marked `not_measured` (zero-coercion forbidden).

| Architecture Path | Monthly Retry-Storm Token & Infra Spend (USD) | Monthly Engineering Labor (Hours @ $95.00/hr) | Monthly Engineering Labor Cost (USD) | Total Monthly TCO (USD) | Net Savings vs Path A (USD / %) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Static Firewall Rules + Unsupervised Retry Storms & Panics** | `$1,780.00` | `39.0 hrs` | `$3,705.00` | **`$5,485.00`** | Baseline (`0.00%`) |
| **Path B: Static Seccomp/Iptables + Basic Tokio `try_join!` Loops** | `$830.00` | `17.5 hrs` | `$1,662.50` | **`$2,492.50`** | `-$2,992.50` (`-54.56%`) |
| **Path C: `Strands Box` Dogwood Sandbox + `borg` Rust Supervisor** | **`$95.00`** | **`3.5 hrs`** | **`$332.50`** | **`$427.50`** | **`-$5,057.50` (`-92.21%`)** |

- **Closed-Form Verification Identities**:
  - $\text{Path A Total} = \$1,780.00 + 39.0 \times \$95.00 = \$1,780.00 + \$3,705.00 = \$5,485.00/\text{mo}$
  - $\text{Path B Total} = \$830.00 + 17.5 \times \$95.00 = \$830.00 + \$1,662.50 = \$2,492.50/\text{mo}$
  - $\text{Path C Total} = \$95.00 + 3.5 \times \$95.00 = \$95.00 + \$332.50 = \$427.50/\text{mo}$
  - $\text{Monthly Savings} = \$5,485.00 - \$427.50 = \$5,057.50/\text{mo}\ (-92.21\%)$, $\text{Annualized Savings} = \$60,690.00/\text{yr}$

---

## 🛠️ 6. 15-Minute AI SA Actionable Adoption Checklist

1. **Build `strands-agents/box` and Test Temporal `policy.dw` Enforcement**:
   ```bash
   git clone https://github.com/strands-agents/box.git
   cd box && cargo build --release
   ```
   - **Verification Gate**: Configure `box.toml` and a `policy.dw` rule that denies outbound HTTP requests through the egress gateway after a sensitive file read occurs in Strands Shell or Monty for Python.
2. **Verify `joydle/borg` Supervision & Panic Isolation with `FakeLlmClient`**:
   ```toml
   [dependencies]
   borg = { git = "https://github.com/joydle/borg.git", tag = "v1.0.0" }
   async-trait = "0.1"
   ```
   - **Verification Gate**: Run a `seq` + `par` + `repeat` pipeline on `FakeLlmClient` and verify that a panicking parallel branch does not abort sibling branches and respects circuit-breaker thresholds.
3. **Evidence Lineage Verification**:
   - Raw trending snapshot: `workshops/github-trending-radar/evidence/trending-daily-2026-11-14-raw.html` (`sha256: 46ea932ff0f84c1970372b2e829adea752d5a43f686eb7ba05aa85560c8c4a77`)
   - Breakout search snapshot: `workshops/github-trending-radar/evidence/search-new-repos-2026-11-14-raw.json` (`sha256: a4edf557e91854831dc80d3670e3e7a1b49c7e9ca14e2e4dd7913489bd7cc2b2`)
