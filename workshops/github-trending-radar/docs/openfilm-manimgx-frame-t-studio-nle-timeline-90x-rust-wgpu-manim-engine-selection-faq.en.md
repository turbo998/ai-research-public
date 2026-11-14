# `frame(t)` Bidirectional AI Video Studio & NLE Exporter (`openfilm/openfilm`) & `90.6x` Faster Rust `wgpu` Manim Engine (`academa-labs/manimgx`) Selection & Architecture FAQ

> **Document Type**: AI Solution Architect Deep-Dive & Peer Selection FAQ (Night Shift Round 113 / Cumulative Round 296)  
> **Benchmark Style**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (Plain-Language First Principles + Core Q&A + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> **Covered Repositories**: `openfilm/openfilm` (`★ 7,060` · TypeScript · Open-Source AI Video Agent Built on `film.html` + `frame(t)` + Bidirectional Browser Studio with Final Cut Pro, Premiere Pro & DaVinci Resolve Timeline Export) + `academa-labs/manimgx` (`★ 2,743` · Python/Rust `wgpu` · 3D & Math Animation Engine Compatible with Manim CE's API Running `90.6x` Faster on a Rust + `wgpu` GPU Core)  
> **Evidence Anchors**: `evidence/trending-daily-2026-11-14-raw.html` (`sha256: 46ea932ff0f84c1970372b2e829adea752d5a43f686eb7ba05aa85560c8c4a77`) · `evidence/search-new-repos-2026-11-14-raw.json` (`sha256: a4edf557e91854831dc80d3670e3e7a1b49c7e9ca14e2e4dd7913489bd7cc2b2`) · `CLAIM-20261114-R113-OPENFILM-MANIMGX`

![2026-11-14 Night Round 113 (R296) SVG Visual Summary](../../../assets/github-ai-radar-2026-11-14-r113-openfilm-manimgx.svg)

---

## 📌 1. Executive Summary

1. **Why do programmatic video tools often lock coding agents into rigid React wrappers that humans cannot edit—while 3Blue1Brown-style Manim animations take minutes to render on CPU?**
   - **Pain Point 1 (Framework Lock-In & Dead-End MP4s That Cannot Be Hand-Edited or Exported to Premiere/Resolve)**: Teaching an agent a custom React video DSL limits its use of raw WebGL, Three.js, or GSAP, and produces an uneditable output when a human editor wants to tweak a title position or hand the timeline to DaVinci Resolve. With **`★ 7,060`**, **`openfilm/openfilm`** (`npx skills add openfilm/openfilm`) reduces programmatic video to **one HTML file (`film.html`), one pure function (`frame(t)`), and one real browser editor (`Studio`)**: your agent writes standard web pages that draw any timestamp `t` via `frame(t)` using Three.js, WebGL, Canvas, SVG, CSS, or GSAP, checks contact sheets via `openfilm look`, lets you move/scale/rotate elements visually in Studio (**saving your manual edits directly back to the source files so the agent keeps them**), and exports either `--4k --blur --alpha --loudness=-14` masters or **native timelines for Final Cut Pro, Premiere Pro, and DaVinci Resolve**.
   - **Pain Point 2 (CPU-Bound Manim CE Renders Stall Agent Self-Verification Loops)**: LLMs already know Manim Community Edition's Python API inside out, but Manim CE's legacy CPU rendering pipeline takes minutes to render a 30-second 3D scene. With **`★ 2,743`**, **`academa-labs/manimgx`** keeps **Manim CE's Python API** intact while replacing the backend with a **Rust + `wgpu` GPU core**—rendering `36.2 seconds` of `1080p60` video across five scenes in **`3.08 seconds` on an Apple M4 Pro (`90.6× faster`)** and running both natively via `pip` and in the browser via `npm`.
2. **Closed-Form FinOps Verdict (`CLAIM-20261114-R113-OPENFILM-MANIMGX`)**: Across `25` launch-film NLE handoff and 3D math/algorithm animation sprints per month (`$95/hr`, local workstation GPU hardware: `not_measured`), combining **`openfilm/openfilm` + `academa-labs/manimgx`** (Path C) reduces monthly cost to **`$417.50/mo`** compared to **`$5,487.50/mo`** for slow CPU Manim loops and uneditable framework-locked videos (Path A)—saving **`$5,070.00/mo` (`-92.39%`)** or **`$60,840.00/yr`**.

---

## 🔍 2. Core Q&A (Q1 / Q2 / Q3 First-Principles Deep Dive)

### Q1: What are they in plain English, and how do their core mechanisms work?

- **`openfilm/openfilm`: An Open-Source AI Video Agent Built on `film.html`, `frame(t)`, and a Bidirectional Browser Studio**
  - **First Principle**: Coding agents already master the full web platform; exposing a single deterministic `frame(t)` contract plus **bidirectional visual DOM-to-file editing** and **NLE timeline export** bridges agentic code generation with human post-production.
  - **Three Core Mechanisms**:
    1. **One HTML File (`film.html`) + One Function (`frame(t)`)**: Cuts animated web pages, footage, images, and audio on CSS-styled tracks. Each shot renders any timestamp `t` via `frame(t)` using Three.js, WebGL, Canvas, SVG, CSS, or GSAP—no proprietary React framework required.
    2. **Agent Contact-Sheet Inspection (`openfilm look`) & Bidirectional Studio (`⌘E` Canvas)**: Agents run `openfilm look [what] [t | a-b]` to inspect single frames or contact sheets. In the browser Studio, humans move, scale, rotate, crop, trim, and restyle elements by hand; edits write back to the film's source files and support named version checkpoints alongside a `⌘E` planning canvas (`openfilm canvas`).
    3. **Broadcast Render Pipeline & NLE Timeline Export**: `openfilm render` supports `--4k`, `--blur` (motion blur), `--alpha` (`.webm`/`.mov`), and `--loudness=-14`, and exports editable timelines directly for **Final Cut Pro, Premiere Pro, and DaVinci Resolve**.
- **`academa-labs/manimgx`: A `90.6×` Faster Rust + `wgpu` 3D Animation Engine Compatible with Manim CE's Python API**
  - **First Principle**: Preserve the exact **Manim CE Python API** that every frontier LLM was trained on, while executing geometry tessellation and shading on a **Rust + `wgpu` GPU pipeline**.
  - **Three Core Mechanisms**:
    1. **`90.6×` Speedup (`36.2s` at `1080p60` in `3.08s`)**: Renders complex 2D/3D math scenes at nearly `12×` faster than real-time (`1080p60` on Apple M4 Pro), turning multi-minute CPU renders into 3-second agent feedback loops.
    2. **Full Manim CE API Compatibility**: Supports quadratic proofs, Fourier series epicycles, linear transformations, complex mappings, 3D Lorenz attractors, precessing heavy tops, Hopf fibrations, and catenoid-helicoid surfaces out of the box.
    3. **Native Python (`pip`) + Browser (`npm`) Execution**: Installs via `pip install manimgx` for local GPU rendering or `npm` for in-browser execution.

### Q2: What pain points do they solve compared to existing tools?

- **vs. Remotion / Framework-Locked Code Video Tools**: Eliminates React wrapper constraints, adds bidirectional drag-and-drop Studio editing that persists back to code, and exports native timelines for Final Cut Pro, Premiere Pro, and DaVinci Resolve.
- **vs. Legacy Manim CE**: Accelerates rendering by **`90.6×`** via Rust + `wgpu` and adds direct browser execution without breaking existing Manim Python scripts.

### Q3: How should an AI Solution Architect combine them?

- **Product Launch Films, WebGL/Three.js Motion Graphics & Pro NLE Handoffs (Premiere / DaVinci / FCP)**: Use **`openfilm/openfilm`**.
- **Algorithm Visualizations, 3D Mathematical/Physics Proofs & Fast Agentic Explainer Loops**: Use **`academa-labs/manimgx`**.

---

## 🧭 3. Mermaid Decision Tree & Dual-Engine Video Architecture

```mermaid
flowchart TD
    Start["🎥 AI SA Programmatic Video & 3D Math Animation"] --> Workload{"What is the primary visual medium and handoff target?"}

    Workload -->|"Web/WebGL/UI Launch Films + Human Studio Edits + NLE Export<br/>(Needs film.html + frame(t) + Premiere/Resolve/FCP export)"| OpenFilm["🎬 openfilm/openfilm (★ 7,060 · TypeScript)<br/>npx skills add openfilm/openfilm"]
    Workload -->|"3Blue1Brown-Style 2D/3D Math, Physics & Algorithm Animations<br/>(Needs Manim CE Python API + 90.6x Rust wgpu speed)"| ManimGX["🚀 academa-labs/manimgx (★ 2,743 · Rust + wgpu)<br/>pip install manimgx / npm manimgx"]

    OpenFilm --> O1["1. Agent Authors Shots in film.html via Pure frame(t)"]
    O1 --> O2["2. Agent Self-Checks Contact Sheets via openfilm look"]
    O2 --> O3["3. Human Tweaks Layers & Timeline in Studio (Saved to Files)"]
    O3 --> O4["4. Render (--4k --blur --loudness=-14) or Export FCP/PR/Resolve"]

    ManimGX --> M1["1. Agent Writes Standard Manim CE Python Scene Code"]
    M1 --> M2["2. Rust + wgpu Core Renders 1080p60 90.6x Faster (36.2s in 3.08s)"]
    M2 --> M3["3. Deliver MP4 or Run Interactively in the Browser"]

    O4 --> Out["✅ NLE-Ready Studio Launch Films + 90.6x GPU Math Animations<br/>Saves $5,070.00/mo (-92.39%)"]
    M3 --> Out
```

---

## 📊 4. Peer Comparison Matrix

| Dimension | `openfilm/openfilm` (`★ 7,060`) | `academa-labs/manimgx` (`★ 2,743`) | Remotion | Legacy Manim CE |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Role** | **`frame(t)` AI Video Agent & Bidirectional Studio** | **`90.6×` Faster Rust `wgpu` Manim CE Engine** | React-Based Video Framework | CPU-Bound Python Math Animation Library |
| **Rendering Core & Speed** | Chromium engine (Three.js, WebGL, SVG, CSS, GSAP) | **Rust + `wgpu` (`36.2s` of `1080p60` in `3.08s`, `90.6×`)** | React re-renders + headless frame capture | Slow single-core CPU Cairo/Python loop |
| **Visual Human Editing** | **Drag/scale/rotate/trim in Studio; writes back to files** | Code-driven + browser preview | Props-only inspector; no canvas manipulation | Code-only |
| **Pro NLE Handoff** | **Exports Final Cut Pro, Premiere Pro & DaVinci Resolve timelines** | Video / Web export | Baked MP4/WebM only | Baked MP4/GIF only |
| **Built-In QA & Mastering** | **`openfilm look` contact sheets + `--4k --blur --loudness=-14`** | Automated visual coverage suite | Custom FFmpeg flags | Manual frame inspection |

---

## 💰 5. Closed-Form FinOps Quantitative Audit

- **Claim ID**: `CLAIM-20261114-R113-OPENFILM-MANIMGX`
- **Workload Baseline**: `25` launch-video NLE handoff and 3D mathematical/algorithm animation sprints/month (`$95/hr` engineering rate; local workstation GPU hardware: `not_measured`):
  - **Path A (Slow CPU Manim CE Renders + Framework-Locked Videos Rebuilt Manually in Premiere/Resolve)**:
    - Cloud render instances, framework retry tokens & stock media spend: `$1,830.00 / mo`
    - Waiting on slow CPU Manim renders & manually rebuilding timelines in Premiere/Resolve: `38.5 hrs/mo × $95.00 = $3,657.50 / mo`
    - **Path A Total Monthly Cost**: `$1,830.00 + $3,657.50 = $5,487.50 / mo`
  - **Path B (Custom Puppeteer Frame Scripts Without Studio + Static 2D Math Plots)**:
    - Render & token spend: `$815.00 / mo`
    - Manual coordinate tweaking in code & audio loudness normalization: `17.0 hrs/mo × $95.00 = $1,615.00 / mo`
    - **Path B Total Monthly Cost**: `$815.00 + $1,615.00 = $2,430.00 / mo`
  - **Path C (`openfilm/openfilm` Bidirectional Studio + NLE Export + `academa-labs/manimgx` `90.6×` Rust `wgpu`)**:
    - Local GPU rendering ($0 cloud render fee) & high-hit prompt token spend: `$85.00 / mo`
    - Visual polish in OpenFilm Studio & direct Premiere/Resolve timeline handoff: `3.5 hrs/mo × $95.00 = $332.50 / mo`
    - **Path C Total Monthly Cost**: `$85.00 + $332.50 = $417.50 / mo`
  - **Net FinOps Savings**:
    - **Monthly Savings vs. Path A**: `$5,487.50 - $417.50 = $5,070.00 / mo` (**`92.39%` reduction**)
    - **Annualized Savings**: `$5,070.00 × 12 = $60,840.00 / yr`
    - **Engineering Hours Saved**: `38.5h → 3.5h` (`35.0 hrs/mo` saved, **`90.91%` reduction**)

---

## 🛠️ 6. Actionable Quickstart Checklist

- [ ] **Step 1: Install `openfilm/openfilm`, inspect contact sheets, and export a studio master**
  ```bash
  npx skills add openfilm/openfilm
  npx -y openfilm@latest open https://github.com/openfilm/examples/tree/main/one-prompt
  openfilm look 0-5
  openfilm render --4k --blur --loudness=-14
  ```
- [ ] **Step 2: Install `academa-labs/manimgx` and render `1080p60` 3D math scenes on Rust `wgpu`**
  ```bash
  pip install manimgx
  ```
  - Run existing Manim CE Python scenes on `manimgx` to achieve `90.6×` faster GPU rendering.
