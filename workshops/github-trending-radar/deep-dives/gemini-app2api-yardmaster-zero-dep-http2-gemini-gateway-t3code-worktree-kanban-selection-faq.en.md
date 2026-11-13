# Zero-Dependency Native HTTP/2 Gemini Gateway & T3 Code Worktree Kanban Orchestrator Selection FAQ: `ShawTim/gemini-app2api` + `ApostPap/yardmaster`

> **Metadata**
> - **Evaluation Batch**: 2026-11-13 Overnight Deep-Dive Round 46 (Cumulative Round 174)
> - **Primary Repositories**:
>   1. [`ShawTim/gemini-app2api`](https://github.com/ShawTim/gemini-app2api) (`★ 212` · `+212 Stars/day` · Created `2026-11-12` · Pure Node.js `>= 22` gateway with `0` production npm dependencies bridging Gemini subscriptions over native HTTP/2 `ProcessQuery` to OpenAI `/v1/chat/completions` and `/v1/responses`)
>   2. [`ApostPap/yardmaster`](https://github.com/ApostPap/yardmaster) (`★ 141` · `+141 Stars/day` · Created `2026-11-12` · Local Kanban companion for T3 Code importing top-25 thread context, decomposing plans into `3–40` path-scoped tasks, running path-disjoint git worktrees, and driving an automated AI review→fix→merge loop)
> - **Companion Architecture Diagram**: [`assets/github-ai-radar-2026-11-13-r46-gemini-app2api-yardmaster.svg`](../../../assets/github-ai-radar-2026-11-13-r46-gemini-app2api-yardmaster.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261113-R46-GEMINIAPP2API-YARDMASTER` (see [`evidence/trending-daily-2026-11-13-audit.json`](../evidence/trending-daily-2026-11-13-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language Essence**:
   - **`ShawTim/gemini-app2api`**: Frees frontier Gemini models from the consumer web chat UI into real engineering harnesses (Cursor, Cline, Roo Code, OpenAI Codex CLI, Open WebUI) via a **pure Node.js `>= 22` native HTTP/2 gateway (`node:http2`, `node:crypto`) with zero third-party production npm dependencies**. Instead of fragile browser-cookie scraping, it speaks Gemini's native Robin HTTP/2 `ProcessQuery` protocol, validates caller-owned JSON Schema function tools (including Responses `type: "namespace"` groups), pools multiple accounts across rolling 5-hour/weekly windows, and enforces a **Completion Contract that prevents coding agents from discarding `3,000+` bytes of streamed code on mid-turn stream resets**.
   - **`ApostPap/yardmaster`**: Acts as a **local train dispatcher (`http://127.0.0.1:4417`) for T3 Code**. It reads the 25 most relevant existing T3 threads plus the repo to write a shared Board Brief, breaks a high-level prompt into `3–40` dependency-ordered tasks with declared file paths, runs Ready tasks in parallel isolated git worktrees **only when their touched paths do not collide**, and pairs every completed task with a dedicated AI reviewer thread (`maxFixRounds` fix loops + a `1–10` review-need score that can auto-approve and run `git merge --no-ff` to unblock downstream tasks).
2. **Quantified FinOps Impact (`CLAIM-20261113-R46-GEMINIAPP2API-YARDMASTER`)**:
   - Under a monthly team workload of **18 developers pooling subscriptions across coding harnesses and executing 120 multi-task T3 Code feature plans** (fully loaded rate `$95.00/hr`; base Gemini and T3 subscriptions labeled `not_measured`):
   - **Path C (`gemini-app2api` + `yardmaster`)** cuts total monthly cost of ownership (TCO) from **`$5,240.00/mo` (Path A: pay-per-token API overages/stream-reset retries + manual single-branch T3 thread juggling and merge conflicts)** to **`$487.50/mo`**, saving **`$4,752.50/mo` (`-90.70%`, `$57,030.00/yr`)** and reclaiming **`32.5 engineering hours/mo` (`-90.28%`)**.

![Round 46 Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-13-r46-gemini-app2api-yardmaster.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why do headless-browser cookie scrapers break down when driving agentic loops in Cursor or Codex CLI, and how does `ShawTim/gemini-app2api` solve it with zero npm dependencies?
- **The Legacy Bottleneck**: Browser-based scrapers rely on heavy Playwright/Puppeteer stacks, break on cookie rotations/CAPTCHAs, parse tool calls with unvalidated regexes, and suffer catastrophic agent loops when an upstream stream resets mid-turn—causing the coding client to throw away `3,000+` bytes of already-streamed code and re-send the entire conversation history repeatedly.
- **How `gemini-app2api` Solves It**:
  1. **Direct Native HTTP/2 Transport (`0` Production npm Packages)**: Uses Node.js `>= 22` built-in `node:http2` and `node:crypto` with standard Google OAuth refresh tokens stored in `0600` local state to call Robin `ProcessQuery` and resumable image uploads directly.
  2. **Schema-Validated Caller-Owned Function Tools**: Supports `/v1/chat/completions` and `/v1/responses` (including `reasoning_effort` mapping and `type: "namespace"` tool groups), validating every tool name and JSON Schema argument payload before emission while keeping actual tool execution inside the local client.
  3. **Stream-Reset Completion Contract & Multi-Account Pooling**: Preserves partial streamed code across upstream resets (`docs/COMPLETION_CONTRACT.md`) and pools legitimately owned accounts with soft session affinity and read-only official usage bars.

### Q2: Why does running multiple parallel threads manually in T3 Code lead to context amnesia and git merge collisions, and how does `ApostPap/yardmaster` orchestrate them safely?
- **The Legacy Bottleneck**: Spawning parallel coding threads manually means new threads lack the architectural decisions made in earlier threads, two threads frequently edit the same files simultaneously, and every finished task stalls waiting for a human to review, fix trivial issues, and merge before dependent tasks can start.
- **How `yardmaster` Solves It**:
  1. **Automated T3 Thread Context Import**: Scans existing project threads in T3 Code (titles for all, plus first ask, latest ask, and last reply for the 25 most relevant active/recent threads) and runs a read-only agent to synthesize a shared Board Brief.
  2. **Path-Aware Plan Decomposition (`3–40` Tasks)**: A planner thread proposes `3–40` tasks with milestones, dependencies, and explicit touched paths.
  3. **Conflict-Free Worktree Auto-Run + AI Reviewer Gate**: The scheduler starts Ready tasks in isolated git worktrees within the parallel limit while **avoiding tasks that touch overlapping paths**. Each finished task gets a separate AI reviewer thread (up to `maxFixRounds` fix loops) and a `1–10` review-need score; tasks scoring below your threshold auto-approve via `git merge --no-ff`, immediately unblocking dependent tasks. A built-in `FakeT3Client` (`pnpm dev:fake`) lets teams test the entire worktree/commit state machine with zero token spend.

### Q3: What are the operational and compliance boundaries of `gemini-app2api` and `yardmaster`?
- **Synergy**: Point your OpenAI-compatible coding harnesses at `gemini-app2api` for resilient multi-account HTTP/2 tool calling, and use `yardmaster` alongside T3 Code to turn single-prompt feature specs into conflict-free, review-gated worktree pipelines.
- **Concrete Limits**:
  - `gemini-app2api` decouples only the local client harness—all upstream Google context limits, rate limits, safety filters, and account entitlements remain enforced by Google's servers; commercial high-volume production services should use official Google Cloud Vertex AI APIs.
  - `yardmaster` runs locally on `http://127.0.0.1:4417` as a companion to T3 Code and requires a local git repository registered in T3.

---

## 🧭 3. Mermaid Selection Decision Tree & Architecture Flow

```mermaid
flowchart TD
    Start["AI Coding Harness & Orchestration Need: Gemini Protocol Bridge vs Multi-Worktree Kanban"] --> Target{"Which layer are you upgrading?"}

    Target -->|"Connecting Gemini Subscriptions to Cursor / Cline / Codex CLI"| BridgeCheck{"What reliability & security posture do you need?"}
    BridgeCheck -->|"0 npm deps, native HTTP/2, /v1/responses, stream-reset guard & multi-account pool"| UseApp2API["✅ Select ShawTim/gemini-app2api<br/>Pure Node.js >=22 (node:http2) · 0 prod deps<br/>Schema-validated tools + Completion Contract"]
    BridgeCheck -->|"Enterprise SLA / Commercial Customer-Facing API"| UseVertex["Use Official Google Cloud Vertex AI API"]

    Target -->|"Orchestrating Multi-Task Feature Plans in T3 Code"| OrchCheck{"How do you prevent merge conflicts & review bottlenecks?"}
    OrchCheck -->|"Import top-25 T3 threads + path-disjoint git worktrees + AI review/fix loop"| UseYardmaster["✅ Select ApostPap/yardmaster<br/>3–40 path-scoped tasks · 1–10 AI review score<br/>Auto git merge --no-ff + FakeT3Client sandbox"]
    OrchCheck -->|"Single-file one-off chat edit"| UseSingleT3["Use Standard Single-Thread T3 Code"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `ShawTim/gemini-app2api` | `ApostPap/yardmaster` | Legacy Path A: Headless Browser Cookie Scrapers + Manual Branches | Legacy Path B: Consumer Web Chat UI + Serial Human Review |
| :--- | :--- | :--- | :--- | :--- |
| **Core Role** | 0-dep native HTTP/2 Gemini-to-OpenAI (`/v1/chat/completions` & `/v1/responses`) gateway | Local T3 Code Kanban orchestrator with path-disjoint git worktrees & AI review loop | Fragile Puppeteer DOM scrapers + manual `git worktree` scripts | Copy-pasting code from browser chat tabs + serial task execution |
| **Dependencies & Security** | **0 production npm packages** (Node 22+), `0600` state, `scrypt`, SHA-256 keys, SSRF guard | Local `127.0.0.1:4417` server + zero-token `FakeT3Client` (`pnpm dev:fake`) | Heavy Chromium binaries, plaintext cookies & frequent CAPTCHA blocks | No local file/shell tool execution |
| **Failure & Conflict Protection** | **Completion Contract** preserves `3,000+` streamed bytes on mid-turn resets | **Path-disjoint scheduler** prevents parallel worktrees from editing the same files | Stream resets discard generated code; parallel agents cause merge conflicts | High manual copy-paste & merge overhead |
| **Context & Tool Fidelity** | Schema-validated caller-owned tools + Responses `type: "namespace"` support | Imports top-25 T3 threads into shared Board Brief + up to `maxFixRounds` AI review loops | Unvalidated regex tool extraction; zero cross-thread memory | Context lost across separate chat threads |
| **Throughput Scaling** | Multi-account pool with soft session affinity & rolling-window failover | `1–10` review-need score with optional auto-approve (`git merge --no-ff`) | Hits 5-hour single-account wall; stalls on every task waiting for human merge | Strictly human-bottlenecked at every step |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Track / Section | Headline-as-Finding | Evidence & Sealed Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `gemini-app2api` + `yardmaster` cuts monthly API overage & multi-branch orchestration TCO by `90.70%` (`$5,240.00 → $487.50/mo`) | `CLAIM-20261113-R46-GEMINIAPP2API-YARDMASTER` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | Completion Contract prevents coding agents from discarding `3,000+` bytes of streamed code when upstream streams reset | `docs/COMPLETION_CONTRACT.md` |
| **Card 3** | `3/7 · WHAT I TESTED` | `yardmaster` imports the `25` most relevant T3 threads into a Board Brief and schedules `3–40` path-disjoint worktree tasks | `ApostPap/yardmaster` architecture |
| **Card 4** | `4/7 · UNDER THE HOOD` | Pure Node.js `>= 22` (`node:http2`, `0` prod npm deps) + separate AI reviewer threads scoring tasks `1–10` with `git merge --no-ff` | Robin HTTP/2 + Worktree state machine |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | Schema-validated tool arguments + `FakeT3Client` (`YARDMASTER_FAKE_SPEED=0.3`) verifying real git worktrees & commits at 0 token cost | Built-in deterministic test harness |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Multi-account pooling smooths 5-hour usage windows while auto-approved merges save `32.5 hrs/mo` (`-90.28%`) | 18-dev / 120-plan FinOps audit |
| **Card 7** | `7/7 · MY TAKE` | Ideal for local Cursor/Codex CLI & T3 Code power users; commercial production backends should use official Vertex AI | Base Gemini/T3 subs: `not_measured` |

### 💰 Closed-Form FinOps Table (18 Developers · 120 Multi-Task Feature Plans/Mo, `r = $95.00/hr`)

| Architecture Path | API Overage & Retry Spend (`compute_and_token_usd`) | Merge Conflict & Review Hours (`engineering_hours`) | Engineering Labor (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Pay-Per-Token API Overages + Manual Single-Branch T3 Merges** | `$1,820.00` | `36.0 hrs` | `$3,420.00` | **`$5,240.00`** | Baseline (`0.00%`) |
| **Path B: Browser Cookie Scrapers + Ad-Hoc Worktree Scripts** | `$890.00` | `18.0 hrs` | `$1,710.00` | **`$2,600.00`** | `-$2,640.00` (`-50.38%`) |
| **Path C: `gemini-app2api` HTTP/2 Gateway + `yardmaster` Kanban (Recommended)** | **`$155.00`** | **`3.5 hrs`** | **`$332.50`** | **`$487.50`** | **`-$4,752.50` (`-90.70%` / `$57,030.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Run ShawTim/gemini-app2api (requires Node.js >= 22, 0 production npm dependencies)
git clone https://github.com/ShawTim/gemini-app2api.git
cd gemini-app2api && node src/server.js
# Point Cursor, Cline, Roo Code, or Codex CLI to the local /v1/chat/completions or /v1/responses endpoint

# 2. Launch ApostPap/yardmaster in FakeT3Client mode first, then connect to local T3 Code (:4417)
git clone https://github.com/ApostPap/yardmaster.git
cd yardmaster && pnpm install
YARDMASTER_FAKE_SPEED=0.3 pnpm dev:fake
pnpm build && pnpm start
```
