# Supervised Rust Agent Runtime (`joydle/borg`), 34-Skill Self-Testing Playbook (`nevertoday/xxd-pstack`) & Reboot Session Resurrection (`fazxes/rex-durable`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 37 (Cumulative Round 461)  
> **Tracked Repositories**:
> - **`joydle/borg`** (`★ 107`, Rust 1.88+ / Tokio, 7-Crate Workspace: `borg`, `borg-macros`, `borg-loop`, `borg-tracing`, `borg-mcp`, `borg-sandbox`, `borg-tools`, `MIT OR Apache-2.0`): Erlang-style supervised agent runtime for Rust featuring `seq / par / repeat / FallbackLadder` compositions, panic isolation, restart-storm meltdown protection, cache-aware pre-dispatch budget admission, behavioral loop guardrails (`Warn / Throttle / Halt`), and shape-verified `execute_resumable` checkpoints
> - **`nevertoday/xxd-pstack`** (`★ 65`, 10-Language Interactive Guide to `pstack`'s 34 Skills across Claude Code, Cursor & Codex) & **`fazxes/rex-durable`** (`★ 65`, Lua / macOS `launchd` & Linux `systemd`, `MIT`): Onboarding playbook teaching teams how to enforce `/poteto-mode` self-testing and before/after evidence on coding agents, paired with a durable session manager (`rex-durable`) that snapshots Rex tabs every 30 seconds and reopens `claude --resume <id>`, `codex resume <id>`, and `fx --resume <id>` across server restarts and reboots  
> **Audit Claim ID**: `CLAIM-20261117-R37-BORG-PSTACK-REX` (base LLM API subscriptions marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Enterprise Backend and Platform Teams Running Long-Lived Multi-Agent Pipelines Hit Three Reliability Failures: Unsupervised Panic/Loop Cascades, Unverified "Fixed!" Claims, and Reboot Session Loss**:
   - **Failure 1 — Unsupervised Parallel Panics & Restart-Storm Token Burn**: When orchestrating multi-agent pipelines (`Planner → parallel Coder/TestWriter/DocWriter → iterative Builder/BuildFixer → Reviewer`) with raw async tasks, a single panicking worker or upstream timeout can bring down sibling tasks, trigger an unbounded retry storm, or force a crashed run to re-execute expensive completed steps from scratch.
   - **Failure 2 — Premature "Fixed!" Claims & Rebooted Empty Shells**: Interactive coding agents routinely declare *"fixed!"* without reproducing the bug or testing their patch—wasting hours in back-and-forth developer loops—while a dev-server reboot wipes out a dozen active Claude Code and Codex terminal tabs.
   - **The Solution Architect Stack (`joydle/borg` Apache-2.0 + `xxd-pstack` + `rex-durable` MIT)**: Build production Rust agent pipelines on **`joydle/borg`** (`MIT OR Apache-2.0`, providing per-child cancellation, panic isolation, sliding-window circuit breakers, pre-dispatch cache-aware budget admission, behavioral loop `Halt` guardrails, and shape-verified `execute_resumable` checkpointing); standardize interactive agent discipline with **`nevertoday/xxd-pstack`** (10-language playbook for `pstack`'s 34 skills and `/poteto-mode` self-verification); and protect terminal workspaces with **`fazxes/rex-durable`** (`MIT`, automatically reopening `claude --resume`, `codex resume`, and `fx --resume` in their exact tab, split, and directory after a reboot).
2. **Closed-Form FinOps Impact (30 Backend & Platform Engineers Running 60,000 Monthly Supervised Agent Pipelines & Overnight Sessions at `$95.00/hr`)**:
   - Migrating from **Path A (Unsupervised Async Loops + Unverified "Fixed!" Claims & Reboot Session Loss at `$5,825.00/mo`)** to **Path C (`borg` Rust Runtime + `xxd-pstack` + `rex-durable` Stack at `$346.00/mo`)** saves **`$5,479.00/mo` (`-94.06%`, or `$65,748.00/yr`)** while cutting crash-recovery, fake-fix debugging, and session restoration labor from `37.0 hrs/mo` to `2.8 hrs/mo` (**`92.43%` reduction**).

![Borg + xxd-pstack + rex-durable Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r37-borg-pstack-rex-durable.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `joydle/borg` bring Erlang-style fault isolation, pre-dispatch budget admission, and shape-verified checkpoint recovery to Rust agent pipelines?
- **Plain-Language Definition**: `borg` (`MIT OR Apache-2.0`, Rust 1.88+ / Tokio) is a **7-crate supervised agent runtime (`borg`, `borg-macros`, `borg-loop`, `borg-tracing`, `borg-mcp`, `borg-sandbox`, `borg-tools`) that composes LLM calls into fault-isolated, budget-gated, resumable pipelines**.
- **Four Production Engineering Capabilities**:
  1. **Typed Pipeline Primitives & Supervision Tree (`seq`, `par`, `repeat`, `FallbackLadder`)**: Cancelling a pipeline cleanly stops every nested agent and in-flight LLM call; a panicking child inside `par([step(Coder), step(TestWriter), step(DocWriter)])` never takes down its siblings; and built-in supervisors enforce backoff with jitter, restart-storm meltdown limits, sliding-window circuit breakers, and cross-model `FallbackLadder`s;
  2. **Behavioral Boundary Guardrails & Cache-Aware Budget Admission**: Inspects every agent-loop boundary for pathological loops, repeated tool calls, or text-only turns (`Warn / Throttle / Halt`), and checks hierarchical sub-budgets with cache-aware pricing *before* every LLM dispatch;
  3. **Shape-Verified `execute_resumable` & Human `Decision` Suspend (`borg-loop`)**: Snapshots each step or loop iteration to a 3-method `CheckpointStore`—skipping finished work after a crash while refusing snapshots taken from a differently shaped pipeline—and suspends runs cleanly when awaiting human `approve / reject / edit` decisions;
  4. **Zero-Key `FakeLlmClient` & `ScriptedAgent` Testing**: Ships a built-in evaluation and testing feature (`--features testing`) so full supervision and checkpoint topologies can be tested in CI without API keys.

### Q2: How do `nevertoday/xxd-pstack` and `fazxes/rex-durable` eliminate unverified "fixed!" claims and terminal reboot amnesia?
- **`nevertoday/xxd-pstack` (10-Language Playbook for `pstack`'s 34 Self-Testing Skills)**:
  - Breaks down `backnotprop/pstack` across 3 beginner lessons, a 9-step walkthrough, 34 skill maps, and 17 how-to guides in 10 languages—teaching teams how `/poteto-mode` forces Claude Code, Cursor, and Codex to **reproduce the failure, test their own fix, and present before/after evidence** before reporting completion.
- **`fazxes/rex-durable` (30-Second Tab Snapshotting & Safe Reboot Resurrection, `MIT`)**:
  - Runs as a `launchd` (macOS) or `systemd` (Linux) service that records what is running in every Rex tab and split every 30 seconds;
  - After a server restart or reboot, it automatically reopens `claude --resume <id>`, `codex resume <id>`, and `fx --resume <id>` with their original `--model` flags and working directories—while safely typing (never auto-running) arbitrary shell commands at the prompt.

### Q3: How should an AI Solution Architect combine `borg`, `xxd-pstack`, and `rex-durable`?
- **Backend Automated Pipelines (`joydle/borg`)**: Implement unattended build-fix-review pipelines in Rust with `borg`'s pre-dispatch budget caps, `FallbackLadder`s, and `execute_resumable` checkpoints.
- **Interactive Developer Workstations (`xxd-pstack` + `rex-durable`)**: Onboard engineers with `xxd-pstack` to enforce `/poteto-mode` self-testing and install `rex-durable` on remote Rex servers so overnight agent sessions survive reboots automatically.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph RustRuntime["Supervised Rust Agent Runtime: joydle/borg (★107, Rust 1.88+ Apache-2.0)"]
        A[Multi-Agent Pipeline Dispatch] --> B[Pre-Dispatch Cache-Aware Budget Admission<br/>+ Behavioral Guardrails Warn / Throttle / Halt]
        B --> C[seq: Planner → par: Coder ∥ TestWriter ∥ DocWriter<br/>Panic Isolation · Circuit Breaker · FallbackLadder]
        C --> D[repeat Up to 8 Rounds: Builder → BuildFixer Until PASS]
        D --> E[execute_resumable CheckpointStore<br/>Skips Completed Steps on Crash + Human Decision Suspend]
    end

    subgraph DevWorkstation["Self-Testing Discipline &amp; Durable Tabs: xxd-pstack (★65) + rex-durable (★65, MIT)"]
        F[Interactive Claude Code / Cursor / Codex Session] --> G[xxd-pstack 34 Skills &amp; /poteto-mode<br/>Reproduce + Self-Test + Before/After Evidence]
        G --> H[fazxes/rex-durable 30s Tab Snapshot<br/>Auto-Runs claude/codex --resume in Exact Tab/Split on Reboot]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Unsupervised Async Loops + Unverified Fixes + Lost Tabs | Option B: Raw `tokio::spawn` Retries + Manual `--resume` Tracking | **Option C (Recommended): `borg` (Apache-2.0) + `xxd-pstack` + `rex-durable` (MIT)** |
| :--- | :--- | :--- | :--- |
| **Parallel Panic Isolation & Loop Circuit Breaking** | ❌ One panicking worker aborts siblings; tool loops burn budget | ⚠️ Custom retry wrappers lack restart-storm meltdown & model ladders | ✅ **Erlang-style supervision, panic isolation, `FallbackLadder` & `Warn/Throttle/Halt` guards** |
| **Crash Checkpointing & Pipeline Shape Safety** | ❌ Re-runs entire pipeline from Step 1 after a crash | ⚠️ Naive file caches corrupt state when pipeline steps change | ✅ **`execute_resumable` skips finished steps and rejects mismatched pipeline shapes** |
| **Prevention of Unverified "Fixed!" Claims** | ❌ Agent claims fixed without running tests; takes 5 rounds of nagging | ⚠️ Relies on ad-hoc developer reminders | ✅ **`xxd-pstack` 34-skill `/poteto-mode` enforces reproduction & before/after proof** |
| **Terminal Session Survival Across Server Reboots** | ❌ All tabs return as empty shells after a reboot | ❌ Manual hunting for session UUIDs across log directories | ✅ **`rex-durable` auto-resumes `claude/codex/fx` with original flags; stages shell commands safely** |
| **Monthly TCO (30 Engineers / 60,000 Runs)** | **`$5,825.00 / mo`** (`$2,310` storm/rerun tokens + `37.0 hrs` rework) | **`$2,545.00 / mo`** (`$930` rerun tokens + `17.0 hrs` manual recovery) | **`$346.00 / mo`** (**`-94.06%` savings**; `$80` budget-gated workers + `2.8 hrs` Decision sign-off) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R37-BORG-PSTACK-REX`)

> **Scope & Boundary Declaration**: Evaluated for a 30-engineer backend and platform organization running **60,000 monthly supervised multi-agent pipelines and overnight terminal sessions** at a blended engineering rate of `$95.00/hr` (base LLM API subscriptions marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Loop/Restart-Storm Token Spend} + (\text{Fake-Fix Rework \& Reboot Recovery Hours} \times \$95.00)$$

| Cost Component | Path A: Unsupervised Async Loops + Fake Fixes | Path B: Raw `tokio::spawn` + Manual IDs | **Path C: `borg` + `xxd-pstack` + `rex-durable`** |
| :--- | :---: | :---: | :---: |
| **Monthly Loop/Restart-Storm & Crash Re-Run Token Spend** | `$2,310.00` | `$930.00` | **`$80.00`** |
| **Monthly Fake-Fix QA, Crash Debug & Tab Recovery Hours** | `37.0 hrs` | `17.0 hrs` | **`2.8 hrs`** (**`92.43%` reduction**) |
| **Monthly Backend & Platform Engineering Labor (`@ $95.00/hr`)** | `$3,515.00` | `$1,615.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,825.00`** | **`$2,545.00`** (`-56.31%`) | **`$346.00`** (**`-94.06%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,280.00 / mo` (`$39,360/yr`) | **`$5,479.00 / mo` (`$65,748.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Pin `joydle/borg` (`tag = "v1.0.0"`) & Validate Pipelines with `FakeLlmClient`**: Add `borg = { git = "https://github.com/joydle/borg.git", tag = "v1.0.0" }` (avoiding the unrelated crates.io package) and test `seq / par / repeat` topologies offline using `--features testing`.
- [ ] **Step 2 — Enable Pre-Dispatch Sub-Budgets & `execute_resumable` Checkpoints**: Configure cache-aware budget admission, repeated-tool-call `Halt` guardrails, and database-backed `CheckpointStore` snapshots on all long-running Rust pipelines.
- [ ] **Step 3 — Onboard Teams with `nevertoday/xxd-pstack`'s 34-Skill Playbook**: Roll out `/poteto-mode` across Claude Code, Cursor, and Codex so agents always reproduce bugs and provide before/after verification evidence.
- [ ] **Step 4 — Install `fazxes/rex-durable` on All Remote Rex Workstations**: Run `./install.sh --add-to-config` to snapshot tabs every 30 seconds and automatically restore `claude --resume` and `codex resume` conversations after reboots.
