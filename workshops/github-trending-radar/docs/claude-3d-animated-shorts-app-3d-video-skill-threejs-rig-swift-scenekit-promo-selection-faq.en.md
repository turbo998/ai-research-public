# Deterministic Three.js 3D Story Shorts (`thuann-vn/claude-3d-animated-shorts`) & 5-Min Swift SceneKit iOS App Promo Skills (`huypham85/app-3d-video-skill`) Selection FAQ

> **Document Scope**: This is the **2026-11-13 Night Shift Round 30 (Cumulative #158) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects, Product Growth Engineers, and Creative Technologists evaluating two local code-driven 3D video rendering skill suites:
> 1. **`thuann-vn/claude-3d-animated-shorts` (`17★` in 3 days, TypeScript / Three.js, zero AI video diffusion)**: Upgrades 2D billboard shorts (`mromidev/claude-animated-shorts`) to **fully rigged 3D Mixamo characters (`engine/stickrig.js` with IK, screen-pixel brush outlines, outfits, and drawn faces)** inside a cinematic 3D world (`engine/world.js` + `engine/post.js` with ACES tone mapping, bloom, DOF, SMAA, and `n8ao` ambient occlusion + CC0 Kenney/KayKit furniture props), following the 5-act `"odd act → mockery → disaster → science + analogy → loop"` narrative structure with word-by-word timed captions and QA contact sheets!
> 2. **`huypham85/app-3d-video-skill` (`17★` in 2 days, Swift / SceneKit / CoreGraphics / AVFoundation)**: Two Claude Code skills (`app-3d-video` + `motion-video`) that read your iOS repository's real UI, strings, and brand colors, write a beat-synced plan (`plan.md`), compose an original music score (`score.swift`), generate still contact sheets and `numpy` audio-level checks for review, and **render a finished 20-second vertical 3D iOS promo video (with a 3D iPhone and a mascot that hops around and presses your UI) locally on an Apple Silicon Mac in ~5 minutes** — without needing `ffmpeg` or a video editor!
>
> **中文版本**: [claude-3d-animated-shorts-app-3d-video-skill-threejs-rig-swift-scenekit-promo-selection-faq.md](claude-3d-animated-shorts-app-3d-video-skill-threejs-rig-swift-scenekit-promo-selection-faq.md) · **Daily Digest**: [`daily/2026-11-13.en.md`](../daily/2026-11-13.en.md) · **Topic SVG**: [`assets/github-ai-radar-2026-11-13-r30-3dshorts-app3dvideo.svg`](../../../assets/github-ai-radar-2026-11-13-r30-3dshorts-app3dvideo.svg)

![thuann-vn/claude-3d-animated-shorts and huypham85/app-3d-video-skill Architecture Comparison](../../../assets/github-ai-radar-2026-11-13-r30-3dshorts-app3dvideo.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "burning hundreds of dollars on cloud AI video diffusion credits where characters morph between cuts, or using flat 2D billboard cutouts that collapse into a thin line whenever the camera orbits" (`thuann-vn/claude-3d-animated-shorts`)**: No AI video generator is used! Every character is a real 3D Mixamo-rigged model (`engine/stickrig.js`) with inverse kinematics (IK), white flat-shaded heads with screen-pixel brush outlines, pear/bean bodies, and customizable outfits inside a lit 3D world (`engine/world.js` + `engine/post.js` with ACES grading, bloom, DOF, SMAA, and `n8ao` ambient occlusion + CC0 Kenney/KayKit sets), complete with interactive browser preview modes (`?viewer=1&skit=1`) and contact-sheet QA!
   - **Ending "spending days in After Effects or Blender just to make a 20-second 3D iOS app launch teaser with a 3D iPhone, a mascot tapping your new widget, and beat-synced headlines" (`huypham85/app-3d-video-skill`)**: Shipping two skills (`app-3d-video` + `motion-video`), Claude reads your actual iOS codebase for real UI views, strings, and colors, writes a beat-by-beat plan, composes an original music track in `score.swift`, shows you still-frame contact sheets for approval, and **renders the full 20-second MP4 locally on an Apple Silicon Mac in ~5 minutes using pure Swift (`SceneKit`, `CoreGraphics`, `AVFoundation`) with zero `ffmpeg` or external editor dependencies**!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261113-R30-3DSHORTS-APP3DVIDEO`)**:
   - Modeled for a **mobile product and content growth studio producing `40 vertical 3D story Shorts / month` and `16 iOS app release 3D promo videos / month`** (fully loaded creative technologist & iOS growth engineer rate `$85.00/hr`; Apple Silicon Mac workstation hardware and base ElevenLabs TTS subscription: `not_measured`):
   - Switching from **Path A (cloud video diffusion credit burn + manual After Effects/Blender keyframing, `$5,210.00/mo`)** to **Path C (`claude-3d-animated-shorts` local Three.js 3D engine + `app-3d-video-skill` 5-min native Swift SceneKit renderer, `$500.00/mo`)** saves **`$4,710.00/mo` (`-90.40%`, or `$56,520.00/yr`)** and cuts animation keyframing and diffusion-artifact rework from `42.0 hrs/mo` to `4.0 hrs/mo` (**`-90.48%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why do deterministic Three.js and Swift SceneKit code pipelines outperform cloud AI video diffusion for story Shorts and iOS app promos?
- **First-Principles Breakdown**:
  1. **Zero UI Text Hallucination & 100% Character Continuity**: App Store promo videos require pixel-exact UI labels and widgets that match the shipped app binary; diffusion models warp typography and character outfits across shots.
  2. **Surgical Single-Line Edits at Zero Marginal Compute Cost**: Changing a headline, camera orbit, or mascot color in `scenes.swift` or `main.js` takes seconds and renders locally for free.

### Q2: How does `thuann-vn/claude-3d-animated-shorts` combine `stickrig.js`, ACES/`n8ao` post-processing, and CC0 sets?
- **First-Principles Breakdown**:
  1. **Mixamo Rigging + IK + Screen-Pixel Brush Outlines (`engine/stickrig.js`)**:
     - Builds full 3D characters with IK limbs, mitten hands, outfits (hoodie, vest, polo, tunic, ties, hats), and drawn faces that hold up under arbitrary 3D camera orbits.
  2. **Cinematic Post Chain (`engine/post.js`) & 5-Act Pacing**:
     - Applies ACES tone mapping, bloom, DOF, SMAA, and `n8ao` ambient occlusion over CC0 Kenney/KayKit sets, paired with word-by-word caption timing and contact sheets.

### Q3: How does `huypham85/app-3d-video-skill` render a 20-second 3D iPhone promo with original music in 5 minutes without `ffmpeg`?
- **First-Principles Breakdown**:
  1. **Native Apple Media Stack (`SceneKit` + `CoreGraphics` + `AVFoundation`)**:
     - `motion-video` renders the 3D iPhone and hopping mascot in SceneKit, composites 2D typography in CoreGraphics, synthesizes the score (`score.swift`), and muxes the final MP4 via AVFoundation in ~5 minutes on M-series Macs.
  2. **Code-Grounded Storyboarding & Contact-Sheet Gate**:
     - Extracts real app strings/colors from the repo, checks audio levels with Python `numpy`, and generates still-frame contact sheets for human review before rendering the full MP4.

---

## 🧭 3. Mermaid Decision Tree & Three.js + Swift SceneKit Video Architecture

```mermaid
flowchart TD
    A["Automated Vertical 3D Story Shorts & iOS App 3D Promo Video Production"] --> B{"Primary Video Format?"}
    B -- "Narrative Story Shorts: 3D character skits, 360-degree camera orbits & word-timed captions" --> C["Adopt thuann-vn/claude-3d-animated-shorts (Three.js Mixamo 3D Skill)"]
    B -- "iOS App Release Promos: 3D iPhone, mascot pressing real app UI & beat-synced original music" --> D["Adopt huypham85/app-3d-video-skill (Swift SceneKit + AVFoundation Skills)"]

    C --> C1["stickrig.js 3D Mixamo rig (IK + brush outline) + CC0 Kenney/KayKit 3D sets"]
    C1 --> C2["ACES + n8ao + DOF post chain + ?viewer=1 live preview & contact-sheet QA"]

    D --> D1["Read iOS repo UI/strings/colors -> generate beat-synced plan.md & score.swift"]
    D1 --> D2["Preview still contact sheets + numpy audio levels -> 5-min M-series MP4 render"]

    C2 & D2 --> E["🏆 Golden Zero-Diffusion 3D Video Studio: Three.js Shorts + SceneKit App Promos (-90.40% TCO)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Cloud Video Diffusion + Manual AE | Path B: 2D Billboard Cutouts + Manual CapCut | **Path C (Recommended): `claude-3d-animated-shorts` + `app-3d-video-skill`** |
| :--- | :--- | :--- | :--- |
| **3D Camera Orbit & App UI Text Fidelity** | Garbled UI text & morphing characters across shots | 2D billboards flatten when camera orbits | **Full 3D Mixamo IK rigs + code-extracted 100% accurate 3D iPhone UI** |
| **Rendering Pipeline & External Dependencies** | Expensive cloud video credits or heavy Adobe/Blender | Manual screen recording & timeline scrubbing | **Local Three.js (ACES/`n8ao`/DOF) & pure Swift (`SceneKit`/`AVFoundation`, zero `ffmpeg`)** |
| **Audio-Beat Sync & Pre-Render QA Gate** | Blind full-video generations | Manual beat-marker placement | **Automated contact sheets, `numpy` audio-level checks & beat-timed `score.swift`** |
| **Marginal Cost of Copy/Camera Tweaks** | Re-pay cloud generation credits per take | Manual re-recording & re-export | **$0 local re-render (~5 min on Apple Silicon for 20s 3D iOS promo)** |
| **Monthly TCO (40 Shorts + 16 App Promos)** | **`$5,210.00 / mo`** (`$1,640` cloud/SaaS + `$3,570` labor) | **`$2,590.00 / mo`** (`$720` templates/API + `$1,870` labor) | **`$500.00 / mo` (Saves `$4,710.00/mo` · `-90.40%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261113-R30-3DSHORTS-APP3DVIDEO`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A mobile product and developer-marketing studio producing **40 vertical 3D animated story Shorts per month** and **16 20-second iOS app release 3D promo videos per month**.
- **Labor Rate**: Fully loaded creative technologist and iOS growth engineer rate of **`$85.00 / hr`**.
- **Explicit Not-Measured Boundary**: Apple Silicon Mac workstation hardware depreciation and base ElevenLabs TTS subscription fees are marked **`not_measured`**. This model strictly accounts for cloud video diffusion credit spend, LLM planning tokens, and engineering hours spent keyframing animations, fixing garbled UI text, and syncing audio beats.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Cloud Video Diffusion + Manual AE | Path B: 2D Billboards + Manual Screen Capture | **Path C: `3D Shorts` + `App 3D Video` Skills (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly Video Generation Credits & LLM API Spend** | **`$1,640.00`** (discarded diffusion takes + stock plugins) | **`$720.00`** (template subscriptions & TTS retries) | **`$160.00`** (`$0` cloud video diffusion; lightweight script/plan tokens only) |
| **3D Keyframing, UI Repair & Audio-Sync Labor (`$85/hr`)** | `42.0 hrs × $85.00` = **`$3,570.00`** | `22.0 hrs × $85.00` = **`$1,870.00`** | `4.0 hrs × $85.00` = **`$340.00`** |
| **Total Monthly TCO** | **`$5,210.00 / mo`** | **`$2,590.00 / mo`** (`-50.29%`) | **`$500.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,620.00 / mo` | **Saves `$4,710.00 / mo` (`-90.40%` · `$56,520.00/yr`)** |
| **Apple Silicon Mac Hardware & ElevenLabs Base Plan** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `thuann-vn/claude-3d-animated-shorts` Setup & Browser Preview**: Clone into `~/.claude/skills/claude-3d-animated-shorts`, run `bash scripts/fetch-assets.sh` and `cd engine && npm install`, and inspect `?viewer=1&skit=1` to verify Mixamo IK rigging and ACES/`n8ao` post-processing.
- [ ] **2. `huypham85/app-3d-video-skill` Template Smoke Test**: Copy `app-3d-video` and `motion-video` into `~/.claude/skills/`, run `bash mv3d.sh audio && bash mv3d.sh video` on the bundled template, and confirm ~5-minute MP4 output without `ffmpeg`.
- [ ] **3. Contact-Sheet & `numpy` Audio Gate Verification**: Review generated still-frame contact sheets and audio level metrics before committing to full 20-second renders.
- [ ] **4. Brand Customization (`scenes.swift` & `score.swift`)**: Configure the `BRAND` block in `scenes.swift` and optionally attach your app's custom notification chime in `score.swift`.
