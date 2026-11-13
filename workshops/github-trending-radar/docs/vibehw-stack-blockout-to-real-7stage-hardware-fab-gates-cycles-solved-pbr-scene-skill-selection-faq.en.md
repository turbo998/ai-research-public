# 7-Stage 23-Skill Hardware Fab Gates (`makoshan/vibehw-stack`) & Cycles-Solved 3D PBR Scene Skill (`gokayfem/blockout-to-real`) Selection FAQ

> **Document Scope**: This is the **2026-11-13 Night Shift Round 22 (Cumulative #150) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects, Embedded Hardware Leads, and 3D Digital-Twin Pipeline Engineers evaluating two physical-reality and inverse-rendering skill suites:
> 1. **`makoshan/vibehw-stack` (`21★` in 1 day, Python, MIT, 23 hardware skills across 7 stages + 6,197-board / 345k-component / 56k-LCSC-part `pcb-reference` DB)**: Forged across **39 3D-printed enclosure revisions and 16 PCB revisions** (smartwatch + 8-channel `OpenEMG` wristband), this skill pack bridges the gap between `"DRC = 0 / watertight STEP"` and `"the physical board boots and fits inside the case"` via executable gates (`bom_rules.py`, `basic_gate.py` locking JLCPCB basic-library C-numbers to avoid ¥20/part extended-library fees, `fab_facts.py`, `review_gate.py`, `step_export_check.py`, and insertion-trajectory sweep checks `pcb-enclosure-fit` / `mako-cad-fit`) under a strict **"Agents Never Touch Money"** rule!
> 2. **`gokayfem/blockout-to-real` (`21★` in 2 days, Python, MIT, for Claude Code, Codex, Cursor, Copilot & Gemini)**: Turns any grey 3D blockout scene into an ordinary editable, relightable `.blend` scene with real Principled BSDF PBR materials and Cycles-fitted lights (**reducing `LPIPS-AlexNet` from `0.463` to `0.134`**) — decomposing a 5-level Nano Banana 2 target photo via **Marigold V2 albedo, MoGe-3 normals/metric depth, and PATINA / Marigold-IID roughness**, back-projecting visibility-tested texels into each object's own UV map, fitting light strengths/colors via a **non-negative Cycles solver**, and routing large per-object residuals to a fresh blind reviewer for geometry edits!
>
> **中文版本**: [vibehw-stack-blockout-to-real-7stage-hardware-fab-gates-cycles-solved-pbr-scene-skill-selection-faq.md](vibehw-stack-blockout-to-real-7stage-hardware-fab-gates-cycles-solved-pbr-scene-skill-selection-faq.md) · **Daily Digest**: [`daily/2026-11-13.en.md`](../daily/2026-11-13.en.md) · **Topic SVG**: [`assets/github-ai-radar-2026-11-13-r22-vibehw-blockouttoreal.svg`](../../../assets/github-ai-radar-2026-11-13-r22-vibehw-blockouttoreal.svg)

![makoshan/vibehw-stack and gokayfem/blockout-to-real Architecture Comparison](../../../assets/github-ai-radar-2026-11-13-r22-vibehw-blockouttoreal.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "AI-generated PCBs that pass `DRC = 0` but rack up ¥20/part JLCPCB extended-library fees or fail physical assembly because a watertight STEP enclosure has a reversed connector or impossible insertion path" (`makoshan/vibehw-stack`)**: Born from 39 3D-printed shell iterations and 16 PCB revisions (`OpenEMG` + smartwatch), `vibehw-stack` ships **23 hardware skills across 7 stages** plus an optional 54 MB `pcb-reference` database (**6,197 open-source boards, 345k components, and 56k LCSC C-numbers**). It enforces `bom_rules.py` and `basic_gate.py` to lock JLCPCB basic-library C-numbers at design time, `fab_facts.py` + `review_gate.py` to audit Gerber/Drill/BOM/CPL physical facts before ordering, `step_export_check.py` + `pcb-enclosure-fit` to verify insertion sweeps, solder-joint heights, and ribbon-cable bend radii, and a hard **"Agents Never Touch Money"** boundary!
   - **Ending "Blender agents that either tweak colors/HDRIs by eye without measurement or run a 2D img2img pass that bakes floor sun-patches and sofa shadows directly into albedo paint" (`gokayfem/blockout-to-real`)**: `blockout-to-real` treats the generated 2D photo strictly as a measurement target, never a texture to paste. It decomposes the view via **Marigold V2 albedo, MoGe-3 normals/metric depth, and PATINA / Marigold-IID roughness**, back-projects visibility-tested texels into each object's own UV map, renders each candidate light alone in Cycles to run a **non-negative linear solve** for light strengths and colors, and uses a fresh blind critic for geometry edits — cutting **`LPIPS-AlexNet` from `0.463` to `0.134`** while outputting a standard relightable `.blend` file!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261113-R22-VIBEHW-BLOCKOUTTOREAL`)**:
   - Modeled for a **hardware product and 3D visualization studio shipping `8 custom PCB + 3D-printed enclosure prototypes / month` and `20 relightable 3D product/interior scenes / month`** (fully loaded hardware & 3D technical artist rate `$90.00/hr`; bench oscilloscope capex and mass-production injection-molding tooling: `not_measured`):
   - Switching from **Path A (unchecked AI EDA exports with extended-part fees/respins + 2D img2img baked-shadow textures, `$5,840.00/mo`)** to **Path C (`vibehw-stack` 23-skill 7-stage gates + `blockout-to-real` UV back-projection & Cycles light solver, `$570.00/mo`)** saves **`$5,270.00/mo` (`-90.24%`, or `$63,240.00/yr`)** and cuts hardware respin and 3D relighting rework from `44.0 hrs/mo` to `4.0 hrs/mo` (**`-90.91%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why do `DRC = 0` PCB files and static zero-interference STEP assemblies still fail on the physical workbench?
- **First-Principles Breakdown**:
  1. **EDA Platforms Do Not Block Unresolved DRCs or Extended-Part Fees**: JLCPCB EDA allows Gerber exports even with unresolved DRC warnings, and every passive missing a Basic Library C-number incurs a ¥20 SMT feeder setup fee.
  2. **Static Boolean Clearance Ignores Insertion Kinematics**: A board and shell with zero static overlap can still fail assembly due to insertion-path collisions, THT solder-pin heights, connector plug housings, or FPC bend radii.

### Q2: How does `makoshan/vibehw-stack` enforce physical-reality gates across 7 stages and 23 skills?
- **First-Principles Breakdown**:
  1. **6,197-Board Reference Grounding & Design-Time Basic-Part Gate (Stages ①–③)**:
     - Queries 6,197 real boards (`pcb-reference`) for proven peripheral wiring and LCSC C-numbers, runs `bom_rules.py` / `basic_gate.py` / `layout_gate.py` during layout, and executes `fab_facts.py` + `review_gate.py` to generate a human sign-off checklist before checkout.
  2. **Insertion-Sweep Verification & Power-Off Pre-Flight (Stages ④–⑤)**:
     - Verifies STEP watertightness and insertion trajectories (`pcb-enclosure-fit` / `mako-cad-fit`), mandates power-off multimeter continuity and 4.2V-LiPo isolation before power-on, and automates board annotation and Apple-style dimensional drawings.

### Q3: How does `gokayfem/blockout-to-real` drop `LPIPS-AlexNet` from `0.463` to `0.134` while producing a camera-independent `.blend`?
- **First-Principles Breakdown**:
  1. **Intrinsic Decomposition & Per-Object Visibility UV Back-Projection**:
     - Uses a 5-level Nano Banana 2 conditioning ladder aligned to object-id masks, extracts shading-free Marigold V2 albedo, MoGe-3 normals/depth, and PATINA or Marigold-IID roughness, and projects only visible texels onto each object's own UV map.
  2. **Cycles Non-Negative Light Solver, LPIPS Pruning & Blind Matrix Scoring**:
     - Renders each candidate light individually in Cycles with Principled BSDF materials, solves non-negative weights/colors against the target, prunes low-contribution lights via LPIPS margins, routes large object errors to a blind reviewer for geometry edits, and scores every scene across all iteration targets.

---

## 🧭 3. Mermaid Decision Tree & vibehw-stack + blockout-to-real Architecture

```mermaid
flowchart TD
    A["AI-Assisted Hardware Prototyping (PCB/SMT/Enclosure) & 3D PBR Scene Authoring"] --> B{"Primary Engineering Bottleneck?"}
    B -- "Hardware Fab & Assembly: Extended-part fees, board respins, or enclosures that fail insertion" --> C["Adopt makoshan/vibehw-stack (7-Stage 23-Skill Hardware Suite)"]
    B -- "3D Scene Look-Dev: Baked shadows in textures, eye-balled HDRIs, or broken multi-camera relighting" --> D["Adopt gokayfem/blockout-to-real (Intrinsic UV Back-Projection + Cycles Solver)"]

    C --> C1["6,197-board DB + bom_rules.py / basic_gate.py + fab_facts.py pre-order gate"]
    C1 --> C2["step_export_check.py + insertion sweep check + strict human-only checkout"]

    D --> D1["Marigold V2 albedo + MoGe-3 normals/depth + PATINA roughness -> per-object UV projection"]
    D1 --> D2["Per-light Cycles basis + non-negative solve + blind geometry critic (LPIPS 0.463 -> 0.134)"]

    C2 & D2 --> E["🏆 Golden Physical & 3D Production Stack: vibehw-stack + blockout-to-real (-90.24% TCO)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Unchecked AI EDA + 2D Img2Img Filter | Path B: Manual BOM Spreadsheets + Unfitted PBR | **Path C (Recommended): `vibehw-stack` + `blockout-to-real`** |
| :--- | :--- | :--- | :--- |
| **JLCPCB Basic-Part & BOM Verification** | Frequent ¥20/part extended-library fees & footprint mismatches | Slow manual LCSC catalog lookups | **6,197-board / 56k-C-number DB + automated `bom_rules.py` & `basic_gate.py`** |
| **PCB-to-Enclosure Fit Verification** | Static boolean overlap only; fails insertion or cable bend | Physical trial-and-error 3D print respins | **`step_export_check.py` + `pcb-enclosure-fit` insertion sweep & solder-height gates** |
| **3D Albedo/Roughness Separation & Relighting** | Bakes sun patches & shadows into paint; breaks on camera move | Manual UV unwrapping & uncalibrated roughness | **Marigold V2 + MoGe-3 + PATINA/Marigold-IID UV back-projection; relights from any camera** |
| **Light Rig Calibration & Perceptual Error** | Eye-balled lights or unmeasured fill lights | Manual trial renders in Cycles | **Non-negative Cycles light solver + blind matrix critic (`LPIPS-AlexNet 0.463 → 0.134`)** |
| **Monthly TCO (8 Prototypes + 20 Scenes)** | **`$5,840.00 / mo`** (`$1,880` fab/render + `$3,960` labor) | **`$2,840.00 / mo`** (`$860` fab/render + `$1,980` labor) | **`$570.00 / mo` (Saves `$5,270.00/mo` · `-90.24%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261113-R22-VIBEHW-BLOCKOUTTOREAL`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A hardware product and 3D visualization studio shipping **8 custom PCB + SMT + 3D-printed enclosure prototypes per month** and authoring **20 relightable Blender `.blend` product/interior scenes per month**.
- **Labor Rate**: Fully loaded hardware engineer and 3D technical artist rate of **`$90.00 / hr`**.
- **Explicit Not-Measured Boundary**: Bench oscilloscope capex and mass-production steel injection-molding tooling are marked **`not_measured`**. This model strictly accounts for PCB/SMT extended-part fees and prototype respins, 3D printing/rendering compute spend, and engineering hours spent on manual BOM cleanup, enclosure respins, and Blender UV/light rework.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Unchecked Fab + 2D Img2Img / Eye HDRI | Path B: Manual BOM Check + Unfitted PBR Maps | **Path C: `vibehw-stack` + `blockout-to-real` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly PCB/SMT Respins, Extended Fees & Render Spend** | **`$1,880.00`** (extended-part fees + enclosure respins + render retries) | **`$860.00`** (moderate prototype & render spend) | **`$210.00`** (0 extended-part fees + first-pass enclosure fit + Cycles solve) |
| **BOM Cleanup, Enclosure Rework & 3D Relighting Labor (`$90/hr`)** | `44.0 hrs × $90.00` = **`$3,960.00`** | `22.0 hrs × $90.00` = **`$1,980.00`** | `4.0 hrs × $90.00` = **`$360.00`** |
| **Total Monthly TCO** | **`$5,840.00 / mo`** | **`$2,840.00 / mo`** (`-51.37%`) | **`$570.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$3,000.00 / mo` | **Saves `$5,270.00 / mo` (`-90.24%` · `$63,240.00/yr`)** |
| **Bench Oscilloscopes & Injection-Molding Tooling** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `makoshan/vibehw-stack` & `pcb-reference` Setup**: Run `bash ~/.local/share/vibehw-stack/scripts/install.sh --with-pcbdb` to install all 23 hardware skills and the 6,197-board LCSC C-number reference database.
- [ ] **2. Pre-Order `bom_rules.py` & `fab_facts.py` Gate**: Execute `bom_rules.py`, `basic_gate.py`, `fab_facts.py`, and `review_gate.py` before every JLCPCB order, confirming that checkout stops for human review and payment.
- [ ] **3. `pcb-enclosure-fit` Insertion Trajectory Sweep**: Run `step_export_check.py` and insertion-path collision checks to validate connector orientation, solder-joint clearance, and ribbon-cable bend radii.
- [ ] **4. `gokayfem/blockout-to-real` Cycles Solve & LPIPS Audit**: Run `blockout-to-real` on grey `.blend` scenes, verify shading-free UV albedo maps and non-negative Cycles light weights, and confirm LPIPS reduction across the target matrix.
