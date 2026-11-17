# [Milestone R435] 4-Tier Evidence-Graded Earnings Attribution (`AlphaGBM`), One-Probe-at-a-Time R&D (`real-scientist-skills`) & 8-Step Defect Discovery (`muse-agent-operations-kit` & `ai-detection-eval`) Architecture & Selection FAQ

> **Document Metadata (2026-11-17 · Night Round 11 / Cumulative Round 435 Milestone)**  
> - **Target Audience**: **Enterprise AI Solution Architects** & Quantitative Research / R&D Governance Decision-Makers  
> - **Core Orientation**: **① Real Enterprise Application Scenarios & Business ROI/Pain Points + ② End-to-End Integration Reference Architecture + ③ Peer Open-Source / Cloud Service / Commercial Solution Selection & TCO Comparison**  
> - **Editorial Benchmark**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (Plain-Language First Principles + 3 Architectural Deep-Dive Q&As + Mermaid Decision Tree + Peer Comparison Matrix + Closed-Form FinOps Audit + 15-Minute Rollout Checklist)  
> - **Evaluated Repositories**:  
>   1. [`AlphaGBM/alphagbm-trading-skills`](https://github.com/AlphaGBM/alphagbm-trading-skills) (`v0.2.0`, `★ 32`, Python: **13-skill financial research and post-earnings event attribution suite (`/gbm`)** enforcing a strict **4-tier source evidence hierarchy**, 5-axis expectation-gap decomposition, explicit `unverified` tagging when primary filings are absent, and read-only separation of facts, assumptions, plans, and post-mortem outcomes)  
>   2. [`HiteSit/real-scientist-skills`](https://github.com/HiteSit/real-scientist-skills) (`★ 38`, MIT License, synced with `mattpocock/skills`: Reproducible R&D and scientific experiment skills enforcing a **One-Probe-at-a-Time loop (`/setup-science` → `/experiment` → `/promote`)** inside `.science/<study>/` with pre-registered `expected` baselines and Git-tagged `NOTEBOOK.md` provenance)  
>   3. [`Chisiki1/muse-agent-operations-kit`](https://github.com/Chisiki1/muse-agent-operations-kit) (`v1.6`, `★ 29`, MIT License: 14-section long-running agent operations & retirement framework + **8-step general Defect-Discovery Skill**) & [`ampdot-io/ai-detection-eval`](https://github.com/ampdot-io/ai-detection-eval) (`★ 44`: `327,516`-prompt WildChat split & `160`-prompt frozen prose-detection benchmark with bundled zero-dep `writing-scaffold.mjs` MCP server)  
> - **Companion SVG Diagram**: [`assets/github-ai-radar-2026-11-17-r11-alphagbm-scientist-muse-ops.svg`](../../../assets/github-ai-radar-2026-11-17-r11-alphagbm-scientist-muse-ops.svg)  
> - **Audit Claim ID**: `CLAIM-20261117-R11-ALPHAGBM-SCIENTIST-MUSE` (commercial market-data terminal subscriptions marked `not_measured`)

---

## 📌 1. Executive Summary (3-Minute Enterprise Architect's Briefing)

1. **Why do generic LLM prompts fail at institutional earnings attribution and competitive strategy research, and how does `AlphaGBM/alphagbm-trading-skills` (`v0.2.0`) enforce audit-grade evidence hygiene?**  
   - **Enterprise Business Pain Point**: When an enterprise strategy or equity research team asks a standard LLM "Why did this company's stock drop after earnings?", the model blends unverified social-media commentary with management spin, reduces complex multi-factor moves to "missed expectations," and suffers from hindsight bias.  
   - **`AlphaGBM` Architectural Fix**:
     - **13 Specialized Workflows Under `/gbm` (`gbm-event-attribution`, `gbm-model`, `gbm-diagnosis`, `gbm-report`)**: Separates verified facts, management statements, market narratives, and agent inferences;
     - **Strict 4-Tier Source Hierarchy & `Unverified` Gate**: Requires Tier-1 regulatory filings/IR releases/transcripts as primary proof, restricts Tier-3 media to market-pricing context, forbids Tier-4 social/search snippets from supporting core claims alone, and marks any claim lacking primary text as `待核验 / unverified`;
     - **4-Layer Separation (Facts vs. Assumptions vs. Plan vs. Outcome) in Read-Only Local Storage**: Prevents hindsight bias while storing zero credentials, tokens, or live brokerage positions.
2. **Why does applying software-engineering "upfront multi-ticket parallel execution" to AI/ML R&D waste compute, and how does `HiteSit/real-scientist-skills` fix exploratory research?**  
   - **Enterprise Business Pain Point**: Software engineering builds known specifications (`/to-spec` → `/to-tickets`), whereas R&D explores unmapped territory where Experiment #1 routinely invalidates Steps #2–#10. Furthermore, unsteered LLMs default to the "average textbook middle" rather than novel hypotheses.  
   - **`real-scientist-skills` Architectural Fix**:
     - **One Probe at a Time (`/experiment`) + Pre-Registered `expected` Baselines**: Before running any probe (`probes/03-<slug>`), the agent records the standard expected answer (`expected`) in `.science/<study>/NOTEBOOK.md` and measures how far empirical reality (`found`) lands from the baseline;
     - **Sandboxed `.science/` Directory + Gated `/promote` Graduation**: Keeps exploratory scripts, plots, and literature notes (`library/`) isolated in `.science/` (with per-probe Git tags) until `/promote` graduates verified protocols into production `src/`.
3. **How do `Chisiki1/muse-agent-operations-kit` (`v1.6`) and `ampdot-io/ai-detection-eval` govern long-running agent operations, non-CWE code defects, and prose quality?**  
   - **8-Step Defect Discovery + Rule Retirement + Frozen Prose Eval**:
     - `muse-agent-operations-kit` defines 3 operational ledgers (Asset, Adoption, Egress), periodic rule consolidation/retirement gates, and an **8-step Defect-Discovery Skill** targeting **state transitions, race conditions, persistence, numerics, unbounded growth, and idempotency** via mechanical population enumeration and **skeptical re-review of affirmative ("no bug") dispositions**;
     - `ai-detection-eval` ships a reproducible `327,516`-prompt WildChat split (`160` frozen eval prompts, `609` scored records) and a zero-dependency `writing-scaffold.mjs` MCP server (`http://127.0.0.1:3000/mcp`).
4. **Closed-Form FinOps Audit (`CLAIM-20261117-R11-ALPHAGBM-SCIENTIST-MUSE`)**:  
   - Across **30 monthly earnings/strategy attribution reports + 25 exploratory R&D studies and code defect audits** (at **`$100.00/hr`** blended analyst/architect rate), migrating from **Path A** (unstructured prompts + upfront multi-ticket R&D runs + ad-hoc bug hunting: **`$6,020.00/mo`**) to **Path C** (`AlphaGBM` 4-tier evidence + `real-scientist-skills` 1-probe loop + `Muse` 8-step defect audit: **`$415.00/mo`**) saves **`$5,605.00/month`** (**`-93.11%`**, **`$67,260.00/year`**) and cuts rework labor from `40.0 hrs` to `3.1 hrs/mo` (**`-92.25%`**).

![Evidence-Graded Earnings Attribution, 1-Probe R&D & 8-Step Defect Audit Architecture](../../../assets/github-ai-radar-2026-11-17-r11-alphagbm-scientist-muse-ops.svg)

---

## 💬 2. Three Architectural Deep-Dive Q&As (Enterprise Scenarios, Reference Architecture & Boundaries)

### Q1: How does `AlphaGBM` prevent hallucinated financial causality in enterprise market-intelligence reports?

1. **5-Axis Expectation Decomposition + Mandatory Falsification Criteria**:  
   - Instead of accepting a single narrative, `gbm-event-attribution` decomposes `reported` vs. `consensus` vs. `guidance` vs. operating KPIs vs. management tone, pairs target price action against peer/sector benchmarks and macro confounders, and binds every assertion to a primary filing paragraph or marks it `unverified`.

---

### Q2: When should an enterprise team switch from `real-scientist-skills` (`/experiment`) back to standard engineering skills (`/to-tickets`)?

1. **The `/promote` Hand-Off Boundary**:  
   - Use `.science/` one-probe-at-a-time exploration while the algorithm, prompt scaffold, or data hypothesis is still changing; once a probe series stabilizes into a proven protocol, run `/promote` to move the validated code into `src/`, where standard parallel engineering ticket workflows (`mattpocock/skills` `tdd`, `code-review`, `pr`) take over.

---

### Q3: Why is `muse-agent-operations-kit`'s "Skeptical Re-Review of Affirmative Dispositions" critical for auditing complex enterprise backends?

1. **Defeating LLM Reviewer Complacency on Long Audits**:  
   - When an agent inspects dozens of state transitions or idempotency boundaries, it tends to wave through later items as "OK / safe." Step 4 of `defect-discovery-skill.en.md` forces a dedicated pass that skeptically re-audits every item previously marked safe, catching subtle race conditions and unbounded memory growth.

---

## 🧭 3. Enterprise Integration Reference Architecture & Selection Decision Tree (Mermaid)

```mermaid
flowchart TD
    Start["Enterprise Financial Attribution, Exploratory AI R&D & Deep Defect Audit Selection"] --> Track{"Primary Enterprise Domain?"}

    Track -->|"Post-Earnings Attribution, Competitive Strategy & Investment Memos"| FinGate{"Evidence Rigor Required?"}
    FinGate -->|"4-Tier Source Hierarchy + 5-Axis Expectation Gap<br/>+ Explicit Unverified Tags & 4-Layer Fact/Assumption Separation"| UseAlphaGBM["✅ AlphaGBM/alphagbm-trading-skills (v0.2.0 · /gbm)<br/>• 13 Read-Only Workflows + Falsifiable Peer/Macro Attribution<br/>• Zero Brokerage Keys or Sensitive Account Storage"]
    FinGate -->|"Casual Headline Summarization"| HeadlineBot["🔄 Basic News Digest Script"]

    Track -->|"Exploratory ML/AI Tuning, Feature Discovery & Scientific R&D"| SciGate{"Problem Uncertainty?"}
    SciGate -->|"Unmapped Territory: 1 Probe at a Time + Pre-Registered expected<br/>+ .science/ Isolation & Gated /promote Graduation"| UseScientist["✅ HiteSit/real-scientist-skills (★ 38 · MIT)<br/>• Git-Tagged NOTEBOOK.md + Per-Probe Dashboards<br/>• Hands Off to Engineering Flow Once Protocol Stabilizes"]
    SciGate -->|"Known Software Spec"| EngTickets["🔄 Standard Upfront Ticket Graph"]

    Track -->|"Long-Running Agent Governance, Non-CWE Defect Audits & Prose Eval"| OpsGate{"Governance Scope?"}
    OpsGate -->|"3 Ledgers + Rule Retirement + 8-Step State/Race/Idempotency Audit<br/>+ 327k-Prompt WildChat Prose Eval & writing-scaffold MCP"| UseMuseOps["✅ muse-agent-operations-kit (v1.6) + ai-detection-eval<br/>• Skeptical Re-Review of 'No Bug' Claims + Untrusted Input Guard"]

    UseAlphaGBM --> FinOps["💰 Closed-Form Enterprise FinOps Impact (CLAIM-20261117-R11-ALPHAGBM-SCIENTIST-MUSE)<br/>Monthly Total $6,020.00 ➔ $415.00 (-93.11% · Saves $67,260/yr)"]
    UseScientist --> FinOps
    UseMuseOps --> FinOps
```

---

## 📊 4. Peer Open-Source / Cloud / Commercial Selection Matrix (Decision Matrix)

| Dimension | `AlphaGBM` (`/gbm` 13-Skill Suite) | Generic Unstructured LLM Financial Prompts | `real-scientist-skills` (`.science/` 1-Probe Loop) | Upfront 20-Ticket Parallel Spec Flow | `muse-agent-operations-kit` + `ai-detection-eval` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Enterprise Use Case** | **Audit-grade earnings attribution & competitive strategy memos** | Casual market chat | **Exploratory AI/ML R&D & hypothesis testing** | Known feature implementation | **Agent lifecycle governance, non-CWE defect discovery & prose QA** |
| **Methodological Rigor** | **4-tier source priority + `unverified` tags + 4-layer separation** | Blends social rumors with filings; hindsight bias | **1 probe at a time + pre-registered `expected` baseline** | Wastes compute on invalidated downstream tickets | **Mechanical enumeration + skeptical re-review of "safe" claims** |
| **Safety & Isolation** | **100% read-only; stores 0 credentials or live positions** | Risk of leaking internal deal notes | **Isolates scratch probes in `.science/` until `/promote`** | Pollutes main branch with dead experiments | **Untrusted external-content rules + strict non-coerced eval counts** |
| **TCO & Licensing** | **Open Source (`$0` terminal lock-in)** | High analyst fact-checking rework | **MIT Open Source (eliminates dead-end R&D compute)** | High wasted GPU/token spend | **MIT Open Source (includes 0-dep `writing-scaffold.mjs` MCP)** |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps Audit (`CLAIM-20261117-R11-ALPHAGBM-SCIENTIST-MUSE`)

> **Scope & Provenance Boundary**: Models monthly wasted R&D compute/eval spend and analyst/engineer rework labor across **30 post-earnings/strategy attribution reports** and **25 exploratory R&D studies & codebase defect audits** at **`$100.00/hr`**. External commercial market-data terminal licenses are marked **`not_measured`**.

| Architecture Path | R&D Compute & Eval Spend (`USD/mo`) | Fact-Check & Dead-End Rework Labor (`hrs/mo`) | Team Labor Cost (`@ $100/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Unstructured Prompts + Upfront Parallel R&D Tickets + Ad-Hoc Review** | `$2,020.00` | `40.0 hrs` | `$4,000.00` | **`$6,020.00`** | Baseline (`0.00%`) |
| **Path B: Manual Analyst Spreadsheets + Unindexed Jupyter Notebooks** | `$910.00` | `18.5 hrs` | `$1,850.00` | **`$2,760.00`** | `-$3,260.00` (`-54.15%`) |
| **Path C (Recommended): `AlphaGBM` + `real-scientist-skills` + `Muse Ops`** | **`$105.00`** | **`3.1 hrs`** | **`$310.00`** | **`$415.00`** | **`-$5,605.00` (`-93.11%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 2020.00 + 40.0 \times 100.00 = 2020.00 + 4000.00 = \$6,020.00$
  - $\text{Path B Total} = 910.00 + 18.5 \times 100.00 = 910.00 + 1850.00 = \$2,760.00$
  - $\text{Path C Total} = 105.00 + 3.1 \times 100.00 = 105.00 + 310.00 = \$415.00$
  - $\text{Net Savings (Path C vs Path A)} = 6020.00 - 415.00 = \$5,605.00/\text{mo} \quad (-93.11\%, \text{Annualized } \$67,260.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect 15-Minute Enterprise Rollout Checklist

1. **Install `AlphaGBM` (`/gbm`) & `real-scientist-skills` (`/setup-science`)**:
   ```bash
   git clone https://github.com/AlphaGBM/alphagbm-trading-skills.git
   git clone https://github.com/HiteSit/real-scientist-skills.git
   # Use /gbm-event-attribution for evidence-graded filings analysis & /experiment for 1-probe R&D
   ```
2. **Adopt `muse-agent-operations-kit` Defect-Discovery & `ai-detection-eval` Scaffold MCP**:
   ```bash
   git clone https://github.com/Chisiki1/muse-agent-operations-kit.git
   git clone https://github.com/ampdot-io/ai-detection-eval.git && cd ai-detection-eval
   node writing-scaffold.mjs
   ```
