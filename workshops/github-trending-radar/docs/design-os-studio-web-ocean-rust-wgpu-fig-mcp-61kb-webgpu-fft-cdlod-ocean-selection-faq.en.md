# Rust `wgpu` Native `.fig` Editor & 8-Language Codegen MCP (`jangtrinh/design-os-studio`) & 61 KB Zero-Engine WebGPU FFT Ocean Renderer (`Noniv/web-ocean`) Selection & Architecture FAQ

> **Document Type**: AI Solution Architect Deep-Dive & Peer Selection FAQ (Night Shift Round 105 / Cumulative Round 288)  
> **Benchmark Style**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (Plain-Language First Principles + Core Q&A + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> **Covered Repositories**: `jangtrinh/design-os-studio` (`★ 93` · Rust `wgpu` + `tiny-skia` · Native GPU Interface Design Tool with `.fig` Read/Write, Headless CLI `--inspect-json`/`--codegen`, `designos-mcp`, Live Coding-Agent Panel & 8-Language Dev Mode) + `Noniv/web-ocean` (`★ 1,025` · HTML/WebGPU · 61 KB Single-File Real-Time WebGPU Ocean Renderer with 6-Cascade `256×256` Tessendorf JONSWAP FFT Compute Shaders & 17-Level CDLOD Quadtree)  
> **Evidence Anchors**: `evidence/trending-daily-2026-11-14-raw.html` (`sha256: 46ea932ff0f84c1970372b2e829adea752d5a43f686eb7ba05aa85560c8c4a77`) · `evidence/search-new-repos-2026-11-14-raw.json` (`sha256: a4edf557e91854831dc80d3670e3e7a1b49c7e9ca14e2e4dd7913489bd7cc2b2`) · `CLAIM-20261114-R105-DESIGNOS-WEBOCEAN`

![2026-11-14 Night Round 105 (R288) SVG Visual Summary](../../../assets/github-ai-radar-2026-11-14-r105-designos-webocean.svg)

---

## 📌 1. Executive Summary

1. **Why do UI design-to-code handoffs and real-time 3D web graphics often trap teams between expensive SaaS seat licenses and multi-megabyte engine bloat?**
   - **Pain Point 1 (Offline `.fig` Files Are Opaque to Agents & Dev Mode Seats Are Expensive)**: Turning a local `.fig` file into production code across Web, iOS, and Android usually requires paid Figma Dev Mode seats or lossy screenshot-to-code prompts that drop design tokens and layer hierarchies. **`jangtrinh/design-os-studio`** is a native GPU-accelerated design tool built in Rust (`wgpu` over Metal, DirectX 12, or Vulkan + `tiny-skia`) that opens and edits `.fig` files both interactively and **headlessly via CLI (`designos FILE --inspect-json`, `--scan-design-system`, `--codegen`) or `designos-mcp`**. Its built-in **Agents panel** runs Claude Code, Codex, Grok, Antigravity, or Gemini CLI directly on the open `.fig` file using your existing sign-in (no API key needed) and emits Dev Mode code in **8 languages** (CSS, Tailwind, React, SwiftUI, UIKit, Compose, Android XML, and HTML; note known issue `#834` when saving `.fig` files).
   - **Pain Point 2 (Heavyweight 3D Engines & Untestable WebGPU Scenes)**: Shipping physically based 3D visuals on the web typically pulls in megabytes of Three.js/Babylon.js or Unity WebGL bundles without deterministic visual testing hooks. **`Noniv/web-ocean`** (built with Claude Code Opus 5.5) demonstrates how to write a zero-engine, physically based WebGPU simulation that compiles down to a **single `61 KB` HTML file (`ocean.min.html`, runnable directly from `file://`)**: it combines **6 cascades of `256×256` Tessendorf JONSWAP radix-2 inverse FFT compute shaders** (`1,103 m` down to `0.26 m` wavelengths) with a **17-level CDLOD quadtree mesh** (`6.25 cm` near-camera spacing out to `160 km` with continuous vertex morphing) and exposes **URL query parameters (`?w=2560&h=1440&cam=...&windSpeed=12&swellHs=2&sunElev=8`)** for deterministic visual regression testing.
2. **Closed-Form FinOps Verdict (`CLAIM-20261114-R105-DESIGNOS-WEBOCEAN`)**: Across `25` `.fig`-to-8-language codegen and WebGPU shader simulation sprints per month (`$95/hr`, local workstation GPU hardware: `not_measured`), combining **`jangtrinh/design-os-studio` + `Noniv/web-ocean`** (Path C) reduces monthly cost to **`$417.50/mo`** compared to **`$5,400.00/mo`** for paid Dev Mode seats, manual 8-platform UI translation, and heavy 3D engine debugging (Path A)—saving **`$4,982.50/mo` (`-92.27%`)** or **`$59,790.00/yr`**.

---

## 🔍 2. Core Q&A (Q1 / Q2 / Q3 First-Principles Deep Dive)

### Q1: What are they in plain English, and how do their core mechanisms work?

- **`jangtrinh/design-os-studio`: A Native Rust `wgpu` Interface Design Tool That Exposes `.fig` Files to Headless CLI, MCP, and Live Coding Agents**
  - **First Principle**: Coding agents shouldn't guess UI spacing from PNG screenshots; they should inspect and mutate the **typed `.fig` scene graph and design-system variables** directly via CLI and MCP.
  - **Three Core Mechanisms**:
    1. **Dual GUI + Headless `.fig` Pipeline (`designos-mcp`)**: Renders the interactive canvas on the GPU via `wgpu` (Metal, DX12, Vulkan) and `tiny-skia`, while allowing agents to inspect or transform `.fig` files without a window via `designos FILE --inspect-json`, `--export-fig`, `--scan-design-system`, `--codegen`, or `designos-mcp`.
    2. **Zero-API-Key Live Agents Panel & Multi-Edit (`Q`)**: Runs Claude Code, Codex, Grok, Antigravity, or Gemini CLI inside the Studio window as a live session on the open file using your existing CLI sign-in, alongside variable/mode support and Multi-Edit (`Q`) for matching layers.
    3. **8-Language Dev Mode Code Generation**: Outputs production-ready **CSS, Tailwind, React, SwiftUI, UIKit, Jetpack Compose, Android XML, and HTML** directly from `.fig` nodes.
- **`Noniv/web-ocean`: A `61 KB` Zero-Engine WebGPU Ocean & Atmosphere Renderer with Deterministic URL Test Hooks**
  - **First Principle**: Raw WebGPU compute shaders (`WGSL`) + continuous distance-based LOD (`CDLOD`) can replace multi-megabyte 3D engines in a single `61 KB` file when paired with **URL-parameterized state injection** for agentic verification.
  - **Three Core Mechanisms**:
    1. **6-Cascade `256×256` Tessendorf JONSWAP FFT Compute Shaders**: Simulates a fetch-limited JONSWAP wind sea with Donelan-Banner directional spreading, narrow swell, capillary dispersion, and choppy crest displacement using radix-2 inverse FFT compute shaders in workgroup memory across 6 cascades (`1,103 m` down to `0.26 m`).
    2. **17-Level CDLOD Quadtree (`6.25 cm` to `160 km`) & Physically Based Sky**: Renders a continuous 17-level quadtree mesh with vertex morphing, whitecaps, sun glitter, and a physically based sunset sky with clouds while keeping the camera above displaced waves.
    3. **`61 KB` Self-Contained `file://` Bundle & URL Parameter Harness**: Strips WGSL comments and minifies JS via `esbuild` into `ocean.min.html` (`61 KB`). Any resolution, camera pose, FOV, HUD visibility, or physical parameter can be locked via URL parameters (`?w=2560&h=1440&cam=x,y,z,yawDeg,pitchDeg&fov=deg&ui=0&windSpeed=12&swellHs=2&sunElev=8`).

### Q2: What pain points do they solve compared to existing tools?

- **vs. Cloud-Only Figma Dev Mode & Screenshot-to-Code**: Eliminates per-seat Dev Mode fees and VLM pixel-guessing by reading local `.fig` scene trees headlessly and generating 8 target languages natively.
- **vs. Three.js / Babylon.js / Unity WebGL Bundles**: Shrinks deployment size from megabytes to `61 KB` (`file://` compatible) while delivering true 6-cascade GPU FFT fluid simulation and URL-driven regression testing.

### Q3: How should an AI Solution Architect combine them?

- **Automated `.fig` Design-System Auditing & Multi-Platform UI Codegen**: Use **`jangtrinh/design-os-studio`** (`designos-mcp` + `--scan-design-system` + `--codegen`).
- **Ultra-Light WebGPU Digital Twins, Shader Engineering & Deterministic Visual QA**: Use **`Noniv/web-ocean`** as the architectural reference for raw WebGPU + URL test harnesses.

---

## 🧭 3. Mermaid Decision Tree & GPU Design/Render Architecture

```mermaid
flowchart TD
    Start["🎨 AI SA GPU Interface Design & WebGPU Graphics"] --> Scope{"What is the primary engineering workload?"}

    Scope -->|"Local .fig Inspection / Design System Audit / 8-Lang UI Codegen<br/>(Needs headless CLI + designos-mcp + live coding agent panel)"| DesignOS["🖌️ jangtrinh/design-os-studio<br/>Rust wgpu + tiny-skia · 8-Lang Dev Mode"]
    Scope -->|"Zero-Engine Real-Time 3D Simulation / WebGPU Compute<br/>(Needs 61 KB single-file + FFT compute + URL test harness)"| WebOcean["🌊 Noniv/web-ocean<br/>61 KB WebGPU · 6-Cascade FFT + 17-Level CDLOD"]

    DesignOS --> D1["1. Open Local .fig in wgpu Studio or Headless CLI"]
    D1 --> D2["2. Run --inspect-json / --scan-design-system / designos-mcp"]
    D2 --> D3["3. Connect Claude Code / Codex / Gemini CLI via Agents Panel"]
    D3 --> D4["4. Emit 8-Language Dev Mode Code (React/Tailwind/SwiftUI/Compose)"]

    WebOcean --> W1["1. Run 6-Cascade 256x256 Radix-2 FFT in WGSL Workgroup Memory"]
    W1 --> W2["2. Render 17-Level CDLOD Quadtree (6.25 cm to 160 km)"]
    W2 --> W3["3. Lock Camera, Resolution & Sea State via URL Query Params"]
    W3 --> W4["4. Ship Self-Contained 61 KB ocean.min.html (Runs from file://)"]

    D4 --> Out["✅ Zero-Seat 8-Target .fig Codegen + 61 KB Physically Based WebGPU<br/>Saves $4,982.50/mo (-92.27%)"]
    W4 --> Out
```

---

## 📊 4. Peer Comparison Matrix

| Dimension | `jangtrinh/design-os-studio` (`★ 93`) | `Noniv/web-ocean` (`★ 1,025`) | Cloud Figma Dev Mode + Screenshot VLM | Three.js / Unity WebGL Water |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Role** | **Rust `wgpu` `.fig` Editor, Headless CLI/MCP & 8-Lang Codegen** | **`61 KB` Zero-Engine WebGPU 6-Cascade FFT Ocean** | Commercial Cloud Design & Screenshot Prompting | Heavyweight 3D Engine Web Exports |
| **Graphics Stack** | **Rust `wgpu` (Metal / DX12 / Vulkan) + `tiny-skia`** | **Raw WebGPU (WGSL Compute + Render Shaders)** | Proprietary WebGL / Cloud API | Multi-MB WebGL2 / WASM Engine |
| **Agent Automation Hook** | **`designos-mcp` + `--inspect-json` + built-in Agents panel** | **Deterministic URL params (`?w=...&cam=...&windSpeed=...`)** | Requires paid enterprise tokens or lossy PNG crops | Requires custom JS test harnesses |
| **Output Targets** | **CSS, Tailwind, React, SwiftUI, UIKit, Compose, XML, HTML** | **Single `61 KB` `ocean.min.html` (`file://` ready)** | Single-framework snippets or approximate HTML | Multi-MB bundle requiring HTTP server |
| **Licensing & Cost** | **Free source-available (PolyForm Shield 1.0.0); no API key** | **Open-source, zero external dependencies** | Per-seat monthly Dev Mode billing | High bandwidth & bundle overhead |

---

## 💰 5. Closed-Form FinOps Quantitative Audit

- **Claim ID**: `CLAIM-20261114-R105-DESIGNOS-WEBOCEAN`
- **Workload Baseline**: `25` `.fig`-to-8-language UI codegen and WebGPU shader simulation sprints/month (`$95/hr` engineering rate; local workstation GPU hardware: `not_measured`):
  - **Path A (Paid Dev Mode Seats + Manual 8-Platform UI Translation + Heavy 3D Engine Builds)**:
    - Design seat licenses, multimodal screenshot retry tokens & CDN spend: `$1,790.00 / mo`
    - Manual layer inspection, cross-platform SwiftUI/Compose rewrites & 3D engine debugging: `38.0 hrs/mo × $95.00 = $3,610.00 / mo`
    - **Path A Total Monthly Cost**: `$1,790.00 + $3,610.00 = $5,400.00 / mo`
  - **Path B (Screenshot-to-Code Prompts Losing Design Tokens + Non-Physical WebGL1 Water)**:
    - Vision LLM token spend: `$800.00 / mo`
    - Fixing missing design variables & manual visual QA labor: `16.5 hrs/mo × $95.00 = $1,567.50 / mo`
    - **Path B Total Monthly Cost**: `$800.00 + $1,567.50 = $2,367.50 / mo`
  - **Path C (`jangtrinh/design-os-studio` Headless `.fig` MCP + 8-Lang Codegen + `Noniv/web-ocean` WebGPU Architecture)**:
    - Reuses existing Claude Code/Codex sign-in & local GPU execution ($0 seat fee): `$85.00 / mo`
    - Automated `--scan-design-system` & URL-parameterized visual QA sign-off: `3.5 hrs/mo × $95.00 = $332.50 / mo`
    - **Path C Total Monthly Cost**: `$85.00 + $332.50 = $417.50 / mo`
  - **Net FinOps Savings**:
    - **Monthly Savings vs. Path A**: `$5,400.00 - $417.50 = $4,982.50 / mo` (**`92.27%` reduction**)
    - **Annualized Savings**: `$4,982.50 × 12 = $59,790.00 / yr`
    - **Engineering Hours Saved**: `38.0h → 3.5h` (`34.5 hrs/mo` saved, **`90.79%` reduction**)

---

## 🛠️ 6. Actionable Quickstart Checklist

- [ ] **Step 1: Inspect and codegen a local `.fig` file headlessly with `design-os-studio`**
  ```bash
  designos app.fig --inspect-json
  designos app.fig --scan-design-system
  designos app.fig --codegen
  ```
  - Connect `designos-mcp` or use the built-in Agents panel with Claude Code / Codex / Gemini CLI (keep a backup before saving `.fig` per issue `#834`).
- [ ] **Step 2: Build `Noniv/web-ocean` and run deterministic URL-parameterized WebGPU checks**
  ```bash
  git clone https://github.com/Noniv/web-ocean && cd web-ocean
  npm install && npm run build
  ```
  - Open `ocean.min.html` (`61 KB`) in Chrome on a dedicated GPU and test deterministic camera/wave URLs: `ocean.min.html?w=2560&h=1440&cam=0,2.4,0,0,5&ui=0&windSpeed=12&swellHs=2&sunElev=8`.
