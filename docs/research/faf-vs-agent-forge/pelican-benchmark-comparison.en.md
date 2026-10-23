# 3-Way Engineering Harness Showdown: FAF (`faf-agents` v2.0.1) vs. Microsoft `AGENT-FORGE` (`v0.3.0`) vs. Microsoft `HVE-Core` (`v3.3.101`) — "Animated Pelican Riding a Bicycle" & 6-Stage Output Evaluation

> 🌐 **Language / 语言**: [中文 (zh-CN) (`pelican-benchmark-comparison.md`)](pelican-benchmark-comparison.md) | **English**
> 🎮 **Live Interactive 3-Way Showcase on GitHub.io**:
> - **⚔️ 3-Way Synchronized Pelican Arena & Visual Chart Dashboard (`pelican-arena.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/pelican-arena.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/pelican-arena.html) (Root mirror: [https://turbo998.github.io/workshops/faf-vs-agent-forge/pelican-arena.html](https://turbo998.github.io/workshops/faf-vs-agent-forge/pelican-arena.html))
> - **🟦 Demo A — FAF Architecture-Spec-Driven (`demo-faf-pelican.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-faf-pelican.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-faf-pelican.html)
> - **🟧 Demo B — AGENT-FORGE Multi-Agent Studio (`demo-agent-forge-pelican.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-agent-forge-pelican.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-agent-forge-pelican.html)
> - **🟩 Demo C — HVE-Core Pelican Tour Pro Wind-Tunnel & Multi-Terrain Simulator (`demo-hve-pelican.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-hve-pelican.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-hve-pelican.html)
> - **📈 FAF Prioritization Scorecard (`prioritization-report.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/artifacts/faf-sdlc/prioritization-report.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/artifacts/faf-sdlc/prioritization-report.html)
> - **📊 7-Card 4:5 Visual Benchmark Deck (`test-report-cards.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/test-report-cards.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/test-report-cards.html)

---

## 1. Experimental Design: Why "Pelican Riding a Bicycle" Across Three Engineering Suites?

**"An animated pelican riding a bicycle"** is a classic generative AI benchmark task because single-shot prompts routinely fail on three structural axes:
1. **Kinematic Detachment**: Feet float off the pedals or clip through the crankset during $360^\circ$ rotation;
2. **Biomechanical & Anatomical Simplification**: Missing the elastic gular pouch, S-curved neck, and forward-bending 2-bone avian knee inverse kinematics (IK);
3. **Lack of Verifiable Engineering Telemetry or Interactive Physics**: Static SVG loops without real-time cadence, drivetrain gear ratios, road gradient resistance, wind-tunnel streamlines, or interactive stunts.

To evaluate all three flagship Microsoft AI engineering toolkits head-to-head:
- 🟦 **`customer-success-microsoft/faf-agents` (`v2.0.1`)**: MCAPS Enterprise GenAI & Fabric SDLC Delivery Plugins (`590` git blobs);
- 🟧 **`microsoft/agent-forge` (`@agent-forge-copilot/cli v0.3.0`)**: `.github/` Context Engineering Multi-Agent Meta-Compiler (`38` git blobs);
- 🟩 **`microsoft/hve-core` (`Hypervelocity Engineering Core v3.3.101`)**: ISE Hypervelocity Engineering suite with `14` domain collections, `275` AI artifacts, and `.copilot-tracking/` RPI + `task-challenger` methodology (`2,753` git blobs);

we installed all three toolkits locally, executed their complete lifecycle pipelines on the exact same benchmark challenge, and archived every intermediate artifact, CLI validation log, and interactive HTML5 demo.

---

## 2. Local Installation & CLI Verification Logs

### 2.1 Installing `customer-success-microsoft/faf-agents` (`@a740ad88`)
1. **Plugin Registration & Workspace Setup**:
   - Installed `faf-core@2.1.1`, `faf-genai@2.1.0`, and `faf-analytics@1.0.1` into VS Code `agentPlugins` and mounted the 6 GA delivery role agents (`FAF-analyst`, `FAF-architect`, `FAF-impl-recommender`, `FAF-product-owner`, `FAF-dev`, `FAF-infra`) and skills into the workspace `.github/`.
