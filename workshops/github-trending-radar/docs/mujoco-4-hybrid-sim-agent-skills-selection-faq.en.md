# Embodied AI Physics Simulation & Agent-Assisted Modeling Selection FAQ: `google-deepmind/mujoco` 4.0 (`mujoco.batch` CPU Thread Pool + MJX/MJWarp GPU + 7 Bundled `SKILL.md`s) vs. GPU-Only Simulators & Raw MJCF Prompting

> **Shift & Round**: `2026-11-08` Night Shift — Round 11 Standalone Selection FAQ  
> **Style Benchmark**: `ai-infra-research/docs/components/ib-vs-ethernet-roce-selection-faq.md` (First-Principles + Plain Language + Closed-Form Worked Example + Production Checklist)  
> **Primary Evaluated Repository**: [`google-deepmind/mujoco`](https://github.com/google-deepmind/mujoco) (**`v4.0.0`**, released November 6, 2026, `Apache-2.0` license; verified in archived raw Daily Trending HTML `evidence/trending-daily-2026-11-08-raw.html` [`sha256: 353914ef...`] article #8 with **`+26` stars today**, `12,869` DOM total stars / `16,331` live REST stars, `measured`)  
> **Companion HD Architecture SVG**: [`assets/github-ai-radar-2026-11-08-r11-mujoco4-sim-skills.svg`](../../../assets/github-ai-radar-2026-11-08-r11-mujoco4-sim-skills.svg)

---

## 📌 Executive Takeaways (Read in 3 Minutes)

1. **What It Really Is (Plain-Language Essence)**: `google-deepmind/mujoco` is Google DeepMind's industrial-grade Multi-Joint dynamics with Contact physics engine (C core + Python/C++/WASM/Unity bindings, `Apache-2.0`). In **MuJoCo `4.0.0` (released November 6, 2026)** and `3.17.0`, it ships three architectural upgrades that directly change how Embodied AI & Robotics Solution Architects build simulation pipelines:
   - **7 Official AI Coding Agent Skills (`doc/skills/*/SKILL.md`) Bundled Inside `pip install mujoco` (`mujoco/doc/`)**: Covering `mujoco-python`, `mujoco-spec-editing`, `mujoco-accelerated` (MJX/MJWarp), `mujoco-parity` (CPU `float64` vs. GPU `float32` stage-by-stage divergence isolation), `mujoco-rendering`, `mujoco-studio`, and `mujoco-gui`—preventing coding agents from hallucinating deprecated MuJoCo 2.x/3.x XML tags;
   - **Native C Thread-Pool Batched Rollout Engine (`include/mujoco/mjbatch.h` / `mujoco.batch.Batch`) + Headless Package Split (`mujoco-core` depending only on `numpy`)**: Steps `nsim` parallel simulations on a thread pool holding compact `mjSTATE_INTEGRATION` rows (`nsim × nstate`) and allocating only one `mjData` workspace per thread (`persistent = 0`), producing **bit-identical `float64` trajectories to a plain single-threaded loop at any thread count**;
   - **Speculative Contacts (`<flag speculative="enable"/>`), Elasto-Plasticity (`mjData.plastic` / `mjSTATE_PLASTIC`), and a 1.4–3× Faster Sparse `Newton` Deformable Flex Solver** (`anonymized_reported, independently_reproduced=false`, cited from official `4.0.0` Release Notes).
2. **When to Choose `mujoco.batch` (CPU `float64`) vs. `MJX` / `MJWarp` (GPU `float32`)**:
   - When running **`N_env <= 256` parallel environments** (online MPC trajectory sampling, `mujoco.sysid` system identification, complex deformable `flexcomp` / elasto-plasticity tasks, or bit-identical `float64` CI regression tests), choose **`mujoco-core` + `mujoco.batch.Batch` (CPU Thread Pool)**—on a 32-thread node running 512 environments, `persistent = 0` cuts active simulation memory from `2,048.00 MB` to **`136.00 MB` (`-93.36%`)**, keeping `mjData` warm in L3 cache with zero GPU `float32` contact drift;
   - When scaling to **`N_env >= 1,024–32,768`** parallel RL training rollouts, switch to **`mujoco.mjx` (JAX) or `mujoco_warp` (CUDA)** and run the bundled `mujoco-parity` skill to isolate `mj_forward` (`float64`) vs. `mjw.forward` (`float32`) discrepancies stage by stage.
3. **Closed-Form Quantitative Impact (`CLAIM-R11-02`, `synthetic, independently_reproduced=false`)**: For an embodied-AI team authoring and debugging **`M_models = 30` articulated-robot / deformable-manipulation simulation tasks per month** (`$3.00/1M` input, `$15.00/1M` output counted strictly once; cloud GPU/CPU instance rental and physical robot lab bills explicitly marked `not_measured`): compared to raw LLM prompting without `doc/skills` + blind GPU `float32` debugging (Path A: 8 rounds/task = 240 rounds/mo, `$61.20/mo` API-only, `90.0h/mo` engineering debugging), adopting **MuJoCo 4.0's 7 bundled `doc/skills/*/SKILL.md` + `MjSpec` + `mujoco-parity` stage isolation** (Path C: 2 rounds/task = 60 rounds/mo) reduces monthly LLM modeling API spend to **`$3.96/mo` (saving `$57.24/mo`, `-93.53%` API-only)** and cuts engineering debugging hours from `90.0h/mo` to **`15.0h/mo` (saving `75.0h/mo`, `-83.33%`)**.

---

## 💬 First-Principles Q&A (Q1 / Q2 / Q3 Plain-Language Deep Dive)

### Q1: Why do coding agents frequently break robotics simulations when writing MJCF XML, and how does MuJoCo 4.0 fix this at the root?

When robotics engineers ask an LLM coding agent to author or migrate MuJoCo XML (MJCF) and GPU batch scripts, three failure modes dominate:
1. **Hallucinated or Removed Legacy XML Elements**: MuJoCo `4.0.0` removed the legacy `cable` plugin (`plugin/elasticity`), the `<composite>` element, and `flexvert` equality constraints (replacing them with `flexcomp` + `<elasticity>` under `integrator="discrete"`), updated `sidesite` tendon wrapping to a homotopy rule, and made `RK4` fourth-order accurate on ball/free joint orientations via the Runge-Kutta-Munthe-Kaas correction. An unguided LLM emits legacy 2.x/3.x tags that immediately fail to compile.
2. **Opaque GPU `float32` vs. CPU `float64` Trajectory Divergence (Sim-to-Sim Gap)**: When scaling to thousands of environments on GPU (`MJX` / `MJWarp`) in `float32`, stiff affine actuators, ill-conditioned mass matrices (`qM`), or overflowed static contact buffers (`nconmax`, `njmax`) cause trajectories to explode. Without a stage-by-stage parity harness, teams waste days tweaking RL hyperparameters for what is actually a physics solver mismatch.
3. **Bloated Container Dependencies**: Installing full desktop viewer and rendering libraries inside headless cloud RL/MPC worker containers wastes image size and triggers OpenGL/EGL initialization errors.

**How MuJoCo 4.0 Solves All Three**:
- **Ships 7 Official `SKILL.md` Guides Inside `pip install mujoco` (`mujoco/doc/skills/`)**: Coding agents read concise `# Good:` vs. `# Avoid:` rules and jump directly to offline Sphinx `.. _Label:` anchors in `mujoco/doc/`;
- **Standardizes Cross-Engine Parity via `mujoco-parity`**: Isolates `mj_forward` (`float64`) against `mjw.forward` (`float32`) stage by stage (kinematics, mass matrix `qM`, unconstrained acceleration, order-insensitive contact matching per geom pair) on identical states;
- **Splits `mujoco-core` from `mujoco-studio`**: Headless servers run `pip install mujoco-core` with `numpy` as the sole dependency.

---

### Q2: How does `mujoco.batch` (`include/mujoco/mjbatch.h`) work under the hood, and why is it vastly more memory-efficient than allocating `N` full `mjData` structs?

When running `nsim = 512` parallel CPU rollouts (e.g., for Model Predictive Control sampling or `mujoco.sysid`), allocating 512 independent `mjData` structs hits the **CPU Memory Bandwidth Wall**:
- A full `mjData` struct holds contact arrays, constraint Jacobians, and sparse factorization scratchpads—typically **`4.0 MB` per environment** on complex articulated/deformable scenes;
- Allocating 512 full `mjData` structs consumes **`512 × 4.0 MB = 2,048.00 MB` (`2.00 GB`)**, overflowing CPU L3 cache (`32–128 MB`) and thrashing DRAM on every step.

**How `include/mujoco/mjbatch.h` (`mujoco.batch.Batch`) Solves This**:
1. **Decouples Persistent Integration State from Scratch Workspace**: The actual integration state (`mjSTATE_INTEGRATION`: `qpos`, `qvel`, `act`, `mjSTATE_PLASTIC`, etc.) queried via `mjb_nstate(b)` is tiny—typically **`16 KB` (`0.015625 MB`) per simulation row**.
2. **`persistent = 0` Thread-Local `mjData` Reuse**: On a `32`-thread CPU (`nthread = 32`) stepping `nsim = 512` simulations, `mjb_makeBatch` allocates only **`32` `mjData` structs** (`32 × 4.0 MB = 128.00 MB`) plus the `512 × 16 KB = 8.00 MB` state matrix (`mjb_state`), totaling **`136.00 MB` (`-93.36%` memory reduction)**!
3. **Bit-Identical Determinism Across Any Thread Count**: Each worker thread loads a simulation row into its L3-resident `mjData`, steps the physics, and writes the updated integration state back. Results are **bit-identical to a plain single-threaded loop regardless of `nthread`**!

---

### Q3: How are the 7 bundled `SKILL.md` modules and MuJoCo 4.0 engine features structured in primary source code?

We inspected `google-deepmind/mujoco` (`v4.0.0`, `include/mujoco/mjbatch.h`, and `doc/skills/`) directly via the GitHub API (`CLAIM-R11-01`, `measured`):

| Skill / Engine Module | Source Path | Core Responsibility & Guardrails |
| :--- | :--- | :--- |
| **`mujoco-python`** | `doc/skills/python/SKILL.md` | `MjSpec`/`MjModel`/`MjData` lifecycle, `model.bind()`, `mujoco.batch.Batch` (`mjbatch.h`), `mujoco.rollout`, `mujoco.sysid`, and energy diagnostics |
| **`mujoco-spec-editing`** | `doc/skills/spec_editing/SKILL.md` | Procedural model building via `mujoco.MjSpec`, prefix sub-model attachment, `implicitfast`, elliptic cones, `solref`/`solimp`, and `spec.recompile()` |
| **`mujoco-accelerated`** | `doc/skills/accelerated/SKILL.md` | GPU/TPU batch rollouts with `mujoco.mjx` (JAX) and `mujoco_warp` (CUDA), `jax.vmap` + `jax.lax.scan`, static contact sizing (`nconmax`, `njmax`), XLA caching |
| **`mujoco-parity`** | `doc/skills/parity/SKILL.md` | Stage-by-stage `mj_forward` (`float64`) vs. `mjw.forward` (`float32`) isolation, stiff affine actuator & `qM` conditioning bounds, order-insensitive contact matching |
| **`mujoco-rendering`** | `doc/skills/rendering/SKILL.md` | Offscreen `mujoco.Renderer`, RGB/metric depth/segmentation masks (`mjtObj`), `MUJOCO_GL=egl/osmesa`, `offwidth`/`offheight` |
| **`mujoco-studio` & `gui`** | `doc/skills/studio/SKILL.md` & `gui/SKILL.md` | Filament PBR renderer, decoupled sim/viewer threads, `WebViewer` WASM streaming, and Dear ImGui/ImPlot plugin layout |
| **MuJoCo 4.0 Core Engine** | `include/mujoco/mjbatch.h` & `model/{speculative,plastic,flex}/` | ① `<flag speculative="enable"/>` conservative advancement against tunneling; ② `mjData.plastic` (`mjSTATE_PLASTIC`) elasto-plasticity; ③ Sparse `Newton` flex solver (`1.4–3x` faster: `anonymized_reported, independently_reproduced=false`) |

---

## 🧭 Architecture & Selection Decision Diagrams (Mermaid)

### Diagram 1: Embodied AI Physics Simulation Backend & Agent Workflow Decision Tree

```mermaid
flowchart TD
    Start["🤖 Embodied AI / Robotics Simulation Workload"] --> Q_Scale{"Parallel Env Count N_env<br/>& Precision Requirement?"}
    
    Q_Scale -->|"N_env <= 256 or strict float64 determinism<br/>(MPC sampling / sysid / elasto-plastic flexcomp)"| CPU_Batch["⚡ MuJoCo 4.0 CPU Batch Path<br/>pip install mujoco-core (numpy-only)<br/>mujoco.batch.Batch (mjbatch.h C thread pool)"]
    CPU_Batch --> CPU_Mem["💾 State vs. Workspace Separation (persistent=0)<br/>nthread mjData structs + nsim compact state rows<br/>Bit-Identical at any thread count"]

    Q_Scale -->|"N_env >= 1,024 massive RL training<br/>(millions of FPS on GPU/TPU)"| GPU_Path["🚀 MuJoCo 4.0 Accelerated GPU/TPU Path<br/>MJX (mujoco.mjx JAX) or MJWarp (mujoco_warp CUDA)<br/>Guided by doc/skills/accelerated/SKILL.md"]
    
    GPU_Path --> Q_Diverge{"Experiencing GPU float32<br/>divergence or tunneling?"}
    Q_Diverge -->|"Fast geom tunneling"| Spec["🛡️ Enable <flag speculative='enable'/><br/>Conservative advancement contact prevention"]
    Q_Diverge -->|"Sim-to-Sim trajectory gap"| Parity["🔬 Run doc/skills/parity/SKILL.md<br/>Stage-by-stage mj_forward vs. mjw.forward isolation<br/>Tune nconmax / njmax & qM conditioning"]

    Start --> Q_Author{"Using an AI Coding Agent<br/>to author/edit MJCF or plugins?"}
    Q_Author -->|"Yes"| Skills["📚 Mount mujoco/doc/skills/*/SKILL.md<br/>Procedural MjSpec editing + local .rst anchor lookup<br/>Zero deprecated 3.x tag hallucinations"]
```

### Diagram 2: Legacy Full-`mjData` Allocation + Unguided Prompting (Path A) vs. MuJoCo 4.0 `mjbatch.h` + 7 Bundled `SKILL.md`s (Path C)

```mermaid
flowchart LR
    subgraph PathA["❌ Legacy Approach (Path A: Raw XML Prompting + N Full mjData Structs)"]
        direction TB
        A1["Coding Agent emits removed 3.x tags<br/>(cable plugin / flexvert equality)"] --> A2["8 debugging rounds/task<br/>480k input + 40k output tokens/task"]
        A3["512 envs allocate 512 full mjData structs<br/>512 × 4.0 MB = 2,048.00 MB overflows L3 cache"] --> A4["Blind reward tuning on GPU float32 drift<br/>90.0 hours/mo engineering debugging"]
    end

    subgraph PathC["✅ MuJoCo 4.0 Architecture (Path C: 7 Bundled SKILL.mds + mjbatch.h + mujoco-parity)"]
        direction TB
        C1["Agent loads mujoco/doc/skills/*/SKILL.md<br/>Builds via MjSpec + 4.0 flexcomp/speculative rules"] --> C2["Converges in 2 rounds/task (-93.53% API cost)<br/>Only 24k input + 4k output tokens/task"]
        C3["mjbatch.h (persistent=0, 32 threads)<br/>32×4.0MB + 512×16KB = 136.00 MB (-93.36% RAM)"] --> C4["mujoco-parity isolates CPU float64 vs. GPU float32<br/>Engineering debugging drops to 15.0 hours/mo (-83.33%)"]
    end
```

---

## 📊 Comparison Matrix Across Simulation & Modeling Approaches

| Dimension | **Path C: `google-deepmind/mujoco` `4.0.0` (`mujoco.batch` + MJX/MJWarp + 7 `SKILL.md`s)** | **Path B: Generic Doc-RAG Chunking + Custom Multiprocessing** | **Path A: Unguided Raw XML Prompting + Single-Backend GPU Tuning** | **Legacy PyBullet / MuJoCo 2.x** |
| :--- | :--- | :--- | :--- | :--- |
| **License & Release Status** | **`Apache-2.0`** (`v4.0.0`, Nov 6, 2026; Daily Trending `+26` stars today, `measured`) | Custom scripts | Engine-dependent | Zlib / Legacy license |
| **Headless Container Footprint** | **`pip install mujoco-core` depends only on `numpy`** | Full wheel + vector DB client | Full desktop OpenGL/GUI wheel | Lightweight, but lacks OpenUSD/MJWarp |
| **CPU Batched Rollout Architecture** | **Native C thread pool `mjbatch.h` (`persistent=0`)**: **`136.00 MB`** for 512 envs, **Bit-Identical** at any thread count | Python `multiprocessing` IPC overhead, **`2,048.00 MB`** | Single-thread loop or `N` full `mjData` copies | Python multiprocessing only |
| **Anti-Tunneling & Elasto-Plasticity** | **Native `<flag speculative="enable"/>` + `mjData.plastic` (`mjSTATE_PLASTIC`) + 1.4–3× Sparse `Newton` flex** | Manual XML setup; prone to missing `integrator="discrete"` | Breaks on removed `cable`/`flexvert` tags | No speculative contacts or continuum $J_2$ plasticity |
| **CPU `float64` vs. GPU `float32` Parity** | **Bundled `mujoco-parity` `SKILL.md`** stage-by-stage `mj_forward` vs. `mjw.forward` isolation | Ad-hoc reward curve comparison | Blind hyperparameter tuning | No unified C + JAX/CUDA dual backend |
| **Agent Modeling Convergence** | **`2` rounds/task** via bundled `mujoco/doc/skills/` | `5` rounds/task (chunking splits XML tables) | `8` rounds/task (hallucinates removed tags) | High hallucination rate on modern features |

---

## 🧮 Quantitative Worked Example & 7-Card Insights (Closed-Form FinOps & Memory Model)

> **Provenance & Scope Gate**: The calculation below is a **closed-form parametric synthetic model (`CLAIM-R11-02`, `synthetic, independently_reproduced=false`)** covering **LLM API token spend for agent-assisted simulation modeling/debugging (API-only), engineering debugging hours, and `mjbatch.h` CPU memory footprint**. Cloud GPU/CPU node rental and physical robot hardware bills are explicitly marked **`not_measured`**. Every derived number is verified by component-level assertions in `tests/radar-integration.cjs`.

### 1. Explicit Input Parameters

- **Monthly Simulation Modeling & Parity Tasks**: $M_{\text{models}} = 30\text{ tasks/month}$
- **LLM Token Rates**:
  - Input price: $P_{\text{in}} = \$3.00 / 1\text{M tokens}$
  - Output price: $P_{\text{out}} = \$15.00 / 1\text{M tokens}$ (**output cost counted strictly once per round**)
- **CPU Batch Memory Parameters (`include/mujoco/mjbatch.h`)**:
  - Parallel simulations: $N_{\text{sim}} = 512$, CPU threads: $N_{\text{thread}} = 32$
  - Full `mjData` workspace size: $S_{\text{data}} = 4.0\text{ MB}$
  - Compact `mjSTATE_INTEGRATION` row (`mjb_nstate`) size: $S_{\text{state}} = 16\text{ KB} = 0.015625\text{ MB}$

### 2. Step-by-Step Closed-Form Derivation

1. **Path A (Unguided Raw XML Prompting + Blind GPU `float32` Debugging)**:
   - Requires $R_A = 8\text{ rounds/task}$ $\Rightarrow N_A = 30 \times 8 = 240\text{ rounds/month}$
   - Per round: $I_A = 0.060\text{M}$ (`60k`) input tokens, $O_A = 0.005\text{M}$ (`5k`) output tokens
   - Per-round API cost: $(0.060 \times \$3.00)_{\text{in}} + (0.005 \times \$15.00)_{\text{out}} = \$0.1800 + \$0.0750 = \$0.2550 / \text{round}$
   - Monthly API total (API-only): $240 \times \$0.1800\text{ (\$43.20 in)} + 240 \times \$0.0750\text{ (\$18.00 out)} = \mathbf{\$61.20 / \text{mo}}$ (`$2.04 / task`)
   - Engineering debugging time: $30 \times 3.0\text{ h} = \mathbf{90.0\text{ h/mo}}$
   - 512-env full `mjData` memory (`persistent = 1`): $512 \times 4.0\text{ MB} = \mathbf{2,048.00\text{ MB}}$ (`2.00 GB`)

2. **Path B (Generic Doc-RAG Chunking without `mujoco-parity` Stage Isolation)**:
   - Requires $R_B = 5\text{ rounds/task}$ $\Rightarrow N_B = 30 \times 5 = 150\text{ rounds/month}$
   - Per round: $I_B = 0.040\text{M}$ (`40k`) input tokens, $O_B = 0.004\text{M}$ (`4k`) output tokens
   - Per-round API cost: $(0.040 \times \$3.00)_{\text{in}} + (0.004 \times \$15.00)_{\text{out}} = \$0.1200 + \$0.0600 = \$0.1800 / \text{round}$
   - Monthly API total (API-only): $150 \times \$0.1200\text{ (\$18.00 in)} + 150 \times \$0.0600\text{ (\$9.00 out)} = \mathbf{\$27.00 / \text{mo}}$ (`$0.90 / task`)
   - Engineering debugging time: $30 \times 1.8\text{ h} = \mathbf{54.0\text{ h/mo}}$

3. **Path C (MuJoCo `4.0.0`: 7 Bundled `doc/skills/*/SKILL.md`s + `MjSpec` + `mujoco.batch` + `mujoco-parity`)**:
   - Converges in $R_C = 2\text{ rounds/task}$ $\Rightarrow N_C = 30 \times 2 = 60\text{ rounds/month}$
   - Per round: $I_C = 0.012\text{M}$ (`12k`) input tokens, $O_C = 0.002\text{M}$ (`2k`) output tokens
   - Per-round API cost: $(0.012 \times \$3.00)_{\text{in}} + (0.002 \times \$15.00)_{\text{out}} = \$0.0360 + \$0.0300 = \$0.0660 / \text{round}$
   - Monthly API total (API-only): $60 \times \$0.0360\text{ (\$2.16 in)} + 60 \times \$0.0300\text{ (\$1.80 out)} = \mathbf{\$3.96 / \text{mo}}$ (`$0.132 / task`)
   - Engineering debugging time: $30 \times 0.5\text{ h} = \mathbf{15.0\text{ h/mo}}$
   - `mjbatch.h` (`persistent = 0`, 32 threads + 512 state rows) memory: $(32 \times 4.0\text{ MB}) + (512 \times 0.015625\text{ MB}) = 128.00\text{ MB} + 8.00\text{ MB} = \mathbf{136.00\text{ MB}}$

### 3. Summary Comparison Table

| Path | Monthly Rounds | Input Cost/Mo | Output Cost/Mo (Counted Once) | **Monthly API Total (API-Only)** | **512-Env Active RAM** | **Debugging Hours/Mo** | **GPU/Robot Lab Infra Bill** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Path A: Raw XML Prompting + Full `mjData`** | `240` (`30×8`) | `$43.20` | `$18.00` | **`$61.20 / mo`** (`$2.04/task`) | `2,048.00 MB` | `90.0 h / mo` | `not_measured` |
| **Path B: Generic Doc-RAG + No Parity Harness** | `150` (`30×5`) | `$18.00` | `$9.00` | **`$27.00 / mo`** (`$0.90/task`) | `2,048.00 MB` | `54.0 h / mo` | `not_measured` |
| **Path C: MuJoCo 4.0 (7 `SKILL.md`s + `mjbatch.h`)** | `60` (`30×2`) | `$2.16` | `$1.80` | **`$3.96 / mo`** (`$0.132/task`) | **`136.00 MB`** (**`-93.36%`**) | **`15.0 h / mo`** | `not_measured` |
| **Net Savings (Path C vs. Path A)** | **`-180 rounds`** (`-75.00%`) | **`-$41.04 / mo`** | **`-$16.20 / mo`** | **`-$57.24 / mo` (`-$686.88/yr`, `-93.53%`)** | **`-1,912.00 MB` (`-93.36%`)** | **`-75.0 h / mo` (`-83.33%`)** | `not_measured` |

---

## ✅ Production Readiness Checklist for Solution Architects

- [ ] **1. Clean Package Split Upgrade to MuJoCo 4.0**: When upgrading from 3.x, run `pip uninstall -y mujoco && pip install mujoco` (or `pip install mujoco-core` on headless RL/MPC servers where `numpy` is the only required dependency).
- [ ] **2. Mount Bundled `mujoco/doc/skills/` in Coding Agents**: Point Claude Code / Copilot CLI to `pathlib.Path(mujoco.__file__).parent / 'doc' / 'skills'` so the agent loads `mujoco-spec-editing`, `mujoco-python`, `mujoco-accelerated`, or `mujoco-parity` before editing models.
- [ ] **3. Audit MuJoCo 4.0 Breaking Changes**:
  - Migrate removed `cable` plugin and `flexvert` constraints to 1D/2D `flexcomp` + `<elasticity>` with `integrator="discrete"`;
  - Verify spatial tendon `sidesite` placements under the new 4.0 homotopy shortest-path rule;
  - Include `mjSTATE_PLASTIC` when saving/restoring models with elasto-plasticity (`springyield` / `flex` `yield`) or open 1D elastic rods.
- [ ] **4. Right-Size CPU vs. GPU Batching**: Use `mujoco.batch.Batch` (`persistent = 0`) for `N_env <= 256` CPU rollouts and bit-identical regression tests; before scaling to `MJX` / `MJWarp` on GPU, run `mujoco-parity` single-step `mj_forward` vs. `mjw.forward` verification.
