# Agent Forge (FAF v2) vs. Microsoft AGENT-FORGE 深度研究与架构对比

[English Version (英文版)](./README.en.md) | [⚔️ 鹈鹕骑自行车同题竞技场 (Live Arena)](./pelican-arena.html) | [双插件实操对比报告](./pelican-benchmark-comparison.md) | [16 维对比矩阵](./comparison-matrix.md) | [7 页 4:5 视觉评测报告](./test-report.md) | [HTML 视觉卡片 (4:5)](./test-report-cards.html) | [机器核验证据账本](./evidence.json)

> **🔥 新增实装同题对决（Hands-On Pelican Bicycle Benchmark — Live on GitHub.io）**：
> 我们已在本地完整实装两套插件，并使用同一经典命题 **“动画版鹈鹕骑自行车（Animated Pelican Riding a Bicycle）”** 分别跑通了 **FAF v2 五阶段 SDLC 规范流** 与 **Microsoft AGENT-FORGE 四智能体 `.github/` 上下文生成流**：
> - **⚔️ 双插件同屏同步对比竞技场 (`pelican-arena.html`)**：[在线打开 GitHub.io 竞技场 →](https://turbo998.github.io/ai-research-public/docs/research/faf-vs-agent-forge/pelican-arena.html)（主站镜像：[turbo998.github.io/workshops/faf-vs-agent-forge/pelican-arena.html](https://turbo998.github.io/workshops/faf-vs-agent-forge/pelican-arena.html)）
> - **🟦 Demo A — FAF 架构规范驱动版 (`demo-faf-pelican.html`)**：余弦定理双连杆逆运动学（`0.00 px` 零滑移）、X-Ray 骨骼矢量透视、1.0x–4.2x 变速齿比与功率遥测仪表盘 + [真实 `compute_scores.py` 立项报告 (`P1 Go: 78.0 / 90.9 / 87.5`)](./artifacts/faf-sdlc/prioritization-report.html)
> - **🟧 Demo B — AGENT-FORGE 多智能体创意剧场版 (`demo-agent-forge-pelican.html`)**：加州海滨三幕光影切换（晴空/落日/星夜车灯）、点击抛沙丁鱼抛物线投喂吞咽、翘前轮特技（Wheelie）、WebAudio 双振荡器铜车铃 + [`forge validate` 8/8 零警告 `.github/` 产物包](./artifacts/agent-forge-context/)
> - **📄 完整实操与过程文档对比报告**：[中文报告 (`pelican-benchmark-comparison.md`)](./pelican-benchmark-comparison.md) | [English Report (`pelican-benchmark-comparison.en.md`)](./pelican-benchmark-comparison.en.md)

> **核心结论（Executive Summary）**：
> 尽管 **`customer-success-microsoft/faf-agents`**（仓库文档自称 **Agent Forge (FAF)**，Marketplace 名称 `agent-forge-plugins`，`v2.0.1`）与 **`microsoft/agent-forge`**（npm 包 `@agent-forge-copilot/cli`，`v0.3.0`）共享了“Agent Forge”这一名称，但二者处于**完全不同的元层级（Meta-Level）**，解决的问题截然不同且天然互补：
> 1. **`customer-success-microsoft/faf-agents` (FAF v2.0.1)** 是面向企业客户交付的 **“预置领域专家团队与全生命周期（SDLC）交付实践插件集”**。它直接提供已经调校好的 **6 个 GenAI 角色 Agent + 6 个 Fabric Analytics 正式注册 Agent（外加 3 个实验性工作流 Runner）+ 17 个专项领域技能（Skills）+ 加权评分卡 + 外部知识库管理（Harness Engineering）**，指导架构师和顾问完成从客户需求梳理、AI 优先级门禁评估、C4 架构设计、预置加速器加权打分（`>70%` 走定制复用 vs. `<40%` 走从零开发）到 Azure Bicep Landing Zone 部署与代码落地的全过程。
> 2. **`microsoft/agent-forge` (`@agent-forge-copilot/cli` v0.3.0)** 是面向任意软件工程仓库的 **“上下文工程元编译器（Context Engineering Meta-Generator Toolkit）”**。它本身不包含任何行业交付方法论或预置业务架构师，而是通过 `forge init` / `forge generate` 驱动一套 **Planner → Orchestrator → 7 个专项 Writer Agents → Deterministic Validator（44 工具白名单 + Levenshtein 距离 `<=3` 自动纠错）→ Smart Merger** 流水线，自动扫描你的代码库（支持 14 种技术栈指示文件）并为你**动态生成**专属的 `.github/agents/`、`.github/prompts/`、`.github/instructions/`、`.github/skills/`、`.github/hooks/`、`.vscode/mcp.json` 与 `.github/workflows/`。

---

## 1. 核验基准与可复验锚点（Verified Commit Baseline）

本研究基于两座仓库在 2026 年 10 月 23 日采集的精确 Git 提交快照进行静态源码与契约核验（`static_contract_verified`，未修改本地全局环境，未包含任何客户隐私数据）：

| 维度 | `customer-success-microsoft/faf-agents` (FAF v2) | `microsoft/agent-forge` (AGENT-FORGE CLI) |
| --- | --- | --- |
| **仓库定位** | 企业级 GenAI / Fabric Analytics 全 SDLC 交付实践与 Copilot 插件市场 | 面向任意 VS Code 项目的 GitHub Copilot 定制文件（`.github/`）多智能体生成工具包 |
| **可见性与许可** | Microsoft 内部 EMU 仓库（`INTERNAL`），`MIT License`（含 Anthropic 衍生文档技能声明） | GitHub 公开仓库（`PUBLIC`），`MIT License` |
| **核验 Commit SHA** | `a740ad88afa0b054e656207e72205002ca6744f0` (`2026-10-21T09:21:48Z`) | `655ff3401d18bd000252907a512a3f674114f708` (`2026-04-16T04:50:36Z`) |
| **Git Tree 规模** | `590` 个文件对象（Blobs）/ `736` 个目录树节点 | `38` 个文件对象（Blobs）/ `48` 个目录树节点 |
| **发布形态与版本** | Copilot Plugin Marketplace (`agent-forge-plugins` `v2.0.1`：`faf-core@2.1.1`、`faf-genai@2.1.0`、`faf-analytics@1.0.1`) | npm CLI 包 `@agent-forge-copilot/cli@0.3.0`（可执行命令 `forge`，Node.js `>=20.0.0`） |
| **核心交互入口** | VS Code Copilot Chat `/FAF-genai-*`、`/FAF-analytics-*` 斜杠命令及角色 Agent 切换 | 终端命令 `forge init`、`forge generate`、`forge validate`、`forge list`、`forge add`、`forge audit` |

---

## 2. 第一部分：`customer-success-microsoft/faf-agents` (FAF v2) 安装与核心体系精读

### 2.1 核心理念：从“僵化的端到端重复 IP”走向“可组合的 Agent 驱动实践”

传统的企业技术交付往往依赖固定的端到端方案加速器（Monolithic Solution Accelerators）：一旦客户的业务领域、数据源或安全合规边界偏离预设模板，团队就不得不推倒重来。

**FAF (Agent Forge)** 提出的范式转移是将可复用 IP 解耦为四层可组合资产：
1. **阶段化角色智能体（Role Agents）**：覆盖 Analyst（需求分析）、Architect（架构与量化评估）、Implementation Recommender（实施路径推荐）、Product Owner（待办拆解）、Developer（开发与自定义代理编排）、Infra（基础设施与 AI Landing Zone）。
2. **领域技能包（Domain Skills）**：按需加载的专项能力，如 `faf-ai-prioritization`（立项优先级与 9 项门禁评估）、`faf-genai-foundry-model-evaluation`（11 维 Foundry 模型选型）、`faf-azure-pricing`（实时调用 `https://prices.azure.com/api/retail/prices` 估算月度 TCO）、`faf-diagrams` / `faf-drawio-azure-diagrams`（架構图绘制）以及 Office 文档生成技能（`docx`、`pptx`、`xlsx`、`pdf`）。
3. **两条标准交付路径（Dual Delivery Paths）**：
   - **路径 A：Agentic Customization（智能体辅助加速器定制，加权得分 `> 70%`）**：当客户需求与既有成熟加速器高度匹配时，基于推荐加速器克隆代码，由 PO Agent 识别差距（Gap Analysis）并交由 Dev Agent 完成定向改造。
   - **路径 B：Agentic Development（智能体从零开发 + Harness Engineering，加权得分 `< 40%`）**：当无匹配加速器时，选用轻量级应用脚手架（App Starters），并通过 **`faf-kb-manager`（Harness Engineering）** 从外部仓库 `customer-success-microsoft/faf-knowledge-bases` 动态拉取技术栈最佳实践知识库注入工作区，指导 Infra / PO / Dev Agent 从零构建。
   - **中间审慎区间（`40% – 70%`）**：标记为 `Further Assessment Required`，强制要求人工架构师介入权衡改造已有加速器与从零构建的成本。
4. **内建可观测与成本度量（FAF Token Benchmark）**：通过 `src/core/hooks.json` 与 `src/core/scripts/faf_benchmark.py`（124,109 字节，附带 53 个单元测试），在不增加任何额外 LLM 调用的前提下，自动采集每次交互的 Token、AI Credits（`nano-AIU / 1,000,000,000`）、活跃执行耗时（自动剔除 `ask_user` 人工等待时间）与子 Agent 归因。

---

### 2.2 安装指南与 VS Code 插件缓存避坑（Installation & Setup）

FAF v2 采用 **VS Code Copilot Agent Plugin Marketplace** 机制分发（定义于 `.github/plugin/marketplace.json`）。

#### 方式一：VS Code 插件市场安装（推荐）

1. **前置条件**：
   - 安装 **VS Code**（建议最新稳定版或 Insiders）并启用 **GitHub Copilot Chat**。
   - 具备访问 `customer-success-microsoft/faf-agents` 的 GitHub 权限（通过 `gh auth login` 或 VS Code GitHub 账户登录）。
   - 打开 VS Code 设置（`Ctrl+,`），搜索 `chat.plugins.enabled` 并勾选启用。
2. **注册 Marketplace 仓库**：
   - 在设置中搜索 `chat.plugins.marketplaces`，点击 **Add Item**，填入：
     ```text
     customer-success-microsoft/faf-agents
     ```
3. **按需安装三大模块化插件**（打开命令面板 `Ctrl+Shift+P` → `Chat: Plugins` 或在扩展视图过滤 `@agentPlugins`）：
   - **`faf-core` (`v2.1.1`)【必装基础包】**：位于 `./src/core/`，提供共享技能（`faf-kb-manager`、`faf-azure-pricing`、`faf-diagrams`、`faf-drawio-azure-diagrams`、`docx`、`pptx`、`xlsx`、`pdf`）与 `hooks.json` 基准测试钩子。
   - **`faf-genai` (`v2.1.0`)【GenAI 交付套件】**：位于 `./src/genai/`，提供 6 个 GA 角色 Agent、3 个 GenAI 专属技能与 9 个 `/FAF-genai-*` 斜杠提示词。
   - **`faf-analytics` (`v1.0.1`)【Fabric Analytics 套件】**：位于 `./src/analytics/`，提供面向 Microsoft Fabric（RTI 实时智能与数据仓库迁移）的 6 个正式注册 Agent、6 个技能与 8 个斜杠提示词。
4. **配置 MCP Servers 与扩展**：
   - 工作区 `.vscode/mcp.json` 默认配置了 3 个核心 MCP 服务：
     - `microsoft-learn` (`https://learn.microsoft.com/api/mcp`)：提供最新 Azure / Fabric 官方文档检索。
     - `deepWiki` (`https://mcp.deepwiki.com/mcp`)：辅助查询开源仓库与架构模式。
     - `github` (`https://api.githubcopilot.com/mcp/`)：用于创建 Issue、管理 Backlog 与代码仓库交互。
   - 配合 Draw.io 架构图生成，建议安装 VS Code 扩展 `hediet.vscode-drawio`。
   - 仓库还在 `src/genai/extensions/faf-agent-workbench/` 下提供了 **FAF Agent Workbench (`v0.1.0`)** 扩展源码（Webview 工作台），支持可视化查看 `scope/`、`specs/`、`impl_rec/`、`arch/`、`plan/` 交付物进度并一键唤起对应 Agent。

#### ⚠️ 关键运维避坑：VS Code 插件升级必须手动清理本地缓存

根据 `docs/marketplace/INSTALL.md`（blob `e86a8676`）实测说明：**在 VS Code UI 中直接卸载插件再重新安装，并不会从 GitHub 拉取最新代码，而是直接复用本地缓存副本！**
升级 FAF 插件时的标准步骤为：
1. 在 VS Code 中卸载 `faf-core`、`faf-genai`、`faf-analytics`；
2. 完全关闭所有 VS Code 窗口；
3. 手动删除本地 `agentPlugins` 缓存目录：
   - **Windows (PowerShell)**：
     ```powershell
     Remove-Item -Recurse -Force "$env:APPDATA\Code\agentPlugins\github.com\customer-success-microsoft\faf-agents"
     ```
   - **macOS / Linux**：
     ```bash
     rm -rf ~/.config/Code/agentPlugins/github.com/customer-success-microsoft/faf-agents
     ```
4. 重新打开 VS Code 并重新安装上述三个插件。

---

### 2.3 FAF 三大插件模块与量化评分机制拆解

#### (1) `faf-genai` (`v2.1.0`)：6 大 GA 角色 Agent 与全流程契约

```
[客户原始纪要/文档]
       │
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. Analyst Agent (/FAF-genai-scope, /FAF-genai-prd)                     │
│    • 技能: faf-ai-prioritization (Value / Feasibility / Readiness)      │
│    • 门禁: 2 Hard Gates + 7 Readiness Gates + 40% Confidence Floor      │
│    • 产物: scope/*.md (Use-Case Prioritization) + specs/prd.md          │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │ Handoff
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 2. Architect Agent (/FAF-genai-spec, /FAF-genai-adr, /FAF-genai-model-eval)│
│    • 技能: faf-genai-foundry-model-evaluation (11 维模型评分卡)         │
│    • 技能: faf-diagrams / faf-drawio-azure-diagrams + faf-azure-pricing │
│    • 产物: specs/spec.md (C4 L1-L3 架构规范) + specs/adr/*.md           │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │ Handoff
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 3. Implementation Recommender (/FAF-genai-recommend-impl)               │
│    • 8 域加权评分卡: UseCase(25%)+Agentic(20%)+AIStack(18%)+Data(15%)   │
│      +Hosting(10%)+API(5%)+UI(4%)+Infra(3%) = 100%                      │
│    • 产物: impl_rec/impl-rec.md                                         │
└──────────────────┬───────────────────────────────────┬──────────────────┘
     Score > 70%   │ (40-70%: 人工复核)                 │ Score < 40%
                   ▼                                   ▼
┌─────────────────────────────────────┐ ┌─────────────────────────────────┐
│ 路径 A: Agentic Customization        │ │ 路径 B: Agentic Development      │
│ • 复用 6 大 Tech Success 代码加速器 │ │ • 选用轻量级 App Starter 脚手架 │
│   或 Copilot Studio 加速器          │ │ • faf-kb-manager 拉取外部知识库 │
│ • PO Agent 识别 Gap 并生成改造任务  │ │ • Infra Agent 部署 Bicep/LZ     │
│ • Dev Agent 执行定向定制改造        │ │ • PO + Dev Agent 从零编码实现   │
└─────────────────────────────────────┘ └─────────────────────────────────┘
```

1. **Analyst Agent (`FAF-analyst.agent.md`)**：
   - **职责**：将非结构化客户访谈、RFP 或会议记录转化为结构化项目范围说明（`scope/`）与产品需求文档（`specs/prd.md`）。
   - **量化优先级评估（`faf-ai-prioritization/references/scoring-framework.yaml`）**：
     - **Value（价值，100%）** = Business Value (`60%`) + Strategic Alignment (`40%`)；
     - **Feasibility（可行性，100%）** = AI Suitability (`35%`) + Technical Feasibility (`40%`) + Risk & Compliance (`25%`)；
     - **Readiness（就绪度，100%）** = Data Readiness (`50%`) + Organizational Readiness (`50%`)；
     - **分档阈值**：`High >= 65`、`Medium 40–64`、`Low < 40`；若证据置信度 `< 40%`（`confidence_floor: 40`），强制标记为 `Provisional`（暂定）。
     - **9 项一票否决/降级门禁**：包含 2 项硬门禁（`ai_unsuitable`、`regulatory_prohibition`）与 7 项就绪门禁（`no_executive_sponsor`、`no_data_available`、`no_data_access`、`no_business_owner`、`stakeholders_not_committed`、`no_run_owner`、`security_approval_missing`）。
2. **Architect Agent (`FAF-architect.agent.md`)**：
   - **职责**：基于 `specs/prd.md` 编写 C4（Context / Container / Component）技术架构规范（`specs/spec.md`）、架构决策记录（`specs/adr/`）、Azure 零售价格估算（调用 `https://prices.azure.com/api/retail/prices`）及 Foundry 模型选型报告。
   - **11 维 Foundry 模型评分卡（`lllm-model-scoring-card.md`）**：覆盖 `task_alignment`、`reasoning`、`multimodal`、`context_window`、`latency`、`cost`、`language_support`、`safety_compliance`、`customizability`、`ecosystem` 以及生命周期硬门槛 **`deprecation_date`（退役日期必须晚于当前日期至少 6 个月，否则直接淘汰）**。
3. **Implementation Recommender Agent (`FAF-impl-recommender.agent.md`)**：
   - **8 域加权评分卡（`accelerators-scoring-card.md`）**：每个具体指标按 `{0%, 25%, 50%, 75%, 100%}` 五档打分，先算各域均值，再按严格权重汇总：
     - `use_case` (**25%**) + `agentic_patterns` (**20%**) + `ai_stack` (**18%**) + `data_scenario` (**15%**) + `hosting` (**10%**) + `api_integration` (**5%**) + `ui_scenario` (**4%**) + `infrastructure` (**3%**) = **100%**。
   - **内置评估目录**：默认对比 6 个 Tech Success 代码级加速器（`agent-openai-python-banking-assistant`、`Agentic-AI-Investment-Analysis-Sample`、`ai-document-processor`、`gpt-rag`、`contentflow`、`live-voice-practice`）及 Copilot Studio 低代码目录（`ContentFlow`、`AISearch Flow`、`Video RAG` 等）。
4. **Product Owner Agent (`FAF-product-owner.agent.md`)**：
   - 将架构规范与实施推荐拆解为可执行的 Sprint Backlog（`plan/`）或直接通过 GitHub MCP 创建仓库 Issues。
5. **Developer Agent (`FAF-dev.agent.md`)**：
   - 除常规编码外，内置 **Custom Agent Orchestration（自定义代理编排）** 工作流：可结合 `faf-kb-manager` 拉取外部知识库，为客户的特定技术栈生成专属开发子代理。
6. **Infra Agent (`FAF-infra.agent.md`)**：
   - 提供两条基础设施工作流：
     - **Workflow 1 (Dev/Demo)**：使用 `azd` + 模块化 Bicep 快速拉起开发验证环境；
     - **Workflow 2 (Production AI Landing Zone)**：基于官方 **`Azure/bicep-ptn-aiml-landing-zone`** 模板构建企业级生产网络隔离、Private Endpoint 与受管标识环境。

#### (2) `faf-analytics` (`v1.0.1`)：面向 Microsoft Fabric 的数据分析交付链

- **源码树与注册清单的差异（重要源码发现）**：
  - `src/analytics/agents/` 目录下共有 **9 个 `.agent.md` 文件**，但 `src/analytics/plugin.json` 仅注册暴露了 **6 个面向用户的核心角色 Agent**：`FAF-analytics-analyst`、`FAF-analytics-architect`、`FAF-analytics-impl-recommender`、`FAF-analytics-assessment`、`FAF-analytics-product-owner`、`FAF-analytics-developer`。其余 3 个（`FAF-analytics-workflow-runner`、`FAF-analytics-workflow-tester`、`FAF-analytics-workflow-batch-runner`）属于内部评测/自动化运行器，未在插件清单中默认暴露。
  - 同时，根据 `analytics/RELEASE_NOTES_v1.md`，`v1.0` 正式版本测试门禁聚焦于 **Analyst + Architect** 在两大黄金场景上的端到端表现：
    1. **Microsoft Fabric Real-Time Intelligence (RTI)**（制造业实时遥测与异常检测）；
    2. **本地 SQL Server / Azure Synapse Dedicated SQL Pool 向 Microsoft Fabric Data Warehouse 迁移**（配合 Medallion 奖牌架构演进）。
  - 仓库内附带的 `docs/analytics/evaluation/faf-analytics-score-below-70-analysis.md` 诚实复盘了早期外部评测得分低于 70%（约 54%–60%）的根因：评测基准期待单次生成巨型一体式文档，而 FAF 将职责拆分到了 Analyst（PRD）、Architect（Spec）与 Assessment（Medallion 规范）多个阶段。

#### (3) `faf-core` (`v2.1.1`)：Harness Engineering 与零额外调用的 Token 基准测试

- **Harness Engineering (`faf-kb-manager`)**：
  - FAF 将高频更新的框架与 SDK 知识从插件本体剥离到独立仓库 `customer-success-microsoft/faf-knowledge-bases`，支持在用户主目录（`~/.faf-kb/`）或项目内（`docs/kb/`）按需检出、刷新和挂载，避免插件体积膨胀与上下文污染。
- **FAF Token Benchmark (`src/core/scripts/faf_benchmark.py`)**：
  - **触发机制**：在任意 Prompt 中加入 `benchmark=true benchmark-label=<label>` 即可激活；未带标记时，`UserPromptSubmit` 平均仅耗时 **`0.93s`**（`0.70–1.19s`），`Stop` 平均耗时 **`1.00s`**（`0.86–1.34s`），随后立即退出。
  - **多数据源适配与精度分级**：
    - 在 **GitHub Copilot CLI / App Session Store** 或开启了 **VS Code OTel (`chat.telemetry.AdHoc.dbSpanExporter.enabled: true` -> `agent-traces.db`)** 时，可采集全部 6 类精确指标（精确 Input/Output/Cached Tokens、逐次模型调用明细、嵌套子 Agent Token、`nano-AIU` 转换的 AI Credits `USD = AI credits * $0.01`）。
    - 若在默认未开启 OTel 的 VS Code Chat 中运行，则降级读取 Workspace Chat Journal，此时仅能获取顶层请求级汇总（2/6 维度完整精度），无法拆分嵌套子 Agent 与缓存 Token。

---

## 3. 第二部分：`microsoft/agent-forge` (`@agent-forge-copilot/cli`) 深度剖析

### 3.1 核心定位：把“手写 `.github/` 配置”变成“多智能体编译流水线”

在日常开发中，为不同技术栈（如 Next.js、FastAPI、Rust、Go、Spring Boot）编写高质量的 GitHub Copilot 定制文件（`.github/agents/*.agent.md`、`.github/instructions/*.instructions.md`、`.github/skills/*/SKILL.md`、`.github/hooks/*.json`、`.vscode/mcp.json`）既繁琐又容易违反 YAML Frontmatter 与工具名规范。

**`microsoft/agent-forge`**（源码合并器 `src/lib/merger.ts` 中保留了其前身标记 `<!-- Generated by SpecForge -->`）正是为此设计的 **Context Engineering Toolkit（上下文工程元工具包）**。

### 3.2 四阶段“规划-执行-校验-合并”流水线（Plan-Then-Execute Pipeline）

```
[用户执行 forge init / forge generate]
       │
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 阶段 1: 工作区探测 (src/lib/detector.ts)                                │
│ • 扫描 14 种 TECH_INDICATORS (package.json, pyproject.toml, go.mod 等) │
│ • 扫描 14 种 PROJECT_TYPE_HINTS 推断项目类型 (web/api/cli/library/...) │
│ • 审计既有 .github/ 下的 agents, prompts, instructions, skills, hooks   │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 阶段 2: 多智能体规划 (Planner -> forge-plan.json)                       │
│ • Greenfield Planner (从自然语言描述规划) / Brownfield Planner (从代码库)│
│ • 选择 6 种编排模式之一: flat | coordinator-worker | multi-perspective  │
│   | tdd | pipeline | iteration                                          │
│ • 产成结构化 GenerationPlan (PlannedAgent, PlannedSkill, PlannedHook...)│
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 阶段 3: 编排器与 7 大专项 Writer Agents (src/cli/writers/*.ts)          │
│ • 调用 copilot -p ... --autopilot --no-ask-user (maxContinues: 25 / 15) │
│ • 7 个 Writer: agent / prompt / instruction / skill / hook / mcp / wf   │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 阶段 4: 确定性修复 + LLM 校验 + 安全合并 (validator.ts & merger.ts)     │
│ • postGenerationValidateAndFix: 修补缺失 Frontmatter、剥离非法字段       │
│ • 对照 44 个 VALID_VSCODE_TOOLS，用 Levenshtein 距离 <=3 修正工具名拼写  │
│ • autoFixHandoffReferences: 自动对齐跨文件 handoffs.agent 引用名称       │
│ • merger.ts: 仅覆盖带 <!-- Generated by AGENT-FORGE --> 标记的文件       │
└─────────────────────────────────────────────────────────────────────────┘
```

1. **工作区自动探测（`src/lib/detector.ts`）**：
   - 自动检测 **14 种技术栈清单文件**（`package.json`、`tsconfig.json`、`pyproject.toml`、`requirements.txt`、`go.mod`、`Cargo.toml`、`pom.xml`、`build.gradle`、`Gemfile`、`composer.json`、`mix.exs`、`Dockerfile`、`docker-compose.yml`、`.csproj`）及 **14 种目录/配置文件提示**，将项目归类为 `web`、`api`、`cli`、`library`、`data-pipeline` 或 `other`。
2. **双模式规划器（Greenfield vs. Brownfield Planner）**：
   - 在 `create`（新建）或 `analyze`（分析现有仓库）模式下，调用 Copilot CLI（`maxContinues: 25`）生成 `.github/forge-plan.json`。
   - 规划器会根据项目复杂度从 **6 种多智能体编排模式（`OrchestrationPattern`）** 中择优：
     - `flat`（扁平独立专家，2–3 个无依赖 Agent）；
     - `coordinator-worker`（协调器+执行器，4+ 跨域复杂项目）；
     - `multi-perspective`（多视角评审，安全/性能/架构交叉审查）；
     - `tdd`（测试驱动红绿重构闭环，`Red → Green → Refactor` Handoff）；
     - `pipeline`（顺序阶段流水线）；
     - `iteration`（生成-评审迭代闭环）。
3. **7 大专项生成代理（Specialized Writer Agents）**：
   - `forge-agent-writer`（生成 `.github/agents/*.agent.md`）
   - `forge-prompt-writer`（生成 `.github/prompts/*.prompt.md`）
   - `forge-instruction-writer`（生成 `.github/instructions/*.instructions.md` 与 `copilot-instructions.md`）
   - `forge-skill-writer`（生成 `.github/skills/<name>/SKILL.md`）
   - `forge-hook-writer`（生成 `.github/hooks/<name>.json`）
   - `forge-mcp-writer`（生成 `.vscode/mcp.json`）
   - `forge-workflow-writer`（生成 `.github/workflows/<name>.md` Agentic Workflows）
4. **确定性 Schema 校验与自愈（`src/lib/validator.ts`）**：
   - LLM 生成的配置文件常出现 Frontmatter 缺失、多出未定义字段、工具名拼写错误或 Handoff 目标 Agent 名称不一致。`validator.ts` 提供了极其扎实的工程兜底：
     - **44 个 VS Code 合法工具名白名单（`VALID_VSCODE_TOOLS`）**：涵盖 `codebase`、`editFiles`、`fetch`、`findTestFiles`、`githubRepo`、`new`、`openSimpleBrowser`、`problems`、`runCommands`、`runNotebooks`、`runSubagent`、`runTasks`、`runTests`、`search`、`searchResults`、`terminalLastCommand`、`terminalSelection`、`testFailure`、`usages`、`vscodeAPI`、`changes`、`extensions`、`todos` 等。
     - **Levenshtein 编辑距离 `<= 3` 自动纠错**：例如将 LLM 误写的工具名自动映射到最接近的合法工具。
     - **跨文件 Handoff 引用修复（`autoFixHandoffReferences`）**：当 A Agent 的 `handoffs.agent` 指向不存在的名称时，自动通过前缀/后缀包含关系或编辑距离匹配到真实生成的 `.agent.md` 文件名。
     - **可选单次 LLM 修复（`forge validate --fix`）**：通过 `callLlmForJson`（`30,000ms` 超时）对复杂语义错误进行 JSON 补丁修复。
5. **11 套零 LLM 调用的内置模板库（`src/lib/gallery.ts`）**：
   - 若执行 `forge init --mode templates`，无需消耗任何 LLM Token（本地文件复制约 `~120ms`），即可从 11 套内置模板中按需安装：`code-review`、`testing`、`documentation`、`deployment`、`onboarding`、`refactoring`、`code-quality-hooks`、`session-logging`、`issue-triage`、`daily-report`、`dev-tools-mcp`。

---

## 4. 第三部分：FAF vs. AGENT-FORGE 核心差异全景对比

关于全部 16 个维度的逐项源码级对比，请参见 [**《16 维深度对比矩阵》 (`comparison-matrix.md`)**](./comparison-matrix.md)。下表浓缩了二者最核心的 **8 大本质区别**：

| 对比维度 | `customer-success-microsoft/faf-agents` (FAF v2.0.1) | `microsoft/agent-forge` (`@agent-forge-copilot/cli` v0.3.0) |
| --- | --- | --- |
| **1. 本质定位（Meta-Level）** | **领域交付团队（Domain Delivery System）**：自身就是一套已经写好的、直接干活的领域专家 Agent 与技能插件 | **元生成器（Meta-Generator / Compiler）**：一套用来“生成别的项目所需的 `.github/` Agent 和配置”的 CLI 工具链 |
| **2. 目标用户与场景** | 微软 CSU / FastTrack / 合作伙伴架构师与交付工程师，面向**企业客户 GenAI 与 Microsoft Fabric 数据项目** | 任意技术栈（Web/API/CLI/库）的软件开发者，希望快速为自己的代码库生成高质量 GitHub Copilot 上下文工程配置 |
| **3. 覆盖的生命周期阶段** | **端到端客户交付 SDLC**：客户立项打分 → PRD → C4 架构与模型选型 → 加速器加权推荐 → Bicep/LZ 部署 → 编码与 Token 审计 | **仓库级上下文工程生命周期**：工作区探测 → 定制方案规划 → 生成 7 类 `.github/` 配置文件 → Schema 校验与自愈 → 增量合并 |
| **4. 资产形态与可定制性** | **固定高价值领域 IP**：预置 6 个 GenAI Agent + 6 个注册 Analytics Agent + 17 个技能 + 外部 `faf-knowledge-bases` | **按项目动态合成**：内置 2 个 Planner + 2 个 Orchestrator + 7 个 Writer Agent + 11 套通用模板，每次运行根据目标仓库生成新 Agent |
| **5. 量化决策与评估模型** | 内置 **3 套业务量化模型**（AI 立项 3 维+9 门禁、Foundry 模型 11 维评估、加速器 8 域加权评分卡）+ **Token/AIU 成本基准测试** | 内置 **工程配置质量审计（`forge audit` / `forge validate`）**：按 0–100 分评估 `.github/` 覆盖度、Frontmatter 合规度与工具/Handoff 完整性 |
| **6. 对云与平台栈的绑定度** | **深度绑定 Azure 与 Microsoft Fabric**（Azure AI Foundry、AI Search、Bicep Landing Zone、Fabric RTI / Medallion DW、Azure 零售价格 API） | **完全云无关、语言无关**（支持 TypeScript/Python/Go/Rust/Java/C#/Ruby/PHP/Elixir 等 14 种技术栈指示器） |
| **7. 运行时依赖** | 依赖 **VS Code Copilot Chat Plugin 机制** + MCP Servers (`microsoft-learn`, `deepWiki`, `github`) + Python 3（用于 `faf_benchmark.py` 与文档技能） | 依赖 **Node.js `>=20`** + **GitHub Copilot CLI (`copilot`)**（`templates` 与纯确定性 `validate` 模式无需调用 LLM） |
| **8. 既有文件保护机制** | 插件资产安装在 VS Code `agentPlugins` 缓存目录，业务交付物写入项目 `scope/`、`specs/`、`impl_rec/`、`plan/`，外部知识库写入 `docs/kb/` | 写入 `.github/` 与 `.vscode/mcp.json`；`merger.ts` 严格检查 `<!-- Generated by AGENT-FORGE -->` 标记，绝不覆盖用户手写或 FAF 资产 |

---

## 5. 实战选型指南与“FAF + AGENT-FORGE”双剑合璧工作流

### 5.1 什么时候用哪一个？

- **选择 `customer-success-microsoft/faf-agents` (FAF v2)**：
  - 你正在做 **Azure AI Foundry / OpenAI 应用或 Microsoft Fabric 数据平台** 的客户售前立项、架构设计、PoC 或生产交付；
  - 你需要一套经过验证的量化工具来回答：“这个客户场景应该复用哪个现有 Solution Accelerator（得分 `>70%`），还是从零开发（`<40%`）？”、“选哪个 Foundry 模型最划算且未来 6 个月不会退役？”、“整套 Azure 资源每月大概花多少钱？”；
  - 你需要直接生成符合企业交付标准的 Word (`docx`)、PPT (`pptx`)、Excel (`xlsx`)、Draw.io 架构图与 AI Landing Zone Bicep 代码。
- **选择 `microsoft/agent-forge` (`@agent-forge-copilot/cli`)**：
  - 你手头有一个**任意语言或框架的代码仓库**（无论是全新的 Greenfield 项目，还是已有的 Brownfield 老项目），希望在几分钟内为它配齐规范的 `.github/copilot-instructions.md`、路径级 `.instructions.md`、TDD/Code Review 专属 Agent 以及提交前代码质量 Hooks；
  - 你希望在 CI/CD 中通过 `forge validate` 与 `forge audit` 自动化检查团队编写的 Copilot Agent 配置文件是否存在工具名拼写错误或断链的 Handoff。

### 5.2 推荐组合拳：在同一个企业项目中串联 FAF 与 AGENT-FORGE

由于 `microsoft/agent-forge` 的 `merger.ts` 具备严格的 HTML 注释标记保护，**二者可以在同一个客户项目仓库中无缝接力，零冲突协同**：

1. **第 1 步（Day 0–Day 2，使用 FAF `faf-genai` / `faf-analytics`）**：
   - 在 VS Code 中加载 FAF 插件，依次运行 `/FAF-genai-scope` → `/FAF-genai-prd` → `/FAF-genai-spec` → `/FAF-genai-recommend-impl`。
   - 完成客户需求收敛、Foundry 模型 11 维选型、Azure 成本估算与 8 域加速器打分。
2. **第 2 步（Day 3，使用 FAF `faf-kb-manager` + `FAF-infra`）**：
   - 若走 **Agentic Customization（`>70%`）**，克隆推荐的加速器代码；若走 **Agentic Development（`<40%`）**，拉取轻量脚手架并通过 `faf-kb-manager` 将 Azure / Agent 框架知识库同步到 `docs/kb/`，再用 `FAF-infra` 生成 Bicep / AI Landing Zone。
3. **第 3 步（Day 4+，使用 `npx @agent-forge-copilot/cli init`）**：
   - 当工程代码骨架落地后，在项目根目录运行：
     ```bash
     npx @agent-forge-copilot/cli init --mode analyze --strategy guided
     ```
   - `AGENT-FORGE` 会自动扫描刚刚落地的代码栈（如 `pyproject.toml`、`package.json`、`Dockerfile`），为你生成贴合该仓库目录结构的 `.github/instructions/*.instructions.md`、TDD 测试 Agent 与 `.github/hooks/` 质量门禁，同时**完好保留** FAF 生成的 `scope/`、`specs/`、`docs/kb/` 以及任何非 AGENT-FORGE 标记的文件。
4. **第 4 步（持续迭代与度量）**：
   - 使用 `forge validate` 校验仓库内所有 `.github/` 定制文件的语法与工具名合法性；
   - 在关键开发任务 Prompt 中附带 `benchmark=true benchmark-label=sprint-1`，利用 FAF 的 `faf_benchmark.py` 持续追踪团队在整个交付周期的 Token 与 AI Credits 消耗。

---

## 6. 本目录交付物索引（Deliverables Index）

- [`README.zh-CN.md`](./README.zh-CN.md) / [`README.md`](./README.md)：中文主研究报告（本文档）
- [`README.en.md`](./README.en.md)：英文完整对应版研究报告（English Research Guide）
- [`comparison-matrix.md`](./comparison-matrix.md) / [`comparison-matrix.en.md`](./comparison-matrix.en.md)：中英文 16 维源码级深度对比矩阵
- [`test-report.md`](./test-report.md) / [`test-report.en.md`](./test-report.en.md)：中英文 7 页 4:5 视觉评测报告（Markdown 版）
- [`test-report-cards.html`](./test-report-cards.html)：自包含 CSP 安全策略的 7 页 4:5 视觉卡片组（可直接浏览器打开或导出海报）
- [`evidence.json`](./evidence.json) & [`evidence/report.json`](./evidence/report.json)：包含精确 Commit SHA、Blob SHA、字节大小及全部评测坐标的机器可读证据账本
- [`review.md`](./review.md)：证据完整性、双语一致性与脱敏合规自检报告
