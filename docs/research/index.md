# AI 研究索引

本索引只列实际公开专题，不代表所有分类已有成果。公开内容与未公开材料分离，不引入后者的链接、原始记录或历史。

## Agent

| 专题 | 子分类 / 标签 | 范围与状态 |
|---|---|---|
| [Omarchy agent 设计机制](omarchy-agent-design/README.md) | Agentic OS 与本地 Harness 集成（`Agentic OS`、`Harness Integration`、`Skills`、`Event-driven Agent`、`Identity & Usage`） | 基于 `omacom/omarchy@9480d1b6a98156314dbabe6bfef08f39f8b9cd07` 的 6 大机制专题（E1–E6）、174 条源码/文档/测试契约断言与 [7 页 4:5 视觉卡片测试报告](omarchy-agent-design/test-report.md)；离线静态契约已核验，上游运行 `not_run` |
| [Personal agents：五产品比较](personal-agents/README.md) | 消费级与工作流 Personal Agents | Meta Muse、Grok Bot、OpenAI dot/dots、Google Gemini Spark、Instinct；企业 Gemini 单列区别。cutoff 2026-10-11，静态公开资料研究 |

### Omarchy agent 设计机制专题材料

- **核心阅读**：[专题总入口](omarchy-agent-design/README.md) · [00 中文总览](omarchy-agent-design/findings/00-summary.md) · [01 Launcher](omarchy-agent-design/findings/01-launcher.md) · [02 Skills](omarchy-agent-design/findings/02-skills.md) · [03 Crash Pipeline](omarchy-agent-design/findings/03-crash-pipeline.md) · [04 Accounts & Usage](omarchy-agent-design/findings/04-accounts-usage.md) · [05 Agent-native Repo](omarchy-agent-design/findings/05-agent-native-repo.md) · [06 Safety Model](omarchy-agent-design/findings/06-safety-model.md)
- **7 页 4:5 视觉卡片测试报告**：[测试报告正文](omarchy-agent-design/test-report.md) · [可离线预览 7 页卡片 HTML](omarchy-agent-design/test-report-cards.html) · [测试报告 JSON](omarchy-agent-design/evidence/test-report.json) · [12 项契约矩阵 CSV](omarchy-agent-design/evidence/test-scenarios.csv) · [鲁棒性 CSV](omarchy-agent-design/evidence/test-robustness.csv) · [批量核验耗时 CSV](omarchy-agent-design/evidence/test-batch-latency.csv)
- **可复核证据**：[源码证据索引](omarchy-agent-design/evidence/source-index.md) · [174 条断言索引 CSV](omarchy-agent-design/evidence/assertion-index.csv) · [证据台账 JSON](omarchy-agent-design/evidence.json) · [归档检查与边界](omarchy-agent-design/review.md)

### Personal agents 专题材料

[31 条来源证据](personal-agents/evidence.json) · [未执行的 benchmark 协议](personal-agents/benchmark.md) · [18 个原创合成案例](personal-agents/cases.json) · [独立 AI 审阅与公开边界](personal-agents/review.md)。

公开评测是第三方报告，未在此重算；模型/framework 分数不代表消费产品表现。协议和案例均为 `not_executed`。

## Model

预留分类，暂无公开专题；不声称已有模型实验或评测结果。

## Infra

| 专题 | 子分类 / 标签 | 范围与状态 |
|---|---|---|
| [阿里云 AI Infra 全栈架构深度测评](alibaba-cloud-ai-infra/README.md) | 云原生 AI 算存网底座与训推平台（`T-Head PPU/CPU`、`Zhenwu M890/V900`、`HPN 7.0`、`Solar-RDMA`、`PAI-Lingjun`、`PAI`、`Bailian`） | 覆盖平头哥真武 PPU（810E/M890/V900/J900）、倚天 CPU、ICN Switch 1.0、磐脉 920、镇岳 510、磐久 AL128、HPN 7.0 + Solar-RDMA、灵骏、PAI 与百炼平台的 L0–L3 架构师视角深度测评与选型决策矩阵；cutoff 2026-10-14，静态公开资料研究（`not_executed_by_design`） |

### 阿里云 AI Infra 全栈架构深度测评专题材料

- **核心阅读**：[深度测评报告正文](alibaba-cloud-ai-infra/README.md) · [21 条一手来源证据台账 JSON](alibaba-cloud-ai-infra/evidence.json) · [技术审校与证据边界记录](alibaba-cloud-ai-infra/review.md)

[返回首页](../../README.md) · [归属与权利边界](../../ATTRIBUTION.md) · [第三方声明](../../THIRD_PARTY_NOTICES.md)
