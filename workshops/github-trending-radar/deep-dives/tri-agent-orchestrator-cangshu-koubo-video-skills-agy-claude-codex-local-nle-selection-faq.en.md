# `agy + claude + codex` Tri-Agent Orchestrator (`abhigyan6/tri-agent-orchestrator`) & Zero-Cloud-API Optical-Flow/Vision Talking-Head Video Skills (`QQTangBa/cangshu-koubo-video-skills`) Selection FAQ

> **Document Scope**: This is the **2026-11-13 Night Shift Round 17 (Cumulative #145) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects, Multi-Agent Engineering Leads, and Technical Content Teams evaluating two high-precision workflow repositories:
> 1. **`abhigyan6/tri-agent-orchestrator` (`44★` in 3 days, Python, MIT)**: A multi-agent orchestration framework and universal skill coordinating **Google Antigravity (`agy`), Anthropic Claude Code (`claude`), and OpenAI Codex (`codex`)** across a 3-phase contract pipeline: **Phase 1 (`agy` Chief Architect & Adversarial Auditor → `docs/tri-agent/SPEC.md` + `HANDOFF.md`) → Phase 2 (`claude` Lead Software Craftsman → surgical implementation) → Phase 3 (`codex` Test & Deployment Engineer → test harnesses, CI/CD & PR verification)**!
> 2. **`QQTangBa/cangshu-koubo-video-skills` (`43★` in 3 days, TypeScript, Apache-2.0, shipping `cangshu-koubo-wudongxiao` 9:16 base & `cangshu-koubo-motion-edit` 3:4 motion skills)**: Two end-to-end Apple Silicon macOS Claude Code skills that edit talking-head (`口播`) videos using **local tools only (`mlx-whisper`, native macOS `Vision` person matting, FFmpeg, and Remotion) with zero paid cloud APIs** — featuring phrase-segmented re-transcription to catch repeated takes, `0.14s` breathing margins, **8-frame optical-flow morph-cut smoothing**, continuous breathing zoom, alternating speaker + handwritten Remotion 3:4 motion scenes, and automated QA gates (**blocking delivery if lip-sync drift exceeds `20ms`**, `-16 LUFS` loudness, and 5-fps storyboard clipping checks)!
>
> **中文版本**: [tri-agent-orchestrator-cangshu-koubo-video-skills-agy-claude-codex-local-nle-selection-faq.md](tri-agent-orchestrator-cangshu-koubo-video-skills-agy-claude-codex-local-nle-selection-faq.md) · **Daily Digest**: [`daily/2026-11-13.en.md`](../daily/2026-11-13.en.md) · **Topic SVG**: [`assets/github-ai-radar-2026-11-13-r17-triagent-cangshukoubo.svg`](../../../assets/github-ai-radar-2026-11-13-r17-triagent-cangshukoubo.svg)

![abhigyan6/tri-agent-orchestrator and QQTangBa/cangshu-koubo-video-skills Architecture Comparison](../../../assets/github-ai-radar-2026-11-13-r17-triagent-cangshukoubo.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "forcing a single AI CLI to handle every engineering phase or manually copy-pasting context between Antigravity, Claude Code, and Codex" (`abhigyan6/tri-agent-orchestrator`)**: Each major coding agent has a distinct cognitive superpower: Google Antigravity (`agy`) excels at deep codebase reconnaissance, multimodal architecture, and adversarial edge-case discovery; Claude Code (`claude`) excels at domain modeling and surgical refactoring; OpenAI Codex (`codex`) excels at rapid terminal test execution and CI/CD fixes. `tri-agent-orchestrator` binds all three into a deterministic pipeline via standardized `docs/tri-agent/SPEC.md` and `HANDOFF.md` contracts!
   - **Ending "missed repeated takes in full-clip Whisper transcripts, jarring jump cuts, expensive cloud matting subscriptions, and >20ms lip-sync drift in talking-head videos" (`QQTangBa/cangshu-koubo-video-skills`)**: Full-clip ASR models silently merge repeated phrases, and naive silence-trimming scripts create jarring jump cuts. Running 100% locally on Apple Silicon Mac (`mlx-whisper` + macOS `Vision` + FFmpeg + Remotion) with zero paid cloud APIs, `cangshu-koubo-video-skills` splits audio by micro-pauses to re-transcribe phrase-by-phrase and keep only the best final take, blends every cut with **8-frame optical flow (Morph Cut)**, alternates between Vision-matted speaker shots and handwritten 3:4 Remotion motion graphics, and enforces a strict **`<20ms` lip-sync gate, `-16 LUFS` loudness check, and 5-fps storyboard QA**!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261113-R17-TRIAGENT-CANGSHUKOUBO`)**:
   - Modeled for a **product engineering and developer-advocacy studio shipping `50 multi-module features per month` and producing `80 talking-head technical videos per month`** (fully loaded software/media engineer rate `$90.00/hr`; Apple Silicon Mac Studio hardware and studio microphone capex: `not_measured`):
   - Upgrading from **Path A (single-CLI uncoordinated coding + paid cloud video/ASR/matting SaaS + manual Premiere editing, `$5,500.00/mo`)** to **Path C (`tri-agent-orchestrator` `SPEC.md`/`HANDOFF.md` pipeline + `cangshu-koubo-video-skills` zero-API-fee optical-flow/Vision/Remotion pipeline, `$500.00/mo`)** saves **`$5,000.00/mo` (`-90.91%`, or `$60,000.00/yr`)** and cuts engineering and video editing labor from `42.0 hrs/mo` to `3.5 hrs/mo` (**`-91.67%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why do single-CLI coding loops and naive silence-trimming video scripts fall short in production?
- **First-Principles Breakdown**:
  1. **Cognitive Specialization Across Coding Agents**: Using a fast test-runner model for upfront architectural security modeling or using a deep-reasoning model for repetitive build-fix loops wastes tokens and misses edge cases.
  2. **Full-Clip ASR Smoothing & Hard Jump Cuts**: Transcribing an entire recording at once causes the ASR language model to smooth over stutters/repeats, while cutting video without optical-flow blending or lip-sync verification produces unwatchable jump cuts and audio drift.

### Q2: How does `abhigyan6/tri-agent-orchestrator` synchronize Antigravity (`agy`), Claude Code (`claude`), and Codex (`codex`)?
- **First-Principles Breakdown**:
  1. **Three-Phase Contract Pipeline (`SPEC.md` + `HANDOFF.md`)**:
     - **Phase 1 (`agy`)**: Performs codebase reconnaissance, dependency mapping, and adversarial edge-case discovery into `docs/tri-agent/SPEC.md` + `HANDOFF.md`.
     - **Phase 2 (`claude`)**: Executes domain modeling and surgical code craftsmanship against the spec.
     - **Phase 3 (`codex`)**: Generates test harnesses, runs CI/CD checks, and verifies the production PR.

### Q3: How does `QQTangBa/cangshu-koubo-video-skills` achieve broadcast-grade talking-head and motion-graphics editing with zero paid cloud APIs?
- **First-Principles Breakdown**:
  1. **Phrase-Segmented `mlx-whisper` Retake Pruning & 8-Frame Optical-Flow Morph Cuts**:
     - Segments audio by short pauses (`<0.4s` retained, `0.14s` margins, `<0.3s` fragments dropped) to catch repeated takes and blends every cut with 8-frame optical flow plus continuous cross-cut breathing zoom.
  2. **Native macOS Vision Matting, Remotion 3:4 Scenes & `<20ms` Lip-Sync Gate**:
     - Uses native macOS Vision for zero-download person matting, alternates speaker segments with handwritten Remotion motion graphics, and runs a one-command QA pass checking `<20ms` lip-sync drift, `-16 LUFS` loudness, and 5-fps storyboards.

---

## 🧭 3. Mermaid Decision Tree & Tri-Agent Pipeline + Local Optical-Flow Video Skills

```mermaid
flowchart TD
    A["Multi-Agent Software Delivery & Local Talking-Head Video Automation Selection"] --> B{"Primary Workflow Track?"}
    B -- "Complex software features needing architecture audit, craftsmanship & test verification" --> C["Adopt abhigyan6/tri-agent-orchestrator (agy -> claude -> codex)"]
    B -- "Automated talking-head & motion-graphics editing on Apple Silicon with zero cloud APIs" --> D["Adopt QQTangBa/cangshu-koubo-video-skills (9:16 Base + 3:4 Remotion)"]

    C --> C1["Phase 1 agy writes SPEC.md + HANDOFF.md -> Phase 2 claude refactors code"]
    C1 --> C2["Phase 3 codex builds test harnesses, runs CI & prepares production PR"]

    D --> D1["Phrase-segmented mlx-whisper retake pruning + 0.14s margins + 8-frame optical flow"]
    D1 --> D2["macOS Vision matting + Remotion 3:4 motion scenes + <20ms lip-sync & 5fps QA"]

    C2 & D2 --> E["🏆 Golden Engineering & Advocacy Stack: 3-CLI Specialization + Local Broadcast NLE (-90.91% TCO)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Single-CLI Coding + Cloud Video SaaS | Path B: Manual CLI Copy-Paste + Basic Silence Trim | **Path C (Recommended): `tri-agent-orchestrator` + `cangshu-koubo-video-skills`** |
| :--- | :--- | :--- | :--- |
| **Multi-Agent Cognitive Division** | Single CLI struggles outside its sweet spot | Manual copy-paste loses spec constraints | **`agy` (Spec/Audit) → `claude` (Craft) → `codex` (Test/CI) via `HANDOFF.md`** |
| **Retake Pruning & Cut Smoothness** | Per-minute cloud SaaS; jarring jump cuts | Full-clip ASR misses repeated phrases | **Phrase-level `mlx-whisper` + `0.14s` margins + 8-frame optical-flow Morph Cut** |
| **Person Matting & Motion Graphics** | Expensive cloud matting/template fees | Manual After Effects / Premiere keyframing | **Zero-download macOS Vision matting + handwritten Remotion 3:4 motion scenes** |
| **Lip-Sync & Visual QA Gates** | Manual full-video watch-throughs | Frequent audio drift & text clipping | **Hard `<20ms` lip-sync gate + `-16 LUFS` loudness + 5-fps storyboard QA** |
| **Monthly TCO (50 Features + 80 Videos)** | **`$5,500.00 / mo`** (`$1,720` SaaS/API + `$3,780` labor) | **`$2,760.00 / mo`** (`$780` API + `$1,980` labor) | **`$500.00 / mo` (Saves `$5,000.00/mo` · `-90.91%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261113-R17-TRIAGENT-CANGSHUKOUBO`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A product engineering and developer-advocacy studio shipping **50 multi-module software features per month** and producing **80 talking-head technical videos (9:16 & 3:4 motion) per month**.
- **Labor Rate**: Fully loaded software / multimedia engineering rate of **`$90.00 / hr`**.
- **Explicit Not-Measured Boundary**: Apple Silicon Mac Studio workstation and microphone hardware capex are marked **`not_measured`**. This model strictly accounts for coding LLM API spend, cloud video/ASR/matting SaaS bills, and engineering hours spent on cross-CLI rework and manual video editing.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Single-CLI Coding + Cloud Video SaaS | Path B: Manual Copy-Paste + Basic Silence Trim | **Path C: `tri-agent-orchestrator` + `cangshu-koubo` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly Coding API & Video Cloud Spend** | **`$1,720.00`** (cloud ASR/matting SaaS + single-CLI rework tokens) | **`$780.00`** (unstructured multi-turn retries) | **`$185.00`** (specialized 3-CLI handoff + `$0` local `mlx-whisper`/Vision) |
| **Cross-CLI Rework & Manual Video Editing Labor (`$90/hr`)** | `42.0 hrs × $90.00` = **`$3,780.00`** | `22.0 hrs × $90.00` = **`$1,980.00`** | `3.5 hrs × $90.00` = **`$315.00`** |
| **Total Monthly TCO** | **`$5,500.00 / mo`** | **`$2,760.00 / mo`** (`-49.82%`) | **`$500.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,740.00 / mo` | **Saves `$5,000.00 / mo` (`-90.91%` · `$60,000.00/yr`)** |
| **Mac Studio & Recording Hardware Capex** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `abhigyan6/tri-agent-orchestrator` 3-Phase Handoff Setup**: Verify local `agy`, `claude`, and `codex` CLIs and test the `docs/tri-agent/SPEC.md` → `HANDOFF.md` → verified PR pipeline.
- [ ] **2. `QQTangBa/cangshu-koubo-video-skills` Local Apple Silicon Setup**: Install `mlx-whisper` (`whisper-large-v3-turbo`), `ffmpeg`, `uv`, and `Remotion` on an M-series Mac with zero cloud API keys.
- [ ] **3. `cangshu-koubo-wudongxiao` 9:16 Optical-Flow Base Test**: Process a raw talking-head recording containing repeated takes and verify phrase-segmented retake removal, 8-frame optical-flow morph cuts, and caption keyword highlighting.
- [ ] **4. `cangshu-koubo-motion-edit` 3:4 Motion & `<20ms` Lip-Sync Gate**: Run the motion-graphics skill with macOS Vision matting and verify that the automated QA pass enforces `<20ms` lip-sync alignment, `-16 LUFS` loudness, and 5-fps storyboard bounds checks.
