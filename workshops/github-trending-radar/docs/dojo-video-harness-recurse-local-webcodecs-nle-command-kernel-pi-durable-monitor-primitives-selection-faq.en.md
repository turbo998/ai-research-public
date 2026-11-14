# Command-Kernel Local WebCodecs Video Editor (`PansaLegrand/dojo-video-harness`) & Pi-Durable Monitor Primitives (`ebetica/recurse`) Deep-Dive & Selection FAQ

> **Document Metadata (2026-11-14 · Night Round 69 / Cumulative Round 252)**  
> - **Benchmark Style**: `ib-vs-ethernet-roce-selection-faq.md` (First-Principles + Plain-Language Deconstruction + 3 Architect Core Questions + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> - **Primary Evaluated Repositories**:  
>   1. [`PansaLegrand/dojo-video-harness`](https://github.com/PansaLegrand/dojo-video-harness) (`★ 53`, MIT local open-source NLE video editor and educational TypeScript agent harness powered by `@dojo-video-engine/* v1.2.3`: delegates complex timeline invariants to a **tested document & command kernel**, exports MP4s directly in the browser via **WebCodecs with zero database, Redis, or cloud workers**, and runs shared loop `0.1.3` with durable checkpoints, deterministic context pruning, and one-way server API key isolation)  
>   2. [`ebetica/recurse`](https://github.com/ebetica/recurse) (`★ 46`, MIT local web-first agentic harness built on **Pi Durable** and Bun 1.4+: reduces long-horizon autonomous workflows to **auto-backgrounding shells, output-triggered `Monitors` [unifying goals, cadence loops, and CI watchers], and worktree-isolated multiagent trees (`subagent.ts`)** over an SSH-tunnelable `:8787` web UI)  
> - **Visual Architecture Diagram**: [`assets/github-ai-radar-2026-11-14-r69-dojovideo-recurse.svg`](../../../assets/github-ai-radar-2026-11-14-r69-dojovideo-recurse.svg)  
> - **Audit Contract ID**: `CLAIM-20261114-R69-DOJOVIDEO-RECURSE` (local workstation hardware depreciation is explicitly marked `not_measured`)

---

## 📌 1. Executive Summary (Understand the Essence in 3 Minutes)

1. **Why do LLMs corrupt multi-track video timelines when editing raw JSON directly, while cloud AI video SaaS platforms require uploading private footage to remote render queues? How does `PansaLegrand/dojo-video-harness` solve both?**  
   - **Plain-Language Essence**: Non-linear video editing involves strict invariants (track ripple behavior, clip bounds, transition overlaps). Letting an LLM calculate millisecond offsets in raw JSON breaks timelines, while cloud video editors lock your media behind paid render workers.  
   - **First-Principles Breakthrough in `dojo-video-harness`**:
     - **Tested Document & Command Kernel + Shared Loop `0.1.3`**: The agent emits typed function calls against a small tool registry while all video-specific timeline rules live in a deterministic, tested document and command kernel. Loop `0.1.3` provides durable checkpoints, deterministic context pruning, and structured pending user questions.
     - **Zero-Cloud Browser WebCodecs Export (`@dojo-video-engine v1.2.3`) + One-Way Key Security**: Launched with `npm run launch` (`http://127.0.0.1:4310`), manual timeline editing, subtitle import, motion graphics, and browser WebCodecs MP4 export require **zero database, zero Redis, zero cloud worker, and zero API keys**. When LLM/ASR keys are configured, saved keys are never returned to the browser and running jobs stay pinned to their initial configuration.
2. **Why build bloated scheduling subsystems for goals, cron loops, and CI watchers when `ebetica/recurse` expresses all of them through three Pi-Durable primitives?**  
   - **Plain-Language Essence**: Autonomous agents waiting on 10-minute builds or CI pipelines usually either block the session or waste tokens polling `sleep 5 && check_status` in a loop.  
   - **First-Principles Breakthrough in `recurse`**:
     - **Auto-Backgrounding Shells + Output-Triggered `Monitors`**: Long-running commands background automatically and wake the agent when they finish. A **Monitor** is a background shell that wakes the agent whenever it prints to stdout — turning a goal checker, a cadence loop, a reminder, or a CI watcher into a tiny monitor skill with zero polling token waste!
     - **In-Process Pi-Durable Multiagent Tree (`subagent.ts`) + `:8787` Web UI**: Every chat is an agent running in a shared Bun process with Pi Durable interruption recovery; agents spawn subagents in isolated git worktrees and report results up the tree, served via an SSH-tunnel-friendly `:8787` web interface with async compaction and `fffgrep`.
3. **Closed-Form FinOps Audit Conclusion (`CLAIM-20261114-R69-DOJOVIDEO-RECURSE`)**:  
   - Modeled for **35 local video editing projects and long-horizon monitor-driven coding workflows/month** (at **`$95.00/hr`** engineering labor): migrating from **Path A** (cloud NLE render workers + polling-heavy agent loops: **`$5,000.00/mo`**, comprising `$1,580.00` cloud render/polling token spend + `36.0h` timeline fix and interrupted shell recovery labor `$3,420.00`) to **Path C** (`dojo-video-harness` WebCodecs command kernel + `recurse` Pi-Durable monitors: **`$417.50/mo`**, comprising `$85.00` event-woken token spend + `3.5h` review labor `$332.50`) saves **`$4,582.50/mo`** (**`-91.65%`**, or **`$54,990.00/yr`**) and cuts engineering hours by **`90.28%`**.

![Dojo Video Harness & recurse Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r69-dojovideo-recurse.svg)

---

## 💬 2. Three Architect Core Questions (Q1–Q3 Deep Dive)

### Q1: Why does `PansaLegrand/dojo-video-harness` keep all video-specific invariants inside a tested Document & Command Kernel rather than inside agent prompts?

1. **Deterministic Domain Kernel Over Probabilistic LLM Arithmetic**:  
   - By exposing a compact, typed command surface to the agent while enforcing timeline ripple, trim, and layer rules inside `@dojo-video-engine v1.2.3`, both human mouse drags and chat agent edits share one crash-free state machine.

---

### Q2: How does `ebetica/recurse` unify goals, cadence loops, and CI watchers under a single `Monitor` primitive?

1. **Stdout-Driven Wakeup Over Polling Loops**:  
   - Because a `Monitor` is simply a background shell that wakes the Pi-Durable agent whenever a line is printed, a cadence loop is just a script printing on a timer, a CI watcher prints when a run status changes, and a goal monitor prints when a condition flips — eliminating polling turns completely.

---

### Q3: How does `dojo-video-harness` protect provider credentials and in-flight jobs during live configuration changes?

1. **Write-Only Browser Key Storage & Job-Pinned Config Snapshots**:  
   - Saved LLM and ASR keys are never echoed back to the browser client, and updating provider settings applies immediately to new requests while in-flight jobs retain the exact configuration they started with.

---

## 🧭 3. Architecture Decision Tree & Topology (Mermaid)

```mermaid
flowchart TD
    Start["Local Human-Agent Video Editing & Event-Woken Autonomous Coding Harness Selection"] --> Scenario{"Target Engineering Workflow?"}

    Scenario -->|"Collaborative Timeline Video Editing + Local Browser MP4 Export"| VideoGate{"Kernel & Privacy Requirement?"}
    VideoGate -->|"Tested Document/Command Kernel + Browser WebCodecs Export<br/>+ Shared Loop 0.1.3 Checkpoints"| UseDojo["✅ PansaLegrand/dojo-video-harness (MIT · TypeScript)<br/>• 0 DB / 0 Redis / 0 cloud worker; 0 API keys for manual NLE & export<br/>• Server-isolated credentials & job-pinned config snapshots"]
    VideoGate -->|"Headless batch transcoding only"| RawFFmpeg["🔄 Raw FFmpeg Script"]

    Scenario -->|"Long-Horizon Autonomous Coding with Background Builds & CI Watchers"| RecurseGate{"Wakeup & Subagent Mechanism?"}
    RecurseGate -->|"Auto-Backgrounding Shells + Output-Triggered Monitors<br/>+ Pi-Durable Worktree Multiagent Tree"| UseRecurse["✅ ebetica/recurse (MIT · Bun 1.4+ & Pi Durable)<br/>• Goals, loops & CI watchers implemented as simple Monitor skills<br/>• SSH-tunnelable :8787 web UI + async compaction & fffgrep"]
    RecurseGate -->|"Naive sleep-and-poll loop"| PollingLoop["⚠️ Polling Loop (High token burn)"]

    UseDojo --> FinOps["💰 Closed-Form FinOps Impact (CLAIM-20261114-R69-DOJOVIDEO-RECURSE)<br/>Monthly Total $5,000.00 ➔ $417.50 (-91.65% · Saves $54,990/yr)"]
    UseRecurse --> FinOps
```

---

## 📊 4. Peer Comparison Matrix (Decision Matrix)

| Evaluation Dimension | `PansaLegrand/dojo-video-harness` (Local WebCodecs NLE) | Cloud Video SaaS / Raw FFmpeg Chat | `ebetica/recurse` (Pi-Durable Monitor Harness) | Polling-Based TUI Agent Frameworks |
| :--- | :--- | :--- | :--- | :--- |
| **Core Control Primitive** | **Tested Document & Command Kernel + Shared Loop `0.1.3`** | Cloud queue or fragile LLM timestamp math | **Auto-background shells + stdout `Monitors` + `subagent.ts`** | Blocking shells or repetitive LLM polling turns |
| **Infra & Privacy Footprint** | **0 DB / 0 Redis / 0 cloud worker; browser WebCodecs MP4** | Uploads private video to paid cloud workers | **Single Bun process on Pi Durable; `:8787` SSH-friendly web UI** | Heavy multi-process RAM & brittle remote TUI rendering |
| **Resilience & Security** | **Durable checkpoints + write-only API keys + job config pinning** | Session drop loses unsaved timeline edits | **Interruption durability + async compaction + safety review** | Dropped SSH session kills background tasks |
| **License & Extensibility** | **MIT open-source; educational & production-ready NLE kernel** | Proprietary per-minute/seat SaaS | **MIT open-source; goals/loops/graphs built as lightweight skills** | Complex custom scheduler plugins |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261114-R69-DOJOVIDEO-RECURSE`)

> **Scope & Boundary Declaration**: This synthetic FinOps model covers monthly cloud video-render worker fees and polling-loop token spend across **35 video editing timelines and long-horizon monitor workflows** plus engineering labor for **timeline corruption fixes and interrupted build recovery** (at **`$95.00/hr`**); local workstation hardware depreciation is explicitly marked **`not_measured`**.

| Architecture Path | Cloud Render & Polling Spend (`USD/mo`) | Timeline Fix & Recovery Labor (`hrs/mo`) | Engineering Labor Cost (`@ $95/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Cloud Render SaaS + Polling Agent Loops** | `$1,580.00` | `36.0 hrs` | `$3,420.00` | **`$5,000.00`** | Baseline (`0.00%`) |
| **Path B: Raw FFmpeg Chat + Manual `tmux` Polling** | `$750.00` | `17.0 hrs` | `$1,615.00` | **`$2,365.00`** | `-$2,635.00` (`-52.70%`) |
| **Path C (Recommended): `Dojo Video` + `recurse` Monitors** | **`$85.00`** | **`3.5 hrs`** | **`$332.50`** | **`$417.50`** | **`-$4,582.50` (`-91.65%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 1580.00 + 36.0 \times 95.00 = 1580.00 + 3420.00 = \$5,000.00$
  - $\text{Path B Total} = 750.00 + 17.0 \times 95.00 = 750.00 + 1615.00 = \$2,365.00$
  - $\text{Path C Total} = 85.00 + 3.5 \times 95.00 = 85.00 + 332.50 = \$417.50$
  - $\text{Net Savings (Path C vs Path A)} = 5000.00 - 417.50 = \$4,582.50/\text{mo} \quad (-91.65\%, \text{Annualized } \$54,990.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect Actionable Checklist

1. **Launch `PansaLegrand/dojo-video-harness` locally on `:4310`**:
   ```bash
   git clone https://github.com/PansaLegrand/dojo-video-harness.git && cd dojo-video-harness
   npm run launch
   ```
2. **Install `ebetica/recurse` on Bun 1.4+ and replace polling loops with `Monitor` skills**:
   ```bash
   curl -fsSL https://github.com/ebetica/recurse/releases/latest/download/install.sh | bash
   recurse /path/to/repo
   ```
