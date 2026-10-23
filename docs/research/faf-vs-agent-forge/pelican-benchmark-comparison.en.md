# Hands-On Dual-Plugin Benchmark: FAF (`faf-agents` v2.0.1) vs. Microsoft `AGENT-FORGE` (`v0.3.0`) — "Animated Pelican Riding a Bicycle" End-to-End Evaluation

> 🌐 **Language / 语言**: [中文 (zh-CN) (`pelican-benchmark-comparison.md`)](pelican-benchmark-comparison.md) | **English**
> 🎮 **Live Interactive Showcase on GitHub.io**:
> - **⚔️ Side-by-Side Pelican Arena (`pelican-arena.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/pelican-arena.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/pelican-arena.html) (Root mirror: [https://turbo998.github.io/workshops/faf-vs-agent-forge/pelican-arena.html](https://turbo998.github.io/workshops/faf-vs-agent-forge/pelican-arena.html))
> - **🟦 Demo A — FAF Architecture-Spec-Driven (`demo-faf-pelican.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-faf-pelican.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-faf-pelican.html)
> - **🟧 Demo B — AGENT-FORGE Multi-Agent Studio (`demo-agent-forge-pelican.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-agent-forge-pelican.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/demo-agent-forge-pelican.html)
> - **📈 FAF Prioritization Scorecard (`prioritization-report.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/artifacts/faf-sdlc/prioritization-report.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/artifacts/faf-sdlc/prioritization-report.html)
> - **📊 7-Card 4:5 Visual Benchmark Deck (`test-report-cards.html`)**: [https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/test-report-cards.html](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/test-report-cards.html)

---

## 1. Experimental Design: Why "Pelican Riding a Bicycle"?

**"An animated pelican riding a bicycle"** is a classic generative benchmark task because naive single-shot prompts routinely fail on three structural axes:
1. **Kinematic Detachment**: Feet float off the pedals or clip through the crankset during $360^\circ$ rotation;
2. **Biomechanical & Anatomical Simplification**: Missing the elastic gular pouch, S-curved neck, and forward-bending 2-bone avian knee inverse kinematics (IK);
3. **Lack of Verifiable Engineering Telemetry or Interactive Physics**: Static SVG loops without real-time cadence, drivetrain gear ratios, headwind drag, or interactive stunts.

To evaluate **`customer-success-microsoft/faf-agents` (FAF v2.0.1)** and **`microsoft/agent-forge` (`@agent-forge-copilot/cli` v0.3.0)** in practice, we installed both toolkits locally and executed each toolkit's complete workflow on this exact task, archiving all intermediate process artifacts and live HTML5 demos.

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

---

## 3. Process Artifacts Comparison (`artifacts/faf-sdlc/` vs. `artifacts/agent-forge-context/`)

