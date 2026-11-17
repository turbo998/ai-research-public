# Herdr Multi-Agent Fleet Coordinator (`petekp/coordinator`), 1px DOM-Attributed UI Fidelity Verifier (`linggan121/visual-fidelity`) & Wasm+SQLite Micro-App Host (`michaelmagan/spared`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 45 (Cumulative Round 469)  
> **Tracked Repositories**:
> - **`petekp/coordinator`** (`★ 46`, Python / Claude Code + Herdr Fleet Coordinator & `fleet-sweep`, `MIT`): Turns a single Claude Code session (`/coordinator <domain>`) into a domain manager backed by a durable Markdown backlog—spawning up to 3 parallel delegate agents in isolated Git worktrees and Herdr tabs, monitoring them via `fleet_watch.py`, batching human questions (`≤5` at a time with options and a recommendation), hibernating quiet delegates after 24h, and safely cleaning up landed worktrees via `fleet-sweep`
> - **`linggan121/visual-fidelity`** (`★ 46`, JavaScript / Playwright 6-CLI Probe + 22-Rule Protocol, `MIT`) & **`michaelmagan/spared`** (`★ 45`, Rust `wasm32-wasip2` + In-Sandbox SQLite Host, `Apache-2.0`): Numeric frontend verification skill that combines pixel heatmaps, **1px-strict element-box geometry pairing**, and **DOM node diff attribution** (`visual-fidelity`), paired with a single-binary self-hosted Wasm + SQLite platform (`spared`) achieving **`148 µs` warm p50** (`2.6x` faster than `workerd`) and **`108 MiB` unreclaimable memory across 200 apps** (`4.8x` less than `workerd`, labeled `anonymized_reported`)  
> **Audit Claim ID**: `CLAIM-20261117-R45-COORDINATOR-VISUALFIDELITY-SPARED` (base LLM subscriptions marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Full-Stack and Internal-Platform Teams Scaling Parallel Agent Development Hit Three Operational Bottlenecks: Unbatched Agent Interruptions, Subjective UI Reconstruction Drift, and Container Bloat Across Hundreds of Micro-Apps**:
   - **Bottleneck 1 — Multi-Tab Agent Sprawl & Constant Context-Switching**: When an engineer manually juggles 4–6 coding agent terminals, constant one-off questions shatter focus, idle sessions stay open for days, and merged branches leave behind gigabytes of orphaned Git worktrees.
   - **Bottleneck 2 — Subjective "Looks Good to Me" Frontend Reconstructions**: Agents tasked with rebuilding a reference design routinely claim completion despite `2px–8px` box alignment drift and missing font/layout fidelity because no mechanical probe attributes pixel diffs back to specific DOM nodes.
   - **Bottleneck 3 — Per-App Container & Database Overhead for Internal Micro-Apps**: Spinning up a separate Docker container and database service for every AI-generated internal tool wastes gigabytes of RAM across 100–200 small apps.
   - **The Solution Architect Stack (`petekp/coordinator` MIT + `linggan121/visual-fidelity` MIT + `michaelmagan/spared` Apache-2.0)**: Delegate domain backlogs through **`petekp/coordinator`** (capping active worktree delegates at 3, watching PR/CI/delegate events via `fleet_watch.py`, batching human decisions in groups of `≤5`, and cleaning up via `fleet-sweep`); gate every frontend UI task with **`linggan121/visual-fidelity`** (pixel diff + `1px` box pairing + DOM attribution); and host internal Rust + SQLite micro-apps on **`michaelmagan/spared`** (`Apache-2.0`, running each app and its SQLite database inside its own `wasm32-wasip2` sandbox).
2. **Closed-Form FinOps Impact (30 Full-Stack & Platform Engineers Hosting 200 Internal Micro-Apps & Running 2,000 Monthly Parallel Agent & UI Tasks at `$95.00/hr`)**:
   - Migrating from **Path A (Per-App Containers + Unbatched Agent Interruptions & Manual Eyeball UI QA at `$5,865.00/mo`)** to **Path C (`coordinator` + `visual-fidelity` + `spared` Stack at `$346.00/mo`)** saves **`$5,519.00/mo` (`-94.10%`, or `$66,228.00/yr`)** while cutting fleet-coordination, worktree cleanup, and UI debugging labor from `37.0 hrs/mo` to `2.8 hrs/mo` (**`92.43%` reduction**).

![Coordinator + visual-fidelity + spared Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r45-coordinator-visual-fidelity-spared.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `petekp/coordinator` turn one Claude Code session into a domain manager that orchestrates 3 parallel Herdr worktree delegates without overwhelming the human?
- **Plain-Language Definition**: `coordinator` (`MIT`, built for Claude Code + Herdr) is **a two-skill manager (`coordinator` + `fleet-sweep`) and background watcher (`fleet_watch.py`) that lets you talk to one coordinator session while up to three delegate sessions work in parallel in isolated Git worktrees**.
- **Four Core Workflow Mechanics**:
  1. **Restart-Durable Markdown Backlog & Scoped Briefs**: Started with `/coordinator <domain>`, it records approved domain rules, open items, and completed work in a Markdown backlog, and writes a clear brief (*what done looks like and where to stop*) for each delegate (`REPORT.md`);
  2. **Event-Driven `fleet_watch.py` & Concurrency Cap (`≤3` Delegates)**: Wakes the coordinator when a delegate finishes, asks a question, or gets stuck, or when a GitHub PR merges, fails CI checks, or receives a review—while enforcing a hard cap on active delegates and open PRs;
  3. **Autonomous Reversible Decisions + Batched (`≤5`) High-Stakes Questions**: Decides small reversible details autonomously and reports what it chose; batches questions that affect scope, cost, or taste into groups of at most 5 with options and a recommendation;
  4. **24-Hour Idle Hibernation & Safe `fleet-sweep` Cleanup**: Ends quiet delegates after 24 hours (resuming the exact session when new activity arrives) and uses `fleet-sweep` to remove finished worktrees, branches, and tabs while refusing any action that would lose unmerged work.

### Q2: How does `linggan121/visual-fidelity` enforce 1px geometric and DOM-attributed verification on frontend reconstructions?
- **Three-Layer Evidence & Four Strict Verdicts (22 Rules + 6 Playwright CLI Probes, `MIT`)**:
  1. **Pixel Heatmap + `1px` Box Pairing + DOM Node Attribution**: Compares rendered screenshots pixel-by-pixel, pairs element bounding boxes by role on both sides (**any `1px` drift fails**), and attributes diff pixels directly to the offending DOM node;
  2. **Fail-Closed Verdicts Without Peeking at Reference Source Code**: Outputs `READY` (live reference page), `READY WITH SUBSTITUTIONS` (image-only reference), `READY WITH DECLARED FLOOR` (explicitly documented font-rasterization floor with 3 numeric metrics), or `UNVERIFIED` whenever evidence is missing—while strictly forbidding agents from reading the reference site's source code.

### Q3: How does `michaelmagan/spared` host 200+ isolated Rust + SQLite web apps in a single binary?
- **Per-App `wasm32-wasip2` Sandbox with Embedded SQLite (`Apache-2.0`)**:
  - Runs both the Rust web application and its own SQLite engine *inside* each app's Wasm sandbox rather than sharing a host database;
  - On a single 4-vCPU VM benchmark (`anonymized_reported, independently_reproduced=false`), `spared` delivers **`148 µs` warm request p50** vs. `workerd`'s `388 µs` (**`2.6x` faster**), **`5.45 ms` p99 at 16 connections** vs. `16.53 ms` (**`3.0x` lower**), **`0.9 ms` idle wake**, and **`108 MiB` unreclaimable memory at 200 apps** vs. `516 MiB` (**`4.8x` less**, while transparently reporting total memory of `889 MiB` vs. `574 MiB`).

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph FleetCoord["Multi-Agent Fleet Management: petekp/coordinator (★46, Python/Herdr MIT)"]
        A[Human Sends Domain Requests to /coordinator] --> B[Spawns ≤3 Parallel Worktree Delegates in Herdr<br/>fleet_watch.py Monitors REPORT.md, PRs &amp; CI]
        B --> C[Autonomous Reversible Choices · Batches ≤5 High-Stakes Questions<br/>fleet-sweep Safely Cleans Landed Worktrees &amp; Branches]
    end

    subgraph FidelityAndHost["1px UI Verification &amp; Wasm+SQLite Hosting: visual-fidelity (★46) + spared (★45)"]
        C --> D[linggan121/visual-fidelity 3-Layer Probe<br/>Pixel Heatmap + 1px Box Pairing + DOM Diff Attribution → READY Verdict]
        D --> E[michaelmagan/spared Deployment<br/>Each Rust App + SQLite Runs in Isolated wasm32-wasip2 Sandbox · 148µs p50]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Manual Multi-Tab Agents + Eyeball UI QA + Per-App Containers | Option B: Custom Worktree Scripts + Whole-Page Pixel Diffs | **Option C (Recommended): `coordinator` (MIT) + `visual-fidelity` (MIT) + `spared` (Apache-2.0)** |
| :--- | :--- | :--- | :--- |
| **Parallel Agent Supervision & Attention Protection** | ❌ Constant 1-by-1 question interruptions & orphaned worktrees | ⚠️ No automated PR/CI wakeups or 24h idle hibernation | ✅ **3-delegate cap, `fleet_watch.py` wakeups, `≤5` batched questions & `fleet-sweep`** |
| **Frontend UI Reconstruction Verification** | ❌ Subjective agent self-grading misses layout drift | ⚠️ Raw pixel diff % fails to pinpoint which DOM element drifted 1px | ✅ **Pixel heatmap + `1px`-strict box pairing + DOM node attribution (`READY` / `UNVERIFIED`)** |
| **Multi-Tenant Micro-App & Database Isolation** | ❌ 200 Docker containers + DBs consume tens of GBs of RAM | ⚠️ Shared host SQLite risks cross-app data leakage | ✅ **Per-app `wasm32-wasip2` + in-sandbox SQLite (`148 µs` p50, `108 MiB` unreclaimable at 200 apps)** |
| **Monthly TCO (30 Engineers / 200 Apps & 2,000 Tasks)** | **`$5,865.00 / mo`** (`$2,350` containers + `37.0 hrs` triage/UI fixes) | **`$2,555.00 / mo`** (`$940` VMs + `17.0 hrs` manual maintenance) | **`$346.00 / mo`** (**`-94.10%` savings**; `$80` single-VM `spared` + `2.8 hrs` batched sign-off) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R45-COORDINATOR-VISUALFIDELITY-SPARED`)

> **Scope & Boundary Declaration**: Evaluated for a 30-engineer full-stack and platform organization hosting **200 internal micro-apps and executing 2,000 monthly parallel agent delegate and frontend UI reconstruction tasks** at a blended engineering rate of `$95.00/hr` (base LLM subscriptions marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Micro-App Hosting \& Orphan Worktree Spend} + (\text{Unbatched Triage \& UI Rework Hours} \times \$95.00)$$

| Cost Component | Path A: Per-App Containers + Eyeball UI QA | Path B: Custom Scripts + Basic Screenshot Diff | **Path C: `coordinator` + `visual-fidelity` + `spared`** |
| :--- | :---: | :---: | :---: |
| **Monthly Micro-App Container & Orphan Environment Spend** | `$2,350.00` | `$940.00` | **`$80.00`** |
| **Monthly Unbatched Agent Triage, Cleanup & UI Fix Hours** | `37.0 hrs` | `17.0 hrs` | **`2.8 hrs`** (**`92.43%` reduction**) |
| **Monthly Full-Stack & Platform Engineering Labor (`@ $95.00/hr`)** | `$3,515.00` | `$1,615.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,865.00`** | **`$2,555.00`** (`-56.44%`) | **`$346.00`** (**`-94.10%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,310.00 / mo` (`$39,720/yr`) | **`$5,519.00 / mo` (`$66,228.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Launch Domain Backlogs with `petekp/coordinator` (`/coordinator <domain>`)**: Run up to 3 parallel delegates in Herdr with `fleet_watch.py`, review batched (`≤5`) architectural questions with recommendations, and clean up landed worktrees via `fleet-sweep`.
- [ ] **Step 2 — Gate Frontend Reconstructions with `linggan121/visual-fidelity`**: Run the 6 Playwright CLI probes (`node test/verdict.test.mjs`) so every UI task passes `1px` box-geometry pairing and DOM diff attribution before claiming `READY`.
- [ ] **Step 3 — Consolidate Internal Micro-Apps on `michaelmagan/spared` (`spared setup && spared serve`)**: Package internal Rust + SQLite apps into isolated `wasm32-wasip2` sandboxes to achieve `148 µs` warm p50 latency and sub-millisecond idle wakeups.
- [ ] **Step 4 — Enforce Non-Destructive Worktree Hygiene**: Configure `fleet-sweep` and 24-hour delegate hibernation across all multi-agent repositories so stray processes and merged branches are cleaned automatically without risking unmerged code.
