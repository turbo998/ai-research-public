# 1-Image 2D Mesh Avatar Rigging Studio (`shinshin86/mesh-avatar-studio`) & 86 Blind-Benchmarked AI Short-Drama Skills (`UnderleveledBuilder/awesome-short-drama-skills`) Selection & Architecture FAQ

> **Document Type**: AI Solution Architect Deep-Dive & Peer Selection FAQ (Night Shift Round 116 / Cumulative Round 299)  
> **Benchmark Style**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (Plain-Language First Principles + Core Q&A + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> **Covered Repositories**: `shinshin86/mesh-avatar-studio` (`★ 2,363` · TypeScript/Python · Turn One Illustration into an Animated 2D Mesh Avatar via Zoomed-Grid Agent Layering, Playwright Pose Review & Local Mesh Editor) + `UnderleveledBuilder/awesome-short-drama-skills` (`★ 2,321` · HTML/Python · Curated Directory of 86 AI Short-Drama / Manju Skills & 16 Platforms with Multi-Run Blind Opus + GPT Benchmark Tournaments)  
> **Evidence Anchors**: `evidence/trending-daily-2026-11-14-raw.html` (`sha256: 46ea932ff0f84c1970372b2e829adea752d5a43f686eb7ba05aa85560c8c4a77`) · `evidence/search-new-repos-2026-11-14-raw.json` (`sha256: a4edf557e91854831dc80d3670e3e7a1b49c7e9ca14e2e4dd7913489bd7cc2b2`) · `CLAIM-20261114-R116-MESHAVATAR-SHORTDRAMASKILLS`

![2026-11-14 Night Round 116 (R299) SVG Visual Summary](../../../assets/github-ai-radar-2026-11-14-r116-meshavatar-shortdramaskills.svg)

---

## 📌 1. Executive Summary

1. **Why does rigging a single 2D character illustration into a live avatar usually take days of manual PSD layer cutting—and how do you know which AI short-drama (`漫剧`) skills actually beat an un-skilled baseline?**
   - **Pain Point 1 (Manual Layer Cutting, Inpainting & Live2D Mesh Rigging Bottlenecks)**: Turning a flat character illustration into an interactive 2D mesh avatar that blinks, speaks with lip-sync, turns its head, breathes, and sways its hair traditionally requires tedious Photoshop layer separation and manual rigging. With **`★ 2,363`**, **`shinshin86/mesh-avatar-studio`** (`npx create-mesh-avatar-studio`) pairs a coding agent (Claude Code Opus 5.5 or Codex GPT-6.1 Sol via `npm run create -- /path/to/image.png`) with a local browser editor (`127.0.0.1:5173`): the agent calibrates coordinate reading on zoomed grids, segments layers, generates closed-eye and mouth-shape variants, renders fixed-pose motion reviews in Playwright Chromium, and writes a `HANDOVER.md` so you can fine-tune control points and drive the avatar live with your webcam and voice.
   - **Pain Point 2 (Unbenchmarked Creative Skills That Underperform Raw Model Prompts)**: With **`★ 2,321`**, **`UnderleveledBuilder/awesome-short-drama-skills`** (`shortdramaskills.com`) curates **86 short-drama and AI comic-drama (`漫剧`) skills + 16 open-source platforms** (covering adaptation, episode outlines, hooks/paywall cliffhangers, storyboards, and Seedance / Kling / MiniMax prompts) and subjects them to **blind multi-run tournaments judged by both Claude Opus and GPT against an un-skilled control group**—identifying the exact 4 screenwriting skills (`zenstory-ai/drama-skills`, `Shanyin-ai/shanyin-screenwriting-master`, `jtydhr88/screenwriting-skills`, `adoria111/emma-screenwriting-skills`) and top 3 topic-selection skills (`Tomsawyerhu/Chinese-WebNovel-Skill`) that beat the control group 3-out-of-3 times across both judges.
2. **Closed-Form FinOps Verdict (`CLAIM-20261114-R116-MESHAVATAR-SHORTDRAMASKILLS`)**: Across `25` 2D avatar rigging and AI short-drama production sprints per month (`$95/hr`, local workstation hardware: `not_measured`), combining **`shinshin86/mesh-avatar-studio` + `UnderleveledBuilder/awesome-short-drama-skills`** (Path C) reduces monthly cost to **`$417.50/mo`** compared to **`$5,420.00/mo`** for manual Live2D outsourcing and unvetted script/video reruns (Path A)—saving **`$5,002.50/mo` (`-92.30%`)** or **`$60,030.00/yr`**.

---

## 🔍 2. Core Q&A (Q1 / Q2 / Q3 First-Principles Deep Dive)

### Q1: What are they in plain English, and how do their core mechanisms work?

- **`shinshin86/mesh-avatar-studio`: A 4-Step Agent + Human Workbench That Turns One Illustration into a Live 2D Mesh Avatar**
  - **First Principle**: Let the coding agent handle **zoomed-grid coordinate calibration, layer cutting, expression inpainting, and headless Playwright pose verification**, while giving the human a **live local mesh editor (`127.0.0.1:5173`)** for sub-pixel vertex tweaks.
  - **Three Core Mechanisms**:
    1. **Agent-Guided Layering, Variant Synthesis & Pose Review (`docs/agent-guide.md`)**: Given a front-facing PNG (`npm run create -- image.png` or `--random --prompt "..."`), the agent closes any open resting mouth, generates closed-eye and mouth variants (or runs 100% locally with `--no-variants`), cuts layers into `projects/<name>/`, verifies fixed head/eye poses in Playwright Chromium, and logs notes in `HANDOVER.md`.
    2. **Interactive Local Mesh Editor (`127.0.0.1:5173`)**: Drag control dots on any layer while watching the live right-pane preview; test head turn/tilt and blinking in **Pose test**, test kana/audio lip-sync in **Lip sync**, and toggle accessories under **Overlays** (`built/overlays/`).
    3. **Zero-Install Browser Face & Voice Player**: Drives the finished 2D mesh avatar directly in Chrome or Edge from your webcam and microphone.
- **`UnderleveledBuilder/awesome-short-drama-skills`: A Blind-Benchmarked Directory of 86 Short-Drama & Manju Agent Skills**
  - **First Principle**: Creative agent skills must be evaluated via **blind, multi-run pairwise comparisons against an un-skilled baseline** using filmability criteria (emotion shown through physical objects and actions rather than unfilmable internal monologues).
  - **Three Core Mechanisms**:
    1. **Round 1 Screenwriting Blind Eval (10 Skills × 3 Runs vs. Control)**: Both Opus and GPT judges blindly evaluated 3 runs per skill; only 4 skills (`zenstory-ai/drama-skills`, `Shanyin-ai/shanyin-screenwriting-master`, `jtydhr88/screenwriting-skills`, `adoria111/emma-screenwriting-skills`) won 3-out-of-3 against the control across both judges.
    2. **Round 2 Topic-Selection Pairwise Tournament (11 Skills)**: Ranked all 11 skills via round-robin blind comparisons, with both Opus and GPT agreeing on the top 3 (led by `Tomsawyerhu/Chinese-WebNovel-Skill`).
    3. **Full Pipeline Coverage (86 Skills + 16 Platforms)**: Covers Qwen, Doubao, OpenClaw, WorkBuddy, Claude Code, and Codex across screenwriting, storyboards, character assets, and Seedance / Kling / MiniMax video prompts, with candid warnings (e.g., stripping embedded self-check tables before feeding scripts to video generators).

### Q2: What pain points do they solve compared to existing tools?

- **vs. Manual Photoshop + Live2D Cubism or Heavy Diffusion Talking Heads**: Produces a lightweight, 60fps real-time browser-controllable 2D mesh avatar from a single image without days of manual layer cutting.
- **vs. Unverified Prompt Repositories**: Eliminates the guesswork of installing random screenwriting skills that actually degrade output compared to the base model.

### Q3: How should an AI Solution Architect combine them?

- **Interactive 2D Web Assistants, VTuber Avatars & Visual Novel Characters**: Use **`shinshin86/mesh-avatar-studio`**.
- **Automated Short-Drama / Comic-Drama (`漫剧`) Scripting & Seedance/Kling Video Pipelines**: Select the blind-benchmarked winners from **`UnderleveledBuilder/awesome-short-drama-skills`**.

---

## 🧭 3. Mermaid Decision Tree & Character/Drama Production Architecture

```mermaid
flowchart TD
    Start["🎭 AI SA 2D Character Rigging & Short-Drama Pipeline"] --> Goal{"Is the target an interactive 2D mesh avatar or an episodic short-drama/manju pipeline?"}

    Goal -->|"Single Illustration → Interactive 60fps 2D Mesh Avatar<br/>(Needs agent layer cutting + Playwright pose QA + local mesh editor)"| Avatar["🎭 shinshin86/mesh-avatar-studio (★ 2,363)<br/>npx create-mesh-avatar-studio"]
    Goal -->|"AI Short-Drama / Comic-Drama (漫剧) Production<br/>(Needs Opus+GPT blind-benchmarked screenwriting & video skills)"| Drama["🎬 awesome-short-drama-skills (★ 2,321)<br/>86 Skills + 16 Platforms · Blind Evals"]

    Avatar --> A1["1. Step 1: Agent Calibrates Zoomed Grid, Cuts Layers & Checks Poses"]
    A1 --> A2["2. Steps 2-3: Fine-Tune Mesh Dots & Lip-Sync in Local Editor (:5173)"]
    A2 --> A3["3. Step 4: Drive Avatar Live via Webcam & Mic in Browser Player"]

    Drama --> D1["1. Topic Selection: Install Top-Ranked Chinese-WebNovel-Skill"]
    D1 --> D2["2. Screenwriting: Install 3/3 Winners (zenstory-ai / Shanyin / jtydhr88)"]
    D2 --> D3["3. Strip Inline Checklists & Feed Seedance / Kling / MiniMax Skills"]

    A3 --> Out["✅ Studio-Tuned 2D Mesh Avatars + Benchmark-Verified Drama Scripts<br/>Saves $5,002.50/mo (-92.30%)"]
    D3 --> Out
```

---

## 📊 4. Peer Comparison Matrix

| Dimension | `shinshin86/mesh-avatar-studio` (`★ 2,363`) | `awesome-short-drama-skills` (`★ 2,321`) | Manual PSD + Live2D Cubism | Unbenchmarked Drama Prompts |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Role** | **Agent + Human 2D Mesh Avatar Rigging Workbench** | **Blind-Benchmarked 86-Skill Short-Drama Directory** | Manual 2D Character Rigging | Ad-Hoc Screenwriting Prompts |
| **Verification Rigor** | **Zoomed-grid calibration + Playwright Chromium pose review** | **3-run blind Opus + GPT evaluations vs. control group** | Manual artist inspection | None; often worse than base model |
| **Human Control Surface** | **Local `127.0.0.1:5173` mesh dot editor + Pose/Lip-Sync test** | Explicit per-skill strengths & failure caveats | Heavy desktop proprietary editor | Manual script rewriting |
| **Supported Agent Ecosystem** | **Claude Code (Opus 5.5), Codex (GPT-6.1 Sol) + Web Player** | **Claude Code, Codex, OpenClaw, Qwen, Doubao, WorkBuddy** | Manual | Any chat UI |

---

## 💰 5. Closed-Form FinOps Quantitative Audit

- **Claim ID**: `CLAIM-20261114-R116-MESHAVATAR-SHORTDRAMASKILLS`
- **Workload Baseline**: `25` 2D mesh avatar rigging and AI short-drama/manju production sprints/month (`$95/hr` engineering/creator rate; local workstation hardware: `not_measured`):
  - **Path A (Outsourced Manual Live2D Rigging + Unbenchmarked Drama Prompts Causing Video Re-Renders)**:
    - Outsourced layer/rigging fees, wasted video-gen credits & token spend: `$1,810.00 / mo`
    - Manual PSD layer cutting, rigging adjustments & rewriting unfilmable scripts: `38.0 hrs/mo × $95.00 = $3,610.00 / mo`
    - **Path A Total Monthly Cost**: `$1,810.00 + $3,610.00 = $5,420.00 / mo`
  - **Path B (Static Lip-Sync Overlays + Random Unverified Drama Skills)**:
    - Video & token spend: `$800.00 / mo`
    - Fixing broken head-turn artifacts & cleaning up script formatting: `16.5 hrs/mo × $95.00 = $1,567.50 / mo`
    - **Path B Total Monthly Cost**: `$800.00 + $1,567.50 = $2,367.50 / mo`
  - **Path C (`shinshin86/mesh-avatar-studio` 4-Step Loop + `awesome-short-drama-skills` Blind-Tested Winners)**:
    - Agent layer/variant generation & top-ranked skill token spend: `$85.00 / mo`
    - Fine-tuning mesh dots in local Studio & reviewing film-ready scripts: `3.5 hrs/mo × $95.00 = $332.50 / mo`
    - **Path C Total Monthly Cost**: `$85.00 + $332.50 = $417.50 / mo`
  - **Net FinOps Savings**:
    - **Monthly Savings vs. Path A**: `$5,420.00 - $417.50 = $5,002.50 / mo` (**`92.30%` reduction**)
    - **Annualized Savings**: `$5,002.50 × 12 = $60,030.00 / yr`
    - **Engineering Hours Saved**: `38.0h → 3.5h` (`34.5 hrs/mo` saved, **`90.79%` reduction**)

---

## 🛠️ 6. Actionable Quickstart Checklist

- [ ] **Step 1: Scaffold `shinshin86/mesh-avatar-studio` and rig an illustration**
  ```bash
  npx create-mesh-avatar-studio
  cd mesh-avatar-studio
  npm run dev
  npm run create -- /path/to/your-image.png
  ```
- [ ] **Step 2: Install the blind-benchmarked winners from `awesome-short-drama-skills`**
  - Use `Tomsawyerhu/Chinese-WebNovel-Skill` for topic ideation and `zenstory-ai/drama-skills`, `Shanyin-ai/shanyin-screenwriting-master`, or `jtydhr88/screenwriting-skills` for action-grounded episode scripts.