| Dimension | 🟦 FAF (`customer-success-microsoft/faf-agents`) | 🟧 Microsoft `AGENT-FORGE` (`microsoft/agent-forge`) |
|---|---|---|
| **Nature of Process Artifacts** | **SDLC Software Engineering Deliverables** (`scope/`, `specs/`, `plan/`): Quantifies business/technical viability, defines testable functional requirements, locks C4 L1–L3 mathematical contracts, evaluates reusable accelerators, and breaks down the backlog. | **Repository `.github/` Context Engineering Suite**: Synthesizes a domain-specific multi-agent team (`.agent.md`), coding standards (`.instructions.md`), reusable workflows (`.prompt.md`), rigging skills (`SKILL.md`), and lifecycle hooks (`hooks.json`). |
| **Archived Files**<br>*(Available in [`artifacts/`](./artifacts/))* | Under [`artifacts/faf-sdlc/`](./artifacts/faf-sdlc/):<br>1. [`scorecard.yaml`](./artifacts/faf-sdlc/scorecard.yaml) & [`history.yaml`](./artifacts/faf-sdlc/history.yaml)<br>2. [`prioritization-report.html`](./artifacts/faf-sdlc/prioritization-report.html)<br>3. [`scope.md`](./artifacts/faf-sdlc/scope.md) (Tier P1 Go)<br>4. [`prd.md`](./artifacts/faf-sdlc/prd.md) (FR-01..FR-05)<br>5. [`spec.md`](./artifacts/faf-sdlc/spec.md) (C4 L1–L3 + 2-Bone IK Law of Cosines)<br>6. [`adr/adr-001-ik-svg-engine.md`](./artifacts/faf-sdlc/adr/adr-001-ik-svg-engine.md)<br>7. [`impl-rec.md`](./artifacts/faf-sdlc/impl-rec.md) (`15.0% < 40%` $\rightarrow$ **Path B Greenfield**)<br>8. [`backlog.md`](./artifacts/faf-sdlc/backlog.md) (2 Epics / 6 Tasks) | Under [`artifacts/agent-forge-context/`](./artifacts/agent-forge-context/):<br>1. [`forge-plan.json`](./artifacts/agent-forge-context/forge-plan.json) (`pipeline` topology)<br>2. [`agents/pelican-character-artist.agent.md`](./artifacts/agent-forge-context/agents/pelican-character-artist.agent.md)<br>3. [`agents/bicycle-kinematics-coder.agent.md`](./artifacts/agent-forge-context/agents/bicycle-kinematics-coder.agent.md)<br>4. [`agents/scene-environment-director.agent.md`](./artifacts/agent-forge-context/agents/scene-environment-director.agent.md)<br>5. [`agents/animation-qa-reviewer.agent.md`](./artifacts/agent-forge-context/agents/animation-qa-reviewer.agent.md)<br>6. [`instructions/pelican-animation-standards.instructions.md`](./artifacts/agent-forge-context/instructions/pelican-animation-standards.instructions.md)<br>7. [`prompts/tune-pelican-choreography.prompt.md`](./artifacts/agent-forge-context/prompts/tune-pelican-choreography.prompt.md)<br>8. [`skills/pelican-svg-rigging/SKILL.md`](./artifacts/agent-forge-context/skills/pelican-svg-rigging/SKILL.md) & [`hooks/hooks.json`](./artifacts/agent-forge-context/hooks/hooks.json) |

---

## 4. Demo Outcomes Comparison (`demo-faf-pelican.html` vs. `demo-agent-forge-pelican.html`)

| Visual & Engineering Aspect | 🟦 Demo A: FAF Architecture-Driven (`demo-faf-pelican.html`) | 🟧 Demo B: AGENT-FORGE Multi-Agent Studio (`demo-agent-forge-pelican.html`) |
|---|---|---|
| **Primary Aesthetic** | **Engineering Kinematics & Telemetry Workbench** (Dark blueprint grid + live cyan/amber vector callouts) | **Art-Directed Coastal Boardwalk Theatre** (3 lighting moods + interactive stunts & WebAudio soundscape) |
| **Leg Pedaling IK** | Analytical Law-of-Cosines 2-Bone IK (`0.00 px` foot-to-pedal slip error verified across $360^\circ$) | Analytical 2-Bone IK coupled with **rear-axle Wheelie pitch rotation ($\theta \in [0, 24^\circ]$)** |
| **Signature Visual Features** | **🔬 X-Ray IK Vector Overlay**: Live crank orbit circle, left/right femur-tibiotarsus bone vectors, real-time interior knee angles (`94° / 138°`), and gular pouch spring deflection vector `Δy_pouch`. | **🌅 3-Mood Coastal Atmosphere**: Switch between `☀️ Sunny Pier`, `🌅 Golden Sunset`, and `🌙 Starlight Night Ride` (with glowing headlamp beam cone), plus ocean waves, flocking seagulls, leather aviator cap, fluttering red scarf, and front wicker fish basket. |
| **Interactive Controls** | • Cadence (`20–130 RPM`)<br>• Drivetrain Gear Ratio (`1.0x–4.2x`)<br>• Headwind Speed (`0–50 km/h`)<br>• Pouch Fish Payload (`0–3 fish`, dynamically increasing mechanical Watts) | • **🐟 Toss Sardine (`Click Canvas / Button`)**: Launches parabolic sardines into the pelican's open beak with gulping pouch physics<br>• **🎪 Wheelie Stunt** & **🚀 Wing-Flap Sprint Boost**<br>• **🔔 WebAudio Brass Bike Bell (`Ding-Ding!`)** |
| **Process Traceability UI** | Interactive 5-stage SDLC ribbon (`FAF-analyst` $\rightarrow$ `FAF-dev`) with embedded specification viewer. | Interactive 4-Agent pipeline ribbon (`pelican-character-artist` $\rightarrow$ `animation-qa-reviewer`) with `.github/` artifact viewer. |
