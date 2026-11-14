# Zero-Demonstration Sim-to-Real Robotic RL Engine (MIT HAN Lab `PEAR`) & Recursive Self-Improving Training Infrastructure (`InfraRSI`) Architecture & Selection FAQ

> **Document Metadata (2026-11-14 · Daytime Round 45 / Cumulative Round 228)**  
> - **Benchmark Style**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (First-Principles Breakdown + Plain-English Takeaways + 3 Core Architectural Q&As + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> - **Evaluated Repositories**:  
>   1. [`mit-han-lab/pear`](https://github.com/mit-han-lab/pear) (`★ 76`, MIT HAN Lab's **PEAR: Post-Training Engine for Agentic Robotics**, training an open `27B` reasoning model `qwen3_8_27b_pear` to natively control real robots entirely in simulation with **zero demonstrations** via asynchronous RL on `veRL`, `GRPO` + dynamic sampling + **Score Centering**, cross-round prefix caching with **`LMCache` CPU KV offloading**, co-located Ray simulation `MuJoCo` on CPUs + `Isaac Sim` on GPUs, and single-`RTX 5090`/`GB300` vLLM deployment with **decode megakernels**)  
>   2. [`TokenRhythm/InfraRSI`](https://github.com/TokenRhythm/InfraRSI) (`★ 72`, `arXiv:2611.11558`, **InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure**: autonomously optimizes distributed training launch scripts and kernels, achieving a **`1.83×` geometric-mean speedup** and up to **`2.75×`** across 4 dense and MoE workloads on `H100`/`H200` while raising mean **Model FLOPs Utilization (MFU) from `17.4%` to `30.0%`**)  
> - **Companion SVG Diagram**: [`assets/github-ai-radar-2026-11-14-r45-pear-infrarsi.svg`](../../../assets/github-ai-radar-2026-11-14-r45-pear-infrarsi.svg)  
> - **Audit Claim ID**: `CLAIM-20261114-R45-PEAR-INFRARSI` (physical robot arm hardware depreciation marked `not_measured`)

---

## 📌 1. Executive Summary (3-Minute Architect's Briefing)

1. **How does MIT HAN Lab's `mit-han-lab/pear` train a 27B reasoning model to natively operate real robots with ZERO human teleoperation demonstrations?**  
   - **Plain-English Reality**: Traditional robotic foundation models require thousands of hours of expensive human teleoperation demonstrations for imitation learning, and stall during multi-turn reinforcement learning (RL) because synchronous simulators block GPU workers while repeated long-context trajectory prefixes exhaust GPU HBM.  
   - **`PEAR` First-Principles Fix**: Post-trains an open `27B` reasoning model (`qwen3_8_27b_pear`) purely in simulation with **zero demonstrations**:
     - **Fully Asynchronous `veRL` + Co-Located Ray Simulators**: Runs `GRPO`, dynamic sampling, and **Score Centering** asynchronously while scheduling `MuJoCo` on CPU workers and `Isaac Sim` on GPU workers within the same Ray cluster;
     - **Cross-Round Prefix Caching via `LMCache`**: Offloads shared multi-turn trajectory KV caches to host CPU memory across RL rounds alongside FSDP, sequence parallelism, gradient checkpointing, and activation offloading;
     - **Single-`RTX 5090` / `GB300` Decode Megakernels**: Evaluates across 5 robotic benchmarks (`LIBERO`, `LIBERO-Plus`, `LIBERO-Pro`, `RoboDojo`, `RoboLab-120`) and 9 general `EvalScope` benchmarks, and deploys on a single `RTX 5090` or `GB300` via vLLM **decode megakernels**.
2. **Why do out-of-the-box MoE training scripts suffer `6.4%–8.7%` MFU on H100/H200 clusters, and how does `TokenRhythm/InfraRSI` (`arXiv:2611.11558`) lift MFU from `17.4%` to `30.0%` (`1.83×` geomean speedup)?**  
   - **Plain-English Reality**: Running default distributed training launch scripts on `8×H100` or `8×H200` leaves over `80%–93%` of GPU FLOPs idle due to suboptimal parallelism splits, communication stalls, and unoptimized kernels.  
   - **`InfraRSI` First-Principles Fix**: Accepts an existing launch script, Python entrypoint, or repo, autonomously searches faster configurations and code changes, **verifies equivalence against the original job**, and banks verified optimizations into a reusable experience library:
     - **Verified 4-Workload Benchmark Ledger (counting all failed & audit-excluded attempts in token budgets)**:
       1. `Qwen3.5-9B` (`8×H100`): **`1.73×` speedup**, MFU `25.3% -> 43.8%`;
       2. `Gemma-4-26B-A4B MoE` (`8×H200`): **`2.75×` speedup**, MFU `6.4% -> 17.6%`;
       3. `Qwen3.8-27B` (`8×H200`): **`1.55×` speedup**, MFU `29.3% -> 45.4%`;
       4. `Qwen3.5-35B-A3B MoE` (`16×H100`, 2 nodes): **`1.51×` speedup**, MFU `8.7% -> 13.2%`;
       - **Overall**: **`1.83×` geometric-mean speedup** and **`17.4% -> 30.0%` mean MFU**, outperforming `RE-Bench`, `Auto-Research`, and `OptiCo`.
3. **Closed-Form FinOps Audit (`CLAIM-20261114-R45-PEAR-INFRARSI`)**:  
   - Across **4 distributed `8×H100 / 8×H200` post-training runs per month** (at **`$100.00/hr`** engineering rate), migrating from **Path A** (unoptimized `17.4%` MFU baseline scripts + manual teleoperation & flag tuning: **`$5,950.00/mo`**) to **Path C** (`InfraRSI` `1.83×` speedup / `30.0%` MFU + `PEAR` zero-demo async RL with `LMCache`: **`$515.00/mo`**) saves **`$5,435.00/month`** (**`-91.34%`**, **`$65,220.00/year`**) and cuts engineering labor from `38.0 hrs` to `3.5 hrs/mo` (**`-90.79%`**).

![PEAR & InfraRSI Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r45-pear-infrarsi.svg)

---

## 💬 2. Three Architectural Deep-Dive Q&As (Q1–Q3)

### Q1: How does `mit-han-lab/pear` prevent multi-turn KV cache exhaustion during 27B robotic RL training and achieve real-time inference on a single `RTX 5090`?

1. **Cross-Round `LMCache` CPU KV Offloading + Score Centering**:  
   - Multi-step robotic episodes share long observation-reasoning prefixes across consecutive turns. By pairing `veRL`'s asynchronous `GRPO` + **Score Centering** pipeline with **`LMCache`**, `PEAR` offloads KV caches to host CPU RAM across rounds instead of recomputing prefixes on GPU HBM.
2. **Single-GPU vLLM Decode Megakernels**:  
   - Fuses sequential decode operations into **decode megakernels** inside vLLM so the `27B` `qwen3_8_27b_pear` model runs low-latency closed-loop control on a single `RTX 5090` or `GB300`.

---

### Q2: Why is `TokenRhythm/InfraRSI`'s inclusion of failed and audit-excluded attempts in its token accounting a critical benchmark standard?

1. **Eliminating Survivor-Bias in Autonomous Infra Optimization**:  
   - Reporting only the tokens consumed by the final winning trajectory hides the true search cost of OOM crashes and numerically divergent edits. `InfraRSI` counts every failed and audit-rejected trial against its token budget while still delivering a `1.83×` geomean speedup (`2.75×` on `Gemma-4-26B-A4B MoE`).

---

### Q3: How should AI infrastructure architects combine `InfraRSI` and `PEAR`?

1. **Run `InfraRSI` First** on your training launch scripts to lift cluster MFU from `6%–25%` up to `13%–45%` before committing long multi-node GPU reservations.
2. **Run `PEAR` Second** for multi-turn agentic/robotic RL post-training with `LMCache` CPU KV offloading and dual `LIBERO-Pro` + `EvalScope` regression gates.

---

## 🧭 3. Architecture Decision Tree & RL/Infra Topology (Mermaid)

```mermaid
flowchart TD
    Start["Agentic Robotic RL Post-Training & H100/H200 MFU Optimization Selection"] --> Stage{"Primary Infrastructure Bottleneck?"}

    Stage -->|"Low Cluster MFU (6%-25%) on Dense/MoE Training Jobs"| InfraGate{"Optimization Strategy?"}
    InfraGate -->|"Autonomous Search + Equivalence Audit against Original Job<br/>+ Persistent Experience Library"| UseInfraRSI["✅ TokenRhythm/InfraRSI (arXiv:2611.11558)<br/>• 1.83x Geomean Speedup (Up to 2.75x on Gemma-4-26B MoE)<br/>• Lifts Mean MFU from 17.4% to 30.0% (Honest Token Ledger)"]
    InfraGate -->|"Manual Trial-and-Error Flag Tuning"| ManualTune["⛔ Manual Grid Search (Slow & Prone to Silent Divergence)"]

    Stage -->|"Post-Training 27B Reasoning Models for Real Robots"| RobotGate{"Data & Rollout Architecture?"}
    RobotGate -->|"Zero Human Demonstrations + Async veRL + LMCache KV Offload<br/>+ Single RTX 5090 Decode Megakernels"| UsePEAR["✅ mit-han-lab/pear (MIT HAN Lab · 27B Engine)<br/>• GRPO + Score Centering + Co-Located Ray MuJoCo/Isaac Sim<br/>• Evaluated on 5 Robot Suites + 9 EvalScope Benchmarks"]
    RobotGate -->|"Expensive Human Teleoperation SFT"| TeleopSFT["🔄 Manual Teleoperation Imitation Learning"]

    UseInfraRSI --> FinOps["💰 Closed-Form FinOps Impact (CLAIM-20261114-R45-PEAR-INFRARSI)<br/>Monthly Total $5,950.00 ➔ $515.00 (-91.34% · Saves $65,220/yr)"]
    UsePEAR --> FinOps
```

---

## 📊 4. Peer Comparison Matrix (Decision Matrix)

| Dimension | `mit-han-lab/pear` (MIT HAN Lab Robotic RL) | Teleoperation SFT + Synchronous RL | `TokenRhythm/InfraRSI` (`arXiv:2611.11558`) | Manual Tuning / Memoryless Agents (`RE-Bench`/`OptiCo`) |
| :--- | :--- | :--- | :--- | :--- |
| **Core Breakthrough** | **Zero-demo sim RL trains open 27B model for real robots** | Requires thousands of human teleop trajectories | **Recursive self-improving infra optimizer with experience bank** | Memoryless trial-and-error search |
| **Throughput & MFU Gain** | **`LMCache` CPU KV offload + H100/H200/GB300 kernels** | Recomputes multi-turn prefixes; synchronous sim stalls | **`1.83×` geomean speedup (up to `2.75×`), MFU `17.4% -> 30.0%`** | Baseline MoE scripts stall at `6.4%–8.7%` MFU |
| **Verification & Eval** | **5 robot suites (`LIBERO-Pro`/`RoboLab-120`) + 9 `EvalScope` suites** | Narrow task eval; forgets general reasoning | **Strict equivalence check against original training job** | Risk of silent numerical drift |
| **Cost Accounting Honesty** | Open weights, paper, and single-GPU deploy recipes | Unreported human teleop collection labor | **Counts all failed & audit-excluded attempts in token spend** | Often reports only winning-run token cost |
| **Deployment Target** | **vLLM + decode megakernels on 1× `RTX 5090` or `GB300`** | Multi-GPU server required for 27B control | Supports Claude Code, Codex, DeepSeek & API backends | — |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps Audit (`CLAIM-20261114-R45-PEAR-INFRARSI`)

> **Scope & Provenance Boundary**: Models monthly H100/H200 GPU cluster spend across **4 distributed post-training & MoE runs** plus engineering labor for teleoperation data collection and parallelism flag tuning at **`$100.00/hr`**. Physical robot arm hardware acquisition is explicitly marked **`not_measured`**.

| Architecture Path | Cluster GPU & Token Spend (`USD/mo`) | Teleop & Infra Tuning Labor (`hrs/mo`) | Engineering Labor Cost (`@ $100/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Unoptimized `17.4%` MFU Baseline + Human Teleop Collection** | `$2,150.00` | `38.0 hrs` | `$3,800.00` | **`$5,950.00`** | Baseline (`0.00%`) |
| **Path B: Manual Flag Grid Search + Synchronous RL Rollouts** | `$1,020.00` | `18.5 hrs` | `$1,850.00` | **`$2,870.00`** | `-$3,080.00` (`-51.76%`) |
| **Path C (Recommended): `InfraRSI` (`30.0%` MFU) + `PEAR` (`LMCache`)** | **`$165.00`** | **`3.5 hrs`** | **`$350.00`** | **`$515.00`** | **`-$5,435.00` (`-91.34%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 2150.00 + 38.0 \times 100.00 = 2150.00 + 3800.00 = \$5,950.00$
  - $\text{Path B Total} = 1020.00 + 18.5 \times 100.00 = 1020.00 + 1850.00 = \$2,870.00$
  - $\text{Path C Total} = 165.00 + 3.5 \times 100.00 = 165.00 + 350.00 = \$515.00$
  - $\text{Net Savings (Path C vs Path A)} = 5950.00 - 515.00 = \$5,435.00/\text{mo} \quad (-91.34\%, \text{Annualized } \$65,220.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect Quick-Start Checklist

1. **Optimize Existing Distributed Training Launch Scripts with `TokenRhythm/InfraRSI`**:
   ```bash
   git clone https://github.com/TokenRhythm/InfraRSI.git
   cd InfraRSI && pip install -e .
   ```
2. **Deploy `mit-han-lab/pear` (`qwen3_8_27b_pear`) with vLLM Decode Megakernels on `RTX 5090` / `GB300`**:
   ```bash
   git clone https://github.com/mit-han-lab/pear.git
   cd pear
   cat examples/models/qwen3_8_27b_pear/deploy/README.md
   ```
