# Tree-Sitter AST Context Firewall (`tokensafe-dev/tokensafe`), 40→20 Hysteresis Cache-Aligned Rolling Summary (`Lentlily22/rolling-summary-tutorial`) & Correction Memory Graph (`assassin808/learn-from-lessons`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 44 (Cumulative Round 468)  
> **Tracked Repositories**:
> - **`tokensafe-dev/tokensafe`** (`★ 46`, v4.0, Python & npm `tokensafe`, `MIT`): Local context firewall and zero-loss runtime for Cursor, Claude Code, Codex, Windsurf, Google Antigravity, Kimi Code, and ChatGPT featuring **`<1ms` SQLite FTS5 BM25 code search (`scoped_search`), cross-boundary frontend/backend route linking (`graph.db`), 9-language Tree-sitter AST slicing with reversible 8-char hash anchors (`expand_ref` `#a1b2c3d4`), superseded output pruning (`-30%–40%`), `>1024px` vision downscaling (`-50%–75%`), and `tokensafe doctor` ghost-token auditing (`2,000–5,000` tokens/turn saved)**
> - **`Lentlily22/rolling-summary-tutorial`** (`★ 46`, JavaScript / SQLite `40→20` Hysteresis Trimming + 2-Message Overlap Seam + `BP1–BP4` Cache Alignment, `MIT` reference implementation) & **`assassin808/learn-from-lessons`** (`★ 46`, Python 3.9+ Zero-Dependency Local Correction Miner & 3-Tier Lesson Graph, `MIT`): Hysteresis rolling-summary architecture that keeps prompt caches warm for 20 consecutive turns (`rolling-summary-tutorial`), paired with a local transcript miner that turns developer corrections into a verified **`Principle → Rule → Case`** memory graph (`learn-from-lessons`)  
> **Audit Claim ID**: `CLAIM-20261117-R44-TOKENSAFE-ROLLINGSUM-LESSONS` (base LLM subscriptions marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Enterprise Engineering Teams and Custom AI Chat Builders Hit Three Context & Memory Failures: Context Trash Blowout, Sliding-Window Cache Thrashing, and Amnesiac Agent Corrections**:
   - **Failure 1 — Context Trash & Multi-IDE Ghost Tokens**: Coding sessions rapidly fill up with lockfiles, ANSI-colored build logs, superseded file reads, oversized screenshots, and duplicate IDE rule files (`.cursorrules`, `CLAUDE.md`, `.windsurfrules`) that silently burn `2,000–5,000` ghost tokens on every turn.
   - **Failure 2 — Sliding-Window Truncation Destroys Prompt Caching on Every Turn**: When a custom chat frontend enforces a naive 30-message sliding window, every turn after message 30 drops message #1—shifting the prefix anchor and invalidating 100% of the prompt cache on every single message.
   - **Failure 3 — Repeating the Same Corrections Every Session**: Engineers repeatedly tell Claude Code or Codex *"don't push yet"* or *"I asked why, not to edit the file"*, only for the next session to make the exact same mistake.
   - **The Solution Architect Stack (`tokensafe` v4.0 MIT + `rolling-summary-tutorial` MIT + `learn-from-lessons` MIT)**: Deploy **`tokensafe-dev/tokensafe` v4.0** across developer workstations to enforce Tree-sitter AST slicing, `<1ms` SQLite FTS5 search, superseded-read pruning, and `tokensafe doctor` ghost-token cleanup; architect custom chat frontends around **`Lentlily22/rolling-summary-tutorial`** (`40→20` hysteresis trimming + 2-message overlap seam + `BP1–BP4` cache breakpoint alignment); and mine local transcripts with **`assassin808/learn-from-lessons`** (`MIT`, extracting quote-backed `Principle → Rule → Case` lessons and injecting scenario-filtered rules via `CLAUDE.md` or `lessons mcp`).
2. **Closed-Form FinOps Impact (30 Full-Stack & AI Platform Engineers Running 65,000 Monthly Multi-IDE Coding Turns & Chat Frontend Sessions at `$95.00/hr`)**:
   - Migrating from **Path A (Unfiltered Context Trash + Sliding-Window Every-Turn Cache Misses & Repeated Corrections at `$5,895.00/mo`)** to **Path C (`tokensafe` v4.0 + `40→20` Hysteresis Summary + `learn-from-lessons` Stack at `$346.00/mo`)** saves **`$5,549.00/mo` (`-94.13%`, or `$66,588.00/yr`)** while cutting repeated-correction and context-reset labor from `37.0 hrs/mo` to `2.8 hrs/mo` (**`92.43%` reduction**).

![TokenSafe + Rolling Summary + Learn-from-Lessons Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r44-tokensafe-rolling-lessons.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `tokensafe-dev/tokensafe` v4.0 combine Tree-sitter AST slicing, `<1ms` SQLite FTS5 search, and reversible hash stashing to eliminate context bloat?
- **Plain-Language Definition**: `tokensafe` v4.0 (`MIT`, one-command install via `npx tokensafe` or `pip install tokensafe`) is **a local context firewall that slices code to exact AST symbols, strips superseded reads and ANSI noise, and indexes the repo in SQLite FTS5 so coding agents stay focused and never hit mid-day quota lockouts**.
- **Key v4.0 Engines (`anonymized_reported, independently_reproduced=false`)**:
  1. **`<1ms` SQLite FTS5 BM25 Search (`scoped_search`) & Cross-Boundary Route Graph (`graph.db`)**: Replaces raw terminal `grep` with trigram BM25 search and links frontend `fetch`/`axios` calls to backend `FastAPI`, `Express`, `Flask`, and `Next.js` routes;
  2. **9-Language Tree-Sitter AST Slicing & Reversible 8-Char Hash Stash (`expand_ref` `#a1b2c3d4`)**: Preserves 100% byte-exact target symbols while folding unrelated code behind reversible `#a1b2c3d4` anchors;
  3. **Superseded Output Pruning (`-30%–40%`), Vision Downscaler (`-50%–75%`) & Ghost Tokens Auditor (`tokensafe doctor`)**: Prunes stale file reads superseded by later edits, scales screenshots `>1024px`, strips ANSI escape sequences, tracks failed hypotheses in `get_mistakes`, and removes `2,000–5,000` wasted ghost tokens per turn across redundant IDE rule files.

### Q2: Why does `Lentlily22/rolling-summary-tutorial`'s `40→20` hysteresis trimming + 2-message seam allowance preserve prompt cache hits across 20 consecutive turns?
- **Four Context-Engineering Innovations (with runnable `reference/` MIT code)**:
  1. **Hysteresis Trimming (`40 → 20` Messages)**: Instead of sliding the window on every turn after message 30 (which invalidates the prefix cache every turn), the window grows from `20` to `40` messages and then trims the oldest `20` all at once—keeping the first-message cache anchor identical for 20 straight turns;
  2. **2-Message Seam Allowance (缝份机制)**: Sends the last `2` messages of the previous batch alongside the `20` newly trimmed messages (`2 + 20`) to the summarizer so topics straddling the cut boundary are never severed;
  3. **4-Breakpoint Cache Alignment (`BP1 Profile → BP2 Tools → BP3 Summary → BP4 History`)**: Aligns summary updates with history trimming on the exact same 20-message boundary so cache rebuilds only once per cycle;
  4. **Isolated Versioned Summary Table + Absolute Dates + A/B Reroll**: Stores summaries in a dedicated table (preventing recursive re-summarization), normalizes relative dates (*"yesterday"*) into absolute dates (*"June 10 evening"*), and retains prior summaries for A/B rerolling.

### Q3: How does `assassin808/learn-from-lessons` turn human corrections into a scenario-filtered 3-tier memory graph?
- **Local Zero-Dependency Pipeline (`lessons scan → dream → view → inject / mcp`, `MIT`)**:
  - Scans local transcripts from Claude Code, Codex, and opencode to find moments where the user corrected the agent;
  - Structures lessons into **Principle → Rule → Case** with exact conversation quotes (marking a lesson verified once seen twice) and filters them by scenario (`lessons index --scenario writing-paper`) before injecting into `CLAUDE.md` / `AGENTS.md` or serving over `lessons mcp`.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph ContextFirewall["Local AST Context Firewall: tokensafe-dev/tokensafe v4.0 (★46, MIT)"]
        A[Cursor / Claude Code / Codex Turn] --> B[tokensafe Hooks &amp; MCP<br/>&lt;1ms SQLite FTS5 Search + Route Graph graph.db]
        B --> C[9-Lang Tree-Sitter Slicing + #a1b2c3d4 Stash<br/>Prunes Superseded Reads -30~40% · Downscales Images -50~75% · Doctor Audit]
    end

    subgraph RollingAndLessons["Hysteresis Cache &amp; Correction Memory: rolling-summary (★46) + learn-from-lessons (★46)"]
        C --> D[rolling-summary-tutorial: 40→20 Hysteresis Trimming<br/>2-Message Seam + BP1–BP4 Cache Alignment + Versioned A/B Summary Store]
        D --> E[assassin808/learn-from-lessons<br/>Mines Local Corrections → Principle/Rule/Case Graph → Scenario Injection / MCP]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Unfiltered Context + 30-Msg Sliding Window + Verbal Reminders | Option B: Static `.cursorignore` + Hard `/clear` Resets | **Option C (Recommended): `tokensafe` v4.0 + `rolling-summary` + `learn-from-lessons` (MIT)** |
| :--- | :--- | :--- | :--- |
| **Code Context Signal-to-Noise & Ghost Token Audit** | ❌ Lockfiles, ANSI codes & duplicate rule files waste thousands of tokens | ⚠️ Static ignore files cannot prune superseded mid-session tool reads | ✅ **Tree-sitter AST slicing (`#a1b2c3d4`), superseded pruning (`-30~40%`) & `doctor` audit** |
| **Prompt-Cache Hit Rate in Multi-Turn Chat Frontends** | ❌ Sliding 1 message per turn invalidates 100% of prompt cache every turn | ❌ Hard `/clear` wipes narrative continuity ("goldfish memory") | ✅ **`40→20` hysteresis trimming + 2-msg seam + `BP1–BP4` alignment keeps cache warm 20 turns** |
| **Cross-Session Retention of Developer Corrections** | ❌ Agent repeats the same mistake in the next session | ⚠️ Monolithic `CLAUDE.md` bloats with uncategorized rules | ✅ **Mines local transcripts into verified `Principle→Rule→Case` graph with scenario filtering** |
| **Monthly TCO (30 Engineers / 65,000 Turns)** | **`$5,895.00 / mo`** (`$2,380` noise/cache-miss burn + `37.0 hrs` rework) | **`$2,565.00 / mo`** (`$950` waste + `17.0 hrs` manual maintenance) | **`$346.00 / mo`** (**`-94.13%` savings**; `$80` FTS5/summary ops + `2.8 hrs` lesson curation) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R44-TOKENSAFE-ROLLINGSUM-LESSONS`)

> **Scope & Boundary Declaration**: Evaluated for a 30-engineer full-stack and AI platform organization executing **65,000 monthly multi-IDE coding turns and custom chat frontend sessions** at a blended engineering rate of `$95.00/hr` (base LLM subscriptions marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Noise/Ghost \& Sliding-Window Cache-Miss Spend} + (\text{Repeated Correction \& Lockout Recovery Hours} \times \$95.00)$$

| Cost Component | Path A: Context Trash + Sliding Window | Path B: Static Ignore + Hard Resets | **Path C: `tokensafe` + Hysteresis + `lessons`** |
| :--- | :---: | :---: | :---: |
| **Monthly Noise, Ghost-Token & Sliding-Window Cache-Miss Spend** | `$2,380.00` | `$950.00` | **`$80.00`** |
| **Monthly Repeated Corrections, Context Reset & Lockout Hours** | `37.0 hrs` | `17.0 hrs` | **`2.8 hrs`** (**`92.43%` reduction**) |
| **Monthly Full-Stack & Platform Engineering Labor (`@ $95.00/hr`)** | `$3,515.00` | `$1,615.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,895.00`** | **`$2,565.00`** (`-56.49%`) | **`$346.00`** (**`-94.13%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,330.00 / mo` (`$39,960/yr`) | **`$5,549.00 / mo` (`$66,588.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Run `npx tokensafe` & `tokensafe doctor` Across All Developer Workstations**: Audit and clean duplicate IDE rule files (`2,000–5,000` ghost tokens/turn saved) and enable `<1ms` SQLite FTS5 search (`scoped_search`), `prune_superseded`, and `optimize_image`.
- [ ] **Step 2 — Implement `40→20` Hysteresis Trimming & `BP1–BP4` Cache Alignment**: Adopt `Lentlily22/rolling-summary-tutorial`'s `reference/` MIT implementation with the 2-message overlap seam, separate versioned summary table, and absolute date normalization.
- [ ] **Step 3 — Schedule Weekly `lessons scan && lessons dream` Runs**: Use `assassin808/learn-from-lessons` to extract developer corrections from Claude Code, Codex, and opencode transcripts into the 3-tier `Principle → Rule → Case` graph.
- [ ] **Step 4 — Inject Scenario-Filtered Lessons via `lessons index --scenario` or `lessons mcp`**: Load only scenario-relevant verified rules into `CLAUDE.md` / `AGENTS.md` so agents stop repeating past mistakes without bloating context.
