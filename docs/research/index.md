# AI 研究专题总索引（Enterprise Cloud & AI Solution Architect Research Index）

> 🌐 **Language / 语言切换**: **[🇨🇳 中文总索引 (index.md)](index.md)** | **[🇬🇧 English Index (index.en.md)](index.en.md)** · **[🏠 返回仓库首页](../../README.md)** | **[🇬🇧 Repository Home](../../README.en.md)**

本索引汇集本仓库全部公开 **Cloud & AI Solution Architect** 架构研究、模型/编排基准测试与选型指南。所有专题均通过数据溯源审计（`evidence.json` + `review.md`），并与非公开草稿严格隔离。

---

## 1. 云原生 Agent 基础设施与超大规模推理（Cloud Agent Infra & Hyperscale Inference）

| 专题（中文 / English） | 核心架构域 | 核心交付物与实测结论 |
|---|---|---|
| **[Azure AI Agent Infrastructure 全栈方案设计与选型 Playbook](azure-agent-infra/README.md)** · **[English](azure-agent-infra/README.en.md)** | 4 层参考架构 · 6 大运行时 · `AKSClaw` · `E2B Firecracker` · `HorizonDB` · **62 篇选型指南** | 27 章全栈架构指南（`Standard_D96as_v7` `108ms` UFFD 恢复、261 节点承载 100K 并发沙箱）、23 套生产级 IaC 蓝图、8 幅 SVG、确定性容量计算器（`31/31` 单测通过）、**[62 篇企业级 Azure AI 选型指南](azure-agent-infra/selection-guides/README.md)**（[EN](azure-agent-infra/selection-guides/README.en.md)）、[7-Card 报告](azure-agent-infra/test-report.md)（[EN](azure-agent-infra/test-report.en.md) · [HTML](azure-agent-infra/cards.html)）与 [H5 交互工作台](azure-agent-infra/index.html) |
| **[DeepSeek DeepInfer 超大规模分离式推理与 Token 经济学](../../ai-infra/reports/2026-11-01/ai-infra-phase167-deepinfer-v41-pd-economics-2026-11-01.md)** · **[English](../../ai-infra/reports/2026-11-01/ai-infra-phase167-deepinfer-v41-pd-economics-2026-11-01.en.md)** | `DeepSeek-V4.1-Flash (552B MoE)` · `E/P/D 分离` · `100 PiB 3FS` · `DSpark` · `GB300 NVL72` | 拆解 `96%` 3FS 缓存命中 `25×` 吞吐放大（`1.50M tok/s/GPU`）、`1P:1D` 配比谷电价 `$38.00/GPU-hr` 账本与 `890 B/tok` KV 压缩；含 [7-Card HTML](../../ai-infra/reports/2026-11-01/ai-infra-phase167-benchmark-cards.html)、[交互工作台](../../ai-infra/reports/2026-11-01/ai-infra-phase167-visual-workbench.html) 与 [仿真脚本](../../ai-infra/experiments/phase167_deepinfer_v41_economics/simulate_deepinfer_economics.py) |
| **[E2B 沙箱集群 Nomad 心跳竞态与编排自愈研究](e2b-nomad-heartbeat-resilience/README.md)** · **[English](e2b-nomad-heartbeat-resilience/README.en.md)** | `HashiCorp Nomad` · `yamux` · `E2B Orchestrator` · `Cgroup Slice` | 基于 `e2b-dev/infra` 源码剖析心跳超时根因与控制面/数据面解耦方案（`<=35s` 抖动零误杀）；含 3 幅 SVG、[7-Card 报告](e2b-nomad-heartbeat-resilience/test-report.md)（[EN](e2b-nomad-heartbeat-resilience/test-report.en.md) · [HTML](e2b-nomad-heartbeat-resilience/test-report-cards.html)） |

---

## 2. 前沿模型、世界模型与决策路由基准（Frontier Models & Decision Routing）

