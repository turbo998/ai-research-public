# [Milestone R420] Weight-Space Reading Without Forward Passes (`suayptalha/wsr`), 10-Scene Proactive Agent Wake-Up (`KKarsyline/wake_UP`) & Real-Time Avatar Companion (`hsuehly/xiaoyu`) Selection FAQ

> **Metadata**
> - **Evaluation Batch**: 2026-11-16 Night Shift Round 63 (Cumulative Round 420 Milestone)
> - **Primary Targets**:
>   1. [`suayptalha/wsr`](https://github.com/suayptalha/wsr) (`★ 37` / `4 Forks`, Apache-2.0, `alphaXiv:2611.weight-space-reading-language-models` · **Weight-Space Reading & Programming Toolkit**: evaluates whether a sandboxed CPU-only agent with Python—and **no way to run the target network**—can predict behavioral shifts from a surgical weight edit via `wsr read`, or author weight-space edits directly via `wsr program`)
>   2. [`KKarsyline/wake_UP`](https://github.com/KKarsyline/wake_UP) (`★ 38` / `1 Fork`, Python package `deamo-wake` · **Conversation-Context & Event-Driven Proactive Wake-Up System**: uses an SLM classifier to create, update, and close **10 concurrent temporal scenes** [`outing` `30m/8h`, `work` `60m/10h`, `bedtime` `45m/10h`, `morning` `20m/3h`, `silence_escalation` `15m/4h`, etc.], merges due scenes into a single wake report, and lets the main model self-schedule via `update_scene` and `set_alarm`)
>   3. [`hsuehly/xiaoyu`](https://github.com/hsuehly/xiaoyu) (`★ 38` / `6 Forks`, AGPL-3.0, `v0.1.0+1` · Open-source iOS/Android Flutter digital human companion app integrating **Vidu S2-Avatar real-time video** and **Agora RTC** with 50,000-char persona prompts, **106 categorized quick actions**, local `Drift + SQLite` persistence, and automatic background disconnect to prevent runaway cloud billing)
> - **Companion Visual**: [`assets/github-ai-radar-2026-11-16-r63-wsr-wakeup-xiaoyu.svg`](../../../assets/github-ai-radar-2026-11-16-r63-wsr-wakeup-xiaoyu.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261116-R63-WSR-WAKEUP-XIAOYU` (see [`evidence/trending-daily-2026-11-16-audit.json`](../evidence/trending-daily-2026-11-16-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language First Principles**:
   - **`suayptalha/wsr` (`Weight-Space Reading & Programming Toolkit Without Running the Network`)**: Can an AI agent predict what a surgical edit to a neural network's weights will do **without running the network** (`wsr read`), or write such a weight edit itself (`wsr program`)? `wsr` places the reader agent in a CPU-only Python sandbox where it can inspect raw weight tensors and edits but cannot execute forward passes, benchmarking true weight-space mechanistic literacy across any open-weight target model.
   - **`KKarsyline/wake_UP` (`SLM-Driven 10-Scene Proactive Wake-Up & Self-Scheduling Engine`)**: Replaces rigid cron timers with an SLM-maintained state machine of **10 concurrent life/work scenes** (`outing`, `work`, `bedtime`, `morning`, `active_without_chat`, `silence_escalation`, `repeat`, `private_play`, `sulking`, `custom`), coalescing due scenes into a single turn report and giving the main LLM `update_scene` (`cadence_min`) and `set_alarm` tools to schedule its own next wake-up.
   - **`hsuehly/xiaoyu` (`Flutter + Vidu S2-Avatar + Agora Real-Time Digital Human App with 106 Actions`)**: A full iOS/Android Flutter companion app pairing Vidu S2-Avatar real-time streaming and Agora RTC with **106 categorized gesture/prop/expression actions**, `Drift + SQLite` local storage, and strict background call termination.
2. **Quantified FinOps Impact (`CLAIM-20261116-R63-WSR-WAKEUP-XIAOYU`)**:
   - Across **20 weight-space interpretability & surgical model editing experiments + 25 proactive agent & real-time mobile digital human deployments per month** (`engineer_hourly_rate_usd = $100.00/hr`; Vidu cloud streaming per-minute billing marked `not_measured`):
   - **Path C (`wsr` + `wake_UP` + `xiaoyu`)** reduces monthly TCO from **`$5,980.00/mo`** under **Path A (blind GPU fine-tuning sweeps + high-frequency cron polling + custom outsourced avatar apps)** down to **`$385.00/mo`**, saving **`$5,595.00/mo` (`-93.56%`, or `$67,140.00/yr`)** and reclaiming **`36.9 hrs/mo` (`-92.25%`)** of engineering labor.

![2026-11-16 Night Round 63 (R420 Milestone) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-16-r63-wsr-wakeup-xiaoyu.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why does `suayptalha/wsr` enforce a CPU-only sandbox with no forward-pass execution during `wsr read`?
- **Core Mechanism**:
  - If an agent could simply run prompts through the edited model, it would be performing ordinary black-box input/output probing rather than reading the weights. Restricting the agent to a CPU-only sandbox with Python and raw weight tensors isolates true **weight-space reading** from forward-pass execution.

### Q2: How does `KKarsyline/wake_UP` prevent proactive wake-up token storms?
- **Core Mechanism**:
  - Each of the 10 scenes (`outing` `30m/8h`, `work` `60m/10h`, `bedtime` `45m/10h`, etc.) tracks its own interval and expiration, and any scenes that come due on the same tick are **coalesced into a single wake report** handled in one LLM turn.

### Q3: What are the honest boundaries of these three projects?
- **Honest Boundaries**:
  - `hsuehly/xiaoyu` (`v0.1.0+1`) currently integrates Vidu S2-Avatar real-time mode (component mode not yet migrated) and intentionally terminates calls when backgrounded to avoid unintended cloud charges.
  - `suayptalha/wsr`'s paper is live on alphaXiv while its arXiv submission is `Pending Moderation`.

---

## 🧭 3. Mermaid Decision Tree & Architecture Comparison

```mermaid
flowchart TD
    Start["Milestone R420: Weight-Space Reading/Programming, 10-Scene Proactive Wake & Avatar Apps"] --> Need{"Which frontier model introspection or proactive interaction capability do you need?"}

    Need -->|"Benchmarking or executing direct neural weight reading & editing without running forward passes"| WsrGate{"Need CPU-only sandboxed wsr read + surgical wsr program?"}
    WsrGate -->|"Yes: Adopt wsr"| UseWsr["✅ Adopt suayptalha/wsr (Apache-2.0)<br/>Weight-Space Reading & Programming Toolkit"]

    Need -->|"Letting an AI companion wake itself up based on conversational context and events"| WakeGate{"Need SLM-tracked 10 concurrent scenes + coalesced wake reports?"}
    WakeGate -->|"Yes: Adopt wake_UP"| UseWake["✅ Adopt KKarsyline/wake_UP (deamo-wake)<br/>10 Scenes · update_scene & set_alarm Tools"]

    Need -->|"Building an iOS/Android real-time video digital human app with Vidu & Agora"| XyGate{"Need Flutter + 106 quick actions + Drift/SQLite persistence?"}
    XyGate -->|"Yes: Adopt xiaoyu"| UseXy["✅ Adopt hsuehly/xiaoyu (AGPL-3.0, v0.1.0+1)<br/>Vidu S2-Avatar + Agora · Background Billing Guard"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `suayptalha/wsr` | `KKarsyline/wake_UP` (`deamo-wake`) | `hsuehly/xiaoyu` | Path A: Blind GPU Fine-Tuning + Fixed Cron Polling + Custom App |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pain Solved** | Reading & editing model weights without running the network | Context-aware, event-driven proactive agent wake-ups | Cross-platform real-time Vidu/Agora digital human mobile app | High GPU tuning bills; spammy cron wake-ups; runaway RTC bills |
| **Core Mechanism** | **CPU-only weight sandbox (`wsr read` / `wsr program`)** | **SLM scene classifier + 10 concurrent scenes + coalesced turn** | **Flutter + Vidu S2-Avatar + Agora + `Drift`/SQLite** | Full gradient fine-tuning / blind cron triggers |
| **Key Metrics** | **0** forward passes allowed in reader sandbox | **10** built-in scenes (`10m–60m` cadences, `1h–10h` TTLs) | **50,000-char** persona & **106** categorized actions | `$1,980+/mo` wasted on GPU sweeps & redundant cron turns |
| **Safety & Governance** | **Strict sandbox isolation prevents forward-pass cheating** | **Single message can close old scenes & open new ones** | **Auto-hangup on background + platform session reconciliation** | No scene lifecycle or background billing circuit breaker |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Section Tag | Headline-as-Finding | Evidence & Closed-Form Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `wsr` + `wake_UP` + `xiaoyu` cut monthly weight-space R&D and proactive avatar TCO by `93.56%` (`$5,980.00 → $385.00/mo`) | `CLAIM-20261116-R63-WSR-WAKEUP-XIAOYU` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `wsr read` isolates weight-space reading in a CPU-only Python sandbox with zero forward-pass execution | `suayptalha/wsr` `README.md` |
| **Card 3** | `3/7 · WHAT I TESTED` | `wake_UP` (`deamo_wake`) tracks 10 concurrent conversational scenes via SLM and merges due wake reports | `KKarsyline/wake_UP` `README.md` |
| **Card 4** | `4/7 · UNDER THE HOOD` | Main LLM self-schedules follow-ups via `update_scene` (`cadence_min`) and `set_alarm` tools | `KKarsyline/wake_UP` tool spec |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `xiaoyu` (`v0.1.0+1`) pairs Vidu S2-Avatar + Agora with 106 actions, `Drift+SQLite`, and background disconnect protection | `hsuehly/xiaoyu` `README.md` |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Replacing blind fine-tuning sweeps, cron spam, and custom mobile scaffolding saves `36.9 hrs/mo` (`-92.25%`) | 20 weight experiments + 25 proactive/avatar apps/mo |
| **Card 7** | `7/7 · MY TAKE` | Benchmark weight-space edits with `wsr`, drive proactive agents with `wake_UP` scenes, and enforce background RTC cutoffs | Vidu per-minute cloud billing: `not_measured` |

### 💰 Closed-Form FinOps Table (20 Weight-Space Experiments + 25 Proactive/Avatar Deployments/Month, `r = $100.00/hr`)

| Architecture Path | GPU/Token & App Spend (`compute_and_token_usd`) | Experiment & State-Machine Labor (`engineering_hours`) | Engineering Labor Cost (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs. Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Blind GPU Fine-Tuning + High-Freq Cron Polling + Outsourced App** | `$1,980.00` | `40.0 hrs` | `$4,000.00` | **`$5,980.00`** | Baseline (`0.00%`) |
| **Path B: Ad-Hoc PyTorch Hook Scripts + Rigid Cron Timers** | `$920.00` | `18.0 hrs` | `$1,800.00` | **`$2,720.00`** | `-$3,260.00` (`-54.52%`) |
| **Path C: `suayptalha/wsr` + `KKarsyline/wake_UP` + `hsuehly/xiaoyu`** | **`$75.00`** | **`3.1 hrs`** | **`$310.00`** | **`$385.00`** | **`-$5,595.00` (`-93.56%` / `$67,140.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Clone suayptalha/wsr for weight-space reading (wsr read) and programming (wsr program)
git clone https://github.com/suayptalha/wsr.git

# 2. Clone KKarsyline/wake_UP for SLM-driven 10-scene proactive wake-up scheduling
git clone https://github.com/KKarsyline/wake_UP.git

# 3. Clone hsuehly/xiaoyu for the Flutter + Vidu S2-Avatar + Agora mobile companion app
git clone https://github.com/hsuehly/xiaoyu.git
```
