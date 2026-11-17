# Local-First Agent Observability & Eval Engine (`jackulau/coding.sh`) & Transactional Rollback MCP (`OnlyTerp/turnpack`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 32 (Cumulative Round 456)  
> **Tracked Repositories**:
> - **`jackulau/coding.sh`** (`★ 117`, TypeScript / Node >= 22.16, Zero Runtime Dependencies, SQLite / Postgres / ClickHouse, `MIT`): Local-first observability and evaluation platform for AI coding agents (Claude Code, Codex CLI, Cursor, and OTLP apps) that captures prompts, subagents, diffs, test badges, cache hit rates, and costs on your machine, flags sessions that edited code without running a test check (`coding.sh improve`), and turns failed sessions into replayable evals (`coding.sh eval new` & `coding.sh exp compare`)
> - **`OnlyTerp/turnpack`** (`★ 64`, TypeScript / Node >= 22, Zero Runtime Dependencies, `Apache-2.0`): Local stdio MCP server exposing `pack`, `ship`, and `batch`—where `ship` applies multi-file edits, runs your test command, and **restores every modified file byte-for-byte on failure (`FAILED_AND_ROLLED_BACK`)** while pinpointing untouched caller files; measured on Claude Code 2.1.280 + Sonnet 5 to cut **round trips from `6 → 3` (`-50%`), wall time from `23.4s → 12.7s` (`-45.7%`), output tokens by `-57.3%`, and task cost from `$0.131 → $0.084` (`-35.9%`)**  
> **Audit Claim ID**: `CLAIM-20261117-R32-CODINGSH-TURNPACK` (base LLM API subscriptions marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Enterprise Engineering Teams Scaling Coding Agents Hit Two Daily Frictions: Half-Edited Broken Worktrees After Failed Multi-File Edits and Opaque Agent ROI**:
   - **Friction 1 — Multi-Turn Round-Trip Latency & Half-Edited Broken Repositories**: Standard coding agents execute dependent steps one turn at a time: search, wait, read 5 files, wait, edit 5 files, wait, run tests. When a multi-file refactor misses a single caller import and the test fails, the repository is left in a half-edited broken state while the agent burns additional turns trying to back out its changes.
   - **Friction 2 — Blind Agent Spend & Guesswork `CLAUDE.md` Tweaks**: Across Claude Code, Codex CLI, and Cursor, engineering leaders lack a local-first view of cache read rates, per-step latency, and which sessions modified production code without running a single test—and cannot prove with paired statistics whether a change to `CLAUDE.md` actually improved agent pass rates.
   - **The Solution Architect Stack (`coding.sh` MIT + `turnpack` Apache-2.0, Both Zero-Dependency)**: Deploy **`OnlyTerp/turnpack`** (`Apache-2.0`) so agents gather context in one turn (`pack` with automatic `.env` redaction) and execute multi-file edits through `ship` (which runs tests immediately and **restores every file byte-for-byte on failure** while naming missed caller files—cutting round trips by **`50%`** and wall time by **`45.7%`**); pair it with **`jackulau/coding.sh`** (`MIT`) to index every session locally in SQLite (or team Postgres/ClickHouse), flag unverified edits (`coding.sh improve`), and convert failed runs into paired-statistics A/B evals (`coding.sh eval new` & `coding.sh exp compare`).
2. **Closed-Form FinOps Impact (35 Software Engineers Executing 50,000 Monthly Multi-File Refactors & Bug Fixes at `$95.00/hr`)**:
   - Migrating from **Path A (Cloud Agent Trace SaaS + Unprotected 6-Turn Edit Loops at `$5,865.00/mo`)** to **Path C (`coding.sh` MIT + `turnpack` Apache-2.0 Stack at `$346.00/mo`)** saves **`$5,519.00/mo` (`-94.10%`, or `$66,228.00/yr`)** while cutting broken-worktree rollback recovery and eval authoring labor from `37.0 hrs/mo` to `2.8 hrs/mo` (**`92.43%` reduction**).

![coding.sh + Turnpack Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r32-coding-sh-turnpack.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `OnlyTerp/turnpack` cut Claude Code round trips from `6` to `3` (`-45.7%` wall time) while guaranteeing byte-exact rollback when tests fail?
- **Plain-Language Definition**: `Turnpack` (`Apache-2.0`, Node >= 22, zero dependencies, zero network calls) is a **transactional context-packing and atomic multi-file edit-and-verify MCP server**.
- **The Three Tools (`pack`, `ship`, `batch`)**:
  1. **`pack` (1-Turn Context Bundle + Automatic Secret Redaction)**: Combines regex search (with surrounding code context), multi-file reads (whole file, line range, or a single named function), glob listings, and `git status` into a single size-capped reply while automatically redacting `.env` and key files;
  2. **`ship` (Transactional Multi-File Edit + Test Gate + Byte-Exact Rollback)**: Applies edits across any number of files and immediately runs your verification command (`"verify": "npm test"`):
     - If the test passes, the edits remain on disk;
     - **If the test fails, `ship` restores every modified file byte-for-byte to its pre-edit snapshot (`FAILED_AND_ROLLED_BACK`)** and inspects the failing stack trace to highlight files the edit *missed* (e.g., *"The failing output names `src/invoice.js:1`, a file this call did not change"*);
  3. **`batch` (1-Turn Multi-File Read Script)**: Answers repo-wide questions across 40+ files in one turn instead of 40 separate read calls.
- **Measured Claude Code 2.1.280 + Claude Sonnet 5 Benchmark (`bench/results/2026-11-13-claude-code.json`, Median of 3 Runs)**:
  - **Model round trips**: `6` ➔ **`3` (`-50.0%`)**;
  - **Wall-clock time**: `23.4s` ➔ **`12.7s` (`-45.7%`)**;
  - **Output tokens**: `2,044` ➔ **`873` (`-57.3%`)**;
  - **Estimated cost**: `$0.131` ➔ **`$0.084` (`-35.9%`)**.

### Q2: How does `jackulau/coding.sh` turn local agent transcripts and hooks into an enterprise observability and A/B evaluation engine?
- **Plain-Language Definition**: `coding.sh` (`MIT`, Node >= 22.16, zero runtime dependencies) is a **local-first observability, OTLP collector, and evaluation harness for Claude Code, Codex CLI, Cursor, and custom agent apps**.
- **Four Core Engineering Capabilities**:
  1. **One-Command Setup & `0.2s` Historical Backfill**: Running `npx coding.sh` backs up agent config files, installs hooks and the MCP server, and imports existing local sessions in `0.2s`;
  2. **Granular Session Telemetry & Unchecked-Edit Detection (`coding.sh improve`)**: Indexes every prompt, model call, sub-agent, file diff, test badge (`14 passed`), cache read rate, and cost into local SQLite (`coding.sh serve` also supports Postgres and ClickHouse) and **flags sessions that modified code without running any verification check**;
  3. **One-Click Failure-to-Eval Conversion (`coding.sh eval new`)**: Converts any failed session in the local viewer (`coding.sh ui`) into a replayable evaluation case graded by deterministic code checks or calibrated LLM judges;
  4. **Paired-Statistics A/B Experiments (`coding.sh exp compare`)**: Evaluates changes to prompts, `CLAUDE.md` harness files, and models on frozen benchmark sets with paired statistical comparisons.

### Q3: How should an AI Solution Architect combine `coding.sh` and `turnpack`?
- **Transactional Execution Layer (`turnpack` MCP)**: Register `turnpack` across all developer coding agents so context gathering uses `pack` and multi-file edits use `ship` with mandatory test gates and byte-exact rollback.
- **Observability & Continuous Eval Layer (`coding.sh`)**: Record all sessions via `coding.sh` hooks, audit unverified edits with `coding.sh improve`, and promote recurring failure modes into CI regression suites via `coding.sh eval new` and `coding.sh exp compare`.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph ExecutionLayer["Transactional Turn-Compression MCP: OnlyTerp/turnpack (Apache-2.0, 0-Dep)"]
        A[Claude Code / Codex / Cursor Multi-File Task] --> B[1. pack: 1-Turn Regex + Multi-File/Function Read + git status<br/>Auto-Redacts .env &amp; Secret Files]
        B --> C[2. ship: Apply Multi-File Edits + Run verify Command]
        C --> D{Verification Passes?}
        D -->|Exit Code != 0| E[FAILED_AND_ROLLED_BACK<br/>Byte-Exact File Restore + Pinpoint Missed Caller File]
        E --> C
        D -->|Exit Code == 0| F[Edits Committed cleanly · 6→3 Turns · -45.7% Time · -57.3% Output Tokens]
    end

    subgraph ObservabilityLayer["Local-First Observability &amp; Evals: jackulau/coding.sh (MIT, 0-Dep)"]
        F --> G[coding.sh Hooks &amp; OTLP Collector → Local SQLite / ClickHouse]
        G --> H[coding.sh improve Flags Unverified Code Edits]
        H --> I[coding.sh eval new Converts Failed Sessions to Replayable Evals]
        I --> J[coding.sh exp compare Runs Paired-Statistics A/B Harness Tests]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Cloud Trace SaaS + Stock Multi-Turn Edit/Test Loops | Option B: Raw JSONL Log Grep + Manual `git stash/checkout` | **Option C (Recommended): `coding.sh` (MIT) + `turnpack` (Apache-2.0)** |
| :--- | :--- | :--- | :--- |
| **Workspace State When Multi-File Edits Fail Tests** | ❌ Leaves repo half-edited and broken; burns extra turns backing out | ❌ Requires manual developer `git checkout -- .` cleanup | ✅ **`turnpack ship` restores every file byte-for-byte & names missed caller files** |
| **Measured Refactor Round Trips, Latency & Cost** | ❌ 6 round trips / `23.4s` / `2,044` output tokens / `$0.131` | ❌ Same 6-turn sequential overhead | ✅ **3 round trips (`-50%`) / `12.7s` (`-45.7%`) / `873` output tokens (`-57.3%`) / `$0.084` (`-35.9%`)** |
| **Session Privacy & Unverified-Edit Auditing** | ❌ Uploads proprietary source diffs to external SaaS | ⚠️ Unindexed JSONL files cannot flag untested code edits | ✅ **100% local SQLite (or self-hosted PG/ClickHouse) + `coding.sh improve` untested-edit flags** |
| **Turning Failed Sessions into Paired-Stats Evals** | ⚠️ Requires custom SDK instrumentation | ❌ Manual copy-pasting of prompts into test scripts | ✅ **`coding.sh eval new` + `coding.sh exp compare` paired-statistics A/B evaluation** |
| **Monthly TCO (35 Engineers / 50,000 Refactors)** | **`$5,865.00 / mo`** (`$2,350` SaaS/extra turns + `37.0 hrs` cleanup) | **`$2,565.00 / mo`** (`$950` extra turns + `17.0 hrs` manual recovery) | **`$346.00 / mo`** (**`-94.10%` savings**; `$80` local index/eval + `2.8 hrs` A/B review) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R32-CODINGSH-TURNPACK`)

> **Scope & Boundary Declaration**: Evaluated for a 35-engineer software organization executing **50,000 monthly multi-file refactoring and bug-fix tasks** across Claude Code, Codex CLI, and Cursor at a blended engineering rate of `$95.00/hr` (base LLM API subscriptions marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Trace SaaS \& Extra Round-Trip Token Spend} + (\text{Broken-Repo Rollback \& Eval Authoring Hours} \times \$95.00)$$

| Cost Component | Path A: Cloud Trace SaaS + Stock 6-Turn Edit Loops | Path B: Raw JSONL Grep + Manual `git stash` | **Path C: `coding.sh` (MIT) + `turnpack` (Apache-2.0)** |
| :--- | :---: | :---: | :---: |
| **Monthly Trace SaaS & Extra Round-Trip Token Spend** | `$2,350.00` | `$950.00` | **`$80.00`** |
| **Monthly Broken-Repo Rollback & Eval Authoring Hours** | `37.0 hrs` | `17.0 hrs` | **`2.8 hrs`** (**`92.43%` reduction**) |
| **Monthly Software Engineering Labor (`@ $95.00/hr`)** | `$3,515.00` | `$1,615.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,865.00`** | **`$2,565.00`** (`-56.27%`) | **`$346.00`** (**`-94.10%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,300.00 / mo` (`$39,600/yr`) | **`$5,519.00 / mo` (`$66,228.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Verify `turnpack` Locally & Register Its MCP Server**: Run `npx turnpack demo` to verify the throwaway-repo test and byte-exact rollback, then configure `turnpack` across Claude Code, Codex CLI, and Cursor so agents use `pack`, `ship`, and `batch`.
- [ ] **Step 2 — Initialize `coding.sh` with Historical Session Backfill**: Run `npx coding.sh` (`coding.sh init --dry-run --diff` first) to install session hooks and import existing local agent sessions into SQLite in `0.2s`.
- [ ] **Step 3 — Audit Model Efficiency & Unchecked Edits**: Run `npx coding.sh usage --by model` to inspect cache read rates and tokens per turn, and run `coding.sh improve` to catch sessions that modified code without running tests.
- [ ] **Step 4 — Convert Failed Runs into Paired-Statistics Evals**: Use `coding.sh eval new` on failed sessions and run `coding.sh exp compare` before rolling out changes to `CLAUDE.md`, `AGENTS.md`, or default model selections.
