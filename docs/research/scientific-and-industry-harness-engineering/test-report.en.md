# Scientific Discovery & Industry Scenario Harness Engineering Benchmark Report (7-Card 4:5 Companion)

> **Provenance**: `anonymized_reported` (`independently_reproduced = false`; all evaluation metrics are extracted directly from `arXiv:2508.02789`, the Microsoft TechCommunity ALE report, and `arXiv:2606.02618v1` main text & Supplementary S1–S6, and verified 100% by `simulator/clio_industry_harness_verifier.py`).
> **Visual Card Deck**: [English 7-Card 4:5 (`cards.html`)](./cards.html) | [中文 7-Card 4:5 (`cards.zh.html`)](./cards.zh.html) | [中文评测报告 (`test-report.md`)](./test-report.md)

---

## Card 1 (`1 / 7` · `HANDS-ON · SCIENTIFIC & INDUSTRY HARNESS`) — Overview & Workbench

**Headline Finding**: **CLIO & Calibrated Deference Push Physical Sciences Agent Accuracy to 75.2% and Close a `+90 mV` Reversible Battery Design Loop**

- **Three Sealed Evaluation Pillars**:
  1. **HLE Biology & Medicine ($n=152$, No External Tools, Pass@1)**: `GPT-4.1 + CLIO` reaches **`22.37% (34/152)`**, achieving a **`+13.82%` net (`+161.64%` relative)** gain over base `GPT-4.1` (`8.55%`) and beating `o3 (high)` (`13.81%`) by **`+61.98%` relative**.
  2. **Agent's Last Exam (ALE, 152 Public Tasks Across 13 Domains, 5-Hour Limit, Pass@1)**: Microsoft Discovery (GitHub Copilot base harness + CLIO mode + dynamic multi-model switching) achieves **`75.2%` in Physical Sciences**, outperforming Claude Code `Opus 5` (`66.6%`) by **`+8.6%`** and single-model Codex `GPT-5.6 Sol` (`56.9%`) by **`+18.3%`**.
  3. **AORFB Wet-Lab Closed-Loop Campaign (`arXiv:2606.02618v1`)**: Across 17 tested molecules and 3 rounds, CLIO detected a **`~2.7 V`** predictor offset, discovered **Compound 3 (`-0.895 V vs SHE`, `+133 mV`)**, diagnosed `pH 14` phosphonate–$\text{K}^+$ ion pairing causing a split oxidation wave ($|i_{\text{ox}}/i_{\text{red}}|=0.18$), and redesigned **Compound 20 (`-0.854 V`, `+92 mV`)**, doubling $|i_{\text{ox}}/i_{\text{red}}|$ to **`0.38`**.

---

## Card 2 (`2 / 7` · `SCENARIO: AORFB NEGOLYTE CLOSED-LOOP`) — Single-Case Deep Dive

**Headline Finding**: **Graded Distrust of a `2.7 V` Miscalibrated Predictor + 3 Consensus Experiments Doubled Redox Reversibility ($|i_{\text{ox}}/i_{\text{red}}|$ `0.18 -> 0.38`)**

| Decision Node | Task Type | Confidence / Support | Action Pill | Quantitative & Mechanistic Outcome |
| :--- | :---: | :---: | :---: | :--- |
| **1. Graphormer $E_{\text{red}}$ Calibration Audit** | `score` | `0.86` | `Confirm` (Downgrade to Soft Rank) | Parent (2) predicted at `-1.998 V` vs `+0.7 V` prompt note (**`2.698 V` offset**); verified substituent shifts (`+0.133 V`, `+0.258 V`) preserved rank order and **excluded $E_{\text{red}}$ from Round 3 hard gate**. |
| **2. Compound 3 Split-Wave Diagnosis** | `choice` | `0.94` (3/3 Consensus $\star$) | `Act automatically` (Run 3 Starred Tests) | Scan-rate (`10–500 mV/s`) & $[\text{OH}^-]$ (`0.1–1 M`) series refuted tautomerization & $\text{OH}^-$ attack; $\text{Li}^+/\text{Na}^+/\text{K}^+$ swap confirmed **dianionic phosphonate–cation pairing**. |
| **3. Compound 20 Sulfonate Redesign** | `noul` | `0.91` | `Act automatically` (Synthesize & Test) | Replaced dianionic phosphonate with monoanionic benzylsulfonate: measured $E_{\text{red}} = -0.854\text{ V}$ (**`+92 mV` gain**), `56.0 mM` KOH solubility, and $|i_{\text{ox}}/i_{\text{red}}| = \mathbf{0.38}$ (**`2.11x`**). |