| 专题（中文 / English） | 核心架构域 | 核心交付物与实测结论 |
|---|---|---|
| **[Gemini 4 Carbon 网安/长程智能体与 20 模型基准评测](gemini-4-carbon-and-20-model-benchmark/README.md)** · **[English](gemini-4-carbon-and-20-model-benchmark/README.en.md)** · [短链](gemini-4-carbon-benchmark/README.md) | 20 模型 Coding & Cyber 矩阵（`Gemini 4 Carbon` · `GPT-6 Astra` · `Opus 5.5` · `Fable 5.1`） | 同价位（`$2/$10`）斩获 17 项官方基准中 `15 项 #1`、网安三项全满贯与 `Gray Swan IPI 0.0% ASR`；含 [7-Card 报告](gemini-4-carbon-and-20-model-benchmark/test-report.md)（[EN](gemini-4-carbon-and-20-model-benchmark/test-report.en.md) · [HTML](gemini-4-carbon-and-20-model-benchmark/test-report-cards.html)）与确定性验证器 |
| **[SKY-001 工程世界模型与 19 模型 Coding Agent 横评](sky-001-and-coding-agent-19-model-benchmark/README.md)** · **[English](sky-001-and-coding-agent-19-model-benchmark/README.en.md)** · [短链](sky-001-coding-agent-benchmark/README.md) | 19 模型 × 11 题企业工程评测与六角色混合路由（`SKY-001` · `Haiku 5.5` · `Sonnet 5.5`） | `Claude Haiku 5.5`（`99.24` 分，`$0.33`）降本 `91.6%` 跃居总榜 `#4`；含 4 幅 SVG、[7-Card 报告](sky-001-and-coding-agent-19-model-benchmark/test-report.md)（[EN](sky-001-and-coding-agent-19-model-benchmark/test-report.en.md) · [HTML](sky-001-and-coding-agent-19-model-benchmark/test-report-cards.html)） |
| **[OpenAI Decisions vs Microsoft Decision-1 八引擎路由横评](openai-decisions-vs-decision-1-routing-benchmark/README.md)** · **[English](openai-decisions-vs-decision-1-routing-benchmark/README.en.md)** | `Switchyard` · `Microsoft Decision-1` · `TypeSafe Jev` · `OpenJev 27B` · `OpenAI Decisions` | 中性路由提示词下三大引擎均达 `40/40 (100%)`，`Decision-1` 成本仅 `$7.6/1M` 且 `0.60` 阈值 100% 拦截失误；含 [7-Card 报告](openai-decisions-vs-decision-1-routing-benchmark/test-report.md) 与 [HTML](openai-decisions-vs-decision-1-routing-benchmark/test-report-cards.html) |
| **[System-One 决策模型与 Foundry 多模型路由架构](decision-model-routing/README.md)** · **[English](decision-model-routing/README.en.md)** | `Microsoft-Decision-1` · `Strands Decider` × Azure AI Foundry | `384` 决策行 + `160` E2E 实测行：验证高频分类低延迟分流与置信度升级兜底机制；含 [实验详情](decision-model-routing/results.md) 与 [7-Card HTML](decision-model-routing/visual-report.html) |
| **[LocalJev 类型化决策桥、概率语义与合规边界](localjev/README.md)** · **[English](localjev/README.en.md)** | `choice / score / noul` 严格 JSON Schema 桥接 · 校准边界 · 许可审计 | 区分协议结构兼容与 Token Logprob 概率校准，明确 `OpenJev 27B` (`CC BY-NC 4.0`) 商业红线；含 [`evidence.json`](localjev/evidence.json) 与 [`review.md`](localjev/review.md) |

---

## 3. 多智能体编排、Harness 工程与技能标准（Multi-Agent Harnesses & Progressive Skills）

