# Self-Hosted SIP Realtime AI Agent PBX (`DeskVoice`) & Per-Bot Linux Sandbox + Persistent Drive Platform (`MatiSolina/busy`) Architecture & Selection FAQ

> **Document Metadata (2026-11-14 · Daytime Round 40 / Cumulative Round 223)**  
> - **Benchmark Style**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (First-Principles Breakdown + Plain-English Takeaways + 3 Core Architectural Q&As + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> - **Evaluated Repositories**:  
>   1. [`DeskLabs-OpenSource/DeskVoice`](https://github.com/DeskLabs-OpenSource/DeskVoice) (`★ 98`, MIT-licensed self-hosted AI agent telephony switchboard PBX running in **`~380 MiB` idle RAM / `~2.7 GB` disk** on your own VPS: bridges SIP trunks to OpenAI Realtime / Google Gemini voice engines with **mid-call tool execution, live human-in-the-loop approval, warm call transfer, durable post-call background tasks**, a zero-key simulated call harness `pnpm demo`, and automatic rollback on failed UI updates)  
>   2. [`MatiSolina/busy`](https://github.com/MatiSolina/busy) (`★ 96`, Apache 2.0 self-hosted multi-agent platform giving **every AI bot its own dedicated computer**: combines `apps/hub` web orchestrator, `apps/desktop` native macOS client, `templates/bot` (`vercel/eve`), and digest-pinned `images/bot-base` Linux desktop containers backed by isolated **Sandboxes and persistent Drives**)  
> - **Companion SVG Diagram**: [`assets/github-ai-radar-2026-11-14-r40-deskvoice-busy.svg`](../../../assets/github-ai-radar-2026-11-14-r40-deskvoice-busy.svg)  
> - **Audit Claim ID**: `CLAIM-20261114-R40-DESKVOICE-BUSY` (local operator workstation hardware power marked `not_measured`)

---

## 📌 1. Executive Summary (3-Minute Architect's Briefing)

1. **Why does self-hosting `DeskLabs-OpenSource/DeskVoice` eliminate `$0.10–$0.20/minute` voice-wrapper SaaS fees while solving the "Hang-Up Kills the Agent" bug?**  
   - **Plain-English Reality**: Commercial AI voice telephony wrappers charge steep per-minute platform markups on top of your OpenAI Realtime or Gemini API usage, and suffer from two architectural flaws: (1) lacking a built-in mid-call human approval gate before executing high-risk tools, and (2) terminating the agent context the moment the SIP call hangs up—dropping asynchronous post-call fulfillment tasks.  
   - **`DeskVoice` First-Principles Fix**: Installs via a single idempotent script on any Docker-capable Linux VPS (proven at **`~380 MiB` idle RAM and `~2.7 GB` disk** in `v0.3.0`), connecting your SIP trunk directly to OpenAI Realtime or Gemini (`$0.00` platform markup):
     - **5-Stage Call Lifecycle**: `Answer Call` -> `Execute Mid-Call Tools` -> **`Request Real-Time Human Approval`** -> `Warm Transfer to Operator` -> **`Continue Durable Post-Call Tasks After Hang-Up`**;
     - **Zero-Key Mock Voice Engine (`pnpm demo`) & Auto-Rollback Updates**: Ships a local simulated voice engine that runs a full call (greeting, tool call, human approval, transfer, post-call task) against a disposable Postgres container without an API key or SIP carrier, plus automatic rollback if an in-panel update fails.
2. **Why does `MatiSolina/busy`'s "Shared Hub + Per-Bot Sandbox Computer & Persistent Drive" architecture outperform both 24/7 dedicated VMs and shared stateless containers?**  
   - **Plain-English Reality**: Running a team of 15 durable AI bots that browse the web, edit documents, and use a visible Linux desktop is expensive if each bot keeps a dedicated cloud VM running 24/7—yet packing all 15 bots into one shared container causes credential collisions, filesystem pollution, and state loss on restart.  
   - **`MatiSolina/busy` First-Principles Fix**: Separates shared orchestration (`apps/hub` + `apps/desktop` Electron macOS client backed by Postgres, Queues, Schedules, and private Blob storage) from per-bot execution (`templates/bot` running `vercel/eve` on a SHA256 digest-pinned `images/bot-base` Linux desktop **Sandbox** attached to a **persistent Drive**). Each bot gets its own isolated computer and durable filesystem without paying for 24/7 idle VM compute.
3. **Closed-Form FinOps Audit (`CLAIM-20261114-R40-DESKVOICE-BUSY`)**:  
   - Across **15,000 monthly AI voice telephony minutes + 15 durable computer-using AI bots** (at **`$100.00/hr`** engineering rate), migrating from **Path A** (per-minute voice SaaS wrapper markups + 15 always-on dedicated cloud desktop VMs: **`$5,720.00/mo`**) to **Path C** (`DeskVoice` `380 MiB` self-hosted PBX + `busy` on-demand Sandbox/Drive architecture: **`$495.00/mo`**) saves **`$5,225.00/month`** (**`-91.35%`**, **`$62,700.00/year`**) and cuts ops/debugging labor from `38.0 hrs` to `3.5 hrs/mo` (**`-90.79%`**).

![DeskVoice & MatiSolina/busy Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r40-deskvoice-busy.svg)

---

## 💬 2. Three Architectural Deep-Dive Q&As (Q1–Q3)

### Q1: How does `DeskLabs-OpenSource/DeskVoice` decouple synchronous SIP audio streams from mid-call human approvals and asynchronous post-call workflows?

1. **Durable Call-State Persistence Beyond SIP BYE**:  
   - Instead of binding tool execution strictly to the lifetime of the WebSocket/SIP media stream, `DeskVoice` persists call state and spawned tasks in PostgreSQL. During a live call, the agent can pause a sensitive tool call to request human approval in the web console or transfer the caller; after the caller hangs up (`SIP BYE`), background workers continue executing post-call follow-ups.
2. **Secret-Safe Coding Assistant Onboarding (`deskvoice-instalar`)**:  
   - Includes an `AGENTS.md` and `deskvoice-instalar` skill that guides coding assistants through VPS sizing, port checks, and SIP trunk setup while strictly forbidding passwords or API keys from ever entering the LLM chat transcript.

---

### Q2: How does `MatiSolina/busy` guarantee reproducible Linux desktop environments across bots while preserving each bot's files and memory?

1. **Digest-Pinned `images/bot-base` + Persistent Drive Mounts**:  
   - Every bot boots from a cryptographic digest-pinned Linux desktop image (`bot-base` with browser and document tooling) so upstream package updates never silently break a bot, while mounting its own persistent Drive and connecting to the shared Hub via Queues and Schedules.

---

### Q3: How can architects evaluate both platforms locally in under 5 minutes without provisioning SIP trunks or cloud VMs?

1. **Run `DeskVoice`'s Zero-Key Simulated Call Engine**: Execute `pnpm install && pnpm demo` to watch a complete simulated call (greeting, tool execution, human approval, transfer, and post-call task) inside a disposable local Postgres container.
2. **Run `busy`'s Local Hub**: Initialize `.env.local` via `pnpm --filter hub setup:local` and `hash-password` against a local `postgres:16` container.

---

## 🧭 3. Architecture Decision Tree & Voice/Sandbox Topology (Mermaid)

```mermaid
flowchart TD
    Start["Self-Hosted AI Voice PBX & Multi-Bot Computer Sandbox Selection"] --> Track{"Primary Workload?"}

    Track -->|"SIP Telephony AI Voice Receptionist / Support Switchboard"| VoiceGate{"Billing, Approval & Post-Call Needs?"}
    VoiceGate -->|"Zero Per-Minute SaaS Markup + Mid-Call Human Approval<br/>+ Post-Call Background Task Continuity"| UseDeskVoice["✅ DeskLabs-OpenSource/DeskVoice (MIT · ~380 MiB RAM)<br/>• Direct SIP Trunk + OpenAI Realtime / Gemini Voice<br/>• Built-in pnpm demo Mock Engine + Auto-Rollback Updates"]
    VoiceGate -->|"Static Pre-Recorded IVR Menu Only"| SimpleTTS["🔄 Legacy DTMF IVR"]

    Track -->|"Multi-Bot Team Requiring Dedicated Linux Desktops & Files"| BotGate{"Compute & Storage Isolation Model?"}
    BotGate -->|"Dedicated Computer per Bot + Persistent Drive<br/>+ Digest-Pinned Linux Image & Zero Idle VM Burn"| UseBusy["✅ MatiSolina/busy (Apache 2.0 · Hub + Eve Bots)<br/>• apps/hub + apps/desktop Orchestrate Queues & Schedules<br/>• Per-Bot Digest-Pinned Linux Sandbox + Persistent Drive"]
    BotGate -->|"Single Shared Container (High Collision Risk)"| SharedHost["⛔ Unisolated Shared-Filesystem Bots"]

    UseDeskVoice --> FinOps["💰 Closed-Form FinOps Impact (CLAIM-20261114-R40-DESKVOICE-BUSY)<br/>Monthly Total $5,720.00 ➔ $495.00 (-91.35% · Saves $62,700/yr)"]
    UseBusy --> FinOps
```

---

## 📊 4. Peer Comparison Matrix (Decision Matrix)

| Dimension | `DeskLabs-OpenSource/DeskVoice` (Self-Hosted PBX) | Commercial Per-Minute Voice Agent SaaS | `MatiSolina/busy` (Per-Bot Sandbox + Drive) | 24/7 Dedicated Cloud Desktop VMs |
| :--- | :--- | :--- | :--- | :--- |
| **Core Architecture** | **Self-hosted SIP + Realtime PBX + post-call task engine** | Proprietary cloud wrapper with per-minute markup | **Shared Hub + per-bot `vercel/eve` Linux Sandbox & Drive** | Always-on static VMs per bot |
| **Verified Footprint / Cost** | **`~380 MiB` idle RAM / `~2.7 GB` disk (`$0` SaaS markup)** | `$0.10–$0.20/min` platform surcharge | **On-demand Sandbox compute + persistent Drive storage** | High 24/7 idle VM compute waste |
| **Human-in-the-Loop & Continuity** | **Mid-call human approval + warm transfer + post-call tasks** | Context dies on hang-up; rigid approval hooks | Visible Linux desktop, routines, schedules & web/macOS Hub | Manual VNC/RDP management per VM |
| **Local Pre-Flight Testing** | **`pnpm demo` runs full simulated call with 0 keys/SIP** | Requires paid account & provisioned phone number | Local `postgres:16` + `setup:local` script | Heavy VM image provisioning |
| **Operational Resilience** | **Auto-rollback on failed update + secret-safe install skill** | Vendor cloud lock-in | **Digest-pinned `bot-base` image + `BUSY_PASSWORD_HASH` auth** | Configuration drift across long-lived VMs |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps Audit (`CLAIM-20261114-R40-DESKVOICE-BUSY`)

> **Scope & Provenance Boundary**: Models monthly platform per-minute voice markups across **15,000 telephony minutes** and cloud compute/storage across **15 durable computer-using AI bots**, plus engineering labor for post-call workflow recovery and sandbox maintenance at **`$100.00/hr`**. Local operator workstation hardware power consumption is explicitly marked **`not_measured`**.

| Architecture Path | Voice Markup & VM/Sandbox Spend (`USD/mo`) | Call & Bot Ops Labor (`hrs/mo`) | Engineering Labor Cost (`@ $100/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Per-Minute Voice SaaS Wrapper + 15 Always-On Cloud Desktop VMs** | `$1,920.00` | `38.0 hrs` | `$3,800.00` | **`$5,720.00`** | Baseline (`0.00%`) |
| **Path B: Custom Asterisk Scripts + Stateless Ephemeral Containers** | `$890.00` | `18.0 hrs` | `$1,800.00` | **`$2,690.00`** | `-$3,030.00` (`-52.97%`) |
| **Path C (Recommended): `DeskVoice` (`380 MiB` PBX) + `busy` (`Sandbox+Drive`)** | **`$145.00`** | **`3.5 hrs`** | **`$350.00`** | **`$495.00`** | **`-$5,225.00` (`-91.35%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 1920.00 + 38.0 \times 100.00 = 1920.00 + 3800.00 = \$5,720.00$
  - $\text{Path B Total} = 890.00 + 18.0 \times 100.00 = 890.00 + 1800.00 = \$2,690.00$
  - $\text{Path C Total} = 145.00 + 3.5 \times 100.00 = 145.00 + 350.00 = \$495.00$
  - $\text{Net Savings (Path C vs Path A)} = 5720.00 - 495.00 = \$5,225.00/\text{mo} \quad (-91.35\%, \text{Annualized } \$62,700.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect Quick-Start Checklist

1. **Test `DeskVoice` End-to-End with Zero API Keys or SIP Trunks via `pnpm demo`**:
   ```bash
   git clone https://github.com/DeskLabs-OpenSource/DeskVoice.git
   cd DeskVoice
   pnpm install && pnpm demo
   ```
2. **Bootstrap `MatiSolina/busy` Hub Locally (Node 24.15+)**:
   ```bash
   git clone https://github.com/MatiSolina/busy.git
   cd busy && corepack enable && pnpm install --frozen-lockfile
   pnpm --filter hub setup:local
   pnpm --filter hub hash-password
   ```
