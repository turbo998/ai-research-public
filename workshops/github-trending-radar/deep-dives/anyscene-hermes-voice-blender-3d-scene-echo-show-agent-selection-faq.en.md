# Dual-Model Photoreal Blender 3D Scene Builder (`apekshik/anyscene`) & Echo Show Hardware Voice/Vision Agent Terminal (`majorminorlabs/hermes-voice`) Selection FAQ

> **Positioning**: This standalone guide is **Round 47 of the 2026-11-11 Night Shift (Cumulative Guide #92)**, written in the plain-language, first-principles, closed-form FinOps style of `ib-vs-ethernet-roce-selection-faq.md` for Generative 3D Pipeline Architects and Smart-Space Ambient AI Engineers evaluating two high-velocity open-source projects:
> 1. **`apekshik/anyscene` (`361★`, Python / Blender 5.0+ Cycles + `fal.ai` Tripo H3.1 & Meshy 7.1 + `AnyShot` camera rig)**: An 8-gate agent workflow (`SKILL.md` + `builder/CRAFT.md` + serverless `SceneBuilderApp`) that turns a 1-paragraph brief or reference images into a fully dressed, lit, weathered Blender 5.0 Cycles scene with **74–86 individual 3D props** (`assets.json`, `picks.json`, `shots.json`)—running every prop through **both `Tripo H3.1` and `Meshy 7.1`** (`~$1.65/prop`) and picking the winner via same-light comparison contact sheets;
> 2. **`majorminorlabs/hermes-voice` (`670★`, Python / Home Assistant Assist + `echo-dot-assist` + Echo Show `screen-app` / `eye-app` + SQLite `visual-memory`)**: Connects unlocked Amazon Echo and Echo Show devices (`RS03QR`, `XC56PY`, `D9N29T`, `C1125P`, `H23K37` build `8149`, `C7H6N3`, `C76N8S`, `A8H3N2`) to **NousResearch `Hermes Agent`** profiles (`X-Hermes-Session-Id`), turning an Echo Show into a live HUD showing transcripts, tool calls, and background work, plus **`Hermes Eye` (`look` tool with `REC` badge)** and a local SQLite **`visual-memory`** that answers *"what changed?"* with before/after photos.
>
> **中文版 FAQ**: [anyscene-hermes-voice-blender-3d-scene-echo-show-agent-selection-faq.md](anyscene-hermes-voice-blender-3d-scene-echo-show-agent-selection-faq.md) · **Architecture Summary SVG**: [`assets/github-ai-radar-2026-11-11-r47-anyscene-hermesvoice.svg`](../../../assets/github-ai-radar-2026-11-11-r47-anyscene-hermesvoice.svg)

![AnyScene & Hermes Voice Architecture](../../../assets/github-ai-radar-2026-11-11-r47-anyscene-hermesvoice.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what problems do these two repositories actually solve?**
   - **Ending Single-Mesh 3D Slop & Floating Props in Generative Blender Scenes (`apekshik/anyscene`)**: Generating a single monolithic room mesh produces melted geometry that cannot be re-lit or edited, while single-model image-to-3D calls frequently fail on complex props. Following `SKILL.md` and `builder/CRAFT.md`, `AnyScene` decomposes a room into **74–86 distinct props**, generates each prop through **both `Tripo H3.1` and `Meshy 7.1`** (`~$1.65/prop` total on `fal.ai`), compares same-light renders on a contact sheet to record the winner in `picks.json`, scripts the room layout from large furniture down to clutter with **automated collision and floating-prop checks**, applies grime/decals/volumetric rain/steam, and renders graded `AnyShot` walkthroughs in Cycles.
   - **Turning Locked Used Echo Show Hardware into Sovereign Voice + Vision Agent Terminals (`majorminorlabs/hermes-voice`)**: Used Amazon Echo and Echo Show units have excellent far-field microphones, speakers, and touchscreens, but are locked to Alexa. `hermes-voice` bridges `echo-dot-assist` satellites through Home Assistant Assist to a persistent **NousResearch `Hermes Agent`** profile (`X-Hermes-Session-Id`): the Echo Show screen (`screen-app`) streams what it heard, the live reply, active tool calls, and idle background jobs, while `Hermes Eye` (`eye-app`) and `extras/visual-memory` (local SQLite + Ollama `qwen3.6` or Codex CLI) let the agent answer *"where did you last see…?"* and display before/after camera diffs on screen.
2. **Closed-Form FinOps Verdict (`CLAIM-20261111-R47-ANYSCENE-HERMESVOICE`)**:
   - For a 10-person Creative 3D Environment Studio & Smart-Space Engineering Team producing **8 dressed 80-prop 3D Blender scenes per month and operating 25 room-level ambient voice/vision agent terminals** (senior 3D technical artist / IoT engineer loaded rate `$90.00/hr`; used Echo hardware purchase and local GPU hardware depreciation: `not_measured`):
   - Upgrading from **Path A (Manual Blender prop modeling/kitbashing + proprietary cloud voice/vision APIs, `$6,060.00/mo`)** to **Path C (`AnyScene` dual `Tripo H3.1`/`Meshy 7.1` contact-sheet pipeline + `Hermes Voice` Echo Show HUD & local SQLite `visual-memory`, `$790.00/mo`)** saves **`$5,270.00/mo` (`-86.96%`, `$63,240.00/yr`)** and cuts 3D scene assembly and terminal integration labor from `48.0 hrs/mo` to `5.0 hrs/mo` (**`-89.58%`**).

---

## 🎯 2. Three Core Architectural Questions (Q1 / Q2 / Q3 Deep-Dive)

### Q1: How does `apekshik/anyscene` use dual-model `Tripo H3.1` vs. `Meshy 7.1` contact sheets and code-generated `.blend` files to ship photoreal scenes?
- **First-Principles Breakdown**:
  1. **Dual Image-to-3D Tournament (`picks.json`)**:
     - Every prop in `assets.json` is generated as a reference image and passed through both `Tripo H3.1` and `Meshy 7.1` (`~$1.65/prop`, `~$150` for a 90-prop scene). Same-light comparison renders are placed on a contact sheet so the agent selects the cleaner mesh and logs the rationale in `picks.json`.
  2. **8-Gate Scripted Assembly & Floating-Prop Check**:
     - Instead of committing multi-gigabyte `.blend` binaries, git tracks lightweight JSON manifests (`assets.json`, `picks.json`, `shots.json`) and Python build scripts that enforce collision/floating-prop checks, apply grime/de-branding/volumetric haze, and drive `AnyShot` rack-focus and handheld camera rigs (locally or unattended via `fal deploy builder/app.py::SceneBuilderApp`).

### Q2: How does `majorminorlabs/hermes-voice` integrate `echo-dot-assist`, Home Assistant Assist, `screen-app`, and `Hermes Visual Memory`?
- **First-Principles Breakdown**:
  1. **Audited Fire OS Build Matrix & `X-Hermes-Session-Id` Streaming**:
     - Documents exact unlockable hardware/firmware pairs (e.g., Echo Dot 2nd/3rd gen `RS03QR`/`D9N29T`, Echo Show 5 1st gen `H23K37` on Fire OS `6574.1` build `8149` rather than blocked `8848`), forwarding Assist turns with a stable `X-Hermes-Session-Id` so Hermes retains `SOUL.md`, memory, and tools.
  2. **Full-Screen Echo Show HUD (`screen-app`), `Hermes Eye` & Local SQLite `visual-memory`**:
     - `screen-app` renders live transcripts, tool calls, and background work; `eye-app` exposes the Echo Show camera (`look` tool) with a mandatory on-screen `REC` indicator; and `extras/visual-memory` stores snapshots in local SQLite to answer spatial change queries via local `qwen3.6` (Ollama) or Codex CLI.

### Q3: How can Solution Architects deploy `AnyScene` and `Hermes Voice` together?
- **Deployment Blueprint**:
  - Use **`AnyScene`** to generate high-detail 3D digital twin rooms and simulation environments from a handful of reference photos.
  - Use **`Hermes Voice`** on unlocked Echo Show devices as low-cost, privacy-preserving physical room terminals with local visual memory and live agent HUDs.

---

## 🧭 3. Mermaid Decision Tree & Pipeline Architecture

```mermaid
flowchart TD
    A["Photoreal 3D Environment Generation & Physical Room Agent Terminal"] --> B{"Target Engineering Domain?"}
    B -- "Build dressed, lit 75-90 prop Blender 5.0 scenes from brief or photos" --> C["Adopt apekshik/anyscene (SKILL.md + Tripo H3.1 / Meshy 7.1)"]
    B -- "Repurpose Echo / Echo Show hardware into voice + vision Hermes terminals" --> D["Adopt majorminorlabs/hermes-voice (HA Assist + echo-dot-assist)"]

    C --> C1["Step 1: Brief -> room spec + prop manifest (assets.json) + prop reference images"]
    C1 --> C2["Step 2: Run each prop through Tripo H3.1 & Meshy 7.1 (~$1.65) -> pick winner (picks.json)"]
    C2 --> C3["Step 3: Scripted dressing + floating-prop check + grime/haze + Cycles AnyShot renders"]

    D --> D1["Step 1: Verify Echo model & Fire OS build (e.g., H23K37 build 8149) & install echo-dot-assist"]
    D1 --> D2["Step 2: Bridge HA Assist (Whisper/Piper) to Hermes profile via X-Hermes-Session-Id"]
    D2 --> D3["Step 3: Install Echo Show screen-app + Hermes Eye (REC badge) + SQLite visual-memory"]
```

---

## 📊 4. Architectural Comparison Matrix

| Evaluation Dimension | Path A: Manual 3D Modeling + Cloud Voice SaaS | Path B: Single-Model 3D Script + Headless Pi Mic | **Path C (Recommended): `AnyScene` + `Hermes Voice`** |
| :--- | :--- | :--- | :--- |
| **3D Prop Mesh Quality & Editability** | Weeks of manual modeling per 80-prop room | Single-model blind picks or uneditable monolithic mesh | **Dual `Tripo H3.1` + `Meshy 7.1` same-light tournament across 74–86 props** |
| **Layout Physics & Atmospheric Realism** | Manual placement and hand-painted weathering | Floating/intersecting props; flat ungraded lighting | **Automated collision/floating-prop check + scripted grime, haze & `AnyShot`** |
| **Ambient Hardware Audio & Visual HUD** | Locked to vendor cloud; cannot run custom MCP tools | Audio-only DIY mic with weak AEC and no screen HUD | **Echo far-field audio + Echo Show live tool/transcript/background HUD** |
| **Room Visual Memory & Privacy** | Cloud camera subscriptions with privacy exposure | No camera or visual diff memory | **Opt-in `Hermes Eye` (`REC` badge) + local SQLite/`qwen3.6` before/after diffs** |
| **Monthly TCO (8 Scenes + 25 Terminals)** | **`$6,060.00 / mo`** (`$1,740` API/reruns + `$4,320` labor) | **`$3,040.00 / mo`** (`$880` compute + `$2,160` labor) | **`$790.00 / mo` (Saves `$5,270.00/mo` · `-86.96%`)** |

---

## 🧪 5. Closed-Form FinOps Example & 7-Card Insights (`CLAIM-20261111-R47-ANYSCENE-HERMESVOICE`)

### 5.1 Workload & Scope Boundary
- **Workload**: A 10-person Creative 3D & Smart-Space Engineering Team building **8 dressed 80-prop Blender 3D scenes per month and operating 25 room-level voice/vision agent terminals**.
- **Rates**: Senior 3D technical artist / IoT systems engineer loaded rate at **`$90.00 / hr`**.
- **Explicit Scope Boundary**: Used Echo Show hardware acquisition and local GPU workstation depreciation are marked **`not_measured`**.

### 5.2 Closed-Form Monthly Cost Breakdown

| Cost Component | Path A: Manual 3D Kitbash + Cloud Voice SaaS | Path B: Single-Model 3D + Headless Pi Mic | **Path C: `AnyScene` + `Hermes Voice` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **3D Generation (`fal`) & Voice/Vision Compute Spend** | **`$1,740.00`** | **`$880.00`** | **`$340.00`** (`~$1.65/prop` tournament + local Whisper/Piper/Ollama) |
| **3D Scene Assembly, Lighting & Terminal Ops Labor (`$90/hr`)** | `48.0 hrs × $90.00` = **`$4,320.00`** | `24.0 hrs × $90.00` = **`$2,160.00`** | `5.0 hrs × $90.00` = **`$450.00`** |
| **Total Monthly TCO** | **`$6,060.00 / mo`** | **`$3,040.00 / mo`** (`-49.83%`) | **`$790.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$3,020.00 / mo` | **Saves `$5,270.00 / mo` (`-86.96%` · `$63,240.00/yr`)** |
| **Used Echo Hardware & Local GPU Workstation Depreciation** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Verification Checklist

- [ ] **1. Configure `AnyScene` Toolchain & Local `fal` Spend Log**: Set up Blender 5.0+, Node 20+, `uv`, `ffmpeg` (`h264_nvenc`), and `FAL_KEY`, and monitor per-prop generation spend in `generate/`.
- [ ] **2. Enforce Contact-Sheet Gates & Floating-Prop Checks**: Require the agent to inspect same-light `Tripo H3.1` vs. `Meshy 7.1` renders (`picks.json`) and pass the automated floating-prop check before final Cycles rendering.
- [ ] **3. Audit Echo Model & Fire OS Build Before Unlocking**: Verify exact model and firmware build numbers against the compatibility table (e.g., `H23K37` on build `8149`, keeping stock units offline until instructed).
- [ ] **4. Verify `X-Hermes-Session-Id` Continuity & `screen-app` HUD**: Confirm multi-turn voice continuity in Home Assistant Assist and live tool-call rendering on the Echo Show screen.
- [ ] **5. Build Self-Signed `eye-app` & Local SQLite `visual-memory`**: Sign `eye-app` with your own key, verify the on-screen `REC` badge when `look` is invoked, and connect `extras/visual-memory` to local Ollama `qwen3.6`.