| 专题（中文 / English） | 核心架构域 | 核心交付物与实测结论 |
|---|---|---|
| **[随前沿模型升级持续演进 Agent Harness：生产级 Skill 审阅、12 KB 预算悬崖修复与协同演化实践手册](agent-harness-model-coevolution/README.zh-CN.md)** · **[English](agent-harness-model-coevolution/README.en.md)** · [总入口](agent-harness-model-coevolution/README.md) | `Model × Harness Co-Evolution` · `反脚手架定律` · `<available_skills> 12 KB 悬崖` · 三层渐进式披露 · `Desktop Canvases` | 基于 `2026-11-18` **120 个 Skill 目录（`113.5 MB`）** 与 `session_store_sql` 遥测实测：描述从 **`~38,600 → 8,019 chars`（`-79.2%`）**，路由可见率 **`1.2% → 100.0%`（`62/62`）**，磁盘瘦身 **`-56.97 MB / -50.2%`**，`OpenClaw` 主干 **`1,390 → 84` 行（`-94.0%`）**，落地目录外 `0 Bytes` `MODEL-SKILL-MATRIX.md`；含 12 幅中英双语 SVG、[`audit-summary.json`](agent-harness-model-coevolution/evidence/audit-summary.json)、[中文工作台](https://turbo998.github.io/workshops/agent-harness-coevolution/index.html)（[EN](https://turbo998.github.io/workshops/agent-harness-coevolution/index.en.html)）与 [中文 7 卡](https://turbo998.github.io/workshops/agent-harness-coevolution/cards.zh.html)（[EN](https://turbo998.github.io/workshops/agent-harness-coevolution/cards.html)） |
| **[Microsoft Agent Framework (MAF v1.0) vs 6 大主流框架基准评测](maf-multi-agent-benchmark/README.md)** · **[English](maf-multi-agent-benchmark/README.en.md)** | `MAF v1.0` · `LangGraph` · `AutoGen v0.4` · `Semantic Kernel` · `OpenAI Agents SDK` · `CrewAI` | MAF 综合得分 **`96.4/100` 居首**：覆盖三层拦截中间件、5 种编排模式（8-Agent 并发提速 `3.61×`）与 MCP/A2A v1.0；含 [7-Card 报告](maf-multi-agent-benchmark/test-report.md)（[EN](maf-multi-agent-benchmark/test-report.en.md) · [HTML](maf-multi-agent-benchmark/test-report-cards.html)）与 [交互工作台](maf-multi-agent-benchmark/index.html) |
| **[主流 Agent Harness 框架源码研究：DSH × Claude Code × HVE Core](harness-engineering-frameworks/README.zh-CN.md)** · **[English](harness-engineering-frameworks/README.en.md)** | 8 层通用 Harness 栈 · `PTC run_code` · 三级上下文压缩 · 四阶段 RPI | 锁定上游 Commit 源码解构：量化 `PTC run_code` `3.59×–7.51×` 级联提速、`94.2%` 前缀缓存保持与 `/clear` 注意力恢复；含 [7-Card 报告](harness-engineering-frameworks/test-report.md)（[EN](harness-engineering-frameworks/test-report.en.md) · [中文卡片](harness-engineering-frameworks/cards.zh.html) · [EN HTML](harness-engineering-frameworks/cards.html)）与 [Playground](harness-engineering-frameworks/index.html) |
| **[科学发现与行业场景 Harness 工程：CLIO 与校准遵从蓝图](scientific-and-industry-harness-engineering/README.md)** · **[English](scientific-and-industry-harness-engineering/README.en.md)** | `Microsoft Discovery` · `CLIO` · `Calibrated Deference` · 独立验证铁律 | 提炼高风险垂直行业 **10 大 Harness 设计法则**（不确定性梯度、灰盒机理约束、跨模型 3 振熔断）；含 [7-Card 报告](scientific-and-industry-harness-engineering/test-report.md)（[EN](scientific-and-industry-harness-engineering/test-report.en.md) · [中文卡片](scientific-and-industry-harness-engineering/cards.zh.html)）与 [工作台](scientific-and-industry-harness-engineering/index.html) |
| **[FAF v2 vs AGENT-FORGE vs HVE-Core 三方研发脚手架对比](faf-vs-agent-forge/README.md)** · **[English](faf-vs-agent-forge/README.en.md)** | `faf-agents v2.0.1` · `@agent-forge-copilot/cli` · `Microsoft HVE-Core` | 厘清角色插件、仓库 `.github/` 元编译器与 RPI 对抗状态机三层互补分工；含 [同屏竞技场](faf-vs-agent-forge/pelican-arena.html) 与 [7-Card HTML](faf-vs-agent-forge/test-report-cards.html) |
| **[企业级 Agent Skills 工程成熟度（L1–L4）与逆向验证架构](agent-skills-and-rea/README.md)** · **[English](agent-skills-and-rea/README.en.md)** | `SKILL.md` 渐进式披露 · `L2 Critic` · `L3 Deterministic Harness` · `L4 AST MCP` | 削减 `85%+` 初始上下文开销，构建从静态指令到确定性验证器与 AST 证据账本的四级企业治理模型；含 [交互导览](agent-skills-and-rea/index.html) 与 [L1–L4 探索台](agent-skills-and-rea/h5/ryan-doser-skills-report/index.html) |

---

## 4. AI 零信任安全、Purview 治理与电商协议（AI Security, Governance & Commerce）

| 专题（中文 / English） | 核心架构域 | 核心交付物与实测结论 |
|---|---|---|
| **[Microsoft 安全与 AI 就绪工程架构：DEFEND 五层模型与 6 大工作负载](defend-partner-playbook/README.md)** · **[English](defend-partner-playbook/README.en.md)** | `5-Tier DEFEND` · 6 大工作负载 360 页部署指南 · `Purview 4-Tier AI` · DLP | 41 项安全能力矩阵、51 项硬性准出关卡与 22 项 P1/P2/P3 部署模块；含确定性验证器（`8/8` 单测通过）与 [7-Card 报告](defend-partner-playbook/test-report.md)（[EN](defend-partner-playbook/test-report.en.md) · [中文卡片](defend-partner-playbook/cards.zh.html) · [EN HTML](defend-partner-playbook/cards.html)） |
| **[Security AI Landing Zone 与 Frontier SOC 架构研究](security-ai-landing-zone/index.zh.md)** · **[English](security-ai-landing-zone/index.md)** | `Microsoft Agent 365` 五大安全支柱 · `M365 E7` · `Defender ISOC & MDASH` | 4–6 周冲刺第 3 周 20 项安全硬门禁与红/蓝/绿安全智能体矩阵；含验证器（`6/6` 单测通过）与 [7-Card 报告](security-ai-landing-zone/test-report.md)（[EN](security-ai-landing-zone/test-report.en.md) · [中文卡片](security-ai-landing-zone/cards.zh.html) · [EN HTML](security-ai-landing-zone/cards.html)） |
| **[Agentic Commerce 全栈协议与硬件签名支付熔断](agentic-commerce/README.md)** · **[English](agentic-commerce/README.en.md)** | `Microsoft Web IQ` · `ACP / UCP` 幂等结账 · `AP2 & x402` FIDO2 支付门禁 | 解决自主购物与企业采购智能体中的网页间接注入、重复扣款与超额授权三大风险；含 [架构总览 SVG](agentic-commerce/assets/overview.svg) |

---

## 5. 每日开源 AI 雷达、Agentic OS 与个人智能体（Daily AI Radar, Agentic OS & Personal Agents）

| 专题（中文 / English） | 核心架构域 | 核心交付物与实测结论 |
|---|---|---|
| **[GitHub AI 趋势与飙升速度雷达（SA 每日情报台）](../../workshops/github-trending-radar/README.md)** · **[English](../../workshops/github-trending-radar/README.en.md)** | 24h 飙升榜 + 7d 新仓黑马榜 · `Hype / Facts / Signal` 评分 · 独立选型 FAQ | 每日追踪并沉淀开源 AI 架构原语与 SA 行动优先级（`2026-11-01` – `2026-11-17` 双语归档）；含 [中文 7-Card](../../workshops/github-trending-radar/cards.html) 与 [EN Deck](../../workshops/github-trending-radar/cards.en.html) |
| **[Omarchy Agent 桌面 OS 集成架构研究](omarchy-agent-design/README.md)** · **[English](omarchy-agent-design/README.en.md)** | `Agentic OS` · 14 分支 Harness 启动器 · 渐进式技能 · 崩溃事件诊断流 | 基于 `omacom/omarchy` 174 条静态源码契约核验（[00–06 分章报告](omarchy-agent-design/findings/00-summary.md)）；含 [7-Card 报告](omarchy-agent-design/test-report.md) 与 [HTML](omarchy-agent-design/test-report-cards.html) |
| **[Personal Agents 五款个人智能体比较与评测协议](personal-agents/README.md)** · **[English](personal-agents/README.en.md)** | `Meta Muse` · `Grok Bot` · `OpenAI dot` · `Gemini Spark` · `Instinct` | 对比运行时隔离、记忆范围与账号边界，配套 [18 案例测试协议](personal-agents/benchmark.md)、[`cases.json`](personal-agents/cases.json) 与 [`evidence.json`](personal-agents/evidence.json) |

---

[返回中文首页](../../README.md) · [English Homepage](../../README.en.md) · [归属与权利边界](../../ATTRIBUTION.md) · [第三方声明](../../THIRD_PARTY_NOTICES.md)

