# Omarchy Agent 设计机制与桌面 Harness 集成架构研究

> 🌐 **Language / 语言切换**: **[🇨🇳 中文版 (README.md)](./README.md)** | **[🇬🇧 English (README.en.md)](./README.en.md)** · **[📊 7-Card 4:5 评测报告](test-report.md)** | **[🃏 离线 7 卡 HTML](test-report-cards.html)**

**架构师核心结论：Omarchy 的工程价值在于把第三方 Coding Agent 统一接入操作系统级启动器、渐进式技能目录、系统崩溃事件流、多账号配额与观测面板，而非重复造轮子实现底层模型循环。** 本研究基于上游规范仓库 `omacom/omarchy` 固定 commit [`9480d1b6a98156314dbabe6bfef08f39f8b9cd07`](https://github.com/omacom/omarchy/commit/9480d1b6a98156314dbabe6bfef08f39f8b9cd07) 执行 174 条静态源码契约核验。

**架构域归属**：`Agent Harness Engineering` → `Agentic OS` · `Multi-Harness Launcher` · `Progressive Skills` · `Event-Driven Diagnostics` · `Quota & Account Governance`。

## 阅读入口

| 文档 | 重点 |
|---|---|
| [00 总览](findings/00-summary.md) | agentic OS定义、架构图、八种模式、七项企业设计、六维轻量平台比较 |
| [01 Launcher](findings/01-launcher.md) | 全14分支、lazy install、默认选择、prompt/env、OpenClaw lifecycle |
| [02 Skills](findings/02-skills.md) | 三部署skill、开发指南分离、六根目录/profiles、渐进上下文与更新 |
| [03 Crash Pipeline](findings/03-crash-pipeline.md) | journal过滤→通知→用户点击→prompt；mute/去重与时序图 |
| [04 Accounts / Usage](findings/04-accounts-usage.md) | provider集合、home/pin、四collector真实函数、cache/failure/切换与Panel契约 |
| [05 Agent-native Repo](findings/05-agent-native-repo.md) | 指令分层、headless/acceptance、plans与历史统计边界 |
| [06 Safety Model](findings/06-safety-model.md) | argv/prompt/credentials/system边界，不是漏洞审计或安全认证 |
| [测试报告（7 页 4:5 视觉卡片版）](test-report.md) | 基于 `benchmark-harness-engineering` 7 页 4:5 视觉版面的 12 项机制契约评测、模式扰动鲁棒性与批量核验耗时 |
| [7 页视觉卡片 HTML（离线自包含）](test-report-cards.html) | CSP 锁定（`default-src 'none'; style-src 'unsafe-inline'`）的可直接预览 4:5 视觉报告卡片组 |

## 可复核材料

[来源索引](evidence/source-index.md) · [逐结论CSV](evidence/assertion-index.csv) · [机器可读证据台账](evidence.json) · [测试报告JSON](evidence/test-report.json) · [12项评测矩阵CSV](evidence/test-scenarios.csv) · [鲁棒性CSV](evidence/test-robustness.csv) · [批量耗时CSV](evidence/test-batch-latency.csv) · [归档检查/待独立复核](review.md)。

| 专题证据 | 内容 |
|---|---|
| [E1 启动矩阵](evidence/e1-launch-matrix.md) | 14 harness无/有prompt argv及env/terminal差异 |
| [E2 Skill Map](evidence/e2-skill-map.md) | 全部SKILL与同目录参考文件、迁移、discovery界限 |
| [E3 Prompt Contract](evidence/e3-prompt-contract.md) | 源码模板字段与argv→prompt边界；不是运行日志 |
| [E4 State Contracts](evidence/e4-state-contracts.md) | registry、collector函数、freshness、JSON→Panel与autoswitch |
| [E5 Methodology](evidence/e5-methodology.md) | 方法、历史分母规则与未采集边界 |
| [Blockers / 缺口](evidence/blockers.md) | 已完成静态研究与尚无运行/版本/全历史证据的区别 |

## 证据标签与边界

**源码事实**是固定bytes中的实现；**文档声明**是上游skill/guide/manual/官网自述；**测试契约（未运行）**只说明断言意图；**分析推断**明确从这些材料综合；**待实验验证**不是成功或零结果。没有完整历史分母、没有真实usage/账单/权限数据，也没有把附件无证据的VM结论作为本研究结果。

本专题发布原创中文机制分析、可复核源码证据索引及 7 页 4:5 视觉卡片契约评测报告；归档不升级为独立人工复核或上游运行验证。根研究索引见[AI 研究索引](../index.md)；源作者与转载边界见[归属与权利边界](../../../ATTRIBUTION.md)及[第三方声明](../../../THIRD_PARTY_NOTICES.md)。
