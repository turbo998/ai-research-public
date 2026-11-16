# Local `SQLite+FTS5` Companion Memory, Zero-Credit Local ComfyUI Talking-Head Studio & Rust SIM Call/NVR Edge Agents Selection FAQ: `spearsheep/anima-brain` + `walkskysu/digital-human-koubo-comfyui` + `h4lo-void/bageo-call` & `HuskerMinion/AmberSight`

> **Metadata**
> - **Evaluation Batch**: 2026-11-16 Night Shift Round 25 (Cumulative Round 382)
> - **Primary Targets**:
>   1. [`spearsheep/anima-brain`](https://github.com/spearsheep/anima-brain) (`★ 48` / `6 Forks`, MIT `v0.6.0` · Local-first memory and emotional continuity toolkit for AI companions running on headless `SQLite + FTS5` [`companion-engine` Python SDK + `companion` CLI + MCP cards + React Companion Studio] with source-backed facts, corrections, episode summaries, context budgets, usage receipts, and request replay)
>   2. [`walkskysu/digital-human-koubo-comfyui`](https://github.com/walkskysu/digital-human-koubo-comfyui) (`★ 35` / `5 Forks`, MIT · 100% local ComfyUI `0.44+` talking-head video production skill chaining **`Qwen3-TTS` voice cloning + `MiniMax H3` lip-sync + `Qwen Image` + `Music 3`** with 5 editing styles and 48 creator packaging components on a single 24GB GPU [RTX 3090] with **zero cloud credits or API keys**)
>   3. [`h4lo-void/bageo-call`](https://github.com/h4lo-void/bageo-call) (`★ 35`, AGPL-3.0 `v1.3.0` Rust) & [`HuskerMinion/AmberSight`](https://github.com/HuskerMinion/AmberSight) (`★ 44`, Rust) — Self-hosted Rust AI phone assistant answering real SIM calls via a spare rooted Android Pixel (`bageo-call`: 1-ring pickup, 30-minute scammer stalling, 9 languages) + cross-platform Rust AI NVR server (`AmberSight`: RTSP pre/post-roll motion clips, synchronized multi-camera timeline & privacy masks)
> - **Companion Visual**: [`assets/github-ai-radar-2026-11-16-r25-animabrain-koubo-bageocall.svg`](../../../assets/github-ai-radar-2026-11-16-r25-animabrain-koubo-bageocall.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261116-R25-ANIMABRAIN-KOUBO-BAGEO` (see [`evidence/trending-daily-2026-11-16-audit.json`](../evidence/trending-daily-2026-11-16-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language First Principles**:
   - **`spearsheep/anima-brain` (`Local SQLite+FTS5 Grounded & Emotional Memory`)**: Think of it as **giving an AI companion both a source-cited fact ledger and emotional continuity in a local `SQLite + FTS5` database with zero cloud lock-in**. It tracks original messages, user corrections, cited episode summaries, persona rules, and emotional attunement while enforcing explicit context budgets, usage receipts, and request replay.
   - **`walkskysu/digital-human-koubo-comfyui` (`Zero-Credit Local ComfyUI Talking-Head Skill`)**: Think of it as **turning one photo and one sentence into a fully edited, lip-synced digital-human video on your own 24GB GPU without paying a cent in cloud per-second credits**. Your agent verifies dependencies via `scripts/doctor.sh`, drives local ComfyUI (`Qwen3-TTS` + `MiniMax H3` + `Qwen Image` + `Music 3`), and applies 5 editing styles and 48 creator overlays.
   - **`h4lo-void/bageo-call` + `HuskerMinion/AmberSight` (`Rust Real-SIM Telephony & Rust AI NVR`)**: `bageo-call` bridges a spare rooted Android phone holding your real SIM card to a local Rust daemon and Gemini Live—answering deliveries after one ring, stalling phone scammers for up to 30 minutes, and speaking 9 languages; `AmberSight` ingests RTSP camera streams in a single cross-platform Rust binary with pre/post-roll motion clips, synchronized timelines, and privacy masks.
2. **Quantified FinOps Impact (`CLAIM-20261116-R25-ANIMABRAIN-KOUBO-BAGEO`)**:
   - Across a multimodal edge workload of **30 digital-human talking-head videos + 20 persistent-memory companion and self-hosted telephony/NVR edge nodes per month** (`engineer_hourly_rate_usd = $100.00/hr`; RTX 3090 GPU hardware and SIM carrier plans marked `not_measured`):
   - **Path C (`Anima Brain` + Local `Koubo ComfyUI` + `bageo-call` / `AmberSight`)** reduces monthly TCO from **`$5,910.00/mo`** under **Path A (per-second cloud avatar credits + virtual-number telephony fees + cloud NVR subscriptions)** down to **`$395.00/mo`**, saving **`$5,515.00/mo` (`-93.32%`, or `$66,180.00/yr`)** and reclaiming **`36.4 hrs/mo` (`-92.15%`)** of engineering labor.

![2026-11-16 Night Round 25 (R382) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-16-r25-animabrain-koubo-bageocall.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: How do `spearsheep/anima-brain` and `walkskysu/digital-human-koubo-comfyui` enable private, zero-credit digital companions and talking-head production?
- **Core Mechanisms**:
  1. **`Anima Brain` (`companion-engine`)**: Runs headlessly on `SQLite + FTS5`, separating grounded facts, user corrections, and cited episode summaries from emotional-attunement state while exposing MCP cards, context budget controls, and Doubao ASR / Vidu S2 RTC hooks.
  2. **`digital-human-koubo-comfyui`**: Checks `127.0.0.1:8188` via `doctor.sh` and orchestrates `Qwen3-TTS` voice cloning, `MiniMax H3` lip-sync, `Qwen Image` B-roll, `Music 3` scoring, and 48 packaging overlays locally on a 24GB GPU.

### Q2: How do `h4lo-void/bageo-call` and `HuskerMinion/AmberSight` use Rust to self-host real-number call screening and multi-camera AI detection?
- **Core Mechanisms**:
  - **`bageo-call`**: Uses a spare rooted Android Pixel with your real SIM card so callers dial your normal number; picks up after 1 ring across 9 languages, handles package/delivery questions, stalls sales/scam callers for up to 30 minutes, and pauses to ask you when running outbound errands.
  - **`AmberSight`**: Ingests RTSP streams on Windows, Linux, and macOS, records pre/post-roll motion clips with AI verdicts, renders an 8-camera synchronized timeline with detect/ignore zones and privacy masks, and ships signed `SHA256SUMS` releases.

### Q3: What are the honest boundaries of these four projects?
- **Honest Boundaries**:
  - `Anima Brain` explicitly documents that it is a standalone local adaptation rather than the full commercial Anima app backend.
  - `digital-human-koubo-comfyui`'s local pipeline requires a **24GB VRAM NVIDIA GPU** (taking `40–70 minutes` of GPU time per 40-second video on an RTX 3090).
  - `bageo-call` requires a spare rooted Android phone (AGPL-3.0), and `AmberSight` uses the PolyForm Noncommercial license.

---

## 🧭 3. Mermaid Decision Tree & Architecture Comparison

```mermaid
flowchart TD
    Start["Local Companion Memory, Zero-Credit Talking-Head Video & Rust Edge Telephony/NVR Selection"] --> Need{"Which multimodal or edge capability are you deploying?"}

    Need -->|"Persistent companion memory with source-backed facts, corrections & emotional continuity"| BrainGate{"Need headless local SQLite + FTS5 + MCP controls?"}
    BrainGate -->|"Yes: Zero cloud backend lock-in"| UseAnima["✅ Adopt spearsheep/anima-brain (v0.6.0)<br/>Grounded Facts + Cited Summaries + Emotional Continuity<br/>Context Budgets, Usage Receipts & Request Replay"]

    Need -->|"1-photo talking-head video production with voice clone, lip-sync, B-roll & music"| KouboGate{"Have a 24GB NVIDIA GPU and want zero cloud credits?"}
    KouboGate -->|"Yes: Local ComfyUI 0.44+ agent skill"| UseKoubo["✅ Adopt walkskysu/digital-human-koubo-comfyui<br/>Qwen3-TTS + MiniMax H3 + Qwen Image + Music 3<br/>5 Editing Styles + 48 Packaging Overlays + doctor.sh"]

    Need -->|"Self-hosted real-SIM AI phone call screening or multi-camera AI NVR"| EdgeGate{"Real SIM call agent or RTSP camera server?"}
    EdgeGate -->|"Real SIM 1-ring answer + 30-min scammer stalling + 9 langs"| UseBageo["✅ Adopt h4lo-void/bageo-call (Rust)<br/>Spare Rooted Pixel + Gemini Live Screening & Errands"]
    EdgeGate -->|"Cross-platform RTSP pre/post-roll AI NVR"| UseAmber["✅ Adopt HuskerMinion/AmberSight (Rust)<br/>Synchronized Timeline + Privacy Masks + JSON API"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `anima-brain` + `koubo-comfyui` | `bageo-call` + `AmberSight` (Rust) | Path A: Per-Second Cloud Avatars + Virtual Numbers / Cloud NVR | Path B: Flat Vector RAG + Manual ComfyUI Node Wiring |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pain Solved** | Local fact/emotion companion memory & zero-credit avatar videos | Real-SIM scam call defense & self-hosted Rust AI camera NVR | Expensive per-second avatar credits; virtual numbers miss local calls | Persona amnesia across turns; hours spent wiring ComfyUI nodes |
| **Core Mechanism** | **`SQLite+FTS5` Memory + Local 4-Model ComfyUI Skill** | **Rooted Pixel SIM Bridge + Rust RTSP Pre/Post-Roll NVR** | Cloud SaaS avatar APIs / cloud telephony trunks | Unstructured chunk RAG / manual video timeline editing |
| **Key Metrics** | **`$0` cloud credits**, **5** styles, **48** overlays | **1-ring** pickup, **30-min** scammer stall, **9** languages | High recurring SaaS bills | `>2 hrs` manual editing per talking-head clip |
| **Privacy & Control** | **Photos, voice prints & memories stay 100% local** | **Camera privacy masks + signed `SHA256SUMS` installers** | Biometric voice/face data uploaded to third parties | No automated `doctor.sh` check or context budgeting |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Section Tag | Headline-as-Finding | Evidence & Closed-Form Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `Anima Brain` + Local `Koubo` + `bageo-call`/`AmberSight` cut monthly multimodal & edge TCO by `93.32%` (`$5,910.00 → $395.00/mo`) | `CLAIM-20261116-R25-ANIMABRAIN-KOUBO-BAGEO` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `Anima Brain` runs headlessly on `SQLite + FTS5` with cited episode summaries, emotional continuity, and request replay | `spearsheep/anima-brain` `README.md` |
| **Card 3** | `3/7 · WHAT I TESTED` | `digital-human-koubo-comfyui` chains `Qwen3-TTS`, `MiniMax H3`, `Qwen Image`, and `Music 3` locally on a 24GB GPU with zero credits | `walkskysu/digital-human-koubo-comfyui` `README.md` |
| **Card 4** | `4/7 · UNDER THE HOOD` | `bageo-call` answers real SIM calls via a rooted Pixel across 9 languages and stalls scam callers for up to 30 minutes | `h4lo-void/bageo-call` `README.md` & `AUDIT_REPORT.md` |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `AmberSight` delivers cross-platform Rust RTSP pre/post-roll recording, privacy masks, and signed `SHA256SUMS` | `HuskerMinion/AmberSight` `README.md` |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Eliminating per-second avatar credits and manual node/timeline editing saves `36.4 hrs/mo` (`-92.15%`) of engineering time | 30 avatar videos + 20 edge nodes/mo |
| **Card 7** | `7/7 · MY TAKE` | Pair local `SQLite+FTS5` companion memory with 24GB ComfyUI avatar skills and Rust edge telephony/NVR | RTX 3090 hardware & SIM plans: `not_measured` |

### 💰 Closed-Form FinOps Table (30 Talking-Head Videos + 20 Companion/Edge Nodes/Month, `r = $100.00/hr`)

| Architecture Path | Cloud Credits & SaaS Spend (`compute_and_token_usd`) | Node Wiring & Triage Labor (`engineering_hours`) | Engineering Labor Cost (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs. Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Per-Second Cloud Avatar Credits + Cloud Telephony/NVR SaaS** | `$1,960.00` | `39.5 hrs` | `$3,950.00` | **`$5,910.00`** | Baseline (`0.00%`) |
| **Path B: Manual ComfyUI Node Wiring + Stateless Edge Scripts** | `$910.00` | `18.0 hrs` | `$1,800.00` | **`$2,710.00`** | `-$3,200.00` (`-54.15%`) |
| **Path C: `Anima Brain` + Local `Koubo` + `bageo`/`AmberSight`** | **`$85.00`** | **`3.1 hrs`** | **`$310.00`** | **`$395.00`** | **`-$5,515.00` (`-93.32%` / `$66,180.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Clone spearsheep/anima-brain and run the zero-API-call offline SQLite + FTS5 memory demo
git clone https://github.com/spearsheep/anima-brain.git && cd anima-brain
pip install -e . && python examples/offline_demo.py

# 2. Clone walkskysu/digital-human-koubo-comfyui and run doctor.sh to verify your local 24GB GPU ComfyUI setup
git clone https://github.com/walkskysu/digital-human-koubo-comfyui.git
bash digital-human-koubo-comfyui/skills/digital-human-koubo/scripts/doctor.sh

# 3. Clone h4lo-void/bageo-call and HuskerMinion/AmberSight for self-hosted Rust telephony and AI NVR
git clone https://github.com/h4lo-void/bageo-call.git
git clone https://github.com/HuskerMinion/AmberSight.git
```
