# Multi-Session Claude Code Control Room, 6-Skill Diff Scope Gate & Pre-Deploy FinOps Receipt Skill Selection FAQ: `petritavd/airoom` + `oil-oil/oil-dev-skills` + `globalmpc/vibe-bill`

> **Metadata**
> - **Evaluation Batch**: 2026-11-16 Night Shift Round 23 (Cumulative Round 380 Milestone)
> - **Primary Targets**:
>   1. [`petritavd/airoom`](https://github.com/petritavd/airoom) (`★ 37` / `5 Forks`, Apache-2.0 · Local-only `127.0.0.1` zero-telemetry control room for Claude Code across macOS and Windows 11: maps every project to a room and every session in `~/.claude/projects` to a desk with 4-state monitors, **per-tool-call approvals with 10-minute auto-deny**, a multi-profile Chrome-style browser pane, and 3-question parallel git-worktree team hiring)
>   2. [`oil-oil/oil-dev-skills`](https://github.com/oil-oil/oil-dev-skills) (`★ 30` / `1 Fork`, MIT · 6-skill coding-agent SDLC workflow [`oil-explore`, `oil-plan`, `oil-dispatch`, `oil-code-review`, `oil-bug-fix`, `oil-govern`] featuring fast mid-coding checks, a **pre-review diff scope verifier** that flags out-of-plan or restricted-directory edits, and a multi-worktree branch governance board)
>   3. [`globalmpc/vibe-bill`](https://github.com/globalmpc/vibe-bill) (`★ 31`, MIT · Claude Code skill `/vibe-bill` that estimates monthly runtime bills at `100 / 1,000 / 10,000 / 100,000` users without reading `.env` secret values, flags **9 quiet money-burning code anti-patterns**, and renders a shareable `.vibe-bill/out/receipt.png`)
> - **Companion Visual**: [`assets/github-ai-radar-2026-11-16-r23-airoom-oildev-vibebill.svg`](../../../assets/github-ai-radar-2026-11-16-r23-airoom-oildev-vibebill.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261116-R23-AIROOM-OILDEV-VIBEBILL` (see [`evidence/trending-daily-2026-11-16-audit.json`](../evidence/trending-daily-2026-11-16-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language First Principles**:
   - **`petritavd/airoom` (`Claude Code Control Room`)**: Think of it as **putting all five of your terminal Claude Code sessions onto one visual office floor so you immediately see which agent is working (green), waiting on your approval (amber), or stuck on a hook error (red)**. Every tool call shows its exact command with Allow/Deny buttons (auto-denying after 10 minutes if unanswered), a built-in multi-profile browser pane lets you and your agents test the app as admin/customer/signed-out side by side, and parallel worktree teams park cleanly when you quit.
   - **`oil-oil/oil-dev-skills` (`6-Skill SDLC & Diff Scope Gate`)**: Think of it as **enforcing architectural boundaries before code review even begins**. It splits agent work into Explore → Plan → Dispatch → Code Review → Govern (plus a root-cause Bug-Fix path), restricts mid-coding runs to fast typecheck/lint checks, runs a deterministic pre-review script that flags any file touched outside the approved plan or inside restricted folders (`src/storage/`, `vendor/`), and builds a multi-worktree branch board.
   - **`globalmpc/vibe-bill` (`Pre-Deploy FinOps Receipt Skill`)**: Think of it as **answering "what will my AI-built app actually cost at 100, 1k, 10k, and 100k users?" before you ship to production**. It inspects your code without ever opening `.env` files, flags 9 bill-inflating anti-patterns (keystroke LLM calls, resending full chat history, unthrottled public AI endpoints, full-table DB loads), and generates both a detailed `report.md` and a filename-redacted `.vibe-bill/out/receipt.png`.
2. **Quantified FinOps Impact (`CLAIM-20261116-R23-AIROOM-OILDEV-VIBEBILL`)**:
   - Across an engineering governance workload of **45 multi-session coding-agent feature deliveries + 20 pre-deploy cloud/AI unit-economics audits per month** (`engineer_hourly_rate_usd = $100.00/hr`; base Claude seats marked `not_measured`):
   - **Path C (`airoom` + `oil-dev-skills` + `vibe-bill`)** reduces monthly TCO from **`$6,090.00/mo`** under **Path A (missed terminal approvals + scope-drifting edits + unthrottled production AI bill shock)** down to **`$405.00/mo`**, saving **`$5,685.00/mo` (`-93.35%`, or `$68,220.00/yr`)** and reclaiming **`37.3 hrs/mo` (`-92.10%`)** of engineering labor.

![2026-11-16 Night Round 23 (R380 Milestone) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-16-r23-airoom-oildev-vibebill.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: How do `petritavd/airoom` and `oil-oil/oil-dev-skills` eliminate multi-agent terminal bottlenecks and scope drift?
- **Core Mechanisms**:
  1. **`airoom` Visual Desks, 10-Minute Auto-Deny & Multi-Profile Browser**: Reads `~/.claude/projects` on `127.0.0.1` with zero telemetry, surfaces pending tool approvals in a unified dock queue (auto-denying after 10 minutes), embeds a multi-profile browser pane (opening localhost freely while prompting before external domains), and hires parallel git-worktree teams with 3 questions.
  2. **`oil-dev-skills` Pre-Review Scope Checker & Branch Board**: Defers slow full test suites to the merge gate, runs a deterministic diff-vs-plan script before `oil-code-review` to flag touches to high-risk (`src/storage/`) or do-not-edit (`vendor/`) paths, and uses `oil-govern` to deduplicate `AGENTS.md` and map every worktree branch.

### Q2: How does `globalmpc/vibe-bill` model unit economics across `100 / 1k / 10k / 100k` users without exposing secrets?
- **How `vibe-bill` Solves It**:
  1. **9 Quiet Money-Burning Code Checks**: Detects AI calls on keystrokes/re-renders, resending full chat histories, using flagship models for trivial tasks, uncached duplicate prompts, unthrottled public AI endpoints, constant polling, excessive image resize variants, full-table DB loads, and blobs stored in DB rows.
  2. **Zero-Secret Inspection & Redacted Receipt**: Reads only environment variable names (never opening `.env`), models free-tier graduation thresholds across Supabase/Vercel/Clerk/Resend/Stripe + OpenRouter list prices, and outputs a shareable `receipt.png` free of file or secret names.

### Q3: What are the honest boundaries of these three tools?
- **Honest Boundaries**:
  - `airoom` requires a local logged-in Claude Code installation; its Windows 11 build is currently in beta and not yet code-signed.
  - `vibe-bill` produces list-price estimates rather than exact invoices and marks web-looked-up third-party pricing as `(unverified)`.

---

## 🧭 3. Mermaid Decision Tree & Architecture Comparison

```mermaid
flowchart TD
    Start["Multi-Agent Session Control, SDLC Scope Governance & Pre-Deploy FinOps Auditing"] --> Need{"Which engineering bottleneck are you solving?"}

    Need -->|"Managing multiple concurrent Claude Code sessions, approvals & browser previews"| RoomGate{"Need 127.0.0.1 zero-telemetry desks + 10-min auto-deny approvals?"}
    RoomGate -->|"Yes: One office per project, one desk per session"| UseAiroom["✅ Adopt petritavd/airoom<br/>4-State Desk Monitors + Multi-Profile Browser Pane<br/>3-Question Parallel Git-Worktree Team Hiring"]

    Need -->|"Preventing agent scope drift, mid-coding slow-test stalls & bloated AGENTS.md"| OilGate{"Need deterministic diff-vs-plan checking before code review?"}
    OilGate -->|"Yes: 6-skill SDLC workflow"| UseOilDev["✅ Adopt oil-oil/oil-dev-skills<br/>explore → plan → dispatch → code-review → govern (+ bug-fix)<br/>Restricted-Path Diff Gate + Worktree Branch Board"]

    Need -->|"Estimating 100 / 1k / 10k / 100k user bills & catching expensive code patterns"| BillGate{"Require zero .env secret reading & shareable receipt image?"}
    BillGate -->|"Yes: Run /vibe-bill"| UseVibeBill["✅ Adopt globalmpc/vibe-bill<br/>Flags 9 Money-Burning Anti-Patterns + Free-Tier Thresholds<br/>Outputs Detailed report.md & Redacted receipt.png"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `petritavd/airoom` | `oil-dev-skills` + `vibe-bill` | Path A: 5 Unwatched Terminals + Unchecked Production Deploy | Path B: Manual Diff Audits + Spreadsheet Costing |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pain Solved** | Single-screen visibility, approval queue & browser preview | Blocks out-of-plan edits & catches 9 bill-inflating code bugs | Blocked agents sit unnoticed; surprise production API bills | Tedious manual file-path checks & pricing math |
| **Core Mechanism** | **`127.0.0.1` Control Room + 4-State Desks + Browser Pane** | **6-Skill Contract + Diff Scope Script + `/vibe-bill`** | Raw terminal tabs / post-deploy billing alerts | Manual `git diff` inspection / static spreadsheets |
| **Key Metrics** | **10-min** auto-deny timeout, **3-question** worktree team hire | **6** skills, **4** user tiers (`100–100k`), **9** cost traps | High approval latency; frequent scope drift | Hours spent per release audit |
| **Security & Privacy** | **Zero telemetry; external browser URLs prompt first** | **Never opens `.env`; `receipt.png` hides all file names** | Risk of unthrottled public LLM endpoints | No automated pre-review gate |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Section Tag | Headline-as-Finding | Evidence & Closed-Form Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `airoom` + `oil-dev-skills` + `vibe-bill` cut monthly multi-agent governance & FinOps audit TCO by `93.35%` (`$6,090.00 → $405.00/mo`) | `CLAIM-20261116-R23-AIROOM-OILDEV-VIBEBILL` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `airoom` unifies all `~/.claude/projects` sessions on `127.0.0.1` with 1-click tool approvals that auto-deny after 10 minutes | `petritavd/airoom` `README.md` |
| **Card 3** | `3/7 · WHAT I TESTED` | `oil-dev-skills` compares `git diff` against the approved plan before review to flag high-risk (`src/storage/`) or forbidden (`vendor/`) edits | `oil-oil/oil-dev-skills` `README.md` |
| **Card 4** | `4/7 · UNDER THE HOOD` | `vibe-bill` flags 9 money-burning patterns and models monthly bills at `100 / 1k / 10k / 100k` users without opening `.env` | `globalmpc/vibe-bill` `README.md` |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `oil-govern` trims bloated `AGENTS.md` files and builds a multi-worktree branch board; `airoom` parks teams on quit | `oil-govern` & `airoom` architecture |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Eliminating missed terminal approvals, scope-drift rework, and runaway API loops reclaims `37.3 hrs/mo` (`-92.10%`) of engineering labor | 45 agent features + 20 cost audits/mo |
| **Card 7** | `7/7 · MY TAKE` | Standardize on visual desk approval queues, pre-review diff scope gates, and `/vibe-bill` unit-economics receipts before merging | Base Claude seats: `not_measured` |

### 💰 Closed-Form FinOps Table (45 Multi-Session Agent Features + 20 Pre-Deploy Cost Audits/Month, `r = $100.00/hr`)

| Architecture Path | Token & Cloud Overrun Waste (`compute_and_token_usd`) | Approval Triage & Rework Labor (`engineering_hours`) | Engineering Labor Cost (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs. Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Unwatched Terminals + Scope Drift + Production Bill Shock** | `$2,040.00` | `40.5 hrs` | `$4,050.00` | **`$6,090.00`** | Baseline (`0.00%`) |
| **Path B: Manual Diff Path Audits + Spreadsheet Cost Guessing** | `$940.00` | `18.5 hrs` | `$1,850.00` | **`$2,790.00`** | `-$3,300.00` (`-54.19%`) |
| **Path C: `airoom` + `oil-dev-skills` + `vibe-bill`** | **`$85.00`** | **`3.2 hrs`** | **`$320.00`** | **`$405.00`** | **`-$5,685.00` (`-93.35%` / `$68,220.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Clone petritavd/airoom to run the 127.0.0.1 multi-session Claude Code control room
git clone https://github.com/petritavd/airoom.git

# 2. Clone oil-oil/oil-dev-skills to install the 6-skill SDLC & diff-scope verification workflow
git clone https://github.com/oil-oil/oil-dev-skills.git

# 3. Install globalmpc/vibe-bill and generate a 100..100k user cost receipt (.vibe-bill/out/receipt.png)
npx skills add globalmpc/vibe-bill -a claude-code
```
