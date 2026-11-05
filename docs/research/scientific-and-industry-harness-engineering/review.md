# 架构师同行评审与事实核查报告 (Peer Review & Fact-Checking Audit)

- **研究主题**：科学发现与行业场景 Harness Engineering 深度研究（基于 Microsoft Discovery 与 CLIO `2508.02789` / `2606.02618v1` 五篇文献）
- **审计状态**：`APPROVED (6/6 单元测试通过 · 4/4 SVG XML 校验通过 · 7-Card 4:5 视觉规范核验通过)`

---

## 1. 原始文献数据与锚点核查表（Quantitative Fact-Check Matrix）

| 核查项 | 文献出处 | 原文精确数值 | 报告与代码核对结果 | 状态 |
| :--- | :--- | :--- | :--- | :---: |
| **HLE Bio/Med 基线与 CLIO 得分** | `arXiv:2508.02789` Table 1 & Fig. 2 | `GPT-4.1`: `8.55% (13/152)`；`o3 (low)`: `11.18% (17/152)`；`o3 (high)`: `13.81% (21/152)`；`GPT-4.1 + CLIO`: `22.37% (34/152)`（注：13 个子表行相加为 `35/152`） | `clio_industry_harness_verifier.py` 同时校验了 `34/152 = 22.37%` 汇总行与 `35/152` 子学科明细和 | ✅ 通过 |
| **CLIO 组件消融收益** | `arXiv:2508.02789` Sec 5.1 | 仅递归认知循环：`+5.92%`（`8.55% -> 14.47%`）；叠加 GraphRAG + DRIFT：`+7.90%`（`14.47% -> 22.37%`），总净增 `+13.82%`（相对 `+161.64%`） | 已精确编码至 `verify_hle_metrics()` 与 Card 3/Card 6 | ✅ 通过 |
| **Discovery 独立验证与 3 次熔断** | MS Learn `concept-tasks-investigations` | 验证进程独立运行（默认 `gpt-5.4`），检查文本与 `.md/.csv/.json/.txt/.py/.yaml`；连续 `>=3` 次相同未解决验证缺口转入 `Needs User Attention` | 已在 `simulate_discovery_validator_gate()` 中完成确定性状态机验证 | ✅ 通过 |
| **ALE 三大科学领域 Pass@1** | TechCommunity Blog (4552705) | 152 公开任务（13 领域，5h 限时）：物理科学 `75.2%`（vs Opus 5 `66.6%` [`+8.6%`], vs Codex `56.9%` [`+18.3%`]）；健康医学 `61.6%`（vs `57.2%` [`+4.4%`]）；生命科学 `64.6%`（vs `60.8%` [`+3.8%`]） | 已精确编码至 `ALE_SCORES` 与 `evidence/ale_benchmark_scores.csv` | ✅ 通过 |
| **AORFB 校准遵从与重设计闭环** | `arXiv:2606.02618v1` Table 1, Table 2, Sec 3.2 | 母体 (2) 预测 `-1.998 V` vs `+0.7 V` 锚点（`~2.7 V` 偏差）；Cmpd 1 `-0.762 V`, `|i_ox/i_red|=0.52`；Cmpd 3 `-0.895 V` (`+133 mV`), `57.9 mM`, `|i_ox/i_red|=0.18`（双峰）；Cmpd 20 `-0.854 V` (`+92 mV`), `56.0 mM`, `|i_ox/i_red|=0.38` | 已在 `verify_aorfb_closed_loop()` 与 Card 2 中完整呈现 | ✅ 通过 |
| **ExLLM 黑盒 vs 灰盒与 pH 14 陷阱** | `arXiv:2606.02618v1` Tables S4 & S5 | 500 evals ($n=6$)：CLIO 灰盒 Top-1 `+10.1%` (`0.544->0.599`)、Mean Top-10 `+14.7%` (`0.504->0.578` vs ExLLM `0.543`)；2,500 evals 湿实验 ExLLM `S1,S2,S3 < 1 mM`（胺基去质子化沉淀） | 已在 `verify_pmo_greybox_gain()` 与 Card 5 中完整验证 | ✅ 通过 |
| **RetroChimera 逆合成漏检教训** | `arXiv:2606.02618v1` Sec S2.4 | 将苯并[c]噌啉偷换为 2-(溴甲基)喹啉，虚报 2 步合成（实际 5 步） | 已作为结构不变量硬门控（Structural Invariant Gate）的反面教材写入 Card 3 与设计要点 2 | ✅ 通过 |

---

## 2. 行业架构设计深度评估（Rubber-Duck Architectural Review）

1. **避免“重概念、轻机制”**：本研究不仅总结了宏观理念，还将 CLIO 的 Algorithm 1/2、方程 S1–S5 多目标门控函数 $J(m)$、不确定性梯度 $\partial U/\partial t$ 震荡判据、以及 Discovery 的 3-Strike 验证状态机全部落实为可执行的 Python 代码与单元测试。
2. **客观呈现正反两面证据**：既展示了 CLIO 在灰盒优化（`+14.7%` Mean Top-10）和湿实验 `pH 14` 跨工况推理上的巨大优势，也如实呈现了其在纯黑盒数值爬山时略逊于 `ExLLM`（`0.544` vs `0.586`）以及在 `RetroChimera` 喹啉母核偷换上的审查盲区，从而推导出“认知校准遵从 + 确定性结构验证器”的混合行业 Harness 架构。
