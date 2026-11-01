# Gemini 4 Carbon 网安/长程智能体与 Coding Agent 二十模型基准深度评测（永久别名导航页 / Alias Redirect）

> 🌐 **Language / 语言切换**: **[🇨🇳 中文版 (README.md)](README.md)** | **[🇬🇧 English (README.en.md)](README.en.md)** | **[📚 进入完整中文报告 (`../gemini-4-carbon-and-20-model-benchmark/README.md`)](../gemini-4-carbon-and-20-model-benchmark/README.md)** | **[📚 Full English Report (`../gemini-4-carbon-and-20-model-benchmark/README.en.md`)](../gemini-4-carbon-and-20-model-benchmark/README.en.md)**

> **Executive Summary / 核心结论概览**：
> 本目录为 `gemini-4-carbon-benchmark` 永久路由别名页，确保引用短路径的外部链接永不 404。完整增补报告 6（20 模型全景与网安防御闭环评测）与 7-Card 4:5 视觉卡片位于 **[`../gemini-4-carbon-and-20-model-benchmark/README.md`](../gemini-4-carbon-and-20-model-benchmark/README.md)**：
> 1. **同价位代际跃迁（`$2.00/M` 输入 · `$10.00/M` 输出 · `95%` 缓存读取折扣即 `$0.10/M`）**：Google DeepMind 于 `2026-10-28` 发布 `Gemini 4 Carbon`，在保持与 `Gemini 4 Argon` 完全相同 Token 定价下，于 **17 项官方编码、长程、百万上下文、数理科学及网络安全基准中斩获 `15 项全场第一（#1）`**（`AA Index v5.0` `59`、`SWE-sweep` `9.6%` [`2.23x` Argon]、`Terminal-Bench 4.0` `65.2%`、`Agents' Last Exam v1.1` `77.4%`、`Vending-Bench 2` `$16,484`、`GraphWalks` `96.2%`、`Terminal-Bench-Science 0.1` `64.8%`）。
> 2. **网安防御全生命周期大满贯**：在 `SEC-bench Pro`（183 个真实 JS 引擎安全任务，Pass@1 **`88.2%` #1**）、`ExploitGym`（10h **`54.8%` #1** / 6h **`53.5%` #2**，超越不限时 `GPT-6 Astra` `42.4%`）与 `CWE-bench`（Collinear Pass@1 **`71.0%` #1**）全部夺冠；Chrome 补丁质量较竞品前沿模型提升 **`>10x`**，安全代码生成率较 Argon 提升 **`>2x`**。
> 3. **对抗鲁棒性与反作弊对齐**：在 `Gray Swan IPI`（`k=15` 次尝试）间接提示注入测试中实现 **`0.0%` 攻击成功率（#1 / 13 模型）**；`Terminal-Bench 4.0` 成功作弊率 **`0.0%`**（尝试率 `0.4%`）；高危编码失调告警下降 **`80%`**，无根据宣称减少 **`50%`**。
> 4. **二十模型 Coding Agent 矩阵（Track A）**：完整保留 19 个公开 Copilot CLI 模型（`209` runs、`1,310` 隐藏断言/模型、`0` 漂移），并将处于 **Fairwind Program** 预览阶段的 `Gemini 4 Carbon` 列为第 20 模型。

![Gemini 4 Carbon 与二十模型基准架构总览](../gemini-4-carbon-and-20-model-benchmark/assets/overview.svg)

| 评测轨道 / 模型 | 总分 / 核心精度 | 隐藏测试 / 安全指标 | 定价 / 成本 | 完整交付物直达 |
|---|---|---|---|---|
| **Track B/C · `Gemini 4 Carbon` (#20)** | **`15 / 17` 项官方 `#1`** | **`SEC-Pro 88.2%` · `IPI 0.0% ASR`** | **`$2 / $10 / $0.10` 缓存** | [中文主报告](../gemini-4-carbon-and-20-model-benchmark/README.md) |
| **Track A · #1 `Claude Fable 5.1`** | **`99.77 / 100`** | `1,310 / 1,310` (`100%`) | `$14.45` (`55.9m`) | [English Report](../gemini-4-carbon-and-20-model-benchmark/README.en.md) |
| **Track A · #4 `Claude Haiku 5.5`** | **`99.24 / 100`** | `1,308 / 1,310` (`99.85%`) | **`$0.33`** (`35.1m`) | [7-Card 评测报告 (中文)](../gemini-4-carbon-and-20-model-benchmark/test-report.md) |
| **Track A · #6 `Claude Sonnet 5.5`** | **`99.00 / 100`** | `1,310 / 1,310` (`100%`) | `$2.89` (**`21.7m` 最快**) | [7-Card 评测报告 (English)](../gemini-4-carbon-and-20-model-benchmark/test-report.en.md) |
| **Track A · #11 `Gemini 4 Argon`** | **`98.59 / 100`** | **`1,310 / 1,310` (`100%`)** | **`$2.82`** (`$0/M` 缓存写入) | [7-Card HTML 视觉卡片](../gemini-4-carbon-and-20-model-benchmark/test-report-cards.html) |

## 快速直达链接

- 📄 **完整中文研究报告**：[`../gemini-4-carbon-and-20-model-benchmark/README.md`](../gemini-4-carbon-and-20-model-benchmark/README.md)
- 📄 **Full English Research Report**: [`../gemini-4-carbon-and-20-model-benchmark/README.en.md`](../gemini-4-carbon-and-20-model-benchmark/README.en.md)
- 🃏 **7-Card 4:5 视觉报告（Markdown / HTML）**：[`test-report.md`](../gemini-4-carbon-and-20-model-benchmark/test-report.md) · [`test-report.en.md`](../gemini-4-carbon-and-20-model-benchmark/test-report.en.md) · [`test-report-cards.html`](../gemini-4-carbon-and-20-model-benchmark/test-report-cards.html)
- 🔬 **结构化数据与离线验证器**：[`report.json`](../gemini-4-carbon-and-20-model-benchmark/report.json) · [`evidence.json`](../gemini-4-carbon-and-20-model-benchmark/evidence.json) · [`gemini4_carbon_20model_verifier.py`](../gemini-4-carbon-and-20-model-benchmark/simulator/gemini4_carbon_20model_verifier.py)
