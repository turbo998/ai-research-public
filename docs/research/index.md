# AI 研究索引 (Bilingual Research Index)

> 🌐 **Language / 语言版本**: **[📘 Azure Agent Infra Playbook (中文)](azure-agent-infra/README.zh-CN.md)** | **[📘 Azure Agent Infra Playbook (English)](azure-agent-infra/README.en.md)** | **[📊 7-Card Report (中文)](azure-agent-infra/test-report.md)** | **[📊 7-Card Report (English)](azure-agent-infra/test-report.en.md)**

本索引只列实际公开专题，不代表所有分类已有成果。公开内容与未公开材料分离，不引入后者的链接、原始记录或历史。

## Agent

| 专题 | 子分类 / 标签 | 范围与状态 |
|---|---|---|
| [AI Agent Infrastructure on Azure 全栈方案设计与选型 Playbook (中文)](azure-agent-infra/README.md) · [English](azure-agent-infra/README.en.md) | Agent Runtime、MicroVM 沙箱、状态持久化与多租户治理（`Foundry`、`ACA Sandboxes`、`AKSClaw`、`E2B Firecracker`、`HorizonDB`、`Entra Agent ID`） | 覆盖四层参考架构、六大运行时光谱（含 `Standard_D96as_v7` `108ms/132ms` 实测锚点）、10万并发沙箱 VMSS 容量模型、80 章行业物理模型、75 套 IaC 蓝图、74 项仿真器（83/83 单测全绿）、8 幅 SVG 架构图、[7 页 4:5 视觉卡片报告 (中文)](azure-agent-infra/test-report.md) / [English](azure-agent-infra/test-report.en.md) 与 [交互式双语 H5 仿真套件](azure-agent-infra/h5/index.html) |
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
| [AI Agent Infrastructure on Azure 全栈方案设计与架构选型 Playbook (中文)](azure-agent-infra/README.md) · [English](azure-agent-infra/README.en.md) | 云原生 Agent 基础设施、硬件虚拟化沙箱与状态数据库（`ACA Dynamic Sessions`、`ACA Sandboxes`、`AKS Kata / AKSClaw`、`E2B on VMSS D96as_v7`、`Azure HorizonDB`、`APIM AI Gateway`） | 85 章全栈架构与行业物理模型深度研究、8 幅自包含 SVG 架构与工作流图、80 套生产级 IaC 蓝图、79 项确定性仿真器（88/88 单测通过）、[7 页 4:5 视觉卡片报告 (中文)](azure-agent-infra/test-report.md) / [English](azure-agent-infra/test-report.en.md) 与 [4 页交互式双语 H5 套件](azure-agent-infra/h5/index.html) |

### Azure AI Agent Infrastructure 专题材料（中英双语 / Bilingual）

- **核心阅读与蓝图**：[中文 Playbook (`README.zh-CN.md`)](azure-agent-infra/README.zh-CN.md) · [English Playbook (`README.en.md`)](azure-agent-infra/README.en.md) · [AKSClaw 多租户 K8s 清单 (`aksclaw-kata-fleet.yaml`)](azure-agent-infra/blueprints/aksclaw-kata-fleet.yaml) · [APIM 10万动态域名限流策略 (`e2b-apim-per-host-policy.xml`)](azure-agent-infra/blueprints/e2b-apim-per-host-policy.xml) · [E2B VMSS D96as_v7 Bicep 模板 (`e2b-vmss-d96as-v7.bicep`)](azure-agent-infra/blueprints/e2b-vmss-d96as-v7.bicep) · [HorizonDB + PgBouncer 检查点参考实现 (`horizondb-langgraph-checkpointer.py`)](azure-agent-infra/blueprints/horizondb-langgraph-checkpointer.py)
- **7 页 4:5 视觉卡片测试报告**：[中文报告 (`test-report.md`)](azure-agent-infra/test-report.md) · [English Report (`test-report.en.md`)](azure-agent-infra/test-report.en.md) · [可离线预览 7 页卡片 HTML (`test-report-cards.html`)](azure-agent-infra/test-report-cards.html) · [密封评测数据 (`report.json`)](azure-agent-infra/report.json) · [12 项场景矩阵 CSV (`test-scenarios.csv`)](azure-agent-infra/evidence/test-scenarios.csv) · [顺序与规模扰动鲁棒性 CSV (`test-robustness.csv`)](azure-agent-infra/evidence/test-robustness.csv) · [VM 代际与预热池恢复延迟 CSV (`test-batch-latency.csv`)](azure-agent-infra/evidence/test-batch-latency.csv)
- **交互式双语 H5 与可运行仿真**：[H5 全景手册 (`h5/index.html`)](azure-agent-infra/h5/index.html) · [AKSClaw × E2B 实时仿真台 (`h5/demo.html`)](azure-agent-infra/h5/demo.html) · [选型决策与 10万沙箱计算器 (`h5/selector.html`)](azure-agent-infra/h5/selector.html) · [可运行全链路仿真脚本 (`demo/run_live_demo.py`)](azure-agent-infra/demo/run_live_demo.py) · [证据台账 (`evidence.json`)](azure-agent-infra/evidence.json) · [归档检查与隐私边界 (`review.md`)](azure-agent-infra/review.md)

[返回首页](../../README.md) · [English Homepage](../../README.en.md) · [归属与权利边界](../../ATTRIBUTION.md) · [第三方声明](../../THIRD_PARTY_NOTICES.md)