---

## Card 3 (`3 / 7` · `WHAT I TESTED`) — Full Evaluation Matrix

**Headline Finding**: **6 Evaluation Suites Spanning 304 Benchmark Tasks and 20 Wet-Lab Molecules Expose 2 Critical Unchecked Boundaries (`✕`)**

| SCENARIO | QUESTION / TASK | MODEL ANSWER | ACTION |
| :--- | :--- | :--- | :--- |
| **1. HLE Bio/Med ($n=152$)** | Expert biology & medicine QA without external tools | **`22.37% (34/152)`** vs `o3 (high)` `13.81%` (`+61.98%` rel) | `Act automatically` |
| **2. ALE Physical Sciences** | 5-hour autonomous scientific computing & derivation | **`75.2%`** vs Opus 5 `66.6%` (`+8.6%`) / Codex `56.9%` (`+18.3%`) | `Act automatically` |
| **3. ALE Life & Health Sci** | 5-hour Life Sciences (`64.6%`) & Health/Medicine (`61.6%`) | Beats single-model Codex harness by **`+3.8%`** and **`+4.4%`** | `Act automatically` |
| **4. AORFB Multi-Objective Gate** | Salvage `2.7 V` offset predictor & design `pH 14` soluble negolyte | Discovered Cmpd 3 (`-0.895 V`, `57.9 mM`) & Cmpd 20 (`-0.854 V`, `56.0 mM`) | `Confirm` |
| **5. ExLLM 2,500-Eval Wet-Lab** | Evolutionary optimization of neutral-pH $\log S$ oracle (`S1–S3`) | **✕ Wet-lab failure (`< 1 mM`)**: Amine groups deprotonated at `pH 14` (`1 M KOH`) | `Send to a human` |
| **6. RetroChimera Route Audit** | Verify starting material core fidelity on Compound 3 | **✕ Missed core swap**: Tool substituted quinoline for benzo[c]cinnoline (2 vs 5 steps) | `Send to a human` |

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`) — Protocol & Scoring Mechanics

**Headline Finding**: **Equations S1–S5 Multi-Objective Gating $J(m)$, Uncertainty Gradient $\partial U/\partial t$, and 3-Strike Separated Validator Protocol**

- **Top Block (Input & Objective Protocol)**: Encodes `arXiv:2606.02618v1` Equations S1–S5 combining normalized scores ($s_{E_{\text{red}}}, s_{\log S}, s_{\text{SA}}, s_{\text{steps}}$) with multiplicative hard gates $\prod \mathbb{I}[\text{gate}_i(m)] \cdot \mathbb{I}[\text{core}(m)]$, plus Calibrated Deference gate relaxation when anchor error $|\Delta E_{\text{anchor}}| > 0.5\text{ V}$.
- **Bottom Block (Deterministic Verifier & Circuit Breaker)**: Encodes CLIO Algorithm 1 dynamic registration of `Completion` $T(s)=0$, real-time $\partial U/\partial t < 0$ vs oscillation detection $\Omega(U) \ge 3$, and Microsoft Discovery's separated `gpt-5.4` validator escalating to `Needs User Attention` after 3 identical `gap_fingerprints`.

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`) — Black-Box vs. Grey-Box & Wet-Lab Perturbation

**Headline Finding**: **Grey-Box Domain Semantics Boosted CLIO Mean Top-10 by `+14.7%` (`+7.4 pts`) and Prevented `pH 14` Electrolyte Precipitation (`57.9 mM` vs `< 1 mM`)**

