# Single-Image to Code-Built 3D Exploding Cutaway Skill (`Nyxera0x/cutaway`) & 19-Layer Character Art PSD Segmentation Skill (`link-ding/image-to-psd`) Selection FAQ

> **Document Scope**: This is the **2026-11-12 Night Shift Round 14 (Cumulative #113) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for Technical Illustration Architects and 2.5D Character Pipeline Leads evaluating two high-precision visual agent skills:
> 1. **`Nyxera0x/cutaway` (`181★`, JavaScript / Three.js / Playwright / Python SFX, Claude Code Skill)**: Turns a single reference picture of a machine, device, or robotic animal into a **code-built Three.js 3D object that takes itself apart** — grading every round against a **10–12 line visual `CHECKLIST.md` (`yes / partial / no`)**, pausing at the approved still, and then filming choreographed per-part camera disassembly, full-object explosion/snap-back, and procedural sound effects (`run_sfx.py`)!
> 2. **`link-ding/image-to-psd` (`73★`, Python / `pillow` / `numpy` / `psd-tools`, Agent Skill)**: Splits a flat character illustration (PNG / JPG / SVG) into a **19-layer (or 20-layer with split `handwear back/front`) editable PSD ready for 2.5D rigging** — **inpainting occluded regions** (the face under the bangs, eye whites under the irises, back hair behind the head), exporting RGBA pixels + grayscale masks per layer, and **reopening the PSD layer-by-layer to fix bleed, gaps, and stray fragments before delivery**!
>
> **中文版本**: [cutaway-image-to-psd-code-built-3d-exploding-sim-19-layer-psd-skill-selection-faq.md](cutaway-image-to-psd-code-built-3d-exploding-sim-19-layer-psd-skill-selection-faq.md) · **Daily Digest**: [`daily/2026-11-12.en.md`](../daily/2026-11-12.en.md) · **Architecture Summary SVG**: [`assets/github-ai-radar-2026-11-12-r14-cutaway-imagetopsd.svg`](../../../assets/github-ai-radar-2026-11-12-r14-cutaway-imagetopsd.svg)

![Nyxera0x/cutaway and link-ding/image-to-psd Architecture Comparison](../../../assets/github-ai-radar-2026-11-12-r14-cutaway-imagetopsd.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "asking an LLM to build a 3D cutaway from a reference image where it writes one rough approximation, skips visual self-grading, and wastes hours animating a broken model" (`Nyxera0x/cutaway`)**: Building code-driven 3D mechanical explainers (like the *Theraphos TH-8* robotic tarantula or *Serrasal PX-7* robotic piranha) fails when geometry and animation are mixed without a visual gate. `cutaway` enforces a **two-stage checklist workflow**: (1) Claude reads the reference image, writes a **10–12 line numbered `CHECKLIST.md`**, rebuilds every shell and gear in Three.js code, and grades its own rendered screenshot line-by-line (`yes`, `partial`, or `no`) until it stops at the still for human sign-off; (2) once approved, it films a cursor clicking each subsystem under its own camera, explodes the entire assembly, snaps it back together, and synthesizes procedural audio (`run_sfx.py`)!
   - **Ending "spending a full day manually cutting a flat character illustration into 19 Photoshop layers and hand-painting the hidden face under bangs and sclera under irises for Live2D/Spine rigging" (`link-ding/image-to-psd`)**: Standard segmentation models only cut visible pixels, leaving transparent holes whenever a 2.5D rig blinks or turns its head. `image-to-psd` studies part occlusion across **19 standard rigging layers** (`back hair`, `front hair`, `face`, `eyewhite`, `irides`, `eyelash`, `topwear`, `handwear`, etc. — splitting `handwear` into `back/front` for 20 layers when hands and props overlap in both directions), **inpaints hidden areas**, exports a `.psd` with RGBA pixels and grayscale masks via `psd-tools`, and **reopens the PSD to fix color bleed and stray fragments before delivery**!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261112-R14-CUTAWAY-IMAGETOPSD`)**:
   - Modeled for a **10-person technical illustration & 2.5D character animation studio producing `16 interactive 3D cutaway films/demos` and `30 19-layer rigged PSD character sheets` per month** (fully loaded senior technical artist rate `$90.00/hr`; commercial Adobe Creative Cloud and Live2D Cubism seat licenses: `not_measured`):
   - Upgrading from **Path A (unguided 3D prompting + manual Photoshop pen-tool layer cutting and occlusion painting, `$5,940.00/mo`)** to **Path C (`Nyxera0x/cutaway` checklist-gated 3D cutaway skill + `link-ding/image-to-psd` 19-layer occlusion-inpainted PSD skill, `$670.00/mo`)** saves **`$5,270.00/mo` (`-88.72%`, or `$63,240.00/yr`)** and cuts manual modeling and layer-cutting labor from `48.0 hrs/mo` to `5.0 hrs/mo` (**`-89.58%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: How does `Nyxera0x/cutaway` enforce visual fidelity via its 10–12 line `CHECKLIST.md`, still-approval gate, and persistent `JOB_DESCRIPTION.md`?
- **First-Principles Breakdown**:
  1. **Per-Object 10–12 Line Checklist & Still-First Gate**:
     - Claude derives 10–12 concrete visual criteria from the reference picture and grades its Three.js build (`yes / partial / no`) every round, stopping at the static still for human verification before filming the disassembly sequence.
  2. **Cumulative Taste Memory (`docs/JOB_DESCRIPTION.md` & `LESSONS.md`)**:
     - Every human correction is appended to `docs/JOB_DESCRIPTION.md`, which Claude reads before every future object.

### Q2: How does `link-ding/image-to-psd` solve occluded-region inpainting and post-export PSD quality assurance?
- **First-Principles Breakdown**:
  1. **19/20 Standard Layer Contract & Occlusion Reconstruction**:
     - Segments visible parts and fills in hidden regions (face under bangs, back hair behind head, eye whites under irises) while keeping original style, colors, pose, and canvas dimensions untouched.
  2. **Round-Trip PSD Reopen & Layer-by-Layer Inspection**:
     - After exporting the `.psd` with RGBA channels and grayscale masks via `psd-tools`, the agent reopens the file and inspects every layer to eliminate bleed, gaps, and stray pixel fragments.

### Q3: How should AI Solution Architects combine `cutaway` and `image-to-psd`?
- **Golden-Combo Pattern**:
  - Use **`Nyxera0x/cutaway`** to turn hardware/system reference renders into interactive Three.js exploding cutaway explainers;
  - Use **`link-ding/image-to-psd`** to convert 2D character concept art into 19-layer Live2D-ready PSDs for embodied desktop assistants!

---

## 🧭 3. Mermaid Decision Tree & 3D Cutaway + 19-Layer PSD Pipeline

```mermaid
flowchart TD
    A["Single-Image 3D Cutaway Simulation & 2.5D Layered PSD Rigging Selection"] --> B{"Primary Visual Deliverable?"}
    B -- "Rebuild one machine/device picture into a code-driven Three.js exploding cutaway film" --> C["Adopt Nyxera0x/cutaway (10-12 Line Checklist + Playwright/ffmpeg)"]
    B -- "Split flat character artwork into a 19-layer PSD with inpainted occluded regions" --> D["Adopt link-ding/image-to-psd (19/20-Layer Contract + psd-tools QA)"]

    C --> C1["Stage 1: Grade 10-12 CHECKLIST.md items (yes/partial/no) & pause at approved still"]
    C1 --> C2["Stage 2: Film cursor-driven part disassembly, full explosion & procedural SFX"]

    D --> D1["Stage 1: Analyze 19 standard parts & inpaint hidden face, sclera & back hair"]
    D1 --> D2["Stage 2: Export RGBA+mask PSD via psd-tools -> reopen & fix bleed/gaps per layer"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Unguided 3D Prompt + Manual PS Pen Cutting | Path B: Single-Shot Three.js + Naive SAM Cutout | **Path C (Recommended): `cutaway` + `image-to-psd`** |
| :--- | :--- | :--- | :--- |
| **3D Code Structural Fidelity** | Drifts from reference; wastes time animating bad geometry | Rough primitives; lacks per-part camera choreography | **10–12 line `CHECKLIST.md` grading + still-approval gate** |
| **Cross-Object Taste Retention** | Repeated prompt nudging | None | **Corrections persist in `docs/JOB_DESCRIPTION.md` & `LESSONS.md`** |
| **2.5D Occluded Region Inpainting** | 6–10 hours of manual PS painting per character | Transparent holes under bangs/irises break rigging | **Automated inpainting of hidden face, eye whites & back hair** |
| **PSD Mask Export & Self-Review** | Manual layer inspection | Loose PNGs without masks or bleed cleanup | **19/20-layer `.psd` with grayscale masks + round-trip reopen QA** |
| **Monthly TCO (16 Cutaways + 30 PSDs)** | **`$5,940.00 / mo`** (`$1,620` API + `$4,320` labor) | **`$2,980.00 / mo`** (`$820` API + `$2,160` labor) | **`$670.00 / mo` (Saves `$5,270.00/mo` · `-88.72%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261112-R14-CUTAWAY-IMAGETOPSD`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A 10-person technical illustration & 2.5D character studio delivering **16 interactive 3D cutaway simulators/films** and **30 19-layer character PSDs per month**.
- **Labor Rate**: Fully loaded senior technical artist rate of **`$90.00 / hr`**.
- **Explicit Not-Measured Boundary**: Commercial Adobe Creative Cloud (Photoshop) and Live2D Cubism PRO seat licenses are marked **`not_measured`**. This model strictly accounts for multimodal/ImageGen API spend and engineering/art hours spent on 3D modeling rework and manual PSD layer cutting/inpainting.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Unguided 3D + Manual PS Layer Cutting | Path B: Single-Shot 3D + Naive SAM Cutout | **Path C: `cutaway` + `image-to-psd` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly Multimodal & Inpainting ImageGen API Spend** | **`$1,620.00`** | **`$820.00`** | **`$220.00`** (Still-first gate + targeted part occlusion generation) |
| **3D Rework, Camera Tuning & PSD Cutting/Inpainting Labor (`$90/hr`)** | `48.0 hrs × $90.00` = **`$4,320.00`** | `24.0 hrs × $90.00` = **`$2,160.00`** | `5.0 hrs × $90.00` = **`$450.00`** |
| **Total Monthly TCO** | **`$5,940.00 / mo`** | **`$2,980.00 / mo`** (`-49.83%`) | **`$670.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,960.00 / mo` | **Saves `$5,270.00 / mo` (`-88.72%` · `$63,240.00/yr`)** |
| **Commercial Photoshop & Live2D Seat Licenses** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `Nyxera0x/cutaway` Exemplar Build Verification**: Install `cutaway` (`npx skills add Nyxera0x/cutaway -g -a claude-code`) and build `node sims/build.mjs tarantula-film` to verify Three.js disassembly and `run_sfx.py` audio.
- [ ] **2. 10–12 Line `CHECKLIST.md` Still Gate**: Require the agent to grade all 10–12 checklist items (`yes/partial/no`) and pause at the static still before filming animations.
- [ ] **3. `link-ding/image-to-psd` 19/20-Layer Occlusion Check**: Install `pillow numpy psd-tools`, run `$image-to-psd`, and verify that occluded regions (`face` under bangs, `eyewhite` under irises, `back hair`) are cleanly filled.
- [ ] **4. Round-Trip PSD Reopen QA**: Verify that the skill reopens the exported `.psd` and cleans up layer bleed and stray fragments before handoff.
