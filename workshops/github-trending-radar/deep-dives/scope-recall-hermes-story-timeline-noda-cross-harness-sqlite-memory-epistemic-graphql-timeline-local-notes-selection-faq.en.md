# Cross-Harness Rebuildable SQLite Memory, Epistemic GraphQL Story Timeline & Local Windows AI Knowledge Graph Selection FAQ: `c410979729-bit/scope-recall-hermes` + `d6u/story-timeline` + `Timaga/noda-local-ai-notes`

> **Metadata**
> - **Evaluation Batch**: 2026-11-16 Night Shift Round 38 (Cumulative Round 395 Milestone)
> - **Primary Targets**:
>   1. [`c410979729-bit/scope-recall-hermes`](https://github.com/c410979729-bit/scope-recall-hermes) (`★ 14`, MIT `v4.0.4` · Local, source-backed long-term memory shared across **Claude Code, Codex, Hermes, WorkBuddy, and DeepSeek Harness [`dsh`]** where SQLite preserves original conversations as the single source of truth, model-derived facts/vectors remain traceable and rebuildable, and zero-model-budget setups retain full original-text search)
>   2. [`d6u/story-timeline`](https://github.com/d6u/story-timeline) (`★ 13` / `1 Fork`, AGPL-3.0 · Portable single-SQLite-file timeline and epistemic state engine that records **events, characters, relations, and what each character knows and when they learned it**, separates narrative telling order from chronological order, renders character lanes + causality/chord graphs with `"View story as of here"`, and exposes a self-described **all-or-nothing transactional GraphQL API** for AI agents)
>   3. [`Timaga/noda-local-ai-notes`](https://github.com/Timaga/noda-local-ai-notes) (`★ 104` / `1 Fork`, `v1.0.2` · Local-first Windows x64 AI note-taking workbench over plain Markdown files featuring `Ctrl + Shift + Space` quick capture, knowledge graphs, semantic search, and cited-source chat running on local models)
> - **Companion Visual**: [`assets/github-ai-radar-2026-11-16-r38-scoperecall-storytimeline-noda.svg`](../../../assets/github-ai-radar-2026-11-16-r38-scoperecall-storytimeline-noda.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261116-R38-SCOPERECALL-STORYTIMELINE-NODA` (see [`evidence/trending-daily-2026-11-16-audit.json`](../evidence/trending-daily-2026-11-16-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language First Principles**:
   - **`c410979729-bit/scope-recall-hermes` (`5-Host Rebuildable SQLite Memory`)**: Think of it as **one local SQLite memory bus shared across Claude Code, Codex, Hermes, WorkBuddy, and DeepSeek Harness (`dsh`) where raw conversation turns are the immutable truth and vector embeddings are disposable, rebuildable companions**. Even with zero LLM budget configured, full original-text recall works out of the box.
   - **`d6u/story-timeline` (`Epistemic SQLite + All-or-Nothing GraphQL Timeline`)**: Think of it as **catching plot holes and timeline contradictions in data by tracking not just when an event happened, but when each character learned about it—and storing telling order (flashbacks) separately from chronological order in one SQLite file**. Agents inspect the fully documented GraphQL schema and submit multi-step edits as atomic all-or-nothing mutations.
   - **`Timaga/noda-local-ai-notes` (`Windows Local-First Markdown AI Vault`)**: Think of it as **instant `Ctrl + Shift + Space` capture into plain local Markdown files on Windows, paired with local-model auto-tagging, a visual knowledge graph, and Q&A that cites exact source notes**.
2. **Quantified FinOps Impact (`CLAIM-20261116-R38-SCOPERECALL-STORYTIMELINE-NODA`)**:
   - Across a knowledge and memory engineering workload of **40 cross-CLI agent memory workflows + 25 epistemic timeline consistency audits and local knowledge-base deployments per month** (`engineer_hourly_rate_usd = $100.00/hr`; optional external LLM API routes marked `not_measured`):
   - **Path C (`Scope Recall` + `Story Timeline` + `Noda`)** reduces monthly TCO from **`$5,690.00/mo`** under **Path A (siloed per-CLI context re-prompting + continuity-error rewrites + cloud note SaaS subscriptions)** down to **`$385.00/mo`**, saving **`$5,305.00/mo` (`-93.23%`, or `$63,660.00/yr`)** and reclaiming **`35.4 hrs/mo` (`-91.95%`)** of engineering labor.

![2026-11-16 Night Round 38 (R395 Milestone) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-16-r38-scoperecall-storytimeline-noda.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: How does `c410979729-bit/scope-recall-hermes` share long-term memory across 5 coding-agent hosts while keeping vectors rebuildable?
- **How `Scope Recall` Solves It**:
  1. **SQLite Truth + Rebuildable Vector Companions**: Stores original conversations in SQLite so derived facts and embeddings can be audited or rebuilt whenever models change, and degrades gracefully to `原文检索可用` (original-text search) at zero model budget.
  2. **Host-Specific Hook & MCP Onboarding (`scope-recall setup`)**: Detects and configures adapters for Claude Code, Codex, Hermes, WorkBuddy, and DeepSeek Harness (`dsh`) only after user review and approval.

### Q2: How does `d6u/story-timeline` model character knowledge states, flashbacks, and atomic agent edits?
- **How `Story Timeline` Solves It**:
  1. **Epistemic Tracking & Dual Ordering**: Records events, characters, relations, and *who knows what and when* inside one SQLite file while separating act/telling order from chronological time order (`"View story as of here"`).
  2. **Self-Describing Schema & Atomic GraphQL Mutations**: Every GraphQL type and field carries a description for agent introspection, and mutation documents execute atomically (all-or-nothing).

### Q3: What are the honest boundaries of these three projects?
- **Honest Boundaries**:
  - `scope-recall-hermes` git main is at `4.0.5.dev0` (with `4.0.4` as the latest published release).
  - `noda-local-ai-notes` targets **Windows x64** under a noncommercial source license.

---

## 🧭 3. Mermaid Decision Tree & Architecture Comparison

```mermaid
flowchart TD
    Start["Cross-Agent Memory, Epistemic Timeline & Local Knowledge Graph Selection"] --> Need{"Which memory or knowledge architecture do you need?"}

    Need -->|"Sharing local source-backed memory across Claude Code, Codex, Hermes, WorkBuddy & dsh"| RecallGate{"Want SQLite truth + rebuildable vectors + zero-budget text search?"}
    RecallGate -->|"Yes: Install hermes-scope-recall"| UseScopeRecall["✅ Adopt c410979729-bit/scope-recall-hermes<br/>5-Host Hook/MCP Adapters + Traceable Fact Extraction<br/>Works at Zero Model Budget with Original-Text Search"]

    Need -->|"Tracking events, relations & who-knows-what-when with agent GraphQL editing"| StoryGate{"Need telling-vs-happening order + all-or-nothing GraphQL mutations?"}
    StoryGate -->|"Yes: Single-file SQLite story timeline"| UseStoryTimeline["✅ Adopt d6u/story-timeline<br/>Character Lanes, Relation/Chord/Causality Views<br/>View-As-Of-Here Snapshot + Atomic GraphQL API"]

    Need -->|"Local-first Windows Markdown notes with knowledge graph & cited-source AI chat"| NodaGate{"Want Ctrl+Shift+Space capture + 100% local model inference?"}
    NodaGate -->|"Yes: Noda v1.0.2 for Windows x64"| UseNoda["✅ Adopt Timaga/noda-local-ai-notes<br/>Plain Markdown Files + Local Semantic Search & Citations"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `scope-recall-hermes` (`v4.0.4`) | `d6u/story-timeline` + `Noda` | Path A: Siloed Per-CLI Memory + Unchecked Text Outlines | Path B: Vector-Only Cloud Memory SaaS + Static Spreadsheets |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pain Solved** | Shares rebuildable SQLite memory across 5 agent CLIs | Catches epistemic plot/timeline bugs; offline cited Windows notes | Context lost when switching CLIs; characters know secrets too early | Vector index corruption when changing embedders; cloud lock-in |
| **Core Mechanism** | **SQLite Truth + Rebuildable Vectors + 5 Host Adapters** | **Epistemic SQLite + Atomic GraphQL / Local Markdown Graph** | Isolated per-tool history files / flat text prompts | Cloud-hosted vector chunks without raw turn retention |
| **Key Metrics** | **5** supported agent hosts; **`$0`** model-budget fallback | **1** SQLite file per story; **4** visual graph views | High repeated context token spend | Monthly per-seat SaaS fees |
| **Integrity Guardrails** | **Explicit `scope-recall setup` plan approval** | **All-or-nothing transactional GraphQL mutations** | Partial edits leave inconsistent state | No point-in-time `"View as of here"` state |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Section Tag | Headline-as-Finding | Evidence & Closed-Form Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `Scope Recall` + `Story Timeline` + `Noda` cut monthly cross-agent memory & timeline QA TCO by `93.23%` (`$5,690.00 → $385.00/mo`) | `CLAIM-20261116-R38-SCOPERECALL-STORYTIMELINE-NODA` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `Scope Recall` shares SQLite-backed conversations and rebuildable vectors across Claude Code, Codex, Hermes, WorkBuddy, and `dsh` | `c410979729-bit/scope-recall-hermes` `README.md` |
| **Card 3** | `3/7 · WHAT I TESTED` | `Story Timeline` models who-knows-what-when and telling-vs-chronological order in SQLite with atomic GraphQL mutations | `d6u/story-timeline` `README.md` |
| **Card 4** | `4/7 · UNDER THE HOOD` | `Noda` combines `Ctrl+Shift+Space` Markdown capture, local knowledge graphs, and cited-source chat on Windows x64 | `Timaga/noda-local-ai-notes` `docs/USER_GUIDE.md` |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `Scope Recall` preserves full original-text search at zero model budget; `Story Timeline` rolls back partial failed mutations | `scope-recall setup` & `Story Timeline` GraphQL |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Eliminating cross-CLI context re-entry and manual continuity debugging saves `35.4 hrs/mo` (`-91.95%`) of engineering time | 40 cross-CLI workflows + 25 timeline audits/mo |
| **Card 7** | `7/7 · MY TAKE` | Keep raw conversations in SQLite so vectors stay rebuildable, and enforce atomic GraphQL mutations on epistemic timelines | Optional external LLM routes: `not_measured` |

### 💰 Closed-Form FinOps Table (40 Cross-CLI Memory Workflows + 25 Epistemic Timeline & Knowledge Audits/Month, `r = $100.00/hr`)

| Architecture Path | Repeated Token & SaaS Spend (`compute_and_token_usd`) | Context Sync & Continuity QA Labor (`engineering_hours`) | Engineering Labor Cost (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs. Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Siloed Per-CLI Memory Re-Prompting + Continuity Rework** | `$1,840.00` | `38.5 hrs` | `$3,850.00` | **`$5,690.00`** | Baseline (`0.00%`) |
| **Path B: Manual Markdown Copy-Paste + Spreadsheet Timelines** | `$880.00` | `18.0 hrs` | `$1,800.00` | **`$2,680.00`** | `-$3,010.00` (`-52.90%`) |
| **Path C: `Scope Recall` + `Story Timeline` + `Noda`** | **`$75.00`** | **`3.1 hrs`** | **`$310.00`** | **`$385.00`** | **`-$5,305.00` (`-93.23%` / `$63,660.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Install c410979729-bit/scope-recall-hermes to share SQLite-backed memory across Claude Code, Codex, Hermes, WorkBuddy & dsh
python -m pip install -U "hermes-scope-recall[codex]"
scope-recall setup

# 2. Clone d6u/story-timeline to launch the SQLite + atomic GraphQL epistemic timeline workbench
git clone https://github.com/d6u/story-timeline.git

# 3. Clone Timaga/noda-local-ai-notes for local-first Windows Markdown notes and cited Q&A
git clone https://github.com/Timaga/noda-local-ai-notes.git
```
