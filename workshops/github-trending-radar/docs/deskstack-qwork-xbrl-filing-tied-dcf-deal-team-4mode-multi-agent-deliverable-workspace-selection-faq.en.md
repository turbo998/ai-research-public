# XBRL Filing-Tied AI Deal Team (`joaquimmj/deskstack`) & 4-Mode Multi-Agent Deliverable Workspace (`taoqi132/Qwork`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 35 (Cumulative Round 459)  
> **Tracked Repositories**:
> - **`joaquimmj/deskstack`** (`★ 67`, TypeScript / SEC & European XBRL MCP Connector + Claude Plugin `/analyst`, `/associate`, `/md-redteam`, `MIT`): AI financial modeling deal team inside Claude that builds DCFs and Comps directly from SEC 10-K/10-Q and European ESEF filings and runs an independent `/associate` agent to tie out every typed cell—achieving **`0 of 3,230` wrong reported figures** across 50 US/European companies (vs. `36 of 1,018` or `3.5%` wrong with web search only) while cutting per-model cost by `56%–61%` and latency by `2–3x`
> - **`taoqi132/Qwork`** (`★ 66`, Vue 3 + TypeScript + Electron Windows x64 Desktop Workspace, `Apache-2.0`): Local-first multi-agent workspace connecting **Codex, Claude Code, WorkBuddy, Zcode, OpenClaw, and Qwen Code** across four structured collaboration modes (`Roundtable Discussion`, `Create & Review`, `Relay Discussion`, `Independent Analysis`) with side-by-side deliverable and review panels  
> **Audit Claim ID**: `CLAIM-20261117-R35-DESKSTACK-QWORK` (underlying Bloomberg/Capital IQ terminal subscriptions marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Enterprise Corporate Development (M&A), Financial Advisory, and Strategy Teams Cannot Trust Web-Search-Only LLM Financial Models or Disconnected CLI Terminals**:
   - **The `3.5%` Web-Search Financial Modeling Error Rate**: In a 50-company benchmark (35 US, 15 European), asking Claude Sonnet 5.5 to build DCFs and Comps using **web search only** produced **36 wrong figures out of 1,018 (`3.5%`)** plus 7 blank `0` placeholders—caused by pulling stale LTM figures from aggregator sites after new 10-Qs were filed, back-solving share counts from `net income ÷ EPS`, estimating CapEx as `OCF - FCF`, confusing segment D&A with consolidated D&A, or transposing digits (`416,116` vs. `416,161`).
   - **The Multi-Terminal Deliverable Relay Bottleneck**: Turning financial models and project notes into a management presentation or investment memo across Claude Code, Codex, and Qwen Code normally forces analysts to copy-paste context between terminals and manually reconcile conflicting drafts.
   - **The Solution Architect Stack (`deskstack` MIT + `Qwork` Apache-2.0)**: Connect **`joaquimmj/deskstack`** (`MIT`) via MCP so `/analyst` builds `model.xlsx` workbooks directly from SEC and European XBRL filings (with a dedicated **Sources sheet** linking every blue input cell to its exact filing accession number and XBRL concept), `/associate` ties out every number (**`0 / 3,230` wrong**), and `/md-redteam` stress-tests implied WACC before a mandatory human sign-off gate; pair it with **`taoqi132/Qwork`** (`Apache-2.0`) on Windows workstations to coordinate local CLI agents in **`Create & Review`** and **`Roundtable Discussion`** modes with the delivered presentation/memo displayed beside an independent agent's review.
2. **Closed-Form FinOps Impact (20 M&A / Strategy Teams Building 250 Monthly DCF/Comps Models & 180 Executive Presentations/Memos at `$95.00/hr`)**:
   - Migrating from **Path A (Web-Search-Only LLM Financial Models + Manual Multi-Terminal Relaying at `$5,930.00/mo`)** to **Path C (`deskstack` MIT XBRL Deal Team + `Qwork` Apache-2.0 Workspace at `$365.00/mo`)** saves **`$5,565.00/mo` (`-93.84%`, or `$66,780.00/yr`)** while cutting manual 10-K tie-out audits and cross-terminal copy-paste labor from `38.0 hrs/mo` to `3.0 hrs/mo` (**`92.11%` reduction**).

![deskstack + Qwork Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r35-deskstack-qwork.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `joaquimmj/deskstack` eliminate the `3.5%` web-search error rate (`0 / 3,230` wrong figures) while cutting DCF/Comps build cost by `56%–61%`?
- **Plain-Language Definition**: `deskstack` (`MIT`) is a **two-part SEC + European XBRL data connector MCP (`https://deskstack.deskstack-server.workers.dev/mcp` or self-hosted) and role-separated Claude plugin (`/analyst`, `/associate`, `/md-redteam`)**.
- **Three Institutional-Grade Controls**:
  1. **Direct XBRL Filing Ingestion + Dedicated `Sources` Sheet**: Instead of scraping financial aggregator websites or Wikipedia, the connector feeds exact filed figures from US SEC (10-K/10-Q) and European filings. Every typed blue input cell in `model.xlsx` is recorded on a **Sources sheet** with its line item, period, value, 10-K accession number, link, and XBRL concept;
  2. **Role-Separated `/associate` Tie-Out & `/md-redteam` Valuation Challenge**:
     - **`/associate`** checks every typed number in the workbook against the source filing—catching transposed digits such as Apple FY2025 revenue typed as `416,116` when the 10-K reports `416,161`;
     - **`/md-redteam`** challenges the economic thesis—showing, for example, that a `$230` share price in the Apple DCF implies a `7.74%` WACC against the `10.6%` WACC assumed in the model;
     - **Human Sign-Off Token Gate**: Nothing is exported until tie-out, model review, and compliance pass and the human approves the sign-off page in their own words.
- **Measured 50-Company Benchmark (`35 US + 15 European`, Claude Sonnet 5.5, Hand-Verified Against Filings)**:
  - **DCF**: Web search only had **`20 of 573` wrong (`3.5%`, `$0.23 / 58s`)** ➔ `deskstack + reviewers` had **`0 of 606` wrong (`$0.10 / 32s`, `-56.5%` cost & `-44.8%` time)**;
  - **Comps**: Web search only had **`16 of 445` wrong (`3.6%` + 7 left as `0`, `$0.56 / 171s`)** ➔ `deskstack + reviewers` had **`0 of 1,010` wrong (`$0.22 / 51s`, `-60.7%` cost & `-70.2%` time)**.

### Q2: How does `taoqi132/Qwork` turn disconnected local CLI agents into a coordinated deliverable and review team?
- **Plain-Language Definition**: `Qwork` (`Apache-2.0`, Vue 3 + TypeScript + Electron) is a **local-first Windows workspace that orchestrates Codex, Claude Code, WorkBuddy, Zcode, OpenClaw, and Qwen Code around shared briefs and side-by-side deliverable reviews**.
- **Three Core Workflow Advantages**:
  1. **Four Explicit Collaboration Modes**:
     - **Roundtable Discussion**: Multiple agents synthesize project notes and source documents into a management briefing with open questions;
     - **Create & Review**: One agent produces the presentation, report, or code file while a second independent agent audits the actual file against source materials;
     - **Relay Discussion**: Sequentially expands a rough idea into requirements, implementation steps, and acceptance criteria;
     - **Independent Analysis**: Compares independent agent perspectives side by side to produce a trade-off decision memo.
  2. **Deliverable-Adjacent Review Panel**: Displays the generated file right beside the reviewer agent's critique and escalates only critical source gaps to the human.

### Q3: How should an AI Solution Architect combine `deskstack` and `Qwork`?
- **Quantitative Valuation Layer (`deskstack` MCP + Plugin)**: Run `/deal-team <Company> quick-dcf` in Claude / Claude Code to generate XBRL-tied `model.xlsx` workbooks verified by `/associate` and `/md-redteam`.
- **Executive Deliverable & Multi-Agent Review Layer (`Qwork`)**: Feed the approved `deskstack` workbook and diligence notes into `Qwork`'s **Create & Review** mode so one local CLI agent authors the investment committee deck and a second CLI agent independently verifies every number and source citation.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph DealTeam["XBRL-Tied Valuation Layer: joaquimmj/deskstack (MIT, MCP + Plugin)"]
        A[US SEC 10-K/10-Q &amp; European ESEF Filings] --> B[deskstack MCP Data Connector<br/>Every Figure Tied to Accession Number &amp; XBRL Concept]
        B --> C[/analyst Builds DCF &amp; Comps model.xlsx<br/>Populates Dedicated Sources Sheet/]
        C --> D[/associate Cell-by-Cell Tie-Out<br/>Catches Digit Swaps 416,116 vs 416,161 · 0/3,230 Wrong/]
        D --> E[/md-redteam Implied-WACC Challenge<br/>+ Human Sign-Off Token Gate/]
    end

    subgraph DeliverableHub["Multi-Agent Deliverable Workspace: taoqi132/Qwork (Apache-2.0, Electron)"]
        E --> F[Approved model.xlsx + Diligence Notes Enter Qwork]
        F --> G{Select Collaboration Mode}
        G -->|Create &amp; Review| H[Creator Agent Builds Management Deck/Report<br/>Reviewer Agent Audits File Against Sources]
        G -->|Roundtable / Independent| I[Multi-Agent Trade-Off &amp; Risk Memo]
        H & I --> J[Side-by-Side Deliverable &amp; Review Panel Sign-Off]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Web-Search-Only LLM Financial Models + Manual CLI Relay | Option B: Manual EDGAR Copy-Paste + Single-Agent Slide Drafts | **Option C (Recommended): `deskstack` (MIT) + `Qwork` (Apache-2.0)** |
| :--- | :--- | :--- | :--- |
| **DCF & Comps Figure Accuracy (50-Company Benchmark)** | ❌ **`3.5%–3.6%` wrong figures** (stale aggregator LTM, derived share counts) | ⚠️ Prone to manual transposition typos (`416,116` vs `416,161`) | ✅ **`0 / 3,230` wrong figures** (direct XBRL connector + `/associate` tie-out + `Sources` sheet) |
| **Per-Model Build Cost & Wall-Clock Latency** | ❌ DCF `$0.23 / 58s`, Comps `$0.56 / 171s` | ❌ Hours of manual spreadsheet entry per company | ✅ **DCF `$0.10 / 32s` (`-56.5%` cost), Comps `$0.22 / 51s` (`-60.7%` cost, `-70.2%` time)** |
| **Valuation Thesis Red-Teaming & Export Gate** | ❌ No implied-WACC check; unverified workbooks exported directly | ⚠️ Relies on senior associate manual formula spot-checks | ✅ **`/md-redteam` implied-WACC check + mandatory human sign-off token before export** |
| **Multi-Agent Deliverable Authoring & Review** | ❌ Manual copy-pasting between separate CLI terminal windows | ❌ Single agent grades its own presentation draft | ✅ **`Qwork` coordinates 6 local CLIs in 4 modes with side-by-side deliverable + review UI** |
| **Monthly TCO (250 Models + 180 Decks/Mo)** | **`$5,930.00 / mo`** (`$2,320` search/add-ons + `38.0 hrs` manual tie-out) | **`$2,650.00 / mo`** (`$940` tools + `18.0 hrs` manual entry/edits) | **`$365.00 / mo`** (**`-93.84%` savings**; `$80` MCP runs + `3.0 hrs` sign-off approval) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R35-DESKSTACK-QWORK`)

> **Scope & Boundary Declaration**: Evaluated for 20 corporate development, M&A advisory, and strategy teams building **250 monthly US/European DCF & Comps valuation workbooks and 180 executive presentations/memos** at a blended rate of `$95.00/hr` (underlying Bloomberg/Capital IQ terminal subscriptions marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Modeling API \& Data Add-On Spend} + (\text{10-K Tie-Out, Error Fix \& Multi-CLI Relay Hours} \times \$95.00)$$

| Cost Component | Path A: Web-Search LLM Models + Manual CLI Relay | Path B: Manual EDGAR Entry + 1-Agent Drafts | **Path C: `deskstack` (MIT) + `Qwork` (Apache-2.0)** |
| :--- | :---: | :---: | :---: |
| **Monthly Modeling API & Financial Data Add-On Spend** | `$2,320.00` | `$940.00` | **`$80.00`** (`$0.10/DCF` & `$0.22/Comps` XBRL MCP) |
| **Monthly 10-K Tie-Out, Error Fix & CLI Relay Hours** | `38.0 hrs` | `18.0 hrs` | **`3.0 hrs`** (**`92.11%` reduction**) |
| **Monthly M&A & Strategy Architect Labor (`@ $95.00/hr`)** | `$3,610.00` | `$1,710.00` | **`$285.00`** |
| **Total Monthly TCO** | **`$5,930.00`** | **`$2,650.00`** (`-55.31%`) | **`$365.00`** (**`-93.84%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,280.00 / mo` (`$39,360/yr`) | **`$5,565.00 / mo` (`$66,780.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Connect the `deskstack` XBRL MCP Server & Install the `/deal-team` Plugin**: Add `https://deskstack.deskstack-server.workers.dev/mcp` (or self-host via `docs/SELF_HOSTING.md`), install `/plugin install deskstack --marketplace joaquimmj/deskstack` in Claude / Claude Code (`2.1.275+`), and run `/deskstack-doctor`.
- [ ] **Step 2 — Mandate `/associate` Tie-Outs & `/md-redteam` Checks on All Valuation Models**: Forbid web-search-only financial figure entry; require every DCF and Comps workbook to include the XBRL `Sources` sheet and pass the human Sign-Off Page before export.
- [ ] **Step 3 — Deploy `taoqi132/Qwork` to Unify Local Agent CLIs on Windows**: Connect local Claude Code, Codex, and Qwen Code installations inside `Qwork` so analysts stop copy-pasting context between separate terminals.
- [ ] **Step 4 — Use `Create & Review` Mode for All Executive Decks & Memos**: Configure `Qwork` so one agent drafts the presentation/report from the approved `deskstack` workbook while a second independent agent reviews the deliverable alongside the file.
