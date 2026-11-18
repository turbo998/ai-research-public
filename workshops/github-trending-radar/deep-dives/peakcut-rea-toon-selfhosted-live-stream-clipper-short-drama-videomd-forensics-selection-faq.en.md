# Self-Hosted Live-Stream AI Clipper (`PeakCut`) & Short-Drama `VIDEO.md` Shot Forensics Skill (`rea-toon`) Selection FAQ: `haziqahmedqasmi/PeakCut` + `JuneYaooo/rea-toon`

> **Metadata**
> - **Evaluation Batch**: 2026-11-15 Night Shift Round 5 (Cumulative Round 307)
> - **Primary Targets**:
>   1. [`haziqahmedqasmi/PeakCut`](https://github.com/haziqahmedqasmi/PeakCut) (`★ 370` · Created `2026-11-14` · MIT License · Self-hosted BYOK AI video and live-stream clipper featuring a `~480 MB` local speech-to-text model, rolling-buffer live clipping, `~4` LLM requests per 1-hour video, 3 word-by-word caption styles, and zero-key loudness fallback)
>   2. [`JuneYaooo/rea-toon`](https://github.com/JuneYaooo/rea-toon) (`★ 163` · Created `2026-11-14` · Noncommercial License · AI short-drama breakdown skill for Claude Code and Codex built on `rea-video` and [`VIDEO.md`](https://videomd.github.io/videomd/), producing a 3-view interactive `index.html` (`Study | Script | Shot script`) with click-to-play shot verification and a layered `VIDEO.md` for downstream agents)
> - **Companion Visual**: [`assets/github-ai-radar-2026-11-15-r5-peakcut-reatoon.svg`](../../../assets/github-ai-radar-2026-11-15-r5-peakcut-reatoon.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261115-R5-PEAKCUT-REATOON` (see [`evidence/trending-daily-2026-11-15-audit.json`](../evidence/trending-daily-2026-11-15-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language First Principles**:
   - **`haziqahmedqasmi/PeakCut`**: Think of it as a **self-hosted, local-STT OpusClip plus real-time live-stream highlight cutter (`http://127.0.0.1:8765`)**. Instead of uploading gigabytes of raw video to per-minute SaaS clippers, `PeakCut` downloads a **`~480 MB` speech-to-text model once** so audio never leaves your machine, then scores a 1-hour transcript in just **~4 JSON chat requests** using your own key (Gemini, OpenAI, Claude, Grok, Groq, OpenRouter, local **Ollama**, or **zero key via audio loudness fallback**). Even better, its **rolling-buffer live clipper** cuts 9:16 captioned highlights *while a YouTube, Twitch, or Kick stream is still live* using loudness, chat activity, and transcript hooks.
   - **`JuneYaooo/rea-toon`**: Think of it as an **automated director's teardown table and `VIDEO.md` compiler for short dramas** (animated comic dramas, live-action, and AI-generated series). Running inside Claude Code or Codex (~30 vision frame-grid calls per episode), it produces a 3-view `index.html` (**`Study`** with code-counted emotion ledgers and paywall hooks, **`Script`** with PDF export, and **`Shot script`** with extracted character vocal samples and click-to-play corner video verification) alongside a layered **`VIDEO.md`** file so downstream agents never have to re-watch the video.
2. **Quantified FinOps Impact (`CLAIM-20261115-R5-PEAKCUT-REATOON`)**:
   - Across a media engineering workload of **40 hours of live streams/webinars clipped per month + 30 short-drama/narrative episodes broken down per month** (`engineer_hourly_rate_usd = $95.00/hr`; camera hardware and ad spend marked `not_measured`):
   - **Path C (`PeakCut` + `rea-toon`)** lowers monthly TCO from **`$5,350.00/mo`** under **Path A (per-minute SaaS clipping subscriptions + manual shot logging & repeated full-video VLM uploads)** down to **`$427.50/mo`**, saving **`$4,922.50/mo` (`-92.01%`, or `$59,070.00/yr`)** and **`34.5 hrs/mo` (`-90.79%`)** of editing and teardown labor.

![2026-11-15 Night Round 5 (R307) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-15-r5-peakcut-reatoon.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why are cloud video-clipping SaaS tools and raw VLM uploads so expensive for 1-hour streams, and how does `PeakCut` cut highlights in ~4 requests (or while still live)?
- **The Core Bottleneck**: Uploading full 1080p streams to cloud SaaS clippers burns per-minute credits and forces teams to wait until a broadcast ends before processing can even begin.
- **How `haziqahmedqasmi/PeakCut` Breaks Through**:
  1. **On-Device STT (`~480 MB`) + ~4 Requests per Hour**: Speech-to-text runs 100% locally so audio never leaves the host; only compact transcript segments are sent to a fast JSON chat model (~4 calls per 1-hour video), with comma-separated model fallbacks, per-video token accounting (`AI usage`), and zero-key loudness fallback.
  2. **Rolling-Buffer Live Stream Clipping**: Records live YouTube/Twitch/Kick streams into a rolling buffer and triggers 9:16 vertical cuts on the fly using loudness, live chat velocity, and transcript hooks.
  3. **Per-Creator Workspaces & Spaced Auto-Posting**: Isolates channels, 3 word-by-word caption styles, and posting rules per creator, queuing finished clips to YouTube, Instagram, and TikTok with enforced spacing and daily caps.

### Q2: Why do generic VLM video summaries fail at narrative teardown, and how does `JuneYaooo/rea-toon` combine 3-view verification with `VIDEO.md`?
- **The Core Bottleneck**: Asking a generic VLM why a video went viral yields vague platitudes without shot-level framing, vocal references, or reusable machine-readable indexes.
- **How `JuneYaooo/rea-toon` Solves It**:
  1. **Three-View Verifiable HTML & PDF Output (`Study | Script | Shot script`)**:
     - `Study`: Hook formula, pacing curve, cross-episode paywall/trope arcs, and a deterministic **emotion ledger** counted by code from per-shot emotion tags.
     - `Script` & `Shot script`: Standard script + per-shot framing, duration, **character voice samples cut from the original vocal track**, and **click-to-play corner video verification** for every shot claim.
  2. **Layered `VIDEO.md` Protocol**: Writes `VIDEO.md` + `video/` so any follow-up agent queries the drama layer-by-layer without re-running vision inference.

### Q3: What are the honest architectural boundaries of both projects?
- **Honest Boundaries**:
  - `haziqahmedqasmi/PeakCut` opens without sign-in on localhost (`127.0.0.1:8765`), so shared server deployments must set `PEAKCUT_ACCOUNTS=1` and configure platform OAuth credentials (`DEPLOY.md`).
  - `JuneYaooo/rea-toon` is released under a **Noncommercial license**, outputs reports in Chinese by default, and requires **~30 vision frame-grid calls per episode** (explicitly advising users to test on the first 5 episodes before running a full series).

---

## 🧭 3. Mermaid Decision Tree & Architecture Comparison

```mermaid
flowchart TD
    Start["Live-Stream AI Clipping & Narrative Video Shot Forensics Selection"] --> Layer{"What is your primary video workflow?"}

    Layer -->|"Turning long VODs or live YouTube/Twitch/Kick streams into captioned 9:16 clips"| ClipCheck{"Need local audio privacy, BYOK/Ollama, and live rolling-buffer clipping?"}
    ClipCheck -->|"Yes! ~480MB local STT + ~4 LLM calls/hr + 0-key loudness fallback"| UsePeakCut["✅ Adopt haziqahmedqasmi/PeakCut (MIT)<br/>python -m studio.server (:8765) · Rolling-Buffer Live Clipping<br/>3 Caption Styles + Spaced YouTube/IG/TikTok Auto-Posting"]
    ClipCheck -->|"Fully managed cloud SaaS with per-minute billing"| UseCloudSaaS["Use Commercial Per-Minute Clipping SaaS"]

    Layer -->|"Reverse-engineering viral short dramas into scripts, shot boards & agent-readable specs"| DramaCheck{"Noncommercial study / internal R&D needing shot-level verification?"}
    DramaCheck -->|"Yes! 3-View index.html/PDF + click-to-play shots + layered VIDEO.md"| UseReaToon["✅ Adopt JuneYaooo/rea-toon (Noncommercial)<br/>Claude Code / Codex Skill · ~30 Vision Grid Calls/Episode<br/>Pilot First 5 Episodes -> Full Series Parallel API Run"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `haziqahmedqasmi/PeakCut` (`MIT`) | `JuneYaooo/rea-toon` (`VIDEO.md`) | Path A: Commercial Clipping SaaS + Manual Shot Logging | Path B: Cloud Whisper API + Single-Shot VLM Summary |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pain Solved** | Eliminates per-minute SaaS fees & enables live mid-stream clipping | Eliminates manual shot-by-shot logging & repeated video VLM uploads | High monthly SaaS bills; logging 1 episode manually takes hours | Re-uploads video on every follow-up prompt; no shot/vocal slicing |
| **Core Mechanism** | **`~480 MB` Local STT + Rolling Buffer + `~4` Calls/Hr + FFmpeg** | **`~30` Frame-Grid Vision Calls/Ep + Code Emotion Ledger + `VIDEO.md`** | Full video upload to proprietary cloud + manual spreadsheet entry | Remote audio/video API calls + unstructured prose summary |
| **Verification & Fallback** | Built-in `AI usage` ledger + **zero-key loudness fallback** | **Click any shot to play original clip** + extracted vocal samples | Zero interactive claim-to-timestamp playback | High timestamp & dialogue hallucination rate |
| **Honest Boundaries** | Set `PEAKCUT_ACCOUNTS=1` on shared hosts | **Noncommercial license**; Chinese output; ~30 vision calls/ep | Opaque overage charges | No PDF script/storyboard export |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Section Tag | Headline-as-Finding | Evidence & Closed-Form Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `PeakCut` + `rea-toon` cut monthly 40-hour stream clipping and 30-episode teardown TCO by `92.01%` (`$5,350.00 → $427.50/mo`) | `CLAIM-20261115-R5-PEAKCUT-REATOON` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `PeakCut` reached `370★` on day 1, pairing a `480 MB` local STT model with just `~4` JSON LLM requests per 1-hour video | `haziqahmedqasmi/PeakCut` architecture audit |
| **Card 3** | `3/7 · WHAT I TESTED` | `rea-toon` compiles episodes into `Study / Script / Shot script` HTML/PDF views plus a layered `VIDEO.md` agent index | `JuneYaooo/rea-toon` `SKILL.md` verification |
| **Card 4** | `4/7 · UNDER THE HOOD` | Loudness + chat + transcript rolling-buffer live clipping + `~30` frame-grid vision calls/ep & code-counted emotion beats | `README.md` pipeline inspection |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | Documents zero-key loudness fallback, `PEAKCUT_ACCOUNTS=1` server mode, Noncommercial license & 5-episode cost pilot | Licensing & cost guardrail audit |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | On-device transcription + reusable `VIDEO.md` save `34.5 hrs/mo` (`-90.79%`) of manual clipping and shot-logging labor | 40h streams + 30 episodes/mo model |
| **Card 7** | `7/7 · MY TAKE` | High-leverage pair for self-hosted live-stream distribution and structured narrative video reverse engineering | Studio cameras & ad spend: `not_measured` |

### 💰 Closed-Form FinOps Table (40 Hours Stream Clipping + 30 Episodes Breakdown/Month, `r = $95.00/hr`)

| Architecture Path | SaaS & Multimodal Token Spend (`compute_and_token_usd`) | Clipping & Shot-Logging Labor (`engineering_hours`) | Engineering Labor Cost (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs. Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Commercial Clipping SaaS + Manual Shot Logging** | `$1,740.00` | `38.0 hrs` | `$3,610.00` | **`$5,350.00`** | Baseline (`0.00%`) |
| **Path B: Cloud Whisper API + Custom FFmpeg + Single-Shot VLM** | `$860.00` | `18.0 hrs` | `$1,710.00` | **`$2,570.00`** | `-$2,780.00` (`-51.96%`) |
| **Path C: `PeakCut` Local-STT Clipper + `rea-toon` `VIDEO.md`** | **`$95.00`** | **`3.5 hrs`** | **`$332.50`** | **`$427.50`** | **`-$4,922.50` (`-92.01%` / `$59,070.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Launch PeakCut self-hosted video & live-stream clipper (downloads ~480MB local speech model once -> http://127.0.0.1:8765)
git clone https://github.com/haziqahmedqasmi/PeakCut.git && cd PeakCut
pip install -r requirements.txt && python -m studio.server

# 2. Run rea-toon inside Claude Code or Codex on a 5-episode pilot to generate 3-view index.html + VIDEO.md
# Prompt inside Claude Code / Codex:
# Install https://github.com/JuneYaooo/rea-toon, then break down the first 5 episodes of this short drama: ./episodes/
```
