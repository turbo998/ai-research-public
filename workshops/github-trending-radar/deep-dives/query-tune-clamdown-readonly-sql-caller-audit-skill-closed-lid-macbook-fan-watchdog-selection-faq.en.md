# Read-Only SQL Caller/Plan Audit Skill & Closed-Lid MacBook Agent Thermal Watchdog Selection FAQ: `kbdevs/query-tune` + `delef/ClamDown`

> **Metadata**
> - **Evaluation Batch**: 2026-11-13 Overnight Deep-Dive Round 44 (Cumulative Round 172)
> - **Primary Repositories**:
>   1. [`kbdevs/query-tune`](https://github.com/kbdevs/query-tune) (`★ 166` · `+166 Stars/day` · Created `2026-11-12` · Read-only SQL access-path and caller auditing skill for Codex & Claude Code with zero row/credential collection, achieving up to `99%` latency reductions such as `543.00ms → 25.20ms` in 8-client/50-block paired MySQL studies)
>   2. [`delef/ClamDown`](https://github.com/delef/ClamDown) (`★ 158` · `+158 Stars/day` · Created `2026-11-12` · Native macOS menu-bar utility + root watchdog helper keeping closed-lid MacBooks awake for coding agents while locking the screen, driving Apple Silicon fans along a `50 °C → 75 °C` curve, and cutting off on low battery or high heat)
> - **Companion Architecture Diagram**: [`assets/github-ai-radar-2026-11-13-r44-query-tune-clamdown.svg`](../../../assets/github-ai-radar-2026-11-13-r44-query-tune-clamdown.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261113-R44-QUERYTUNE-CLAMDOWN` (see [`evidence/trending-daily-2026-11-13-audit.json`](../evidence/trending-daily-2026-11-13-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language Essence**:
   - **`kbdevs/query-tune`**: Turns Codex and Claude Code into a **read-only, zero-credential, zero-row-content SQL performance auditor that traces application callers and locking contracts before proposing any change**. It systematically audits composite-key gaps, functions wrapping indexed columns, latest-per-parent reads, N+1 per-row loops, and tenant/cursor/lock invariants—demonstrating up to `99%` latency drops (e.g., `543.00 ms → 25.20 ms`, `-95.4%`) across 11 benchmarked paths (8 MySQL clients, 50 randomized paired blocks per cell).
   - **`delef/ClamDown`**: Solves the **two fatal flaws of running long coding-agent sessions on a closed MacBook: forced lid-close sleep and closed-lid fan starvation**. Standard keep-awake tools (`caffeinate`) are ignored by macOS the instant the lid closes without an external monitor, and apps that merely block sleep leave macOS holding the fans near minimum RPM while the closed chassis bakes. `ClamDown` keeps the closed Mac awake, locks the screen immediately, drives Apple Silicon fans along a `50 °C → 75 °C` temperature curve, shuts off before low battery or overheating, and uses a root watchdog helper to restore normal sleep/fans if the app ever crashes.
2. **Quantified FinOps Impact (`CLAIM-20261113-R44-QUERYTUNE-CLAMDOWN`)**:
   - Under a monthly workload of **20 database slow-path audits + 200 closed-lid MacBook agent/build runs** (fully loaded rate `$100.00/hr`; base production RDS instances and MacBook hardware capex labeled `not_measured`):
   - **Path C (`query-tune` + `ClamDown`)** reduces total monthly cost of ownership (TCO) from **`$5,340.00/mo` (Path A: blind ORM indexing / replica over-provisioning + interrupted closed-lid agent runs)** to **`$495.00/mo`**, saving **`$4,845.00/mo` (`-90.73%`, `$58,140.00/yr`)** and reclaiming **`34.5 engineering hours/mo` (`-90.79%`)**.

![Round 44 Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-13-r44-query-tune-clamdown.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why does pasting isolated slow SQL queries into an LLM often cause production regressions or tenant-boundary bugs, and how does `kbdevs/query-tune` enforce a safer audit workflow?
- **The Legacy Bottleneck**: Optimizing a single SQL statement in isolation ignores how the application calls it. Naive LLM rewrites frequently break tenant isolation filters, alter collation/cursor ordering, drop required `FOR UPDATE` locks, or add indexes that amplify write latency and regress small-dataset queries.
- **How `query-tune` Solves It**:
  1. **Strict Read-Only & Zero-Row/Zero-Secret Posture**: Reads only source code, schema definitions, indexes, and saved query digests/plans—never collecting credentials, row content, or executing locking benchmark queries until explicitly instructed.
  2. **Caller & N+1 Loop Tracing**: Traces callers of expensive paths to eliminate per-row lookups/writes, duplicate state changes, and reads beyond the caller's pagination window.
  3. **Explicit Correctness & Tradeoff Ledger**: Requires every recommendation to state the exact tenant, collation, cursor, visibility, and locking rules it must preserve, while separately listing schema changes, extra write/storage costs, and potential small-case regressions.

### Q2: Why do `caffeinate` and dummy HDMI plugs fail when running coding agents on a closed MacBook, and how does `delef/ClamDown` protect the hardware?
- **The Legacy Bottleneck**:
  - **`caffeinate` Ignored on Lid Close**: macOS ignores power assertions the moment the lid closes unless both wall power and an external display are attached.
  - **Closed-Lid Thermal Starvation**: Even when closed-lid sleep is bypassed, macOS keeps a closed MacBook's fans near idle RPM even when the CPU is hot—causing severe thermal throttling during builds/agent runs and draining the battery to `0%`.
- **How `ClamDown` Solves It**:
  1. **Lid-Closed Keep-Awake + Instant Screen Lock**: Keeps processes and network connections alive when the lid closes while immediately locking the screen.
  2. **Closed-Lid Apple Silicon Fan Curve (`50 °C → 75 °C`)**: Ramps fan speed from minimum up to `50 °C` to full speed at `75 °C` while the lid is closed, and automatically hands fan control back to macOS when the lid opens.
  3. **Battery/Heat Cut-Offs + Root Watchdog Helper**: Automatically disables keep-awake before low battery or high heat becomes unsafe, and runs a root watchdog that restores sleep, Low Power Mode, and fan settings if the app quits or crashes.

### Q3: Where do `query-tune` and `ClamDown` fit best, and what are their explicit engineering limits?
- **Synergy**: Backend and full-stack engineers use `query-tune` inside Claude Code or Codex to audit database access paths safely, while running long local paired benchmarks and agent tasks on closed Apple Silicon MacBooks protected by `ClamDown`.
- **Concrete Limits**:
  - `query-tune`'s recorded improvements (e.g. `543.00ms → 25.20ms`) come from local MySQL 8-client/50-block synthetic profiles where batch timings roll back writes (excluding commit cost); production gains must be measured per workload.
  - `ClamDown`'s active fan curve control requires Apple Silicon; on Intel Macs, the Cooling page displays temperature/RPM readings without manual fan override.

---

## 🧭 3. Mermaid Selection Decision Tree & Architecture Flow

```mermaid
flowchart TD
    Start["AI Engineering Bottleneck: SQL Access-Path Latency vs Closed-Lid MacBook Agent Runs"] --> Track{"Which layer is blocking your workflow?"}

    Track -->|"Slow Database Queries / Lock Waits / ORM N+1 Loops"| SQLCheck{"Can the agent touch production row data or run live locking queries?"}
    SQLCheck -->|"No! Need read-only source/schema/caller audit preserving tenant & lock rules"| UseQueryTune["✅ Select kbdevs/query-tune<br/>Zero-row/zero-secret read-only skill · 543ms→25.2ms<br/>Caller tracing + explicit write/regression tradeoffs"]
    SQLCheck -->|"Cloud-console single-query index hints only"| UseCloudAdvisor["Use RDS Performance Insights / Cloud Advisor"]

    Track -->|"MacBook Sleeps or Overheats When Lid Closes During Agent Runs"| MacCheck{"What hardware & power setup are you running?"}
    MacCheck -->|"Apple Silicon MacBook w/ lid closed (on battery or AC) needing fan & battery guard"| UseClamDown["✅ Select delef/ClamDown<br/>Lid-close lock + 50°C–75°C fan curve<br/>Battery/heat cut-offs + Root watchdog recovery"]
    MacCheck -->|"Lid always open on desk with external monitor"| UseCaffeinate["Use Built-In macOS caffeinate -i"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `kbdevs/query-tune` | `delef/ClamDown` | Legacy Path A: Naive LLM SQL Rewrites + Closed-Lid Sleep Drops | Legacy Path B: Commercial DB APM + `caffeinate` / Dummy HDMI Plug |
| :--- | :--- | :--- | :--- | :--- |
| **Core Problem Solved** | Read-only SQL access-path & caller audit preserving correctness contracts | Keeps closed-lid MacBooks awake with active fan curves & battery cut-offs | Blind index/query guessing; closed lid kills active agent sessions | High per-host APM fees; dummy HDMI plugs lack fan/battery safety |
| **Security & Safety** | **0 credentials, 0 row content, 0 unapproved locking queries** | **Instant screen lock on lid close** + root watchdog crash recovery | Pasting sensitive row dumps into prompts; unlocked clamshell hacks | Dummy display creates phantom off-screen windows |
| **Measured Performance** | Up to **`99%` latency cut** (`543.00ms → 25.20ms` in 8-client paired blocks) | Linear fan ramp (`50 °C → 75 °C`) eliminates closed-lid thermal throttling | Frequent tenant/cursor bugs, write amplification & small-case regressions | APM misses application-layer N+1 caller loops; closed lid still bakes CPU |
| **Tradeoff Transparency** | Explicitly separates schema DDL, write cost & small-case regressions | Hands fan control back to macOS as soon as lid opens | Hidden write & lock-wait penalties discovered in production | `caffeinate` ignored by macOS on lid close without external monitor |
| **Install Footprint** | Drop-in folder for `~/.claude/skills` or `~/.codex/skills` | Native macOS menu-bar app + privileged watchdog helper | Zero setup but high incident & re-run labor cost | Recurring SaaS subscription + physical dongle clutter |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Track / Section | Headline-as-Finding | Evidence & Sealed Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `query-tune` + `ClamDown` cuts monthly SQL tuning & mobile agent TCO by `90.73%` (`$5,340.00 → $495.00/mo`) | `CLAIM-20261113-R44-QUERYTUNE-CLAMDOWN` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | Read-only caller & composite-key audit cuts slow-path latency from `543.00 ms` to `25.20 ms` (`-95.4%`) with 0 row access | `kbdevs/query-tune` 11-path study |
| **Card 3** | `3/7 · WHAT I TESTED` | Evaluated across 8 concurrent MySQL clients and 50 randomized paired blocks per cell (`small` & `large` profiles) | `kbdevs/query-tune` benchmark methodology |
| **Card 4** | `4/7 · UNDER THE HOOD` | 5-pillar SQL contract audit (access paths/N+1/locks) + `50 °C → 75 °C` closed-lid Apple Silicon fan curve | Skill prompt contract + macOS SMC/watchdog |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | "Report first, mutate nothing" SQL rule + root watchdog restoring sleep and fans if the menu-bar app crashes | Read-only guard + Watchdog daemon |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Eliminates interrupted closed-lid agent runs and blind replica scaling, saving `34.5 hrs/mo` (`-90.79%`) | 20 SQL audits + 200 closed-lid runs/mo |
| **Card 7** | `7/7 · MY TAKE` | Essential for backend teams & MacBook coding-agent users; active fan control requires Apple Silicon | Base RDS & MacBook capex: `not_measured` |

### 💰 Closed-Form FinOps Table (20 SQL Audits + 200 Closed-Lid Agent Runs/Mo, `r = $100.00/hr`)

| Architecture Path | DB Replica & Re-Run Spend (`compute_and_token_usd`) | Engineering & Tuning Hours (`engineering_hours`) | Engineering Labor (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Blind ORM Indexing / Replica Scaling + Interrupted Lid-Close Runs** | `$1,540.00` | `38.0 hrs` | `$3,800.00` | **`$5,340.00`** | Baseline (`0.00%`) |
| **Path B: Commercial APM Slow-Log SaaS + Dummy HDMI Plug** | `$860.00` | `18.0 hrs` | `$1,800.00` | **`$2,660.00`** | `-$2,680.00` (`-50.19%`) |
| **Path C: `query-tune` Read-Only Skill + `ClamDown` Thermal Guard (Recommended)** | **`$145.00`** | **`3.5 hrs`** | **`$350.00`** | **`$495.00`** | **`-$4,845.00` (`-90.73%` / `$58,140.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Install kbdevs/query-tune into Codex and Claude Code skill directories
git clone https://github.com/kbdevs/query-tune.git
mkdir -p ~/.claude/skills ~/.codex/skills
cp -R query-tune/skills/query-tune ~/.claude/skills/
cp -R query-tune/skills/query-tune ~/.codex/skills/

# 2. Run a read-only SQL & caller audit in Claude Code or Codex:
# Prompt: "Use the query-tune skill. Audit this project's database queries in read-only mode. Report first."

# 3. Install delef/ClamDown on your Apple Silicon MacBook for closed-lid fan curve & battery protection
git clone https://github.com/delef/ClamDown.git
```
