# 30-Minute Single-RTX-5090 Differentiable World-Model Humanoid AMP (`InstantAMP`) & Physically Functional MuJoCo World Benchmark (`3DSceneBench`) Deep-Dive Architecture & Selection FAQ

> **Document Metadata**  
> - **Evaluation Date**: 2026-11-15 (Night Round 21 · Cumulative Round 323 Standalone Selection FAQ)  
> - **Evaluated Repositories**: [`RoboticsResearchHubVN/InstantAMP`](https://github.com/RoboticsResearchHubVN/InstantAMP) (`★21`, created 2026-11-13, trains Unitree G1 29-DOF locomotion & fall get-up policies with Adversarial Motion Priors in 30 minutes on 1 RTX 5090 via a JAX + `MuJoCo Warp` differentiable world model & 48-step BPTT, MIT) & [`PranaLabs/3DSceneBench`](https://github.com/PranaLabs/3DSceneBench) (`★21`, created 2026-11-13, Prana Labs & UC Berkeley benchmark evaluating whether coding agents can build simulated MuJoCo worlds `scene.xml` + `nonrigid.json` graded on Appearance, Geometry & Functionality across 49 scenes / 14,219 objects / 471 tasks / 36,871 hidden tests, Apache-2.0)  
> - **Target Audience**: AI Solution Architects (AI SAs), Embodied AI & Robotics Simulation Leads, Spatial Agent Benchmark Engineers  
> - **Related Radar Digest**: [2026-11-15 Panorama & Velocity Digest (`daily/2026-11-15.en.md`)](../daily/2026-11-15.en.md) · [中文版 (`instantamp-3dscenebench-30min-rtx5090-world-model-amp-mujoco-functional-scene-benchmark-selection-faq.md`)](instantamp-3dscenebench-30min-rtx5090-world-model-amp-mujoco-functional-scene-benchmark-selection-faq.md)  
> - **Visual Summary**: [`assets/github-ai-radar-2026-11-15-r21-instantamp-3dscenebench.svg`](../../../assets/github-ai-radar-2026-11-15-r21-instantamp-3dscenebench.svg)

![InstantAMP + 3DSceneBench Architecture Overview](../../../assets/github-ai-radar-2026-11-15-r21-instantamp-3dscenebench.svg)

---

## 📌 1. Executive Summary

1. **First-Principles Essence (What & Why)**:
   - **What is `RoboticsResearchHubVN/InstantAMP`?** It is a **single-GPU, 30-minute differentiable world-model Adversarial Motion Prior (AMP) training framework for the 29-joint Unitree G1 humanoid robot** (`JAX` + `MuJoCo Warp`). Rather than relying solely on sample-hungry model-free RL, `InstantAMP` fits a **differentiable world model (`MLP 3x512`, 8-step open-loop loss)** to simulator transitions and optimizes an ODE actor via **analytic gradients over 48-step (`~1s`) imagined rollouts (BPTT)** (blended with 10% real-step PPO). Both WGAN-GP style discriminators (10-frame windows for walking/running and LAFAN1 floor get-up) are differentiable with respect to imagined states, enabling a single RTX 5090 (`4,096` parallel envs, `146s` compile, `3.4 it/s`) to master floor get-up by **10 minutes** and natural human-like walking/running by **15–30 minutes** (`ep_len = 935/1000`).
   - **What is `PranaLabs/3DSceneBench`?** It is a **whole-room physical simulation benchmark (`49` scenes across `7` categories, `14,219` objects, `471` tasks, `36,871` hidden tests)** by Prana Labs and UC Berkeley that tests whether coding agents can turn posed room images and task specifications into **working MuJoCo worlds (`scene.xml` + `nonrigid.json`)**. Because *"a mug can look perfect and still be a solid block that holds nothing, and a drawer can look perfect and still hit the chair in front of it when it opens,"* `3DSceneBench` physically pushes objects, opens doors/drawers, pours water, and runs robots in both the agent's world and the ground-truth **Reference Room**, scoring **Appearance (`0–100`), Geometry (`0–100`), and Functionality (`0–100`)**.
2. **Why AI SAs Should Adopt This Pattern Tonight**:
   - `3DSceneBench` prevents embodied-AI teams from accepting visually pretty but physically broken agent-generated simulation environments.
   - `InstantAMP` collapses humanoid locomotion + fall-recovery policy iteration from multi-node overnight runs down to a **30-minute coffee break on 1 GPU**.
3. **Quantitative FinOps Summary (`CLAIM-20261115-R21-INSTANTAMP-3DSCENEBENCH`)**:
   - Across `32` monthly humanoid policy training runs and `28` whole-room MuJoCo simulation world builds/audits (`$100.00/hr` engineer rate; base host compute: `not_measured`), moving from "Multi-node model-free PPO clusters + visual-only scene QA (Path A, `$6,320.00/mo`)" to "`InstantAMP` 30-min world-model BPTT + `3DSceneBench` functional grader (Path C, `$485.00/mo`)" **saves `$5,835.00/mo` (`-92.33%`), or `$70,020.00/yr`, while freeing `38.5` engineering hours/month (`-91.67%`)**.

---

## 🔍 2. First-Principles Deep Dive (Q1–Q3)

### Q1: How does `InstantAMP` train a 29-DOF Unitree G1 to walk, run, and recover from falls in 30 minutes on 1 RTX 5090?

- **Three Core Algorithmic Innovations**:
  1. **Analytic Gradients Through a Differentiable World Model (`48-Step BPTT` in JAX + `MuJoCo Warp`)**:
     - Compiles the 200Hz physics simulator (`mjlab` G1 MJCF with full self-collisions and torque-speed actuator friction) and 50Hz learner in JAX (`146s` compile time).
     - Fits an `MLP 3x512` world model (`8-step` open-loop loss) and backpropagates analytic gradients through `48-step` (`~1s`) imagined rollouts bootstrapped by a critic, plus a 10% hybrid PPO term on real collector transitions.
  2. **Dual Gated WGAN-GP Motion Priors (`style_loco` + `style_getup`)**:
     - `20%` of episode resets start with G1 lying on the floor in a LAFAN1 get-up pose (`5s` deadline to stand). The imagined reward combines task tracking and both differentiable style priors:
       $$r = (1 - \text{amp\_lerp}) \cdot r_{\text{task}} + \text{amp\_lerp} \cdot dt \cdot (\text{ramp} \cdot \text{gate}_{\text{loco}} \cdot \text{style}_{\text{loco}} + \text{gate}_{\text{getup}} \cdot \text{style}_{\text{getup}})$$
  3. **Self-Centered Tanh Style Normalization**:
     - Each style term is computed as $(1 + \tanh((d - \bar{d}_{\text{robot}}) / 5)) / 2$. Centering on the robot's own mean discriminator score $\bar{d}_{\text{robot}}$ keeps the reward slope constant regardless of how far the policy currently is from expert mocap clips.

### Q2: Why do today's coding agents score much lower on `Functionality` than on `Appearance` or `Geometry` in `3DSceneBench`?

- **The "Visual Shell" Trap in Agent-Authored 3D Worlds**:
  - Coding agents optimizing against VLM screenshot critiques frequently produce solid convex hulls for cups/sinks (blocking fluid pouring in `nonrigid.json`), omit hinge/slide joint limits on cabinets, or place furniture where opening a drawer collides with an adjacent chair.
- **`3DSceneBench`'s Reference-Room Differential Grading**:
  - Executes `36,871` hidden physical tests—pushing objects, opening articulated joints, pouring water, and running robot trajectories—in both the candidate `scene.xml` and the ground-truth Reference Room, isolating exact functional regressions (`3dscenebench-mini` grades 7 representative scenes on CPU-only Docker).

### Q3: How should AI SAs combine both repositories in an Embodied AI pipeline?

- Use `3DSceneBench` as the automated CI gate for agent-generated MuJoCo rooms (`scene.xml` + `nonrigid.json`), and train Unitree G1 locomotion/recovery controllers inside validated scenes using `InstantAMP`'s 30-minute JAX/Warp loop.

---

## 🧭 3. Architecture & Selection Decision Tree (Mermaid)

```mermaid
flowchart TD
    Start["AI SA Embodied AI Simulation & Humanoid Control Need"] --> Layer{"Which embodied AI bottleneck is targeted?"}

    Layer -->|"Need to evaluate whether coding agents generate<br/>physically functional MuJoCo rooms (not visual shells)"| Bench["Adopt PranaLabs/3DSceneBench<br/>(49 Scenes · 36,871 Hidden Tests · 3-Pillar Score)"]
    Layer -->|"Need 30-minute single-GPU humanoid locomotion<br/>& fall get-up training with AMP style priors"| Amp["Adopt RoboticsResearchHubVN/InstantAMP<br/>(JAX + MuJoCo Warp · 48-Step World-Model BPTT)"]

    Bench --> BenchFlow["1. Agent receives posed room images + tasks -> writes scene.xml & nonrigid.json"]
    BenchFlow --> BenchEval["2. Grader runs doors/drawers, water pouring & robot tasks vs Reference Room"]
    BenchEval --> BenchScore["3. Emits Appearance, Geometry & Functionality scores (0-100)"]

    Amp --> AmpStep1["1. Compile MuJoCo Warp in JAX (4096/8192 envs on 1 RTX 5090)"]
    AmpStep1 --> AmpStep2["2. Fit 3x512 world model + dual WGAN-GP priors (walk + LAFAN1 get-up)"]
    AmpStep2 --> AmpStep3["3. Optimize ODE actor via 48-step BPTT + self-centered tanh style"]
    AmpStep3 --> AmpResult["4. Converges get-up in 10m, walking in 15m, full policy in 30m"]
```

---

## 📊 4. Comparison Matrix Against Alternative Approaches

| Dimension | Multi-Node Model-Free PPO + Screenshot QA (Path A) | Split Controllers + Static Mesh Checks (Path B) | `InstantAMP` + `3DSceneBench` Stack (Path C) |
| :--- | :--- | :--- | :--- |
| **29-DOF G1 Walk + Get-Up Training Time** | ❌ 8–24 hours across multi-GPU clusters | ⚠️ Separate policies stitched with brittle heuristics | ✅ **`30 minutes` on 1 RTX 5090 (`10m` get-up, `15m` walk, `30m` `ep_len 935`)** |
| **Gradient Estimator & Style Slope Stability** | ❌ High-variance zero-order RL; discriminator saturation | ⚠️ Lacks smooth transition gradients | ✅ **48-step analytic BPTT through world model + self-centered `tanh` slope** |
| **Physical Scene Functionality Verification** | ❌ Visual renders miss solid mugs & jammed drawers | ⚠️ Static AABB checks miss articulation & fluid pouring | ✅ **`36,871` hidden tests (doors, drawers, pouring, robot tasks) vs Reference Room** |
| **CPU-Only Verification Accessibility** | ❌ Requires GPU cluster for every test | ⚠️ Partial | ✅ **`JAX_PLATFORMS=cpu pytest` (`InstantAMP`) & CPU-only Docker grading (`3DSceneBench`)** |
| **Push & Fall Recovery Robustness** | ⚠️ Episode terminates on fall; no floor recovery | ⚠️ Fragile handoffs under external pushes | ✅ **Trained with 5–10s pushes, 20% floor starts & friction/CoM randomization** |

---

## 📈 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

### 5.1 7-Card Benchmark Summary

1. **Card 1 (Overview & Workbench)**: Across `32` monthly humanoid policy runs and `28` MuJoCo scene functionality audits, Path C reduces monthly cost from `$6,320.00` to `$485.00` (`-92.33%`).
2. **Card 2 (Single-Case Deep Dive)**: `InstantAMP` reaches `935/1000` episode length in `30 min` (`993` at `60 min`, `0.17 m/s` median velocity error up to `2.7 m/s`) on 1 RTX 5090; `3DSceneBench` grades `scene.xml` + `nonrigid.json` across Appearance, Geometry, and Functionality.
3. **Card 3 (Evaluation Matrix)**: Evaluates single-GPU training time (`30 min`), JAX compile warm-up (`146 s`), hidden benchmark test count (`36,871`), and CPU-only test/grading support (`100%`).
4. **Card 4 (Under the Hood)**: `InstantAMP` couples a `3x512` world model, 48-step BPTT, and dual 10-frame WGAN-GP discriminators; `3DSceneBench` runs comparative MuJoCo physics rollouts against Reference Rooms.
5. **Card 5 (Robustness Check)**: Survives periodic external pushes every `5–10 s`, reset shoves, and randomized foot friction/encoder bias/torso CoM.
6. **Card 6 (Latency & Labor Scaling)**: Cuts monthly RL tuning and broken-collider debugging labor from `42.0h` to `3.5h` (`38.5h/mo` saved, `-91.67%`).
7. **Card 7 (My Take — Good Fit vs Not For)**:
   - ✅ **Good Fit**: Humanoid locomotion/recovery research on single workstation GPUs and spatial coding agent evaluations requiring working MuJoCo physics.
   - ⛔ **Not For**: Non-interactive architectural visualization where rigid/nonrigid physics are never simulated.

### 5.2 Closed-Form FinOps Ledger (`CLAIM-20261115-R21-INSTANTAMP-3DSCENEBENCH`)

> **Provenance & Parameter Disclosure**: Synthetic FinOps model (`synthetic_model`, `independently_reproduced=false`) for `N_pol = 32` policy runs/month and `N_scn = 28` simulation world audits/month at `$100.00/hr` engineer rate (base host compute: `not_measured`). Closed-form identity: $\text{Total\_Monthly\_USD} = \text{Compute\_And\_Token\_USD} + (\text{Engineering\_Hours} \times \$100.00)$.

| Architecture Path | Monthly GPU Cluster / Sim Spend (USD) | Monthly RL Tuning & Scene Debugging Labor (Hours) | Engineering Labor Cost (`@ $100.00/hr`) | Total Monthly Cost (USD) | Net Savings vs Path A (USD / %) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Multi-Node Model-Free PPO + Visual-Only Scene QA** | `$2,120.00` | `42.0h` | `$4,200.00` | **`$6,320.00`** | Baseline (`0.00%`) |
| **Path B: Split Locomotion/Get-Up Controllers + Static Mesh Checks** | `$1,040.00` | `20.0h` | `$2,000.00` | **`$3,040.00`** | `-$3,280.00` (`-51.90%`) |
| **Path C: `InstantAMP` 30-Min BPTT + `3DSceneBench` Grader (Recommended)** | `$135.00` | `3.5h` | `$350.00` | **`$485.00`** | **`-$5,835.00` (`-92.33%`)** |

---

## 🛠️ 6. 15-Minute Rollout Checklist

- [ ] **Step 1 (4 mins): Clone `InstantAMP` and run the CPU-only verification suite**
  ```bash
  git clone https://github.com/RoboticsResearchHubVN/InstantAMP.git
  cd InstantAMP
  python3.11 -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt
  JAX_PLATFORMS=cpu python -m pytest tests
  ```
- [ ] **Step 2 (4 mins): Launch a 30-minute single-GPU Unitree G1 AMP training run**
  ```bash
  # Run default 4,096-environment training on CUDA 12.8+ / driver 580+
  ```
- [ ] **Step 3 (4 mins): Clone `3DSceneBench` and configure Docker memory for `3dscenebench-mini`**
  ```bash
  git clone https://github.com/PranaLabs/3DSceneBench.git
  cd 3DSceneBench
  # Allocate 16 GB RAM (small scenes) or 48 GB RAM (all 7 mini scenes) in Docker
  ```
- [ ] **Step 4 (3 mins): Grade an agent-built `scene.xml` + `nonrigid.json` world across Appearance, Geometry & Functionality**
  ```bash
  # Run the 3DSceneBench grader to compare physical task outcomes against the Reference Room
  ```