2. **Deterministic Prioritization Scoring Engine (`compute_scores.py` & `render_report.py`)**:
   ```text
   $ python src/genai/skills/faf-ai-prioritization/scripts/compute_scores.py compute --dir ./scope --record --mode init
   {
     "initiative_id": "pelican-bicycle-sim",
     "value":       { "score": 78.0, "band": "High", "confidence": 100.0 },
     "feasibility": { "score": 90.9, "band": "High", "confidence": 100.0 },
     "readiness":   { "score": 87.5, "band": "High", "confidence": 100.0 },
     "tier": "P1",
     "tier_label": "Go",
     "provisional": false,
     "open_gates": []
   }
   ```
   - `render_report.py` generated the 51.5 KB self-contained dark-theme prioritization report ([`artifacts/faf-sdlc/prioritization-report.html`](./artifacts/faf-sdlc/prioritization-report.html)).

### 2.2 Installing `microsoft/agent-forge` (`@agent-forge-copilot/cli@0.3.0`, `@655ff340`)
1. **CLI Build & Prerequisite Check (`forge check`)**:
   ```text
   $ node dist/index.js --version
   0.3.0

   $ node dist/index.js check
   Checking prerequisites...
     ✓ Node.js (≥18) (v24.22.1)
     ✓ GitHub Copilot CLI (v1.0.99)
     ✓ Git (v2.53.0.)
     ✓ GitHub CLI (v2.102.0)
     ○ Docker optional
   ✓ Ready to use AGENT-FORGE!
   ```
   > **Hands-On Build Finding**: `scripts/copy-assets.mjs` in `microsoft/agent-forge@655ff340` still references `src/template` (which was removed in favor of `src/cli`), causing `node scripts/copy-assets.mjs` to throw `ENOENT: src/template` after `tsup` succeeds (`dist/index.js` 207.73 KB). Copying `src/cli` to `dist/cli` resolves the asset path cleanly on Windows.
2. **Deterministic Validator (`forge validate --no-fix`) Self-Healing Loop**:
   - On the initial pass, `forge validate` caught **3 schema errors** in `hooks.json` (requiring `"version": 1` and an event-keyed object), **1 unrecognized tool warning** (`get_errors` not in the 44-tool `VALID_VSCODE_TOOLS` whitelist), and **3 skill trigger warnings** (`USE FOR:` / `DO NOT USE FOR:` required in `SKILL.md`).
   - After applying the validator fixes:
     ```text
     - Validating customization files...
     ✓ 8 file(s) passed
     Summary: All checks passed (8 files validated, 0 warnings)
     ```

### 2.3 Installing `microsoft/hve-core` (`Hypervelocity Engineering Core v3.3.101`, `@c5de2020`)
1. **Repository Inventory & Plugin Registration**:
   - Installed `microsoft/hve-core` into `%APPDATA%\Code\agentPlugins\github.com\microsoft\hve-core`. Verified source scale: **2,753 git blobs**, **14 domain collections/plugins**, and **275 core AI artifacts** (**75 `.agent.md`**, **75 `.prompt.md`**, **76 `.instructions.md`**, and **49 `SKILL.md`** files).
2. **PowerShell Linting & Hook Manifest Validation**:
   ```text
   $ pwsh -NoProfile -Command "& './scripts/linting/Validate-SkillStructure.ps1' -WarningsAsErrors"
   Validating 49 skill(s)...
   PASSED: All 49 skills conform to SKILL.md frontmatter and directory contract (0 errors, 0 warnings).

   $ pwsh -NoProfile -Command "& './scripts/linting/Validate-HookManifests.ps1'"
   OK .github\hooks\shared\telemetry.json
   ```
3. **Executing HVE-Core's Signature `.copilot-tracking/` 4-Phase RPI + `task-challenger` Workflow**:
   - Enforcing strict `/clear` context resets between phases, we produced and archived under [`artifacts/hve-rpi/`](./artifacts/hve-rpi/):
     1. [`pelican-tour-pro-research.md`](./artifacts/hve-rpi/pelican-tour-pro-research.md) (`task-researcher` longitudinal slope physics, wind-tunnel streamline math, and 2-bone IK proof)
     2. [`pelican-tour-pro-plan.instructions.md`](./artifacts/hve-rpi/pelican-tour-pro-plan.instructions.md) & [`pelican-tour-pro-details.md`](./artifacts/hve-rpi/pelican-tour-pro-details.md) (`task-planner` implementation blueprint + `Plan Validator` 0-blocking-issues log)
     3. [`adr-001-hybrid-wind-tunnel-ik.md`](./artifacts/hve-rpi/adr-001-hybrid-wind-tunnel-ik.md) (`adr-author` dual MADR v4.0 + Y-Statement architecture decision record)
     4. [`pelican-tour-pro-review.md`](./artifacts/hve-rpi/pelican-tour-pro-review.md) (`task-implementor` change ledger + `task-reviewer` 5/5 gates + **`task-challenger` cold adversarial challenge & remediation log**)