| QUESTION / ANSWER | ORIGINAL (BLACK-BOX) | PERTURBED (GREY-BOX / WET-LAB) | CHANGE (PTS / %) |
| :--- | :---: | :---: | :---: |
| **1. CLIO PMO Top-1 Score (500 evals, $n=6$)** | `0.544 ± 0.065` | **`0.599 ± 0.095`** | **`+5.5 pts (+10.1%)`** |
| **2. CLIO (Efficiency) Top-1 Score ($n=6$)** | `0.541 ± 0.062` | **`0.602 ± 0.066`** | **`+6.1 pts (+11.3%)`** |
| **3. CLIO PMO Mean Top-10 Score ($n=6$)** | `0.504 ± 0.059` | **`0.578 ± 0.103`** (Beats ExLLM `0.543`) | **`+7.4 pts (+14.7%)`** |
| **4. ExLLM PMO Mean Top-10 Score ($n=6$)** | `0.525 ± 0.011` | `0.543 ± 0.008` | `+1.8 pts (+3.4%)` |
| **5. Wet-Lab Solubility in `1 M KOH (pH 14)`** | `ExLLM S1/S2/S3`: **`< 1.0 mM`** | `CLIO Cmpd 3 / 20`: **`57.9 / 56.0 mM`** | **`+56.9 mM (>50x)`** |

---

## Card 6 (`6 / 7` · `LATENCY & SCALING`) — Test-Time Scaling & ACT Tradeoff

**Headline Finding**: **Recursive Cognition (`+5.92%`) + GraphRAG/DRIFT Reduction (`+7.90%`) Deliver a `2.62x` Accuracy Gain and Dominate 5-Hour ALE Horizons**

- **HLE Bio/Med Ablation Scaling**: Base `GPT-4.1` (`8.55%`) $\rightarrow$ `+ CLIO Recursive Loop` (`14.47%`) $\rightarrow$ `+ GraphRAG & DRIFT` (**`22.37%`**) vs `o3 (low)` (`11.18%`) and `o3 (high)` (`13.81%`).
- **ALE 5-Hour Horizon Scaling**: Physical Sciences **`75.2%`** (vs `66.6%` Opus 5, `56.9%` Codex); Life Sciences **`64.6%`** (vs `60.8%`); Health & Medicine **`61.6%`** (vs `57.2%`).
- **Rate-Limit Micro-Batching**: Autonomous downshift from `40–60` library enumeration to **`6`-candidate micro-batches** eliminates rate-limit timeouts during Round 3 generation.

---

## Card 7 (`7 / 7` · `MY TAKE`) — Good Fit vs. Not For & Engineering Readiness

**Headline Finding**: **Enterprise Harnesses Must Evolve from "Blind Tool Pipelines" to "Calibrated Deference + Separated Validation + Structural Oracles"**

- **✅ Good Fit**:
  1. **Out-of-Distribution R&D & Engineering with Imperfect Oracles**: Molecular/materials discovery, semiconductor fab yield RCA, and macro-regime financial risk modeling.
  2. **Tri-Tier Grey-Box Optimization**: Problems combining numerical predictors, process step limits, and natural-language physical/operational constraints (`pH 14`, chamber chemistry, regulatory clauses).
  3. **Multi-Hour / Multi-Week Human-AI Investigations**: Asynchronous Shared Session DAGs requiring warm-start belief graphs, Regret Reflection, and mid-stream human belief editing.
- **⛔ Not For**:
  1. **Sub-100ms Real-Time Microservices**: CLIO's multi-channel exploration and GraphRAG clustering trade compute time for high-stakes accuracy (ACT framing).
  2. **Tool Invocation Without Deterministic Structural Guards**: As shown by `RetroChimera`'s quinoline core swap, cognitive agents must be paired with deterministic SMARTS/AST structural validators.
  3. **Purely Opaque `[0,1]` Black-Box Functions with Zero Domain Semantics**: Simple evolutionary mutation (`ExLLM`) is more sample-efficient when no domain physics or grey-box thresholds exist.
