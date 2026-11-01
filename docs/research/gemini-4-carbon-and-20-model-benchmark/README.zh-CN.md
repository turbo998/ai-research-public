# Gemini 4 Carbon 网安/长程智能体与 Coding Agent 二十模型基准深度评测（增补报告 6 · 简体中文归档索引）

> **主报告（简体中文）**: [`README.md`](./README.md) · **English Version**: [`README.en.md`](./README.en.md)
> **7-Card 4:5 视觉评测报告**: [`test-report.md`](./test-report.md)（中文） · [`test-report.en.md`](./test-report.en.md)（English） · [`test-report-cards.html`](./test-report-cards.html)（CSP 自包含交互式卡片）
> **机器可读契约与证据锁**: [`report.json`](./report.json) · [`evidence.json`](./evidence.json) · [`evidence/verifier-summary.json`](./evidence/verifier-summary.json) · [`review.md`](./review.md)

本文件为 [`README.md`](./README.md) 的显式 `zh-CN` 语言入口，方便双语自动化与跨仓索引调用。核心结论速览：

1. **同价位代际跃迁（`$2.00/M` 输入 · `$10.00/M` 输出 · `95%` 缓存读取折扣即 `$0.10/M`）**：Google DeepMind 于 `2026-10-28` 发布 `Gemini 4 Carbon`，在与 `Gemini 4 Argon` 完全相同的 Token 定价下，于 **17 项官方编码、长程、百万上下文、数理科学及网安基准中斩获 `15 项第一（#1）`**（`AA Index v5.0` `59`、`SWE-sweep` `9.6%` [Argon 的 `2.23x`]、`Terminal-Bench 4.0` `65.2%`、`Agents' Last Exam v1.1` `77.4%`、`Vending-Bench 2` `$16,484`、`GraphWalks` `96.2%`、`Terminal-Bench-Science 0.1` `64.8%`）。
2. **网安防御全生命周期领跑**：`SEC-bench Pro` **`88.2%` (#1)**、`ExploitGym` **`54.8%` (10h #1) / `53.5%` (6h #2，超越不限时 GPT-6 Astra 的 `42.4%`)**、`CWE-bench` **`71.0%` (#1)**；Chrome 真实漏洞补丁质量较竞品前沿模型提升 **`>10x`**，安全代码生成率较 Argon 提升 **`>2x`**。
3. **对抗鲁棒性与反作弊对齐**：`Gray Swan IPI`（`k=15` 次尝试）间接提示注入攻击成功率 **`0.0%` (#1 / 13 模型)**；`Terminal-Bench 4.0` 成功作弊率 **`0.0%`**（尝试率 `0.4%`）；高严重度编码失调告警较 Argon 降低 **`80%`**，无根据宣称减少 **`50%`**。
4. **二十模型 Coding Agent 矩阵（Track A）**：完整保留 19 个公开 Copilot CLI 模型（`209` runs、`1,310` 隐藏测试/模型、`0` 漂移），并将处于 **Fairwind Program** 预览阶段的 `Gemini 4 Carbon` 列为第 20 模型。请直接参阅 [`README.md`](./README.md) 获取完整数据表。
