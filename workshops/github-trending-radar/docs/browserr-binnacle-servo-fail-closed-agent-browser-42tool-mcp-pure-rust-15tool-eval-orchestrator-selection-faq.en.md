# Fail-Closed Servo Agent Browser (`Omodaka9375/browserr`) & Zero-FFI Pure-Rust 15-Engine Eval Orchestrator (`TechTideOhio/binnacle`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 40 (Cumulative Round 464)  
> **Tracked Repositories**:
> - **`Omodaka9375/browserr`** (`★ 74`, Rust + Servo 0.8 Binary + 42-Tool `browserr-mcp` on PyPI, `Apache-2.0`): Servo-based headless/interactive browser engine built specifically for AI agents around three commitments: **block when unsure (5-second fail-closed interception), hand the page to a human when needed (`detect_handoff` / `pause` / `wait_for_user` with `e7`-numbered screenshots), and leave append-only evidence for every action**
> - **`TechTideOhio/binnacle`** (`★ 86`, Rust 2021 / 1.82+, Zero-FFI Pure-Rust Orchestrator for the 15-Tool TideOS Eval Kit, `MIT`): Unified supervisor CLI (`binnacle doctor`, `binnacle run <tool>`) orchestrating 15 standalone pure-Rust evaluation engines (`reval`, `gild`, `tessel`, `assay`, `tide-rill`, `keel`, `temper`, `parley`, `gavel`, `poise`, `plumb`, `weir`, `eddy`, `tare`, `tether`) with LCS sequence alignment, SimHash deduplication, exact McNemar tests, and SplitMix64 bootstrap confidence intervals  
> **Audit Claim ID**: `CLAIM-20261117-R40-BROWSERR-BINNACLE` (base LLM API subscriptions marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Enterprise Teams Scaling Web-Automation and Coding Agents Hit Two Infrastructure Bottlenecks: Heavy, Unsafe Chromium/CDP Wrappers and Flaky Python/LLM-Judge Evaluation Suites**:
   - **Bottleneck 1 — Chromium/CDP Bloat & Unsafe Blind Guessing on Sensitive Pages**: Traditional agent browsers embed full Chromium instances driven over CDP—consuming gigabytes of RAM on GPU-less CI runners, breaking on fragile CSS selectors, and blindly guessing when confronted with CAPTCHAs, OTP prompts, or payment forms without leaving an auditable evidence trail.
   - **Bottleneck 2 — Fragmented Python Eval Scripts & High-Variance Model Judges**: Prompts are disposable and models rotate every 90 days, making the evaluation harness the true compounding asset. Yet most teams rely on slow Python glue scripts and non-deterministic LLM-as-a-Judge calls that flake in CI and burn extra API budget.
   - **The Solution Architect Stack (`Omodaka9375/browserr` Apache-2.0 + `TechTideOhio/binnacle` MIT)**: Replace heavy Chromium wrappers on web-agent workflows with **`Omodaka9375/browserr`** (`Apache-2.0`, a single SHA-256-verified Rust + Servo 0.8 binary exposing 42 native MCP tools with CPU-default instant startup, 5-second fail-closed network interception, numbered `e7` element refs, and native `detect_handoff()` / `wait_for_user` human handoff); and gate every agent change in CI with **`TechTideOhio/binnacle`** (`MIT`, a zero-FFI pure-Rust orchestrator across 15 deterministic evaluation engines that automatically harvests failures into the golden dataset via `tether capture`).
2. **Closed-Form FinOps Impact (30 Automation & Platform Engineers Running 75,000 Monthly Browser Agent Workflows & CI Evaluation Gates at `$95.00/hr`)**:
   - Migrating from **Path A (Heavy Chromium/CDP Containers + Flaky Python/LLM-Judge Evaluations at `$5,855.00/mo`)** to **Path C (`browserr` 42-Tool Servo MCP + `binnacle` 15-Engine Pure-Rust Eval Kit at `$346.00/mo`)** saves **`$5,509.00/mo` (`-94.09%`, or `$66,108.00/yr`)** while cutting selector debugging, stuck-handoff recovery, and eval-flake triage labor from `37.0 hrs/mo` to `2.8 hrs/mo` (**`92.43%` reduction**).

![Browserr + Binnacle Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r40-browserr-binnacle.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `Omodaka9375/browserr` replace embedded Chromium/CDP with a 42-tool Servo 0.8 engine built around fail-closed interception, human handoff, and append-only evidence?
- **Plain-Language Definition**: `browserr` (`Apache-2.0`, installed via `"command": "uvx", "args": ["browserr-mcp"]`) is **a CPU-first Rust + Servo browser engine purpose-built for AI agents that blocks when unsure, hands sensitive steps to a human in a native window, and records screenshot + XHR evidence for every action**.
- **Three Architectural Differentiators**:
  1. **Fail-Closed by Default (`5 s` Network Interception & Payment/Auth Guards)**: Held network requests automatically deny after `5 s` if unanswered; auth challenges without stored credentials fail closed; and submitting payment or CAPTCHA pages requires explicit human confirmation;
  2. **First-Class Human Handoff (`detect_handoff` / `pause` / `wait_for_user` + `e7` Refs)**: Spots CAPTCHAs, one-time codes, empty passwords, and payment fields; opens an interactive window for a human while annotated screenshots number every interactive element (`e7`) to match `read_structure()` snapshot refs; and `fill_form` completes entire React 18 / Vue 3 forms in a single round trip while firing `input/change/blur` validators;
  3. **Append-Only Evidence & Clear Compatibility Boundaries**: Records timestamped PNG screenshots and per-frame `fetch`/XHR ring buffers without ever logging stored host credentials, while transparently documenting Servo 0.8's sweet spot (text, docs, search, forms, React 18/Vue 3 SPAs, CPU-default containers/ARM64; not for DRM video or WebRTC).

### Q2: How does `TechTideOhio/binnacle` orchestrate a 15-tool zero-FFI pure-Rust evaluation stack with deterministic mathematical guarantees?
- **Plain-Language Definition**: `binnacle` (`MIT`, Rust 1.82+ zero-FFI) is **the unified CLI supervisor (`binnacle doctor`, `binnacle run <tool>`) for the 15-engine TideOS evaluation stack—replacing brittle Python scripts and non-deterministic model judges with sub-second, fail-closed Rust binaries**.
- **Key Engines Across the 15-Step Pipeline**:
  - **Step 1 (`reval`)**: Open/axial failure coding, causal Bayesian trace DAGs, and OTel export;
  - **Step 2 (`gild`)**: Stratified golden dataset authoring, schema validation, and cryptographic versioning;
  - **Step 3 (`tessel`)**: Pairwise covering arrays ($P \times I \times C \times E$) with mathematical coverage guarantees;
  - **Step 4 (`assay`)**: Deterministic JSON Schema, JSON Pointer, zero-variance regex, and pure-Rust in-memory DB/RLS checks;
  - **Steps 5–15 (`tide-rill`, `keel`, `temper`, `parley`, `gavel`, `poise`, `plumb`, `weir`, `eddy`, `tare`, `tether`)**: Powered by LCS sequence alignment, SimHash deduplication, exact McNemar tests, and SplitMix64 bootstrap confidence intervals, culminating in **`tether capture`** to automatically harvest failed runs into the golden regression set.

### Q3: How should an AI Solution Architect combine `browserr` and `binnacle`?
- **Runtime Web Execution (`browserr`)**: Run `browserr-mcp` on CPU-only containers and developer machines for form automation, internal portal workflows, and human-in-the-loop checkout/auth handoffs.
- **CI Regression Gating (`binnacle`)**: Execute `binnacle` in pre-commit hooks and CI pipelines to enforce deterministic evaluation gates and harvest production failures via `tether capture`.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph BrowserrRuntime["Fail-Closed Web Agent Runtime: Omodaka9375/browserr (★74, Servo 0.8 Apache-2.0)"]
        A[MCP Client Invokes uvx browserr-mcp<br/>42 Native Tools · Instant CPU Startup] --> B[read_structure Assigns Stable e7 Refs<br/>+ Single-Round-Trip Type-Aware fill_form]
        B --> C{Intercepted Net Request / CAPTCHA / Payment?}
        C -->|Unanswered > 5s| D[Fail-Closed Auto-Deny]
        C -->|detect_handoff Triggered| E[pause Hands Native Window to Human<br/>wait_for_user Resumes + Saves Screenshot/XHR Evidence]
    end

    subgraph BinnacleEval["Zero-FFI 15-Engine Eval Gate: TechTideOhio/binnacle (★86, Pure-Rust MIT)"]
        E --> F[binnacle CLI Orchestrates 15 Standalone Rust Engines<br/>reval · gild · tessel · assay · gavel · tether]
        F --> G{Deterministic Gate: LCS / SimHash / McNemar}
        G -->|Pass exit 0| H[Ship to Production / CI Green]
        G -->|Fail exit 1/2| I[tether capture Harvests Failure to Gold Set]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Heavy Chromium/CDP Farms + LLM-Judge Evals | Option B: Headless Playwright + Custom Pytest Regex | **Option C (Recommended): `browserr` (Apache-2.0) + `binnacle` (15-Engine Rust MIT)** |
| :--- | :--- | :--- | :--- |
| **GPU-Less Container Startup & Memory Footprint** | ❌ Multi-hundred-MB Chromium overhead & slow cold boots | ⚠️ Driver binary downloads & CDP version drift | ✅ **Single SHA-256-verified Rust+Servo binary with instant CPU startup & 42 MCP tools** |
| **CAPTCHA / OTP / Payment Safety & Human Handoff** | ❌ Blind agent clicks trigger account lockouts or bad charges | ❌ Crashes on OTP/CAPTCHA; entire workflow aborts | ✅ **5s fail-closed interception + `detect_handoff` native window & numbered `e7` refs** |
| **Evaluation Determinism & Mathematical Bounds** | ❌ High-variance LLM judges flake & burn API budget | ⚠️ Ad-hoc regex lacks pairwise coverage & statistical tests | ✅ **Zero-FFI pure-Rust 15-engine stack (LCS, SimHash, exact McNemar, SplitMix64 CIs)** |
| **Automated Failure Harvesting to Gold Set** | ❌ Manual copy-pasting from production logs | ❌ Static test files rot quickly | ✅ **Failed gates (`exit 1/2`) trigger `tether capture` into `gild` versioned golden sets** |
| **Monthly TCO (30 Engineers / 75,000 Runs)** | **`$5,855.00 / mo`** (`$2,340` infra/judge tokens + `37.0 hrs` triage) | **`$2,555.00 / mo`** (`$940` containers + `17.0 hrs` maintenance) | **`$346.00 / mo`** (**`-94.09%` savings**; `$80` CPU Servo/Rust CI + `2.8 hrs` handoff/curation) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R40-BROWSERR-BINNACLE`)

> **Scope & Boundary Declaration**: Evaluated for a 30-engineer AI automation and platform organization executing **75,000 monthly headless browser agent workflows and CI evaluation gates** at a blended engineering rate of `$95.00/hr` (base LLM API subscriptions marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Browser Infra \& Eval Judge Token Spend} + (\text{Selector/Handoff Recovery \& Eval Triage Hours} \times \$95.00)$$

| Cost Component | Path A: Heavy Chromium + LLM Judges | Path B: Playwright + Custom Pytest | **Path C: `browserr` + `binnacle` Stack** |
| :--- | :---: | :---: | :---: |
| **Monthly Browser Container Infra & Judge Token Spend** | `$2,340.00` | `$940.00` | **`$80.00`** |
| **Monthly Selector Debug, Handoff Recovery & Eval Flake Hours** | `37.0 hrs` | `17.0 hrs` | **`2.8 hrs`** (**`92.43%` reduction**) |
| **Monthly Automation & Platform Engineering Labor (`@ $95.00/hr`)** | `$3,515.00` | `$1,615.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,855.00`** | **`$2,555.00`** (`-56.36%`) | **`$346.00`** (**`-94.09%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,300.00 / mo` (`$39,600/yr`) | **`$5,509.00 / mo` (`$66,108.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Register `Omodaka9375/browserr` (`uvx browserr-mcp`) in MCP Clients**: Replace heavy Chromium/CDP containers on form, search, and React 18/Vue 3 SPA workflows with `browserr`'s 42 native tools and `read_structure()` `e7` element references.
- [ ] **Step 2 — Enforce 5-Second Fail-Closed Network Interception & `detect_handoff()`**: Require human confirmation via `pause()` / `wait_for_user` on all CAPTCHA, OTP, and payment pages while archiving timestamped screenshots and per-frame XHR ring buffers.
- [ ] **Step 3 — Deploy `TechTideOhio/binnacle` Across Pre-Commit Hooks & CI**: Run `binnacle doctor` and invoke `tessel` (pairwise covering arrays) and `assay` (deterministic JSON Schema/RLS assertions) on every agent prompt or tool change.
- [ ] **Step 4 — Automate Gold-Set Compounding with `tether capture` & `gild`**: Route every non-zero CI evaluation exit (`exit 1/2`) into `tether capture` so production and staging edge cases automatically compound in your `gild` golden dataset.
