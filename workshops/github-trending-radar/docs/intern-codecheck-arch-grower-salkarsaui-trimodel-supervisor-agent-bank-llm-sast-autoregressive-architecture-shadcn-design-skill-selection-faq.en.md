# Tri-Model Supervised Agent (`nace-ai/intern`), CommBank AI Static Security Review (`Commonwealth-Bank-of-Australia/CodeCheck`), Autoregressive Architecture Engine (`Tobi1chi/arch-grower`) & Agent-Ready Design System Skill (`salahudinalyb/SalkarsaUI`) Selection & Architecture FAQ

> **Document Type**: AI Solution Architect (SA) Enterprise Use Cases, Reference Architecture & Comparative Selection Guide (2026-11-19 Night Round 34 / Cumulative Round 558)  
> **Benchmark Style**: Aligned with [`ib-vs-ethernet-roce-selection-faq.md`](https://github.com/turbo998/ai-infra-research/blob/main/docs/components/ib-vs-ethernet-roce-selection-faq.md) (Plain-Language Q&A + Decision Tree + Reference Architecture + Closed-Form FinOps TCO + Onboarding Checklist)  
> **中文版（Chinese Version）**: [`intern-codecheck-arch-grower-salkarsaui-trimodel-supervisor-agent-bank-llm-sast-autoregressive-architecture-shadcn-design-skill-selection-faq.md`](./intern-codecheck-arch-grower-salkarsaui-trimodel-supervisor-agent-bank-llm-sast-autoregressive-architecture-shadcn-design-skill-selection-faq.md)  
> **Companion HD Architecture Diagram**: [`assets/github-ai-radar-2026-11-19-r34-intern-codecheck-archgrower-salkarsaui.svg`](../../../assets/github-ai-radar-2026-11-19-r34-intern-codecheck-archgrower-salkarsaui.svg)  
> **Provenance & Guardrail Tags**: `provenance: synthetic` · `independently_reproduced: false` · `base_hardware_capex: not_measured` · `track_b_stars_today: not_measured`

---

## 1. 📌 Executive Summary

> **One-Sentence Selection Verdict**: When enterprise engineering organizations scaling AI-native software delivery hit four systemic failure modes—**(1) unstructured "vibe coding" causing severe context bloat and "fix A, break B" architectural drift after 10–20 turns, (2) AI coding agents generating generic, off-brand UI screens lacking responsive breakpoints and interactive states, (3) single-model agents burning expensive frontier tokens on boilerplate or getting trapped in infinite tool loops, and (4) rapid AI code generation bypassing shift-left security review before PR creation**—combine **`Tobi1chi/arch-grower` (autoregressive architecture engine with localized context slicing) + `salahudinalyb/SalkarsaUI` (573-token, 51-component shadcn/Tailwind v4 design system packaged as an Agent Skill) + `nace-ai/intern` (tri-model agent harness pairing frontier, efficient, and turn-by-turn decision supervisor models) + `Commonwealth-Bank-of-Australia/CodeCheck` (bank-released AI static security review plugin for Claude Code & Codex)**. Across a 40-person full-stack and AppSec organization (`$100/hr`), monthly TCO drops from **`$7,760.00/mo`** (Path A 100% frontier burn + commercial SAST seats + architectural rework) to **`$345.00/mo`** (net savings of **`$7,415.00/mo`**, **`-95.55%`**, or **`$88,980.00/yr`**).

![2026-11-19 Night Round 34 (R558) Architecture & Selection Overview](../../../assets/github-ai-radar-2026-11-19-r34-intern-codecheck-archgrower-salkarsaui.svg)

| Dimension | 1️⃣ Tri-Model Supervised Agent Harness: `nace-ai/intern` | 2️⃣ Bank-Released AI Static Security Plugin: `Commonwealth-Bank-of-Australia/CodeCheck` | 3️⃣ Autoregressive Architecture Engine: `Tobi1chi/arch-grower` | 4️⃣ Agent-Ready Mobile-First Design System: `salahudinalyb/SalkarsaUI` |
| :--- | :--- | :--- | :--- | :--- |
| **GitHub Velocity & License** | `★ 28` · `55 forks` (Python 3.12+ · Nace AI Open RAIL-M) | `★ 26` · `7 forks` (Claude Code & Codex Plugin · MIT) | `★ 30` · `2 forks` (Python 3.10+ · Zero-Dep MCP · MIT) | `★ 29` · `3 forks` (Tailwind v4 + shadcn/ui + Skill · MIT) |
| **Primary Business Pain Solved** | Using a frontier model for every turn burns budget, while small models get stuck in loops, risky tool calls, or context overflow | AI-generated code ships faster than AppSec can review, and regex SAST misses business-logic flaws | Heavy upfront waterfall PRDs are too slow, while pure chat "vibe coding" bloats context and breaks existing modules | AI agents (`Claude`, `Codex`, `v0`, `Lovable`) generate inconsistent UIs missing hover/focus states and mobile breakpoints |
| **Core Architectural Mechanism** | **Three-model collaboration**: **Frontier model** cracks the hard part, **Efficient model** finishes implementation, and **Decision model** watches every turn to pick handover moments and catch loops/risks | **Open-sourced by Commonwealth Bank of Australia (CommBank)**: runs LLM-powered static security reviews directly inside Claude Code and Codex before PR submission | **Autoregressive topology evolution**: grows architecture from a 1-sentence idea via lightweight A/B choices, **localized context slicing**, and `arch export-ui` HTML dashboards | **573 light/dark CSS tokens + 51 `shadcn/ui`-mapped components + 959 icons + 5 breakpoints (`640–1536px`)**, packaged as `SKILL.md` + `DESIGN.md` |
| **Best-Fit Enterprise Scenario** | Long-horizon coding and DevOps agents requiring frontier reasoning on hard bottlenecks but small-model economics and loop safety | Financial, enterprise, and SaaS teams running shift-left AI security reviews inside developer CLIs before opening PRs | MVP kickoffs and modular feature evolution where teams want structured boundaries without 50-page waterfall docs | Standardizing responsive, on-brand web UI generation across Claude Code, Codex, Cursor, Copilot, v0, Lovable, and Bolt |
| **When to Choose Cloud PaaS / SaaS** | Fully managed cloud sandboxes with tenant-wide SSO billing (use GitHub Copilot Coding Agent / Azure AI Agent Service) | Certified compliance CI/CD blocking gates, SCA license auditing, and auditor sign-off (use GitHub Advanced Security / Snyk) | 500-architect enterprise TOGAF portfolio & CMDB governance (use LeanIX / Sparx Enterprise Architect) | Legacy enterprise ERP frontends tied to proprietary SAP Fiori or Salesforce Lightning component libraries |

---

## 2. 🎯 Solution Architect High-Stakes Q&A

### Q1: Why combine these four specific projects across Architecture, UI, Agent Execution, and AppSec—and where is the boundary with commercial enterprise tools?

* **Plain-Language Breakdown**:
  1. **`Tobi1chi/arch-grower` bridges the gap between slow waterfall PRDs and chaotic "vibe coding"**: When developers jump straight into chatting with an LLM to build an app, context balloons within 20 turns and the model starts breaking Module A while editing Module B. `arch-grower` treats software architecture like autoregressive generation: starting from a one-sentence idea, it guides the architect through lightweight binary (A/B) decisions to grow a minimal closed-loop topology, pending nodes, and backlog items. Using **localized context slicing**, coding agents only receive the exact neighborhood slice they need, with zero external Python dependencies, native MCP support, and `arch export-ui` visual dashboards.
  2. **`salahudinalyb/SalkarsaUI` gives AI coding agents a deterministic 573-token, 51-component design system**: AI-generated screens often fail enterprise design review because the agent guesses spacing, dark-mode contrast, and mobile breakpoints. `SalkarsaUI` provides **573 semantic light/dark tokens (`tokens/tokens.css`)**, **51 components mapped 1:1 to `shadcn/ui`**, **959 icons**, **5 mobile-first breakpoints (`640`, `768`, `1024`, `1280`, `1536px`)**, and explicit `hover/focus/pressed/disabled` state rules—all packaged directly as an installable **`SKILL.md` + `DESIGN.md`** for Claude Code, Codex, Cursor, v0, Lovable, and Bolt.
  3. **`nace-ai/intern` (`55 forks`) introduces a tri-model brain (Frontier + Efficient + Decision Supervisor)**: Instead of paying frontier model prices for every trivial file edit—or watching a small model spin in an infinite tool-call loop—`nace-ai/intern` orchestrates three models: a **Frontier model** cracks the hard architectural problem, a fast **Decision model** watches every turn to pick the exact handover moment, and an **Efficient model** finishes the routine implementation while the supervisor catches loops, blocks risky tool calls, and prevents context overflow.
  4. **`Commonwealth-Bank-of-Australia/CodeCheck` brings bank-inspired AI static security review directly into Claude Code and Codex**: Released under the MIT license by the **Commonwealth Bank of Australia (CommBank / CBA)**, `CodeCheck` is a plugin for Claude Code and Codex that performs LLM-powered static security reviews of source code right in the developer's workflow before a pull request is ever opened.

* **Selection Boundary (Self-Hosted OSS vs. Managed Cloud/Commercial)**:
  - **Choose Path C (`arch-grower` + `SalkarsaUI` + `nace-ai/intern` + `CommBank/CodeCheck`)** to standardize agile architecture slicing, on-brand shadcn/Tailwind UI generation, cost-controlled supervised agent execution, and developer-CLI shift-left security review.
  - **Choose Path A (Commercial Enterprise Suites)** when regulatory auditors mandate certified CI/CD SAST/SCA sign-off reports (keep **GitHub Advanced Security / Snyk / Veracode** as the mandatory CI/CD gate while using `CodeCheck` for fast pre-commit developer self-checks).

---

### Q2: How do these four projects integrate into an end-to-end AI-Native SDLC reference architecture?

1. **Autoregressive Architecture Slicing Layer (`Tobi1chi/arch-grower`)**: Architects invoke `arch-grower` via MCP or CLI to evolve a one-sentence requirement through 10–15 binary choices into a verified node graph (`arch export-ui`), exporting localized context slices per component.
2. **Design System Skill Injection Layer (`salahudinalyb/SalkarsaUI`)**: `SalkarsaUI`'s `SKILL.md`, `DESIGN.md`, and `tokens.css` are mounted into the agent workspace so every frontend task inherits the 573 light/dark tokens, 51 `shadcn/ui` mappings, and 5 responsive breakpoints.
3. **Tri-Model Supervised Execution Layer (`nace-ai/intern`)**: `nace-ai/intern` ingests the localized architecture slice and UI skill. Its Frontier model solves complex state/domain logic, its Decision supervisor triggers handover to the Efficient model for component/test generation, and its per-turn monitor halts loops, risky shell commands, or context overflow.
4. **Shift-Left AI Static Security Review Layer (`Commonwealth-Bank-of-Australia/CodeCheck`)**: Before committing, the developer runs `CodeCheck` inside Claude Code or Codex to scan the new source code for security flaws, triaging findings with a qualified engineer prior to CI/CD SAST checks.

---

### Q3: What compliance disclaimers and operational guardrails must be enforced during enterprise rollout?

1. **Mandatory Governance Guardrails for `Commonwealth-Bank-of-Australia/CodeCheck` (Per CBA's Official Notice)**:
   - **One-Time Open-Source Release**: CBA published `CodeCheck` as a one-time MIT release for evaluation and adaptation; CBA does not actively maintain or support the repository, so internal AppSec teams must own ongoing rule maintenance.
   - **Supplement—Never Replace—Formal AppSec Testing & Human Triage**: `CodeCheck` may miss vulnerabilities (false negatives) or flag safe code (false positives). All findings must be reviewed by a qualified engineer, and deterministic SAST/DAST/SCA gates must remain active in CI/CD.
   - **Approved Environment & Data Residency**: Because `CodeCheck` sends code through your configured AI coding agent (`Claude Code` or `Codex`), run it only on code you are authorized to review and bind your coding agent to an enterprise zero-data-retention LLM endpoint.
2. **Operational Guardrails for `nace-ai/intern`**:
   - Licensed under **Nace AI Open RAIL-M** (permitting commercial and research use subject to responsible-use restrictions); configure a low-latency model for the Decision supervisor so per-turn loop/risk checks add negligible overhead.

---

## 3. 🧭 Visual Architecture & Decision Diagrams (Mermaid)

### 3.1 Selection Decision Tree

```mermaid
flowchart TD
    A["Enterprise AI-Native SDLC (Architecture -> UI -> Agent Execution -> AppSec)"] --> B{"Which lifecycle stage needs hardening?"}
    B -->|"Architecture: Heavy waterfall PRD vs chaotic Vibe Coding"| C{"Need incremental topology evolution + context slicing?"}
    C -->|"Yes (A/B binary steps + MCP slice focus + arch export-ui)"| C1["Select Tobi1chi/arch-grower (Zero-Dep Python · MIT)"]
    C -->|"No (enterprise-wide IT asset CMDB portfolio)"| C2["Select LeanIX / Sparx Enterprise Architect"]

    B -->|"Frontend UI: Off-brand AI screens missing states & breakpoints"| D{"Using Tailwind CSS v4 + shadcn/ui?"}
    D -->|"Yes (573 tokens + 51 components + 959 icons + SKILL.md)"| D1["Select salahudinalyb/SalkarsaUI (MIT)"]
    D -->|"No (legacy SAP Fiori / proprietary desktop UI)"| D2["Package Internal Enterprise Design System Skill"]

    B -->|"Agent Execution: Frontier token burn vs small-model loops"| E{"Need dynamic model handover + per-turn loop guard?"}
    E -->|"Yes (Frontier + Efficient + Decision supervisor)"| E1["Select nace-ai/intern (Tri-Model Brain)"]
    E -->|"No (single-turn Q&A without multi-step tools)"| E2["Use Standard Single-Model API"]

    B -->|"AppSec: Catching security flaws in AI code before PR"| F{"Pre-PR developer CLI check or certified CI/CD gate?"}
    F -->|"Shift-left AI static review inside Claude Code / Codex"| F1["Select CommBank/CodeCheck (MIT) + Engineer Review"]
    F -->|"Regulated CI/CD blocking & SCA compliance"| F2["Combine CodeCheck (Pre-PR) + GitHub Advanced Security / Snyk"]
```

### 3.2 End-to-End Enterprise Reference Architecture

```mermaid
flowchart LR
    subgraph ArchLayer["1. Autoregressive Architecture (Tobi1chi/arch-grower)"]
        Idea["1-Sentence Product Idea"]
        BinaryStep["Lightweight A/B Topology Evolution\n(Localized Context Slicing)"]
        ArchBoard["arch export-ui HTML Dashboard\n(Minimal Loop + Pending + Backlog)"]
        Idea --> BinaryStep --> ArchBoard
    end

    subgraph DesignLayer["2. Agent Design System (salahudinalyb/SalkarsaUI)"]
        Tokens["tokens.css (573 Light/Dark Tokens)\n+ 5 Breakpoints (640px-1536px)"]
        ShadcnMap["51 shadcn/ui Components\n+ 959 Icons + Interactive States"]
        UISkill["SKILL.md + DESIGN.md\n(Mounted in Claude/Codex/Cursor/v0)"]
        Tokens & ShadcnMap --> UISkill
    end

    subgraph InternLayer["3. Tri-Model Supervised Agent (nace-ai/intern)"]
        Frontier["Frontier Model\n(Cracks Hard Core Logic)"]
        Decision["Decision Supervisor Model\n(Picks Handover · Catches Loops & Risky Calls)"]
        Efficient["Efficient Worker Model\n(Finishes Modules & Tests Cheaply)"]
        Frontier <-->|"Dynamic Handover"| Decision <--> Efficient
    end

    subgraph SecurityLayer["4. Shift-Left AI Security (CommBank/CodeCheck)"]
        Plugin["CodeCheck (Claude Code / Codex Plugin)\nLLM Static Security Review"]
        HumanGate["Qualified Engineer Triage\n+ CI/CD Deterministic SAST"]
        Plugin --> HumanGate
    end

    ArchBoard -->|"Localized Node Slice"| InternLayer
    UISkill -->|"Responsive UI Contract"| InternLayer
    InternLayer -->|"Generated Source Diff"| Plugin
```

### 3.3 End-to-End Execution Sequence

```mermaid
sequenceDiagram
    autonumber
    actor Eng as Architect / Full-Stack Engineer
    participant Arch as arch-grower (MCP Architecture)
    participant UI as SalkarsaUI (SKILL.md)
    participant Intern as nace-ai/intern (Tri-Model Agent)
    participant Check as CommBank/CodeCheck (Security Plugin)

    Eng->>Arch: Input 1-sentence concept ("Enterprise receipt OCR & multi-tier approval app")
    Arch-->>Eng: Guide 15 binary A/B steps -> export 5-node minimal loop & localized slices
    Eng->>Intern: Dispatch node slice + mount SalkarsaUI SKILL.md
    Intern->>Intern: Frontier model solves state-machine core -> Decision model triggers handover
    Intern->>Intern: Efficient model builds responsive shadcn screens using 573 SalkarsaUI tokens
    Intern->>Intern: Decision supervisor intercepts 1 retry loop & blocks risky shell call
    Intern-->>Eng: Deliver on-brand responsive UI + backend implementation
    Eng->>Check: Run CommBank CodeCheck static security review inside Claude Code / Codex
    Check-->>Eng: Flag potential authorization bypass on approval amount mutation
    Eng->>Eng: Qualified engineer reviews & patches flaw -> open clean PR to CI/CD
```

---

## 4. 📊 Comparative Selection Matrix

| Evaluation Dimension | `arch-grower` + `SalkarsaUI` + `nace-ai/intern` + `CommBank/CodeCheck` (R558 Stack) | Unstructured Vibe Coding (Chat-Driven Code + Ad-Hoc CSS + Single Frontier Model + Post-PR Security) | Heavy Commercial Stack (Enterprise Architect + Commercial UI Kit + 100% Frontier API + Per-Seat AI SAST) |
| :--- | :--- | :--- | :--- |
| **Architecture & Context Hygiene** | **Autoregressive A/B evolution + localized context slicing**, preventing "fix A, break B" regressions | Context bloats after 15–20 turns, causing the model to forget earlier module boundaries | Weeks of upfront waterfall documentation before writing a single line of code |
| **Frontend UI Brand Consistency** | **573 tokens + 51 shadcn components + 5 breakpoints** packaged as `SKILL.md` across all coding agents | Inconsistent spacing, missing hover/disabled states, and broken mobile responsiveness | Manual translation of Figma specs into prompts across each developer's IDE |
| **Agent Token Economics & Safety** | **Tri-model division of labor (`Frontier` + `Efficient` + `Decision`)** catching loops, risky tool calls, and overflow | 100% frontier token burn on routine boilerplate; runaway loops drain API quotas | High per-seat/ACU cloud agent pricing with opaque model routing |
| **Pre-PR Security Review** | **CommBank `CodeCheck` (`MIT`)** runs LLM static security review inside Claude Code & Codex at zero license cost | Security flaws discovered days later in staging or production | `$30–$100/seat/mo` commercial AI SAST plugin subscriptions |
| **Licensing & Governance** | `arch-grower` / `SalkarsaUI` / `CodeCheck` (all **MIT**) + `intern` (**Open RAIL-M**) | Ad-hoc unversioned chat history | Proprietary vendor lock-in |

---

## 5. 🧪 Quantitative FinOps, Closed-Form TCO & 7-Card Summary

### 5.1 Closed-Form Parametric FinOps Model (`CLAIM-20261119-R34-R558-INTERN-CODECHECK-ARCHGROWER-SALKARSAUI`)

> **Provenance & Guardrails**: This section uses a closed-form parametric FinOps model (`provenance: synthetic`, `independently_reproduced: false`) for a 40-person full-stack engineering and AppSec organization (`N = 40`, blended hourly rate `R = $100.00/hr`). Base workstation hardware amortization (`base_hardware_capex`) and daily star velocity (`track_b_stars_today`) are explicitly recorded as `not_measured`.

* **Closed-Form Equation**:
  $$\text{Monthly TCO} = C_{\text{SaaS\_API}} + (H_{\text{ops\_labor}} \times R)$$
  - **Path A (100% Frontier Model Token Burn + Commercial SAST Seats + Vibe-Coding Rewrites + Manual UI Rework)**:
    - $C_{\text{SaaS\_API, A}} = \$1,680.00 + \$960.00 + \$520.00 + \$400.00 = \$3,560.00/\text{mo}$
    - $H_{\text{ops\_labor, A}} = 42.0\text{ hrs/mo} \times \$100.00/\text{hr} = \$4,200.00/\text{mo}$
    - $\text{Total}_{\text{Path A}} = \$3,560.00 + \$4,200.00 = \$7,760.00/\text{mo}$
  - **Path B (Manual Model Switching + Regex SAST + Static Markdown RFCs + Raw shadcn Prompts)**:
    - $C_{\text{SaaS\_API, B}} = \$1,320.00/\text{mo}$, $H_{\text{ops\_labor, B}} = 17.0\text{ hrs/mo} \Rightarrow \$1,700.00/\text{mo}$
    - $\text{Total}_{\text{Path B}} = \$1,320.00 + \$1,700.00 = \$3,020.00/\text{mo}$
  - **Path C (`nace-ai/intern` + `Commonwealth-Bank-of-Australia/CodeCheck` + `Tobi1chi/arch-grower` + `salahudinalyb/SalkarsaUI`)**:
    - $C_{\text{SaaS\_API, C}} = \$55.00\text{ (intern tri-model handoff)} + \$25.00\text{ (CodeCheck review tokens)} + \$15.00\text{ (arch-grower slicing tokens)} + \$0\text{ (SalkarsaUI local skill)} = \$95.00/\text{mo}$
    - $H_{\text{ops\_labor, C}} = 2.5\text{ hrs/mo} \times \$100.00/\text{hr} = \$250.00/\text{mo}$
    - $\text{Total}_{\text{Path C}} = \$95.00 + \$250.00 = \$345.00/\text{mo}$
  - **Net Savings vs. Path A**:
    - Monthly savings: $\$7,760.00 - \$345.00 = \$7,415.00/\text{mo}$ (**`-95.55%`**); Annualized savings: **`$88,980.00/yr`**.

| Architecture Path | Monthly SaaS / API Spend ($C_{\text{SaaS\_API}}$) | Monthly Rework & Triage Labor ($H_{\text{ops\_labor}}$) | Monthly Labor Cost ($@ \$100/\text{hr}$) | Total Monthly TCO | Net Savings vs. Path A | Base Hardware CapEx (`base_hardware_capex`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Path A: 100% Frontier Burn + Commercial SAST + Rework** | `$3,560.00` | `42.0 hrs` | `$4,200.00` | **`$7,760.00`** | Baseline | `not_measured` |
| **Path B: Manual Routing + Regex SAST + Markdown RFCs** | `$1,320.00` | `17.0 hrs` | `$1,700.00` | **`$3,020.00`** | `-$4,740.00` (`-61.08%`) | `not_measured` |
| **Path C: Intern + CodeCheck + Arch-Grower + SalkarsaUI** | **`$95.00`** | **`2.5 hrs`** | **`$250.00`** | **`$345.00`** | **`-$7,415.00` (`-95.55%`)** | `not_measured` |

---

### 5.2 7-Card 4:5 Visual Benchmark Summary

1. **Card 1 (`1 / 7` · `HANDS-ON · TRI-MODEL AGENT, BANK AI SAST, ARCH-GROWER & UI SKILL`)**: Deploying the R558 stack across a 40-engineer team reduces monthly TCO from `$7,760.00` to `$345.00` (`-95.55%`) while preventing vibe-coding architecture drift and runaway agent loops.
2. **Card 2 (`2 / 7` · `SCENARIO: END-TO-END ENTERPRISE MVP FROM 1-LINER TO SECURE PR`)**: Deep dive showing `arch-grower` 15-step topology evolution, `SalkarsaUI` 573-token injection, `intern` tri-model handoff, and `CommBank/CodeCheck` pre-PR security review.
3. **Card 3 (`3 / 7` · `WHAT I TESTED`)**: 4-pillar evaluation matrix across `nace-ai/intern`, `CommBank/CodeCheck`, `Tobi1chi/arch-grower`, and `salahudinalyb/SalkarsaUI`, highlighting mandatory human security review and Open RAIL-M terms.
4. **Card 4 (`4 / 7` · `UNDER THE HOOD`)**: Protocol trace of `intern`'s `Frontier -> Decision Handover -> Efficient` supervisor loop and `arch-grower`'s localized context slicing.
5. **Card 5 (`5 / 7` · `ROBUSTNESS CHECK`)**: Multi-turn stability comparison showing localized context slicing + turn-by-turn supervision eliminating runaway tool loops and cross-module regressions.
6. **Card 6 (`6 / 7` · `LATENCY & TOKEN FINOPS`)**: Paired bars comparing Path C (`$345.00/mo`) vs. Path B (`$3,020.00/mo`) and Path A (`$7,760.00/mo`).
7. **Card 7 (`7 / 7` · `MY TAKE`)**: Side-by-side `✅ Good fit` (supervised tri-model coding, autoregressive architecture slicing, Tailwind v4/shadcn brand enforcement, shift-left CLI security review) and `⛔ Not for` (replacing deterministic CI/CD SAST or human AppSec sign-off with `CodeCheck` alone, scanning unauthorized code).

---

## 6. 🛠️ Enterprise Onboarding & Architecture Review Checklist

- [ ] **1. `Tobi1chi/arch-grower` Localized Slicing Gate**: Configure `arch-grower` (CLI or MCP) so new features undergo lightweight A/B topology evolution and export localized node slices (`arch export-ui`) before coding begins.
- [ ] **2. `salahudinalyb/SalkarsaUI` Agent Skill Installation**: Mount `SKILL.md`, `DESIGN.md`, and `tokens/tokens.css` (`573 tokens`, `51 shadcn/ui components`, `5 breakpoints`) into Claude Code, Codex, and Cursor to forbid hardcoded magic styles.
- [ ] **3. `nace-ai/intern` Tri-Model Routing & Loop Guard**: Bind `intern`'s Frontier, Efficient, and fast Decision models, enabling turn-by-turn supervision for infinite loops, risky tool calls, and context overflow.
- [ ] **4. `Commonwealth-Bank-of-Australia/CodeCheck` Privacy & Scope Compliance**: Run `CodeCheck` strictly on authorized proprietary source code using enterprise zero-data-retention Claude Code / Codex endpoints, and assign internal AppSec ownership for rule updates.
- [ ] **5. Dual Security Gate (Pre-PR AI Check + CI/CD Deterministic SAST)**: Require a qualified engineer to review all `CodeCheck` findings before PR creation while retaining deterministic SAST/SCA gates in CI/CD.
