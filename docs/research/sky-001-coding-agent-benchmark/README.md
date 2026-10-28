# SKY-001 工程世界模型与 Coding Agent 十九模型基准深度评测（永久别名导航页 / Alias Redirect）

> 🌐 **Language / 语言切换**: **[🇨🇳 中文版 (README.md)](README.md)** | **[🇬🇧 English (README.en.md)](README.en.md)** | **[📚 进入完整中文报告 (`../sky-001-and-coding-agent-19-model-benchmark/README.md`)](../sky-001-and-coding-agent-19-model-benchmark/README.md)** | **[📚 Full English Report (`../sky-001-and-coding-agent-19-model-benchmark/README.en.md`)](../sky-001-and-coding-agent-19-model-benchmark/README.en.md)**

> **Executive Summary / 核心结论概览**：
> 本目录为 `sky-001-coding-agent-benchmark` 永久路由别名页，确保引用短路径的外部链接永不 404。完整双轨深度研究与 7-Card 视觉卡片位于 **[`../sky-001-and-coding-agent-19-model-benchmark/README.md`](../sky-001-and-coding-agent-19-model-benchmark/README.md)**：
> 1. **`Claude Haiku 5.5` 改写轻量级 Coding Agent 性价比天花板（总榜 #4，`99.24` 分，`$0.33`）**：在 19 模型 × 11 题（`209` 次 CLI 运行，每模型 `1,310` 项隐藏断言）中，`Haiku 5.5` 以 **`$0.33`（比 `Haiku 4.5` 降本 `91.6%`）** 斩获 **`99.24 / 100`**，仅次于 `Fable 5.1`（`99.77`）、`Opus 5.5`（`99.68`）与 `Opus 5`（`99.59`）。
> 2. **`Gemini 4 Argon` 实现 `1,310 / 1,310`（`100%`）隐藏断言全通（总榜 #10，`98.59` 分，`$2.82`）**：彻底消除前代 `Gemini 3.8 Flash` 的 34 项隐藏测试失败，耗时缩短 `47.1%`。
> 3. **Skyfall AI `SKY-001` 工程世界模型**：通过 `Hierarchical Composer + Construction World Model` 两阶段分层状态规划，在 `Jaguar E-Type`（103 叶节点，树深 $D=5$）上将串行关键路径从 `10,336` 步压缩至 **`105` 步（`98.44x` 加速）**；在 1,000 例 CAD 基准上取得 **`79.7%` IoU、`3.9s/例`、`$0.005/例`**（比 `GPT-6 Astra` **快 `51.0x`、便宜 `150.0x`**）。

![SKY-001 与 19 模型 Coding Agent 基准架构概览](../sky-001-and-coding-agent-19-model-benchmark/assets/overview.svg)

| 评测轨道 / 模型 | 总分 / 核心精度 | 耗时 / 关键路径 | 成本 | 完整交付物直达 |
|---|---|---|---|---|
| **Track A · #1 `Fable 5.1`** | **`99.77 / 100`** (`1,310/1,310`) | `10,031s` (`167.2m`) | `$3.22` | [中文主报告](../sky-001-and-coding-agent-19-model-benchmark/README.md) |
| **Track A · #2 `Claude Opus 5.5`** | **`99.68 / 100`** (`1,310/1,310`) | `4,877s` (`81.3m`) | `$2.69` | [English Report](../sky-001-and-coding-agent-19-model-benchmark/README.en.md) |
| **Track A · #4 `Claude Haiku 5.5`** | **`99.24 / 100`** (`1,308/1,310`) | `3,167s` (`52.8m`) | **`$0.33`** (`-91.6%`) | [7-Card 评测报告 (中文)](../sky-001-and-coding-agent-19-model-benchmark/test-report.md) |
| **Track A · #10 `Gemini 4 Argon`** | **`98.59 / 100`** (`1,310/1,310`) | `2,710s` (`45.2m`) | `$2.82` | [7-Card HTML 视觉卡片](../sky-001-and-coding-agent-19-model-benchmark/test-report-cards.html) |
| **Track B · `SKY-001` (1,000 CAD)** | **`79.7%` IoU** (vs Astra `79.1%`) | **`3.9s/例`** (`51.0x` 加速) | **`$0.005/例`** (`150x` 降本) | [离线验证器 (`simulator/`)](../sky-001-and-coding-agent-19-model-benchmark/simulator/sky001_and_19model_verifier.py) |
