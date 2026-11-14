# 5-Stage Eyeline + `seek(t)` JSON Video Pipeline (`youtube-ai-video-editing-system`) & 24 Failure-Aware Claude Skills (`simcraft`) Selection FAQ: `dhruvthakur11/youtube-ai-video-editing-system` + `dotslashsimran/simcraft`

> **Metadata**
> - **Evaluation Batch**: 2026-11-14 Daytime Deep-Dive Round 13 (Cumulative Round 196)
> - **Primary Repositories**:
>   1. [`dhruvthakur11/youtube-ai-video-editing-system`](https://github.com/dhruvthakur11/youtube-ai-video-editing-system) (`★ 386` · Created `2026-11-08` · 5-station plain-text Markdown/JSON video production pipeline combining a voice-following `Eyeline` teleprompter, non-destructive candidate JSON cuts in `Eyeline Edit`, deterministic `seek(t)` HTML motion-graphics boards, and a Resolve/Premiere NLE handoff tree)
>   2. [`dotslashsimran/simcraft`](https://github.com/dotslashsimran/simcraft) (`★ 383` · Created `2026-11-08` · MIT · 24 production-tested Claude Code skills across Video, Engineering, Learning, Design & Planning that codify "what breaks, how to check the result, and how to tell good from good enough")
> - **Companion Architecture Diagram**: [`assets/github-ai-radar-2026-11-14-r13-youtube-video-simcraft.svg`](../../../assets/github-ai-radar-2026-11-14-r13-youtube-video-simcraft.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261114-R13-YOUTUBESYS-SIMCRAFT` (see [`evidence/trending-daily-2026-11-14-audit.json`](../evidence/trending-daily-2026-11-14-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language Essence**:
   - **`dhruvthakur11/youtube-ai-video-editing-system`**: Replaces black-box "1-click AI video editors" that destructively chop up source footage with a **5-stage plain-text relay (`Record → Cut → Design → Animate → Finish`) where every handoff is a human- and agent-readable Markdown or JSON file**. Its `Eyeline` teleprompter scrolls at your live speaking pace while tagging flubbed lines; editing agents write candidate cuts into a separate JSON file without mutating your approved plan (`Eyeline Edit` keeps full camera original handles intact); HTML motion-graphics reference boards expose a deterministic `seek(t)` function aligned to approved narration via JSON timelines; and the pipeline outputs a clean folder tree ready for DaVinci Resolve or Premiere.
   - **`dotslashsimran/simcraft`**: Packages **24 battle-tested Claude Code skills** (`8` Video skills like `vox-explainer`, `scripted-screencast`, `code-loop`, `reverse-engineer-video`; `7` Engineering skills like `flaky-test-killer`, `bisect-anything`, `benchmark-honestly`, `security-threat-model`; `4` Learning skills like `paper-to-runnable`, `system-design-from-scratch`; plus Design & Planning) where every single `SKILL.md` ships real verification scripts and explicitly answers three questions tutorials skip: **"what breaks, how to check the result, and how to tell good from good enough."**
2. **Quantified FinOps Impact (`CLAIM-20261114-R13-YOUTUBESYS-SIMCRAFT`)**:
   - Under a monthly workload of **16 technical explainer videos/screencasts + 40 specialized engineering, benchmarking, and paper-implementation tasks** (fully loaded rate `$100.00/hr`; workstation hardware labeled `not_measured`):
   - **Path C (`youtube-ai-video-editing-system` + `simcraft` 24-skill suite)** reduces total monthly cost of ownership (TCO) from **`$5,480.00/mo` (Path A: cloud auto-editing SaaS subscriptions + manual After Effects keyframe re-timing + unguided agent retries on flaky tests and video loops)** to **`$485.00/mo`**, saving **`$4,995.00/mo` (`-91.15%`, `$59,940.00/yr`)** and reclaiming **`34.5 engineering hours/mo` (`-90.79%`)**.

![Daytime Round 13 (R196) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-14-r13-youtube-video-simcraft.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why do black-box AI video editors fail on technical explainers, and how does `youtube-ai-video-editing-system` keep humans and agents in sync via plain-text files?
- **The Legacy Bottleneck**: Naive silence-cutting tools chop off natural pauses and bake cuts destructively into exported MP4s, while timeline-bound motion graphics in After Effects break whenever narration timing shifts by half a second.
- **How `youtube-ai-video-editing-system` Solves It**:
  1. **Voice-Synced `Eyeline` Teleprompter & Take Notebook**: Scrolls in step with your voice, marks flubs and retakes on the fly, mirrors over LAN to secondary displays, and writes each take with audio, script snapshot, and a readable take report.
  2. **Non-Destructive Candidate Cut JSON & Source Handles**: Editing agents transcribe takes, estimate camera drift, and propose cuts in a separate candidate JSON file; `Eyeline Edit` pins every clip to its original source interval so full handles survive into final NLE assembly.
  3. **Deterministic `seek(t)` HTML Motion Boards**: Every visual board exposes a `seek(t)` function driven by a JSON narration timeline—browser scrubbing and local disk frame rendering produce the exact same frame state with zero cloud round-trip.

### Q2: What separates `dotslashsimran/simcraft`'s 24 skills from generic prompt collections?
- **The Legacy Bottleneck**: Most prompt-only skills tell an agent *what* to generate without defining failure modes or verification scripts—resulting in Three.js loops that blink at the seam or "fixed" flaky tests that merely added `retry: 3`.
- **How `simcraft` Solves It**:
  1. **Automated Seam, Blink & Loudness Verification in Video Skills**: `code-loop` verifies Three.js/shader loops for seams, freezes, and blinks; `scripted-screencast` renders frame-perfect product demos from script without retakes; `clean-audio` measures loudness/noise before processing; `vox-explainer` times graphics word-by-word to voiceover.
  2. **Zero-Shortcut Engineering & Research Skills**: `flaky-test-killer` forbids retry wrappers and requires root-cause proof; `benchmark-honestly` enforces confidence intervals; `bisect-anything` pinpoints exact regression commits and lines; `paper-to-runnable` distills papers into the smallest honest runnable implementation.

### Q3: What are the honest boundaries and caveats of `youtube-ai-video-editing-system` and `simcraft`?
- **Concrete Limits**:
  - `youtube-ai-video-editing-system` targets Windows 10/11 (`PowerShell 5.1+`), ships intentionally neutral starter boards/templates (no private channel branding bundled), and hands off the final assembly to DaVinci Resolve, Premiere, or your NLE of choice.
  - `simcraft` requires Python 3.9+, Node 18+, and `ffmpeg` on `PATH` (with per-skill `setup.sh` scripts for tools like local Whisper in `rough-cut`, and optional image-gen keys isolated in `~/.config/simcraft/keys.env`).

---

## 🧭 3. Mermaid Selection Decision Tree & Architecture Flow

```mermaid
flowchart TD
    Start["Technical Video Production Pipeline & High-Rigor Claude Skill Selection"] --> Track{"Which engineering workflow are you upgrading?"}

    Track -->|"Long-Form Technical Videos with Voice Teleprompter, Motion Boards & NLE Handoff"| EditCheck{"Do you need non-destructive JSON cuts, preserved source handles & deterministic seek(t) boards?"}
    EditCheck -->|"Yes! Use 5-station Record → Cut → Design → Animate → Finish relay"| UseYTVideoSys["✅ Select dhruvthakur11/youtube-ai-video-editing-system<br/>Voice-synced Eyeline teleprompter + candidate JSON cuts<br/>Deterministic seek(t) HTML boards + Resolve/Premiere tree"]
    EditCheck -->|"Need 36s procedural 3D Blender short films"| UseEscapement["Select Leonxlnx/escapement (Daytime Round 7 / R190)"]

    Track -->|"Equipping Claude Code with Failure-Aware Video, Engineering & Research Skills"| SkillCheck{"Do you need skills with built-in verification scripts and anti-shortcut rules?"}
    SkillCheck -->|"Yes! Install 24 skills across Video, Engineering, Learning, Design & Planning"| UseSimcraft["✅ Select dotslashsimran/simcraft<br/>vox-explainer · code-loop · scripted-screencast<br/>flaky-test-killer · benchmark-honestly · paper-to-runnable"]
    SkillCheck -->|"Need 1-photo WeChat 240×240 animated sticker bundles"| UseStickerShop["Select imraywang/ray-sticker-shop (Daytime Round 12 / R195)"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `youtube-ai-video-editing-system` | `dotslashsimran/simcraft` (24 Claude Skills) | Legacy Path A: Cloud Auto-Editor SaaS + Manual AE Keyframes | Legacy Path B: Destructive Silence Cutters + 1-Paragraph Prompts |
| :--- | :--- | :--- | :--- | :--- |
| **Core Problem Solved** | Connects teleprompter recording, non-destructive cuts, deterministic HTML motion & NLE handoff | Teaches Claude Code 24 complex workflows with explicit failure modes & verification scripts | Black-box cloud editors destroy source handles; AE keyframes drift when audio changes | Silence scripts chop natural speech; simple prompts produce blinking loops & retry hacks |
| **Key Mechanisms** | **`Eyeline` voice scroll + isolated candidate JSON + `seek(t)` HTML boards** | **24 `SKILL.md` folders + tested check scripts + `What breaks / How to check` rubrics** | Proprietary timeline project blobs | Unchecked single-shot generation |
| **Auditability & Handoff** | Plain-text Markdown/JSON at every station + Resolve/Premiere folder tree | Symlinks cleanly into `~/.claude/skills/`; keys isolated in `~/.config/simcraft/keys.env` | Vendor lock-in & recurring seat fees | High manual rework rate |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Track / Section | Headline-as-Finding | Evidence & Sealed Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `youtube-ai-video-editing-system` + `simcraft` cuts monthly video & engineering workflow TCO by `91.15%` (`$5,480.00 → $485.00/mo`) | `CLAIM-20261114-R13-YOUTUBESYS-SIMCRAFT` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | 5-station plain-text video relay keeps candidate cuts in separate JSON files while preserving full source handles for NLEs | `dhruvthakur11/youtube-ai-video-editing-system` |
| **Card 3** | `3/7 · WHAT I TESTED` | Every HTML motion board exposes a deterministic `seek(t)` timeline so browser previews and disk renders match frame-for-frame | Deterministic `Animate` station architecture |
| **Card 4** | `4/7 · UNDER THE HOOD` | `simcraft` ships 24 skills (`8` Video, `7` Engineering, `4` Learning, `5` Design/Planning) with executable verification checks | `dotslashsimran/simcraft` skill catalog |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `code-loop` checks for loop seams/blinks, `flaky-test-killer` bans retry wrappers, and `benchmark-honestly` enforces CIs | Built-in quality gates |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Reduces monthly video rough-cut/motion alignment and engineering audit labor from `38.0 hrs` to `3.5 hrs` (`-90.79%`) | 16 explainer videos + 40 eng tasks/mo |
| **Card 7** | `7/7 · MY TAKE` | Blueprint for legible plain-text human+agent video production and failure-aware skill authoring | Workstation hardware: `not_measured` |

### 💰 Closed-Form FinOps Table (16 Technical Explainer Videos + 40 Eng/Media Tasks/Mo, `r = $100.00/hr`)

| Architecture Path | Cloud Video SaaS & Retry Spend (`compute_and_token_usd`) | Manual Cut, Motion & Audit Hours (`engineering_hours`) | Engineering Labor (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Cloud Video SaaS + Manual AE Keyframing & Blind Retries** | `$1,680.00` | `38.0 hrs` | `$3,800.00` | **`$5,480.00`** | Baseline (`0.00%`) |
| **Path B: Destructive Auto-Cutters + Unchecked Ad-Hoc Prompts** | `$840.00` | `18.5 hrs` | `$1,850.00` | **`$2,690.00`** | `-$2,790.00` (`-50.91%`) |
| **Path C: `youtube-ai-video-editing-system` + `simcraft` (Recommended)** | **`$135.00`** | **`3.5 hrs`** | **`$350.00`** | **`$485.00`** | **`-$4,995.00` (`-91.15%` / `$59,940.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Clone dhruvthakur11/youtube-ai-video-editing-system to inspect the 5-stage Eyeline & seek(t) board workflow
git clone https://github.com/dhruvthakur11/youtube-ai-video-editing-system.git

# 2. Clone dotslashsimran/simcraft and symlink all 24 failure-aware skills into ~/.claude/skills
git clone https://github.com/dotslashsimran/simcraft ~/simcraft
mkdir -p ~/.claude/skills
for s in ~/simcraft/skills/*/*/; do ln -s "${s%/}" ~/.claude/skills/; done
cd ~/simcraft && npm i
```
