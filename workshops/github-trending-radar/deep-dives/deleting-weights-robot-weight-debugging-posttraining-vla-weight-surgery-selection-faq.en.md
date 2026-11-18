# `<0.05%` Gate-Projection Deletion Tuning (`agentic-learning-ai-lab/deleting-weights` NeurIPS 2026) & 65-Row Gradient-Free Robot Weight Surgery (`jushengzhang/robot-weight-debugging`) Selection FAQ

> **Document Scope**: This is the **2026-11-13 Night Shift Round 8 (Cumulative #136) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects, LLM Post-Training Leads, and Embodied AI / VLA Researchers evaluating two surgical weight-space repositories:
> 1. **`agentic-learning-ai-lab/deleting-weights` (`82★` in 3 days, Python, MIT, NYU & University of Calgary **NeurIPS 2026** paper `arXiv:2611.10866`, HuggingFace `Jacklu0831/deletion-tuning-masks`)**: Official code for **Deletion Tuning** — demonstrating that **zeroing fewer than `0.05%` of pretrained weights** (learning a binary mask over the gate projection of transformer blocks with no other parameter changes) matches Full Fine-Tuning (FFT) at scale across **GRPO, SFT, and on-policy self-distillation (SDFT)**, producing compressed bitmap masks **hundreds to thousands of times smaller** than FFT checkpoints while preventing the up to **`5.4`-point prior-task accuracy drop** seen in FFT, LoRA, and random sparse fine-tuning!
> 2. **`jushengzhang/robot-weight-debugging` (`54★` in 4 days, Python, Apache-2.0, Stanford & X-Era AI `arXiv:2611.09376`, `v0.1.0`)**: Official code and 16 full agent transcripts for *"Can LLMs Debug Robots by Editing Their Weights?"* — where an LLM agent (`GPT-6 Astra`) inspects a pretrained $\pi_{0.5}$ robot policy's weights and repairs instruction-paraphrase failures by **editing just `65 token-embedding rows`** via weight inspection and budgeted simulator feedback (**zero gradient updates, zero new demonstrations**), lifting held-out LIBERO-Plus accuracy from **`86.3%` to `92.0%`** (`74.3% → 87.5%` on the 335 edited-token episodes, $p = 1.31 \times 10^{-10}$, with **zero binary outcome changes** across the other 430 episodes)!
>
> **中文版本**: [deleting-weights-robot-weight-debugging-posttraining-vla-weight-surgery-selection-faq.md](deleting-weights-robot-weight-debugging-posttraining-vla-weight-surgery-selection-faq.md) · **Daily Digest**: [`daily/2026-11-13.en.md`](../daily/2026-11-13.en.md) · **Topic SVG**: [`assets/github-ai-radar-2026-11-13-r8-deletingweights-robotweight.svg`](../../../assets/github-ai-radar-2026-11-13-r8-deletingweights-robotweight.svg)

![deleting-weights and robot-weight-debugging Architecture Comparison](../../../assets/github-ai-radar-2026-11-13-r8-deletingweights-robotweight.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "multi-gigabyte Full Fine-Tuning checkpoint sprawl and the 5.4-point catastrophic forgetting penalty during RL post-training" (`agentic-learning-ai-lab/deleting-weights`)**: Post-training an LLM with GRPO, SFT, or SDFT traditionally modifies 100% of weights (producing massive checkpoints and losing up to `5.4` points on prior tasks) or constrains updates to low-rank LoRA adapters. `deleting-weights` proves that **zeroing fewer than `0.05%` of gate-projection weights** — with zero other weight changes — matches Full Fine-Tuning at scale! Each task is stored as a compressed bitmap mask hundreds to thousands of times smaller than an FFT checkpoint, and because `>99.95%` of pretrained weights remain untouched, prior-task accuracy stays near base levels!
   - **Ending "expensive teleoperation data collection and full gradient retraining just to fix a robot VLA policy that times out on unfamiliar phrasing" (`jushengzhang/robot-weight-debugging`)**: When a pretrained $\pi_{0.5}$ robot policy fails on a phrased instruction like *"position the glass container of fermented grapes atop the storage unit for dishes and utensils"* (timing out at 300 steps), gradient fine-tuning risks breaking existing skills. `robot-weight-debugging` lets an LLM agent inspect the weight matrix and **surgically edit 65 token-embedding rows** with zero gradient updates and zero new demonstrations — succeeding in 85 steps, boosting 765 held-out LIBERO-Plus episodes from `86.3%` to `92.0%` ($p = 1.31 \times 10^{-10}$), and causing **zero binary outcome changes** on the 430 untouched-token episodes!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261113-R8-DELETINGWEIGHTS-ROBOTWEIGHT`)**:
   - Modeled for an **LLM and embodied AI team delivering `24 domain post-trained LLM variants per month` and `16 robot policy instruction hotfixes per month`** (fully loaded ML/robotics engineer rate `$105.00/hr`; base pretraining cluster capex and physical robot arm hardware: `not_measured`):
   - Upgrading from **Path A (Full Fine-Tuning checkpoints + continual-learning replay + teleop retraining for robot policies, `$7,950.00/mo`)** to **Path C (`deleting-weights` `<0.05%` bitmap Deletion Tuning + `robot-weight-debugging` 65-row gradient-free weight surgery, `$915.00/mo`)** saves **`$7,035.00/mo` (`-88.49%`, or `$84,420.00/yr`)** and cuts ML/robotics engineering toil from `46.0 hrs/mo` to `5.0 hrs/mo` (**`-89.13%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why do dense gradient updates and low-rank adapters struggle with continual RL forgetting and localized VLA bugs?
- **First-Principles Breakdown**:
  1. **Global Activation Drift & Catastrophic Forgetting**: Updating all parameters (or adding dense low-rank matrices) during RL shifts representations globally, degrading prior-task accuracy by up to `5.4` points.
  2. **Overkill Gradient Loops for Lexical Misalignment**: When a VLA policy already knows the motor skill but fails on rare token embeddings, backpropagating through the entire network is slow and risks motor regressions.

### Q2: How does `agentic-learning-ai-lab/deleting-weights` match Full Fine-Tuning by zeroing `<0.05%` of weights?
- **First-Principles Breakdown**:
  1. **Gate-Projection Binary Mask Optimization & Spectral Alignment**:
     - Learns a binary mask over transformer gate projections across GRPO, SFT, and SDFT (`uv` environments `envs/grpo`, `envs/sft`, `envs/sdft`), matching FFT across stable rank, spectrum drift, and principal-weight overlap.
  2. **100×–1,000× Compressed Bitmap Masks**:
     - Serializes each post-trained capability as a compact bitmap (`Jacklu0831/deletion-tuning-masks`) while preserving base-model accuracy on prior tasks.

### Q3: How does `jushengzhang/robot-weight-debugging` repair $\pi_{0.5}$ robot policies via 65-row gradient-free weight surgery?
- **First-Principles Breakdown**:
  1. **Weight-Space Inspection + Budgeted Simulator Rollouts**:
     - An LLM agent inspects pretrained token-embedding geometry, proposes targeted edits to `65 token-embedding rows`, and validates them with budgeted simulator rollouts without computing gradients or collecting new demos.
  2. **Strict Lexical Locality & Full Transcript Provenance**:
     - Raises accuracy on the 335 edited-token episodes from `74.3%` to `87.5%` while leaving the 430 unedited-token episodes at exactly `411 / 430` successes, with all 16 editing session transcripts archived in `transcripts/`.

---

## 🧭 3. Mermaid Decision Tree & Bitmap Deletion Tuning + 65-Row Weight Surgery Architecture

```mermaid
flowchart TD
    A["LLM Post-Training & Embodied VLA Policy Repair Architecture Selection"] --> B{"Primary Model Evolution Goal?"}
    B -- "LLM Post-Training (GRPO/SFT/SDFT): Match FFT without 5.4-pt forgetting or multi-GB checkpoints" --> C["Adopt agentic-learning-ai-lab/deleting-weights (NeurIPS 2026 Deletion Tuning)"]
    B -- "Embodied VLA Policy Repair: Fix instruction paraphrase/suffix failures with zero gradients" --> D["Adopt jushengzhang/robot-weight-debugging (65-Row Embedding Surgery)"]

    C --> C1["Learn binary mask zeroing <0.05% of transformer gate-projection weights"]
    C1 --> C2["Export 100x-1000x smaller compressed bitmap masks with near-zero forgetting"]

    D --> D1["Inspect pretrained pi0.5 embedding geometry + budgeted simulator feedback"]
    D1 --> D2["Edit 65 token-embedding rows: 74.3%->87.5% on target tokens, 0 regressions on others"]

    C2 & D2 --> E["🏆 Golden Minimal-Intervention Stack: <0.05% Bitmap Masks + 65-Row Surgery (-88.49% TCO)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Full Fine-Tuning (FFT) + Teleop Retraining | Path B: Standard LoRA + External Prompt Rewriters | **Path C (Recommended): `deleting-weights` + `robot-weight-debugging`** |
| :--- | :--- | :--- | :--- |
| **Modified Parameter Footprint** | `100%` of weights (tens of GBs per checkpoint) | `0.1%–2%` float adapter matrices | **`<0.05%` zeroed gate weights (bitmap); `65 rows` in robot embedding** |
| **RL Prior-Task Retention** | Loses up to **`5.4 points`** on prior tasks | Degrades on prior tasks & rank-limited | **Maintains near-base prior-task accuracy while matching FFT** |
| **Robot Policy Bug Repair Speed** | Days of teleop collection & gradient runs | Runtime LLM rewriter adds latency | **Zero gradients, zero new demos; direct 65-row weight edit (`0` runtime lag)** |
| **Untouched-Instruction Safety** | Global gradient drift causes regressions | Rewriter can distort valid prompts | **Zero binary outcome changes across all 430 untouched episodes** |
| **Monthly TCO (24 LLM Variants + 16 Robot Fixes)** | **`$7,950.00 / mo`** (`$3,120` compute + `$4,830` labor) | **`$3,940.00 / mo`** (`$1,420` compute + `$2,520` labor) | **`$915.00 / mo` (Saves `$7,035.00/mo` · `-88.49%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261113-R8-DELETINGWEIGHTS-ROBOTWEIGHT`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: An ML and robotics engineering team shipping **24 domain-specialized post-trained LLM variants per month (GRPO/SFT/SDFT)** and executing **16 robot policy instruction-failure hotfixes per month**.
- **Labor Rate**: Fully loaded ML / robotics research engineering rate of **`$105.00 / hr`**.
- **Explicit Not-Measured Boundary**: Base pretraining cluster capex and physical robot hardware arms are marked **`not_measured`**. This model strictly accounts for post-training/simulation GPU compute, checkpoint storage bills, and engineering hours spent mitigating catastrophic forgetting and repairing policy failures.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Full Fine-Tuning + Teleop Retraining | Path B: LoRA Adapters + Prompt Rewriters | **Path C: `deleting-weights` + `robot-weight-debugging` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly GPU Compute & Checkpoint Storage Spend** | **`$3,120.00`** (full-weight RL/SFT runs + multi-TB checkpoint storage) | **`$1,420.00`** (adapter training & evaluation runs) | **`$390.00`** (`<0.05%` bitmap mask training + budgeted simulator rollouts) |
| **Forgetting Replay, Teleop Collection & Eval Labor (`$105/hr`)** | `46.0 hrs × $105.00` = **`$4,830.00`** | `24.0 hrs × $105.00` = **`$2,520.00`** | `5.0 hrs × $105.00` = **`$525.00`** |
| **Total Monthly TCO** | **`$7,950.00 / mo`** | **`$3,940.00 / mo`** (`-50.44%`) | **`$915.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$4,010.00 / mo` | **Saves `$7,035.00 / mo` (`-88.49%` · `$84,420.00/yr`)** |
| **Pretraining Cluster Capex & Physical Robot Arms** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `deleting-weights` `uv` Environments (`grpo` / `sft` / `sdft`) & Bitmap Mask Check**: Set up `uv venv envs/grpo --python 3.10`, load `Jacklu0831/deletion-tuning-masks`, and verify `<0.05%` gate-projection mask application and prior-task retention.
- [ ] **2. Spectral Geometry & Continual-Learning Audit**: Compare stable rank, spectrum drift, and prior-task accuracy against LoRA and FFT baselines before promoting post-trained masks.
- [ ] **3. `jushengzhang/robot-weight-debugging` 65-Row Edit & 16-Transcript Review**: Inspect `transcripts/pi_lang_c` and `edits/pi05-language-c` following `docs/REPRODUCING.md`, verifying the `86.3% → 92.0%` LIBERO-Plus improvement.
- [ ] **4. Untouched-Token Zero-Regression Verification**: Run held-out episodes that exclude edited tokens (mirroring the 430-episode control split) to confirm zero binary outcome regressions before deployment.