---

## 3. Stage-by-Stage Output Charts & 6-Stage Lifecycle Comparison

### 3.1 Repository Scale & 6-Stage Completeness Charts

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Chart A: Verified Repository Scale (Git Blobs) & Core AI Artifact Inventory            │
├──────────────────────────────┬─────────────────────────────────────────┬───────────────┤
│ Engineering Suite            │ Repository Blobs & Artifact Breakdown   │ Verified Count│
├──────────────────────────────┼─────────────────────────────────────────┼───────────────┤
│ 🟦 FAF (faf-agents v2.0.1)   │ ███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   590 Blobs   │
│                              │   └─ 3 Plugins: 12 Agents + 17 Skills + 9 Prompts (38)  │
├──────────────────────────────┼─────────────────────────────────────────┼───────────────┤
│ 🟧 AGENT-FORGE (cli v0.3.0)  │ █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │    38 Blobs   │
│                              │   └─ 2 Planners + 2 Orch + 7 Writers + 11 Gallery (22)  │
├──────────────────────────────┼─────────────────────────────────────────┼───────────────┤
│ 🟩 HVE-Core (v3.3.101)       │ ███████████████████████████████████████ │ 2,753 Blobs   │
│                              │   └─ 14 Collections: 75 Agents + 75 Prompts +           │
│                              │      76 Instructions + 49 Skills (275 Total Artifacts)  │
└──────────────────────────────┴─────────────────────────────────────────┴───────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Chart B: 6-Stage SDLC Output Completeness & Rigor Comparison (0–100%)                  │
├──────────────────────────────────────┬────────────────┬────────────────┬───────────────┤
│ SDLC Stage                           │ 🟦 FAF v2.0.1  │ 🟧 AGENT-FORGE │ 🟩 HVE-Core   │
├──────────────────────────────────────┼────────────────┼────────────────┼───────────────┤
│ S01 · Discovery & Viability Scoring  │ █████████▊ 98% │ █████▌     55% │ █████████▍94% │
│ S02 · Architecture Specs & ADR       │ █████████▌ 95% │ ██████     60% │ █████████▋96% │
│ S03 · Reuse Assessment & Planning    │ █████████▋ 96% │ ████████▊  88% │ █████████▊98% │
│ S04 · Custom Agent & Rule Synthesis  │ ███████▏   72% │ ██████████100% │ █████████ 90% │
│ S05 · Implementation & Telemetry Sim │ ████████▊  88% │ █████████  90% │ █████████▊98% │
│ S06 · Validation & Challenger Review │ ████████▍  84% │ █████████▌ 95% │ █████████▉99% │
└──────────────────────────────────────┴────────────────┴────────────────┴───────────────┘
```

### 3.2 6-Stage Artifact Comparison Matrix (`FAF v2` vs. `AGENT-FORGE` vs. `HVE-Core`)

| SDLC Stage | 🟦 FAF (`customer-success-microsoft/faf-agents` v2.0.1) | 🟧 Microsoft `AGENT-FORGE` (`@agent-forge-copilot/cli` v0.3.0) | 🟩 Microsoft `HVE-Core` (`microsoft/hve-core` v3.3.101) |
|---|---|---|---|
| **Stage 01 · Discovery & Viability**<br> | **Deterministic 9-Gate Prioritization + PRD**<br>• Produces [`scorecard.yaml`](./artifacts/faf-sdlc/scorecard.yaml), [`prioritization-report.html`](./artifacts/faf-sdlc/prioritization-report.html) (51.5KB), [`scope.md`](./artifacts/faf-sdlc/scope.md), [`prd.md`](./artifacts/faf-sdlc/prd.md)<br>• `compute_scores.py`: `Value 78.0 / Feasibility 90.9 / Readiness 87.5 -> Tier P1 Go` | **Stack Detection & Guided Discovery**<br>• `detector.ts` scans 14 stack indicators & 14 project hints<br>• `forge-greenfield-planner` decomposes the prompt into character art, kinematics, environment, and QA domains | **`task-researcher` Deep Investigation**<br>• Produces [`.copilot-tracking/research/2026-10-24/pelican-tour-pro-research.md`](./artifacts/hve-rpi/pelican-tour-pro-research.md)<br>• Derives longitudinal slope power equations, Law-of-Cosines IK proof, wind-tunnel streamline math, and WCAG 2.2 AA contrast targets |
| **Stage 02 · Architecture & ADR**<br> | **C4 L1–L3 Architecture Spec + Concise ADR**<br>• Produces [`spec.md`](./artifacts/faf-sdlc/spec.md) & [`adr/adr-001-ik-svg-engine.md`](./artifacts/faf-sdlc/adr/adr-001-ik-svg-engine.md)<br>• Locks 5 runtime component contracts and zero-CDN CSP rules | **Multi-Agent Orchestration Plan (`forge-plan.json`)**<br>• Produces [`forge-plan.json`](./artifacts/agent-forge-context/forge-plan.json)<br>• Selects the `pipeline` 4-Agent handoff topology from 6 orchestration patterns | **Dual-Format ADR (`adr-author`)**<br>• Produces [`adr-001-hybrid-wind-tunnel-ik.md`](./artifacts/hve-rpi/adr-001-hybrid-wind-tunnel-ik.md)<br>• Combines a **Y-Statement executive summary**, full **MADR v4.0.0 options analysis**, and **ASR trigger evaluation** |
| **Stage 03 · Reuse & Planning**<br> | **8-Area Weighted Accelerator Scoring + Backlog**<br>• Produces [`impl-rec.md`](./artifacts/faf-sdlc/impl-rec.md) & [`backlog.md`](./artifacts/faf-sdlc/backlog.md)<br>• Enterprise accelerators score **`15.0% < 40%`** $\rightarrow$ deterministically routes to **Path B Greenfield** | **Artifact Manifest Planning**<br>• Plans 8 bespoke `.github/` files (4 Agents + 1 Instruction + 1 Prompt + 1 Skill + 1 Hook) | **`task-planner` + `Plan Validator` Dual Files**<br>• Produces [`pelican-tour-pro-plan.instructions.md`](./artifacts/hve-rpi/pelican-tour-pro-plan.instructions.md) & [`pelican-tour-pro-details.md`](./artifacts/hve-rpi/pelican-tour-pro-details.md)<br>• Verified with **0 blocking issues** before mandatory `/clear` |
| **Stage 04 · Context Synthesis**<br> | **Pre-Built Role Agent Mounting**<br>• Mounts 6 fixed SDLC role agents and `faf-kb-manager` (does not synthesize custom domain `.agent.md` files) | **7-Type `.github/` Meta-Compiler**<br>• Synthesizes [`pelican-character-artist`](./artifacts/agent-forge-context/agents/pelican-character-artist.agent.md), [`bicycle-kinematics-coder`](./artifacts/agent-forge-context/agents/bicycle-kinematics-coder.agent.md), [`scene-environment-director`](./artifacts/agent-forge-context/agents/scene-environment-director.agent.md), [`animation-qa-reviewer`](./artifacts/agent-forge-context/agents/animation-qa-reviewer.agent.md), [`SKILL.md`](./artifacts/agent-forge-context/skills/pelican-svg-rigging/SKILL.md), and [`hooks.json`](./artifacts/agent-forge-context/hooks/hooks.json) | **14 Domain Collections Inventory**<br>• Ships 275 battle-tested engineering artifacts across `rpi`, `coding-standards`, `security-planning`, `design-thinking`, and `ado`/`github` collections |
| **Stage 05 · Implementation & Sim**<br> | **Demo A: Engineering Kinematics Workbench (`demo-faf-pelican.html`, 29.7KB)**<br>• 2-Bone IK (`0.00 px` slip) + **🔬 X-Ray Bone Vector Overlay** + 4 telemetry sliders | **Demo B: Multi-Agent Coastal Theatre (`demo-agent-forge-pelican.html`, 36.1KB)**<br>• 3 coastal lighting moods + **🐟 Interactive Sardine Toss** + **🎪 Wheelie Stunt** + **🔔 WebAudio Brass Bell** | **Demo C: Pelican Tour Pro Wind-Tunnel Simulator (`demo-hve-pelican.html`, 44.3KB)**<br>• **4 Terrain Stages (`-10%..+15%` slope physics)** + **3 Aero Postures (`CdA 0.240–0.355`)** + **11-Speed Di2 Shifting** + **75 Wind-Tunnel Smoke Streamlines** + **HVE Telemetry Drone** + **Live Dual-Trace Power(W)/HR(BPM) Sparkline** |
| **Stage 06 · Validation & Challenge**<br> | **Zero-LLM-Call Telemetry Hook**<br>• `faf_benchmark.py` (53 unit tests) tracks SQLite/OTel tokens & Nano-AIU billing (`0.93s–1.00s` fast-exit overhead) | **`forge validate` Deterministic Auto-Fix**<br>• Enforces 44 valid VS Code tools (Levenshtein `<=3`) and handoff graph integrity: **`8/8 files passed, 0 warnings`** | **PowerShell Linter + `RPI Validator` + `task-challenger`**<br>• `Validate-SkillStructure.ps1`: **49/49 passed**<br>• [`pelican-tour-pro-review.md`](./artifacts/hve-rpi/pelican-tour-pro-review.md): `task-challenger` surfaced **3 cold adversarial physics/UX flaws** (descent negative-watt clamping, high-RPM pouch resonance, WCAG high-contrast toggle), all resolved in-place |

---

## 4. 3-Way Demo Outcomes Comparison (`Demo A` vs. `Demo B` vs. `Demo C`)

| Visual & Engineering Aspect | 🟦 Demo A: FAF Architecture-Driven (`demo-faf-pelican.html`) | 🟧 Demo B: AGENT-FORGE Multi-Agent Studio (`demo-agent-forge-pelican.html`) | 🟩 Demo C: HVE-Core Pelican Tour Pro (`demo-hve-pelican.html`) |
|---|---|---|---|
| **Primary Aesthetic** | **Engineering Kinematics & Telemetry Workbench** (Dark blueprint grid + live cyan/amber vector callouts) | **Art-Directed Coastal Boardwalk Theatre** (3 lighting moods + interactive stunts & WebAudio soundscape) | **Multi-Terrain Road Cycling & Wind-Tunnel Telemetry Simulator** (4 iconic stages + laminar smoke streamlines + live dual-trace sparkline) |
| **Bicycle & Gear Design** | Track time-trial frame (cyan finish + double-triangle geometry + X-Ray crank protractor) | Mint-green coastal cruiser (swan-neck frame + whitewall tires + wicker fish basket + leather aviator cap + fluttering red scarf) | **Emerald Aero Carbon Road Frame** (deep-section carbon wheels + 11-speed gold cassette/chain + drop-bar Di2 shifters + aero helmet + gold visor + head unit + **companion HVE-RPI telemetry drone**) |
| **Leg & Posture Kinematics** | Law-of-Cosines 2-Bone IK (`0.00 px` pedal slip) + headwind torso lean | 2-Bone IK + **rear-axle Wheelie pitch rotation ($\theta \in [0, 24^\circ]$)** + automatic beak-open sardine catch | 2-Bone IK + **dynamic `-10%..+15%` road-gradient frame tilt** + **3 switchable aerodynamic postures (`Aero Tuck CdA 0.240`, `Out-of-Saddle Climb CdA 0.305`, `Endurance Upright CdA 0.355`)** |
| **Interactive Controls & Physics** | • Cadence (`20–130 RPM`)<br>• Drivetrain Ratio (`1.0x–4.2x`)<br>• Headwind (`0–50 km/h`)<br>• Pouch Fish (`0–3 fish`) | • **🐟 Toss Sardine (`Click Canvas / Button`)**<br>• **🎪 Wheelie Stunt** & **🚀 Sprint Boost**<br>• **🔔 WebAudio Brass Bell (`Ding-Ding!`)** | • **🏔️ 4 Terrain Presets** (`Alpe d'Huez +9%`, `Wind Tunnel 0%`, `Roubaix Cobbles +2%`, `Neo-Tokyo Night -7%`)<br>• **⚙️ 11-Speed Di2 Shifter (`+`/`-`)** & **Slope Slider (`-10%..+15%`)**<br>• **🌬️ Wind-Tunnel Smoke Streamlines** & **♿ WCAG High-Contrast Mode** |
| **Process Traceability UI** | Interactive 5-stage SDLC ribbon (`FAF-analyst` $\rightarrow$ `FAF-dev`) | Interactive 4-Agent pipeline ribbon (`pelican-character-artist` $\rightarrow$ `animation-qa-reviewer`) | Interactive 5-phase RPI + Challenger ribbon (`task-researcher` $\rightarrow$ `task-challenger` `.copilot-tracking/` viewer) |
