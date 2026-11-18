# Editable VFML Viral Video Studio (`fendouai/ViralForge` `v0.1.0`) & Budget-Capped Autonomous 3D FPS Repro (`wquguru/fable52-fps-repro`) Selection FAQ

> **Document Scope**: This is the **2026-11-13 Night Shift Round 15 (Cumulative #143) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects, Growth Engineering Leads, and Creative Technologists evaluating two reproducible media and 3D code-generation pipelines:
> 1. **`fendouai/ViralForge` (`93★` in 2 days, TypeScript, Apache-2.0, `v0.1.0`, Node 22.15+, MCP Server + Agent Skill)**: An agent-native studio for viral short videos that deconstructs any reference clip into a **7-part Viral DNA report** (hook, shot-by-shot structure, word anchors, beat grid, caption style, emotional curve, conversion logic), compiles it into an **editable VFML (ViralForge Markup Language) project**, and generates **10 costed variants for A/B testing** in one click!
> 2. **`wquguru/fable52-fps-repro` (`87★` in 2 days, HTML / Shell / Python, MIT, Claude Code 2.1.242+ & `claude-fable-5-2`)**: A transparent one-prompt 3D FPS reproduction benchmark shipping 4 playable single-file HTML experiments (`01-audio` 5m cache vs `01-audio-1h` 1h cache, `02-materials`, `03-models`, and `04-fps` **SUBLEVEL 07** — a `131 KB` single-HTML 3D shooter built in **73 autonomous turns for `$15.96` API cost**), complete with `--max-budget-usd` caps (`scripts/run.sh`), audited cache metrics (`data/metrics.tsv`), isolated `agent-browser` visual self-checks (`builder_system_04.md`), and deterministic frame-by-frame recording via `window.__dbg.step` (`scripts/rec/`)!
>
> **中文版本**: [viralforge-fable52-fps-repro-vfml-video-studio-budget-capped-3d-fps-selection-faq.md](viralforge-fable52-fps-repro-vfml-video-studio-budget-capped-3d-fps-selection-faq.md) · **Daily Digest**: [`daily/2026-11-13.en.md`](../daily/2026-11-13.en.md) · **Topic SVG**: [`assets/github-ai-radar-2026-11-13-r15-viralforge-fable52fps.svg`](../../../assets/github-ai-radar-2026-11-13-r15-viralforge-fable52fps.svg)

![fendouai/ViralForge v0.1.0 and wquguru/fable52-fps-repro Architecture Comparison](../../../assets/github-ai-radar-2026-11-13-r15-viralforge-fable52fps.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "black-box AI video generators that spit out uneditable MP4s and manual timeline scrubbing when producing 10 A/B ad variants from a winning short video" (`fendouai/ViralForge` `v0.1.0`)**: Instead of treating a viral video as opaque pixels, `ViralForge` extracts its **Viral DNA** (hook, shot-by-shot structure, word anchors, beat grid, caption style, emotional curve, conversion logic) and rebuilds it as an **editable VFML project**. Swap the product and script once, and it compiles **10 costed A/B variants** via FFmpeg + MCP/Skill!
   - **Ending "opaque 'one-prompt 3D game' demos that hide their system prompts, runaway token bills, cache-TTL economics, and browser visual QA loops" (`wquguru/fable52-fps-repro`)**: `fable52-fps-repro` open-sources all 4 single-file HTML experiments (culminating in the `131 KB` `04-fps` SUBLEVEL 07 3D shooter built in **73 hands-free turns for `$15.96`**), the exact prompts (`prompts/01–04`), `--max-budget-usd` runner (`scripts/run.sh`), 5m vs 1h prompt-cache telemetry (`data/metrics.tsv`), isolated `agent-browser` self-check rules, and a deterministic `window.__dbg.step` frame recorder!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261113-R15-VIRALFORGE-FABLE52FPS`)**:
   - Modeled for a **growth marketing and interactive web studio producing `60 short-video campaigns (600 A/B variants) per month` and `25 interactive 3D browser demos per month`** (fully loaded creative technologist / growth engineer rate `$85.00/hr`; paid social ad media spend and physical camera gear: `not_measured`):
   - Upgrading from **Path A (black-box video diffusion slot-machines for 600 variants + uncapped multi-turn 3D vibe-coding, `$5,680.00/mo`)** to **Path C (`ViralForge v0.1.0` VFML 10-variant studio + `fable52-fps-repro` `--max-budget-usd` / `agent-browser` / `__dbg.step` harness, `$555.00/mo`)** saves **`$5,125.00/mo` (`-90.23%`, or `$61,500.00/yr`)** and cuts manual timeline editing and 3D debugging labor from `44.0 hrs/mo` to `4.0 hrs/mo` (**`-90.91%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why do black-box MP4 generators and uncapped multi-turn 3D prompts burn budgets in production?
- **First-Principles Breakdown**:
  1. **Uneditable MP4s Break Systematic A/B Testing**: Growth teams need to test 10 hooks/scripts against the exact same beat grid and shot timing; regenerating full videos from scratch destroys structural consistency and multiplies API costs 10×.
  2. **Uncapped Long-Horizon Loops & Real-Time Capture Jitter**: Running 70+ autonomous coding turns without `--max-budget-usd`, prompt-cache TTL tuning (`5m` vs `1h`), or isolated visual self-inspection risks runaway spend and broken WebGL shaders.

### Q2: How does `fendouai/ViralForge` (`v0.1.0`) turn viral videos into editable VFML projects and 10 costed variants?
- **First-Principles Breakdown**:
  1. **7-Axis Viral DNA Extraction**:
     - Deconstructs reference videos into hook, shot-by-shot structure, word anchors, beat grid, caption style, emotional curve, and conversion logic.
  2. **Editable VFML Intermediate Representation & MCP/Skill Surface**:
     - Compiles the deconstructed structure into an editable VFML project and renders 10 costed variants for A/B testing via Node 22.15+, FFmpeg, MCP, and Agent Skills.

### Q3: What engineering patterns enable `wquguru/fable52-fps-repro` to build a `131 KB` 3D FPS in 73 autonomous turns for `$15.96`?
- **First-Principles Breakdown**:
  1. **Hard `--max-budget-usd` Ceiling & 5m vs. 1h Cache Audit (`data/metrics.tsv`)**:
     - `scripts/run.sh` enforces a strict dollar cap per run and logs 5-minute (`01-audio`) vs. 1-hour (`01-audio-1h`) cache hit economics via `scripts/metrics.py`.
  2. **Isolated `agent-browser` Visual Self-Check & Deterministic `__dbg.step` Recording**:
     - `builder_system_04.md` instructs the agent to inspect its own WebGL output in an isolated `agent-browser` session, while `scripts/rec/` calls `window.__dbg.step` to advance and record frames deterministically.

---

## 🧭 3. Mermaid Decision Tree & VFML Video Studio + Budget-Capped 3D FPS Architecture

```mermaid
flowchart TD
    A["Short-Video A/B Replication & Autonomous 3D WebGL Generation Selection"] --> B{"Primary Creative Engineering Goal?"}
    B -- "Deconstruct viral videos & ship 10 editable A/B variants per product" --> C["Adopt fendouai/ViralForge (v0.1.0 Viral DNA + VFML + MCP/Skill)"]
    B -- "Autonomously generate single-file 3D WebGL games/demos with strict budget & visual QA" --> D["Adopt wquguru/fable52-fps-repro (--max-budget-usd + __dbg.step)"]

    C --> C1["Extract 7-axis Viral DNA (hook, beat grid, word anchors, emotional curve)"]
    C1 --> C2["Compile to editable VFML project -> render 10 costed A/B variants"]

    D --> D1["scripts/run.sh enforces 5m/1h cache policy & --max-budget-usd ceiling"]
    D1 --> D2["Isolated agent-browser self-check + deterministic __dbg.step frame capture ($15.96 / 73 turns)"]

    C2 & D2 --> E["🏆 Golden Creative Stack: VFML Structural Remix + Budget/Frame-Locked 3D Generation (-90.23% TCO)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Black-Box Video Diffusion + Uncapped 3D Loops | Path B: Manual CapCut Clones + Single-Turn Three.js | **Path C (Recommended): `ViralForge v0.1.0` + `fable52-fps-repro`** |
| :--- | :--- | :--- | :--- |
| **Short-Video Structural Control** | Uneditable MP4s; loses beat grid across variants | Slow manual timeline slicing | **7-axis Viral DNA report → editable VFML → 10 costed A/B variants** |
| **3D Generation Budget & Cache Control** | Uncapped token burn; unmeasured cache misses | Shallow 1-turn geometry | **Hard `--max-budget-usd` cap + audited 5m/1h `metrics.tsv` (`$15.96` / 73 turns)** |
| **Visual QA & Deterministic Recording** | Blind code output; stuttery real-time screen capture | Manual browser reloads | **Isolated `agent-browser` self-check + deterministic `window.__dbg.step` recorder** |
| **Agent Integration Surface** | Manual web UI only | Copy-paste snippets | **Native MCP Server + Agent Skill + reproducible `scripts/run.sh`** |
| **Monthly TCO (600 Variants + 25 3D Demos)** | **`$5,680.00 / mo`** (`$1,940` API + `$3,740` labor) | **`$2,860.00 / mo`** (`$820` API + `$2,040` labor) | **`$555.00 / mo` (Saves `$5,125.00/mo` · `-90.23%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261113-R15-VIRALFORGE-FABLE52FPS`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A growth and interactive studio producing **60 short-video campaigns (600 A/B variants) per month** and **25 interactive single-file 3D browser demos per month**.
- **Labor Rate**: Fully loaded creative technologist / growth engineering rate of **`$85.00 / hr`**.
- **Explicit Not-Measured Boundary**: Paid social media ad-buy spend and physical camera equipment capex are marked **`not_measured`**. This model strictly accounts for video/LLM generation API bills and engineering hours spent re-cutting variants and debugging 3D WebGL scenes.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Black-Box Video Diffusion + Uncapped 3D | Path B: Manual CapCut + Unchecked Three.js | **Path C: `ViralForge v0.1.0` + `fable52-fps-repro` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly Video & LLM Generation API Spend** | **`$1,940.00`** (600 full video generations + uncapped 3D loops) | **`$820.00`** (ad-hoc multi-turn retries) | **`$215.00`** (VFML structural reuse + cache-optimized `--max-budget-usd` runs) |
| **Variant Re-Cutting & 3D WebGL Debugging Labor (`$85/hr`)** | `44.0 hrs × $85.00` = **`$3,740.00`** | `24.0 hrs × $85.00` = **`$2,040.00`** | `4.0 hrs × $85.00` = **`$340.00`** |
| **Total Monthly TCO** | **`$5,680.00 / mo`** | **`$2,860.00 / mo`** (`-49.65%`) | **`$555.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,820.00 / mo` | **Saves `$5,125.00 / mo` (`-90.23%` · `$61,500.00/yr`)** |
| **Paid Social Ad Spend & Physical Camera Gear** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `fendouai/ViralForge` (`v0.1.0`) Viral DNA & VFML 10-Variant Build**: Run ViralForge on Node 22.15+, extract a Viral DNA report from a reference clip, edit the VFML project, and generate 10 costed A/B variants.
- [ ] **2. ViralForge MCP Server & Skill Integration**: Attach the ViralForge MCP server and Agent Skill to your coding agent for automated campaign repurposing.
- [ ] **3. `wquguru/fable52-fps-repro` Budget-Capped Run & Cache Audit**: Inspect `data/metrics.tsv` via `python3 scripts/metrics.py` to compare `5m` vs. `1h` cache TTL costs, and launch new 3D builds via `scripts/run.sh` with `--max-budget-usd`.
- [ ] **4. Isolated `agent-browser` + `__dbg.step` Deterministic Capture**: Adopt `prompts/builder_system_04.md` and `window.__dbg.step` (`scripts/rec/`) so autonomous 3D builds self-inspect and record zero-dropped-frame previews.
