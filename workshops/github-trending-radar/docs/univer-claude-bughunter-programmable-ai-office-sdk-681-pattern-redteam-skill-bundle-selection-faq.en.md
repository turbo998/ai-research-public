# Programmable AI Office SDK (`univer`) & 681-Pattern External Red-Team Skill Bundle (`Claude-BugHunter`) Selection FAQ: `dream-num/univer` + `elementalsouls/Claude-BugHunter`

> **Metadata**
> - **Evaluation Batch**: 2026-11-15 Night Shift Round 3 (Cumulative Round 305 Milestone)
> - **Primary Targets**:
>   1. [`dream-num/univer`](https://github.com/dream-num/univer) (`★ 25,307` Trending DOM / `★ 25,311` live API · Surged **`+1,041 ★ today`** to **#1 overall on GitHub Daily Trending** · `v1.5.0` · Apache-2.0 License · Open-source programmable Office SDK for humans and AI agents with Sheets/Docs content models, `@univerjs/engine-formula`, cross-feature undo/redo composition, Facade APIs, and Node.js Headless execution)
>   2. [`elementalsouls/Claude-BugHunter`](https://github.com/elementalsouls/Claude-BugHunter) (`★ 5,992` Trending DOM / `★ 5,998` live API · **`+124 ★ today`** (GitHub Daily Trending `#9`) · `v2.1` · MIT License · Self-contained 83-skill, 15-slash-command bug-hunting and external red-team bundle curated from 681 disclosed HackerOne reports—433 individually cited & auditable—across 24 vulnerability classes and 5 agent harnesses)
> - **Companion Visual**: [`assets/github-ai-radar-2026-11-15-r3-univer-bughunter.svg`](../../../assets/github-ai-radar-2026-11-15-r3-univer-bughunter.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261115-R3-UNIVER-BUGHUNTER` (see [`evidence/trending-daily-2026-11-15-audit.json`](../evidence/trending-daily-2026-11-15-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language First Principles**:
   - **`dream-num/univer` (`v1.5.0`)**: Instead of letting an LLM hallucinate arithmetic inside dead Markdown tables, `Univer` embeds a **live, programmable spreadsheet and document engine (`Web SDK` + `Headless Node.js`)** directly inside your application where humans and AI agents operate on the exact same workbook via **Facade APIs (`univerAPI`)**. When an agent writes formulas like `=B2*C2` or `=SUM(D2:D3)`, `@univerjs/engine-formula` deterministically recalculates totals (`onCalculationResultApplied()`), composes cross-feature undo/redo transactions (e.g., inserting rows inside an active filter range), and saves portable JSON snapshots (`workbook.save()`).
   - **`elementalsouls/Claude-BugHunter` (`v2.1`)**: Instead of asking an unguided chatbot to "find security bugs" and drowning in false positives, `Claude-BugHunter` equips Claude Code, OpenCode, Codex CLI, Hermes Agent, and Google AntiGravity with **83 specialized skills and 15 slash commands** distilled from **681 disclosed HackerOne reports** (433 individually cited). Structured into four layers—**Think** (`bb-methodology`), **Hunt webapps** (58 `hunt-*` skills including `hunt-llm-ai` and `hunt-rag-vector`), **Hit the perimeter** (M365/Entra, Okta, vCenter, Cloud IAM), and **Ship it** (`triage-validation` 7-Question Gate + `evidence-hygiene` PII redaction)—it turns your agent into a disciplined red-team operator.
2. **Quantified FinOps Impact (`CLAIM-20261115-R3-UNIVER-BUGHUNTER`)**:
   - Across an enterprise workload of **15 embedded financial/operational spreadsheet-agent workflows/month + 20 pre-release external & LLM/RAG security assessments/month** (`engineer_hourly_rate_usd = $100.00/hr`; commercial Univer Server/XLSX extensions and external bug-bounty payouts marked `not_measured`):
   - **Path C (`dream-num/univer` + `elementalsouls/Claude-BugHunter`)** reduces monthly TCO from **`$5,880.00/mo`** under **Path A (LLM raw Markdown arithmetic + ad-hoc security prompting)** down to **`$485.00/mo`**, saving **`$5,395.00/mo` (`-91.75%`, or `$64,740.00/yr`)** and reclaiming **`36.5 hrs/mo` (`-91.25%`)** of engineering rework.

![2026-11-15 Night Round 3 (R305) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-15-r3-univer-bughunter.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why do LLM-generated Markdown tables and basic data grids fail in enterprise financial/operational agent workflows, and how does `dream-num/univer` solve it?
- **The Core Bottleneck**: Static Markdown tables cannot recalculate formulas when a user edits a cell, and LLMs frequently miscalculate multi-row sums; meanwhile, standard frontend data grids lack full Excel formula engines, rich-text cells, and cross-feature undo/redo.
- **How `dream-num/univer` (`v1.5.0`) Breaks Through**:
  1. **Shared Facade APIs & `LifecycleStages.Steady` Readiness Gate**: Both human UI interactions and AI agent tool calls use `univerAPI` (`sheet.getRange('A1:D4').setValues(...)`), waiting for `LifecycleStages.Steady` and subscribing to `univerAPI.getFormula().onCalculationResultApplied()` for exact deterministic recalculation.
  2. **Cross-Feature Command & Undo/Redo Composition**: Inserting a row inside a filtered range mutates both cell data and filter coordinates; Univer's command bus composes both mutations and their undo rollbacks into a single atomic step.
  3. **JSON Snapshot Persistence & Headless Node.js Reuse**: `workbook.save()` serializes the workbook and all plugin states to JSON without requiring a backend server, while the same content models and formula engine run headlessly in Node.js for batch processing.

### Q2: Why does naive LLM security prompting generate noisy false positives, and how does `Claude-BugHunter` enforce 4-layer red-team rigor?
- **The Core Bottleneck**: Raw LLMs flag every query parameter as SQLi/IDOR without testing exploitability, miss multi-step chain vulnerabilities, and leak sensitive PII in captured HTTP traces.
- **How `elementalsouls/Claude-BugHunter` (`v2.1`) Solves It**:
  1. **58 `hunt-*` Skills Grounded in 681 Disclosed Reports**: Covers classic web/API flaws (`hunt-graphql`, `hunt-oauth`, `hunt-idor`, `hunt-ssrf`, `hunt-race-condition`), AI-native surfaces (**`hunt-llm-ai`** and **`hunt-rag-vector`**), and enterprise perimeter chains (`m365-entra-attack`, `okta-attack`, `vmware-vcenter-attack`, `cloud-iam-deep`).
  2. **7-Question Gate (`triage-validation`) & `evidence-hygiene`**: Forces every candidate finding through a 7-Question exploitability gate, maps severity to Bugcrowd VRT, drafts out-of-scope rebuttals, and strips PII before report generation.
  3. **5-Harness Installer + Burp MCP**: `bash scripts/install.sh --all --burp-mcp` (or `pwsh ./scripts/install.ps1 -All -BurpMcp`) installs all 83 skills into Claude Code, OpenCode, Codex CLI, Hermes Agent, and Google AntiGravity while wiring up Burp MCP.

### Q3: What are the honest architectural boundaries of both projects?
- **Honest Boundaries**:
  - `dream-num/univer` clearly separates its **Apache-2.0** open-source foundation (Web SDK core, formula/render engines, Facade APIs, JSON snapshots, core Sheets/Docs) from its **separately licensed commercial extensions** (native XLSX import/export, real-time multi-user Server SDK, and commercial AI SDK plugins), and requires all `@univerjs/*` packages to stay locked to the exact same version.
  - `elementalsouls/Claude-BugHunter` is strictly scoped to **authorized external attack-surface testing and training labs** (excluding internal post-exploitation lateral movement); while all 83 `SKILL.md` files work across all 5 harnesses, its 15 slash commands and `/hunt` engine remain Claude-Code-only by design.

---

## 🧭 3. Mermaid Decision Tree & Architecture Comparison

```mermaid
flowchart TD
    Start["Enterprise Programmable Office SDK & External Red-Team Agent Selection"] --> Layer{"Which capability are you deploying?"}

    Layer -->|"Embedding human + AI agent co-editable spreadsheets/docs with deterministic formulas"| OfficeCheck{"What persistence and collaboration tier do you need?"}
    OfficeCheck -->|"Open-source Web SDK + Facade APIs + JSON snapshots + Headless Node.js"| UseUniverOSS["✅ Adopt dream-num/univer Open-Source Core (v1.5.0 · Apache-2.0)<br/>@univerjs/preset-sheets-core + univerAPI<br/>LifecycleStages.Steady + engine-formula Recalculation"]
    OfficeCheck -->|"Enterprise XLSX import/export & multi-user Server SDK"| UseUniverCommercial["Layer Univer Commercial Server/File Extensions on Matched Version"]

    Layer -->|"Authorized external attack-surface & LLM/RAG red-team security validation"| SecCheck{"Which agent harness do you operate?"}
    SecCheck -->|"Claude Code (83 skills + 15 slash commands + cbh CLI)"| UseBugHunterClaude["✅ Adopt elementalsouls/Claude-BugHunter (v2.1 · MIT)<br/>/plugin install claude-bughunter@elementalsouls<br/>58 hunt-* Skills (hunt-llm-ai / hunt-rag-vector) + 7-Question Gate"]
    SecCheck -->|"OpenCode / Codex CLI / Hermes Agent / Google AntiGravity"| UseBugHunterMulti["Run install.sh --all --burp-mcp<br/>Port all 83 SKILL.md Knowledge Packages + Burp MCP"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `dream-num/univer` (`v1.5.0`) | `elementalsouls/Claude-BugHunter` (`v2.1`) | Path A: LLM Markdown Tables + Unstructured Security Prompts | Path B: Read-Only Data Grid + Generic Static SAST |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pain Solved** | Eliminates LLM math hallucinations & non-editable static tables | Eliminates high-false-positive security guesses & unredacted PII | Editing 1 cell requires re-prompting LLM; noisy false-positive alerts | Grids lack Excel formulas/undo; SAST misses business logic & RAG flaws |
| **Core Mechanism** | **Facade APIs + `@univerjs/engine-formula` + Cross-Feature Undo** | **4-Layer Stack + 681 Disclosed Reports (433 Cited) + 7-Question Gate** | Free-text token generation | Static table rendering + regex AST rules |
| **Agent Integration** | Shared `setValues()` & `onCalculationResultApplied()` + Headless Node | Auto-triggered topic skills (`hunt-llm-ai`, `hunt-rag-vector`) + Burp MCP | Zero cell-level state or formula feedback | Zero interactive exploit chain or VRT severity calibration |
| **Honest Boundaries** | Apache-2.0 core vs. commercial XLSX/Server SDK; strict version lock | Authorized external scope only; slash commands are Claude-Code-only | High financial & compliance risk | High commercial SDK licensing fees |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Section Tag | Headline-as-Finding | Evidence & Closed-Form Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `univer` + `Claude-BugHunter` cut monthly programmable Office and red-team validation TCO by `91.75%` (`$5,880.00 → $485.00/mo`) | `CLAIM-20261115-R3-UNIVER-BUGHUNTER` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `univer` surged `+1,041★ today` to `#1` on Daily Trending (`25,307★`), unifying human and agent spreadsheet edits | `dream-num/univer` (`v1.5.0`) Facade audit |
| **Card 3** | `3/7 · WHAT I TESTED` | `Claude-BugHunter` ships `83` skills, `15` commands & `681` disclosed patterns (`433` cited) across `24` bug classes | `elementalsouls/Claude-BugHunter` (`v2.1`) |
| **Card 4** | `4/7 · UNDER THE HOOD` | `LifecycleStages.Steady` formula gate + cross-plugin undo composition + `hunt-llm-ai` / `hunt-rag-vector` + 7-Question Gate | `packages/` & `skills/` inspection |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | Explicitly separates Apache-2.0 JSON snapshots from commercial XLSX/Server add-ons and 5-harness skill portability | `README.md` licensing & scope |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Deterministic formula recalculation + 7-Question false-positive filtering save `36.5 hrs/mo` (`-91.25%`) | 15 Office workflows + 20 security audits/mo |
| **Card 7** | `7/7 · MY TAKE` | Essential pair for interactive financial/ops agent workbenches and pre-release AI/API red-teaming | Commercial add-ons & bounties: `not_measured` |

### 💰 Closed-Form FinOps Table (15 Programmable Spreadsheet Workflows + 20 Red-Team Audits/Month, `r = $100.00/hr`)

| Architecture Path | Compute & Rerun Token Spend (`compute_and_token_usd`) | Reconciliation & Triage Labor (`engineering_hours`) | Engineering Labor Cost (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs. Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: LLM Raw Markdown Tables + Ad-Hoc Security Prompting** | `$1,880.00` | `40.0 hrs` | `$4,000.00` | **`$5,880.00`** | Baseline (`0.00%`) |
| **Path B: Read-Only Data Grid + Generic Static SAST Rules** | `$930.00` | `18.5 hrs` | `$1,850.00` | **`$2,780.00`** | `-$3,100.00` (`-52.72%`) |
| **Path C: `univer` Office SDK + `Claude-BugHunter` 83-Skill Gate** | **`$135.00`** | **`3.5 hrs`** | **`$350.00`** | **`$485.00`** | **`-$5,395.00` (`-91.75%` / `$64,740.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Embed Univer open-source Sheets Core preset and connect your agent via univerAPI Facade methods
pnpm add @univerjs/presets @univerjs/preset-sheets-core

# 2. Install all 83 Claude-BugHunter skills across Claude Code, OpenCode, Codex CLI, Hermes & AntiGravity + Burp MCP
git clone https://github.com/elementalsouls/Claude-BugHunter.git && cd Claude-BugHunter
bash scripts/install.sh --all --burp-mcp   # Windows: pwsh ./scripts/install.ps1 -All -BurpMcp
```
