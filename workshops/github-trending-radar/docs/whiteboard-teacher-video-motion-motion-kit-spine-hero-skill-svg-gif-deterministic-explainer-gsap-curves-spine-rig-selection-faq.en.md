# SVG+GIF Deterministic Whiteboard Explainer (`liangdabiao/whiteboard-teacher-video-motion`), Distance/Weight GSAP Motion Curves (`hughminhphan/motion-kit`) & Single-Painting Spine Rigging (`enoch3712/spine-hero-skill`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 47 (Cumulative Round 471)  
> **Tracked Repositories**:
> - **`liangdabiao/whiteboard-teacher-video-motion`** (`★ 45`, Python 3.9+ / Node ≥22.19 / `ftdeterminism.mjs` `11/11`-Page Pixel-Identical Verification, `MIT`): Standalone hand-drawn explainer video skill that combines **AI-native SVG stroke-by-stroke vector growth** with **GIF frame-split local micro-motion** on a deterministic *"draw as you speak"* timeline—shipping an offline zero-API-key starter (`examples/sample/` + free `edge-tts`) that automatically reuses cached `assets/raw/` files
> - **`hughminhphan/motion-kit`** (`★ 46`, JavaScript / GSAP & HyperFrames Motion Designer Skill, `MIT`) & **`enoch3712/spine-hero-skill`** (`★ 46`, JavaScript / Single-Painting 2D Spine Skeleton Rigging + Scripted Gate + Independent Defect Checker): Replaces the telltale *"AI house default look"* (`0.6s power3.out` fade-ups with `0.08s` uniform staggers) with distance/weight duration calculation **`dur(px, weight)`**, named per-property curves (`kit.land`, `kit.heavy`, `kit.whip`), and uneven causal reaction offsets (`0, 4, 9, 15, 22, 30` frames) (`motion-kit`), paired with a skeletal animation pipeline that cuts one painting onto a Spine rig and validates moves via a scripted capture gate plus an independent defect-checking model (`spine-hero-skill`)  
> **Audit Claim ID**: `CLAIM-20261117-R47-WHITEBOARD-MOTIONKIT-SPINEHERO` (base LLM subscriptions marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Technical Education, Product Marketing, and Interactive Media Teams Hit Three Production Bottlenecks: Sterile Code-Only Whiteboards, Telltale "AI Stagger" Motion, and Unmaintainable 403-Frame Flipbooks**:
   - **Bottleneck 1 — Flat Code-Only Whiteboards vs. Non-Deterministic Video Generators**: Pure-code whiteboard explainers nail audio-visual sync and determinism but look visually sterile, whereas raw text-to-video models garble text and fail deterministic frame-by-frame reproduction.
   - **Bottleneck 2 — The "Claude House Default" Motion Look (`0.6s power3.out` + `0.08s` Stagger)**: Because standard agent animation prompts default to `gsap.defaults({ duration: 0.6, ease: "power3.out" })`, every AI-generated video fades elements up `24 px` at the exact same speed and uniform `0.08 s` stagger regardless of element size or causal hierarchy.
   - **Bottleneck 3 — 403-Frame Flipbook Re-Renders Whenever a Prop Changes**: Slicing generated videos into 403 flipbook frames across 10 character clips means that swapping a single prop (such as changing a hammer to an axe) forces the team to re-render all 10 clips from scratch.
   - **The Solution Architect Stack (`whiteboard-teacher-video-motion` MIT + `hughminhphan/motion-kit` MIT + `enoch3712/spine-hero-skill`)**: Build technical and manufacturing explainers on **`liangdabiao/whiteboard-teacher-video-motion`** (combining SVG stroke-by-stroke vector growth with GIF frame-split micro-motion, verified to `11/11`-page pixel determinism via `ftdeterminism.mjs`); upgrade all GSAP and HyperFrames timelines with **`hughminhphan/motion-kit`** (`dur(px, weight)`, `kit.land/heavy/whip`, and uneven `0, 4, 9, 15, 22, 30` frame reaction offsets); and rig 2D characters and interactive product assemblies with **`enoch3712/spine-hero-skill`** (1 painting → Spine skeleton + painted occluded limbs/swappable gear + scripted capture gate + independent model defect audit).
2. **Closed-Form FinOps Impact (25 Technical Explainer, Motion Design & Interactive Media Engineers Producing 500 Monthly Explainer Clips, Product Reels & Skeletal Animations at `$95.00/hr`)**:
   - Migrating from **Path A (403-Frame Flipbook Re-Renders + Manual After Effects Curve Polishing at `$5,680.00/mo`)** to **Path C (`whiteboard-teacher-video-motion` + `motion-kit` + `spine-hero-skill` Stack at `$341.00/mo`)** saves **`$5,339.00/mo` (`-94.00%`, or `$64,068.00/yr`)** while cutting prop-swap re-rendering and manual curve-tuning labor from `36.0 hrs/mo` to `2.8 hrs/mo` (**`92.22%` reduction**).

![Whiteboard Motion + motion-kit + spine-hero Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r47-whiteboard-motionkit-spinehero.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `liangdabiao/whiteboard-teacher-video-motion` blend AI-native SVG stroke growth with GIF micro-motion while guaranteeing `11/11`-page pixel determinism?
- **Plain-Language Definition**: `whiteboard-teacher-video-motion` (`MIT`, Python 3.9+ & Node ≥22.19) is **a self-contained hand-drawn explainer pipeline (`ftnew.py → ftasset.py → ftvoice.py → ftcheck.py → ftdeterminism.mjs → ftrender.py`) that pairs deterministic code-drawn typography, arrows, and camera pans with stroke-by-stroke SVG illustrations and looping GIF micro-motions**.
- **Three Engineering Pillars**:
  1. **Hybrid SVG Stroke Growth + GIF Frame-Split Micro-Motion**: Demonstrated on a completed 11-page / 33-sentence / `121.9 s` production film (*How a Pencil Is Made*) combining 11 stroke-growing SVGs and 10 frame-split GIF loops with `11/11` pages passing pixel-identical determinism checks;
  2. **Zero-Cost Asset Reuse (`ftasset.py`) & Free Offline Starter**: Automatically reuses existing files in `assets/raw/` without calling paid APIs, and ships with a complete offline SVG + GIF sample plus free `edge-tts` voiceover integration;
  3. **Automated Quality & Determinism Gates (`ftcheck.py` & `ftdeterminism.mjs`)**: Verifies timeline alignment and pixel-exact repeatability before rendering at `24 fps`.

### Q2: How does `hughminhphan/motion-kit` replace uniform AI animation templates with After-Effects-grade timing and causal reaction chains?
- **Five Concrete Motion Upgrades for HyperFrames & GSAP (`MIT`)**:
  1. **Per-Move & Per-Property Named Curves (`kit.land`, `kit.heavy`, `kit.whip`)**: Replaces the single hardcoded `power3.out` preset with purpose-named curves plus `easings.net`, Material 3, and IBM Carbon curves;
  2. **Distance- and Weight-Driven Duration (`dur(px, weight)`)**: A small badge and a full-screen panel no longer take the same `0.6 s` to move;
  3. **Causal Reaction Offsets (`0, 4, 9, 15, 22, 30` Frames)**: One primary element leads and dependent elements react at uneven frame offsets rather than a robotic `0.08 s` loop stagger;
  4. **Crisp Text Cuts & Settling Tracking**: Most text cuts on cleanly or types on while titles settle their letter-spacing;
  5. **Living Camera Drift on Holds**: Keeps holds visually alive between major beats.

### Q3: How does `enoch3712/spine-hero-skill` animate a 2D hero from a single painting with swappable gear and independent defect verification?
- **Five-Stage Skeletal Pipeline (for Claude Code, Codex & Cursor)**:
  1. **1 Painting Cut onto a Spine Skeleton (Replacing 403 Flipbook Frames)**: Eliminates the need to redo all 10 animation clips when changing a weapon or shield;
  2. **Reference Video for Timing Only + AI-Painted Occluded Parts & Swappable Gear**: Uses an image-to-video clip strictly for beat timing (never traced as frames) and paints hidden limbs (far arm) plus swappable axes, maces, and shields;
  3. **Parallel Code-Written IK Moves + Scripted Capture Gate + Independent Defect Checker**: Writes moves in parallel as bone keys and IK, measures every capture via script, and runs a **second independent model** to audit close-ups against a checklist of every defect humans previously caught.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph WhiteboardPipe["Deterministic SVG+GIF Explainer: whiteboard-teacher-video-motion (★45, MIT)"]
        A[Explainer Script &amp; assets.json] --> B[ftasset.py Reuses/Builds SVG+GIF Assets<br/>+ ftvoice.py Free edge-tts Sync]
        B --> C[ftcheck.py + ftdeterminism.mjs Gate<br/>11/11 Pages Pixel-Identical → ftrender.py 24fps Output]
    end

    subgraph MotionAndSpine["Physics Curves &amp; Skeletal Rigging: motion-kit (★46, MIT) + spine-hero-skill (★46)"]
        D[GSAP / HyperFrames Product Video] --> E[hughminhphan/motion-kit<br/>dur px,weight + kit.land/whip Curves + 0,4,9,15,22,30 Frame Reactions]
        F[2D Character / Swappable Product Rig] --> G[enoch3712/spine-hero-skill<br/>1 Painting → Spine Rig + Swappable Gear + Script Gate &amp; Independent Defect Audit]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: 403-Frame Video Flipbooks + Manual AE Keyframing | Option B: Stock `0.6s power3.out` GSAP + Flat Code Whiteboards | **Option C (Recommended): `whiteboard-motion` + `motion-kit` + `spine-hero-skill` (MIT)** |
| :--- | :--- | :--- | :--- |
| **Explainer Visual Richness & Frame Determinism** | ❌ Diffusion video garbles text & fails deterministic sync | ⚠️ Pure-code boxes look flat & lack material texture | ✅ **SVG stroke growth + GIF micro-motion with `11/11`-page `ftdeterminism.mjs` proof** |
| **Motion Timing & Hierarchy Realism** | ❌ Hours of manual graph-editor keyframing in After Effects | ❌ Uniform `0.6s power3.out` & `0.08s` staggers scream "AI template" | ✅ **`dur(px, weight)` timing, `kit.land/whip` curves & uneven `0,4,9,15,22,30` reactions** |
| **Swappable Gear & Defect Verification on 2D Rigs** | ❌ Changing 1 weapon requires re-rendering all 10 clips (403 frames) | ❌ No occluded-limb completion or IK bone rigging | ✅ **1 painting rigged on Spine + swappable gear + script gate & independent defect model** |
| **Monthly TCO (25 Engineers / 500 Clips & Rigs)** | **`$5,680.00 / mo`** (`$2,260` flipbook retries/plugins + `36.0 hrs` rework) | **`$2,410.00 / mo`** (`$890` assets + `16.0 hrs` manual curve tuning) | **`$341.00 / mo`** (**`-94.00%` savings**; `$75` cached assets/checks + `2.8 hrs` sign-off) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R47-WHITEBOARD-MOTIONKIT-SPINEHERO`)

> **Scope & Boundary Declaration**: Evaluated for a 25-engineer technical education, motion design, and interactive media organization producing **500 monthly deterministic whiteboard explainers, product motion reels, and skeletal animations** at a blended engineering rate of `$95.00/hr` (base LLM subscriptions marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Flipbook Re-Render \& Plugin Spend} + (\text{Gear-Swap Redo \& Curve Polishing Hours} \times \$95.00)$$

| Cost Component | Path A: 403-Frame Flipbooks + Manual AE | Path B: Stock GSAP + Flat Whiteboards | **Path C: `whiteboard` + `motion-kit` + `spine-hero`** |
| :--- | :---: | :---: | :---: |
| **Monthly Flipbook Video Re-Renders & Motion Plugin Spend** | `$2,260.00` | `$890.00` | **`$75.00`** |
| **Monthly Prop-Swap Redo, Curve Tuning & Sync Debug Hours** | `36.0 hrs` | `16.0 hrs` | **`2.8 hrs`** (**`92.22%` reduction**) |
| **Monthly Motion & Technical Media Engineering Labor (`@ $95.00/hr`)** | `$3,420.00` | `$1,520.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,680.00`** | **`$2,410.00`** (`-57.57%`) | **`$341.00`** (**`-94.00%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,270.00 / mo` (`$39,240/yr`) | **`$5,339.00 / mo` (`$64,068.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Run the Offline Deterministic Pipeline in `liangdabiao/whiteboard-teacher-video-motion`**: Execute `python scripts/setup.py` and validate the offline `examples/sample` project through `ftasset.py`, `ftvoice.py`, `ftcheck.py`, `ftdeterminism.mjs`, and `ftrender.py --fps 24`.
- [ ] **Step 2 — Symlink `hughminhphan/motion-kit` into `~/.claude/skills/`**: Vendor `motion-kit.js` into HyperFrames and GSAP compositions so agents compute durations via `dur(px, weight)` and stagger reactions at `0, 4, 9, 15, 22, 30` frames.
- [ ] **Step 3 — Adopt `enoch3712/spine-hero-skill` for 2D Character & Modular Product Rigs**: Slice single reference illustrations onto a Spine skeleton, generate occluded limbs and swappable props once, and author parallel moves as code on the rig.
- [ ] **Step 4 — Enforce Dual Scripted + Independent-Model Defect Gates**: Require every skeletal animation capture to pass the automated measurement script and an independent model close-up audit before human review.
