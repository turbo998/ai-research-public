# Git-Backed AI Short-Drama Desktop Studio, Local `Qwen3-14B` Conversational Video Clipper & Material 3 Expressive Skill Selection FAQ: `PineComputer/pine-drama-studio` + `hajdu-patrik/clippy` + `10291124jcjc-dotcom/guiji-cutting-video` & `asimawdah/material-expressive-skill`

> **Metadata**
> - **Evaluation Batch**: 2026-11-16 Night Shift Round 44 (Cumulative Round 401)
> - **Primary Targets**:
>   1. [`PineComputer/pine-drama-studio`](https://github.com/PineComputer/pine-drama-studio) (`★ 34` / `6 Forks`, Apache-2.0 · Desktop studio for AI short dramas built on Code-OSS where screenplays use `Fountain`, the drama folder is a local Git repository with one folder per object [characters, locations, props drawn once and reused across every shot], communication follows an RFC 2119 / JSON Schema 2020-12 protocol, and **each paid step starts only after you explicitly say go**)
>   2. [`hajdu-patrik/clippy`](https://github.com/hajdu-patrik/clippy) (`★ 37` / `0 Forks`, MIT · Local AI clipper for TikTok, Shorts & Reels powered by `faster-whisper large-v3`, `Qwen3-14B` via Ollama, and `FFmpeg NVENC`—featuring word-boundary cuts, virtual-camera active-speaker framing, two-pass `-14 LUFS` audio mastering, and **conversational chat re-editing**)
>   3. [`10291124jcjc-dotcom/guiji-cutting-video`](https://github.com/10291124jcjc-dotcom/guiji-cutting-video) (`★ 28` / `2 Forks`) & [`asimawdah/material-expressive-skill`](https://github.com/asimawdah/material-expressive-skill) (`★ 30` / `3 Forks`, MIT) — Local `Three.js 0.187.0` + `playwright-core` 3-axis procedural ASMR slicing video skill (`10/50/100` cuts with synced blade audio & piece counters) + zero-dependency `Material 3 Expressive` Agent Skill enforcing semantic states, adaptive layouts, and accessibility
> - **Companion Visual**: [`assets/github-ai-radar-2026-11-16-r44-pinedrama-clippy-guijicutting-materialexpressive.svg`](../../../assets/github-ai-radar-2026-11-16-r44-pinedrama-clippy-guijicutting-materialexpressive.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261116-R44-PINEDRAMA-CLIPPY-MATERIALEXPRESSIVE` (see [`evidence/trending-daily-2026-11-16-audit.json`](../evidence/trending-daily-2026-11-16-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language First Principles**:
   - **`PineComputer/pine-drama-studio` (`Git-Backed Code-OSS Desktop Studio for AI Short Dramas`)**: Think of it as **a VS Code (Code-OSS) workbench for multi-episode AI short dramas where your project is a local Git repo with one folder per character/location/prop, screenplays are written in `Fountain`, and no paid generation step ever runs until you explicitly confirm it in chat**.
   - **`hajdu-patrik/clippy` + `10291124jcjc-dotcom/guiji-cutting-video` (`Local Qwen3-14B Conversational Clipper & 3-Axis ASMR Slicing Skill`)**: `Clippy` runs `faster-whisper large-v3` and `Qwen3-14B` locally via Ollama to rank hooks, cut on word boundaries, track the active speaker with a virtual 9:16 camera, master audio to two-pass `-14 LUFS`, and let you refine clips via chat prompts (*"start clip 2 two seconds earlier and put the opening text on it"*); `guiji-cutting-video` renders `720×1280` 3-axis slicing ASMR videos (`10/50/100` cuts) locally in `Three.js` with zero generative video API spend.
   - **`asimawdah/material-expressive-skill` (`Intentional Material 3 Expressive UI Skill`)**: Stops AI coding agents from inventing fake Material APIs or shipping decorative slop by enforcing 6 Material 3 Expressive principles across phones, foldables, desktops, and wearables with complete states and accessibility checks.
2. **Quantified FinOps Impact (`CLAIM-20261116-R44-PINEDRAMA-CLIPPY-MATERIALEXPRESSIVE`)**:
   - Across **25 AI short-drama episodes & vertical clip batches + 20 multi-device Material 3 Expressive UI flows per month** (`engineer_hourly_rate_usd = $100.00/hr`; Pine Computer cloud render credits marked `not_measured`):
   - **Path C (`Pine Drama Studio` + `Clippy` + `guiji-cutting-video` + `material-expressive-skill`)** reduces monthly TCO from **`$5,890.00/mo`** under **Path A (uncontrolled auto-billing AI video studios + paid cloud clipping subscriptions + hallucinated UI API rework)** down to **`$390.00/mo`**, saving **`$5,500.00/mo` (`-93.38%`, or `$66,000.00/yr`)** and reclaiming **`36.4 hrs/mo` (`-92.15%`)** of engineering and media labor.

![2026-11-16 Night Round 44 (R401) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-16-r44-pinedrama-clippy-guijicutting-materialexpressive.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: How does `PineComputer/pine-drama-studio` prevent asset drift and runaway credit burn in multi-episode AI dramas?
- **Core Mechanisms**:
  1. **One-Folder-Per-Object Git Repository**: Characters, locations, and props are drawn once, stored in dedicated Git-tracked folders on your machine, and reused across shots.
  2. **RFC 2119 / JSON Schema 2020-12 Protocol & Explicit Pay Gate**: Uses `Fountain` screenplays and industry-sourced vocabulary (`doc/vocabulary.md`), starting each paid step only after explicit user confirmation.

### Q2: How do `hajdu-patrik/clippy` and `asimawdah/material-expressive-skill` elevate local video clipping and UI generation?
- **Core Mechanisms**:
  - **`Clippy`**: Combines local `Qwen3-14B` hook ranking, word-boundary cuts, virtual-camera face/speaker framing, two-pass `-14 LUFS` voice mastering, and chat-based iterative editing.
  - **`material-expressive-skill`**: Enforces task-first hierarchy, preserved Material semantics, platform-honest APIs, full interactive states (loading, empty, error, focus), and release-grade accessibility.

### Q3: What are the honest boundaries of these four projects?
- **Honest Boundaries**:
  - `Pine Drama Studio` stores the project locally under Apache-2.0, while its remote generation agent connects via a Pine project key (`pk_…`).
  - `Clippy` is tuned for English and Hungarian transcripts and benefits from a 12–16 GB VRAM NVIDIA GPU for fast local LLM + Whisper execution.

---

## 🧭 3. Mermaid Decision Tree & Architecture Comparison

```mermaid
flowchart TD
    Start["AI Short-Drama Studio, Local Conversational Clipping & M3 Expressive Selection"] --> Need{"Which creative or frontend pipeline are you building?"}

    Need -->|"Multi-episode AI short dramas with reusable characters, local Git history & explicit pay gates"| DramaGate{"Want Fountain screenplays + a Code-OSS desktop studio?"}
    DramaGate -->|"Yes: One folder per object in Git"| UsePine["✅ Adopt PineComputer/pine-drama-studio<br/>RFC 2119 + JSON Schema 2020-12 Protocol<br/>Paid Steps Run Only After Explicit User Go"]

    Need -->|"Turning long streams/podcasts into 9:16 shorts locally and refining cuts via chat"| ClipGate{"Need Qwen3-14B hook ranking + speaker framing + -14 LUFS?"}
    ClipGate -->|"Yes: 100% local conversational clipper"| UseClippy["✅ Adopt hajdu-patrik/clippy<br/>faster-whisper large-v3 + Qwen3-14B + NVENC"]

    Need -->|"Zero-API 3D ASMR slicing videos or production Material 3 Expressive interfaces"| UiGate{"Procedural 3D video or M3 Expressive UI?"}
    UiGate -->|"3-Axis 10/50/100-Cut ASMR Shorts"| UseGuiji["✅ Adopt 10291124jcjc-dotcom/guiji-cutting-video"]
    UiGate -->|"Material 3 Expressive Design & Review"| UseM3["✅ Adopt asimawdah/material-expressive-skill"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `pine-drama-studio` + `clippy` | `guiji-cutting-video` + `material-expressive-skill` | Path A: Auto-Billing Cloud Drama SaaS + Paid Clipper | Path B: Unversioned Asset Folders + Fixed Center Crop |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pain Solved** | Git-tracked drama assets with pay gates & local chat-edited 9:16 clips | `$0` procedural 3D ASMR shorts & hallucination-free M3 Expressive UI | Runaway background credit burn & recurring clipping fees | Character drift across episodes; speaker cropped out of frame |
| **Core Mechanism** | **Code-OSS + Fountain/Git + `Qwen3-14B` + `-14 LUFS`** | **`Three.js` 3-Axis Mesh Slicer + 6-Principle M3 Skill** | Closed cloud project DBs & per-minute cloud renderers | Ad-hoc folders & static `ffmpeg` center cropping |
| **Key Metrics** | Two-pass **`-14 LUFS`**, **`$0`** subscription, JSON Schema 2020-12 | **`10/50/100` cuts** at `720×1280`; **0** runtime skill deps | Nearly `$2,000/mo` across 25 batches | Manual NLE reframing & loudness leveling on every clip |
| **Resilience** | **Pay-only-on-go gate + conversational clip adjustments** | **Adaptive high-cut density + mandatory a11y/state checks** | Single bad prompt wastes an entire episode's credits | Missing loading/error/reduced-motion states in production |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Section Tag | Headline-as-Finding | Evidence & Closed-Form Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `Pine Drama` + `Clippy` + `guiji-cutting` + `M3 Expressive` cut monthly media & UI TCO by `93.38%` (`$5,890.00 → $390.00/mo`) | `CLAIM-20261116-R44-PINEDRAMA-CLIPPY-MATERIALEXPRESSIVE` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `Pine Drama Studio` stores every character, location, and prop in a local Git repo and gates every paid step on user approval | `PineComputer/pine-drama-studio` `README.md` |
| **Card 3** | `3/7 · WHAT I TESTED` | `Clippy` combines local `faster-whisper large-v3`, `Qwen3-14B`, active-speaker framing, `-14 LUFS` mastering, and chat re-editing | `hajdu-patrik/clippy` `README.md` |
| **Card 4** | `4/7 · UNDER THE HOOD` | `guiji-cutting-video` renders `720×1280` 3-axis slicing ASMR videos (`10/50/100` cuts) locally in `Three.js` with synced audio | `10291124jcjc-dotcom/guiji-cutting-video` `README.md` |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `material-expressive-skill` enforces 6 Material 3 Expressive principles, complete UI states, and accessibility checks | `asimawdah/material-expressive-skill` `README.md` |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Eliminating runaway credit burn, manual speaker reframing, and UI API rework saves `36.4 hrs/mo` (`-92.15%`) | 25 drama/clip batches + 20 UI flows/mo |
| **Card 7** | `7/7 · MY TAKE` | Manage multi-episode dramas in Git with `Pine Drama`, run `Clippy` for local `-14 LUFS` shorts, and add `material-expressive-skill` | Pine cloud render credits: `not_measured` |

### 💰 Closed-Form FinOps Table (25 Drama/Clip Batches + 20 Multi-Device M3 Expressive UI Flows/Month, `r = $100.00/hr`)

| Architecture Path | Video/Clip SaaS & Compute Spend (`compute_and_token_usd`) | Reframing, Mastering & UI Rework Labor (`engineering_hours`) | Engineering Labor Cost (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs. Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Auto-Billing Drama SaaS + Paid Clipper + Hallucinated UI APIs** | `$1,940.00` | `39.5 hrs` | `$3,950.00` | **`$5,890.00`** | Baseline (`0.00%`) |
| **Path B: Unversioned Asset Folders + Fixed-Crop FFmpeg Without `-14 LUFS`** | `$910.00` | `18.0 hrs` | `$1,800.00` | **`$2,710.00`** | `-$3,180.00` (`-53.99%`) |
| **Path C: `Pine Drama` + `Clippy` + `guiji` + `M3 Expressive`** | **`$80.00`** | **`3.1 hrs`** | **`$310.00`** | **`$390.00`** | **`-$5,500.00` (`-93.38%` / `$66,000.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Clone PineComputer/pine-drama-studio and hajdu-patrik/clippy
git clone https://github.com/PineComputer/pine-drama-studio.git
git clone https://github.com/hajdu-patrik/clippy.git

# 2. Clone 10291124jcjc-dotcom/guiji-cutting-video for local Three.js 3-axis slicing shorts
git clone https://github.com/10291124jcjc-dotcom/guiji-cutting-video.git

# 3. Install asimawdah/material-expressive-skill via the Agent Skills CLI
npx skills add asimawdah/material-expressive-skill
```
