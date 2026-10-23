# Agent Forge (FAF v2) vs. Microsoft AGENT-FORGE 机制契约与能力评测报告（7 页 4:5 视觉卡片版）

[English Version](./test-report.en.md) | [返回主研究报告](./README.zh-CN.md) | [16 维对比矩阵](./comparison-matrix.md) | [HTML 4:5 视觉卡片](./test-report-cards.html) | [机器核验数据 (`report.json`)](./evidence/report.json)

> **Provenance 声明**：本报告严格遵循 **7-Card 4:5 Visual Benchmark Report Standard**，所有百分比、权重、门禁阈值、工具白名单数量与 Hook 延迟数据均提取自 `customer-success-microsoft/faf-agents@a740ad88afa0b054e656207e72205002ca6744f0`（590 Blobs）与 `microsoft/agent-forge@655ff3401d18bd000252907a512a3f674114f708`（38 Blobs）的封印源码证据（`static_contract_verified_and_anonymized_reported`, `independently_reproduced=false`）。

---

## Card 1 (`1 / 7` · `HANDS-ON · AGENT SYSTEMS`) — Overview & Workbench

### **FAF v2 提供 3 大插件与 12 个注册领域角色 Agent；AGENT-FORGE 编译全部 7 类 `.github/` 定制资产**

| 工作台分栏 (Workbench Column) | 核心指标与核验结果 | 源码证据锚点 |
| --- | --- | --- |
| **左栏：评测场景与阈值分档 (Scenarios & Thresholds)** | • **12 个源码级核验场景**：**8 个** `Act automatically` (`>=80%`)，**2 个** `Confirm` (`33%–67%`)，**2 个** `Send to a human` (`0%`)<br>• **FAF 加速器推荐阈值**：`>70%` 定制复用 / `40%–70%` 人工复核 / `<40%` 从零开发<br>• **FAF AI 立项阈值**：`High >=65` / `Medium 40–64` / `Low <40`（`<40%` 置信度底线） | `evidence/report.json`<br>`accelerators-scoring-card.md`<br>`scoring-framework.yaml` |
| **中栏：双系统契约输入 (Dual System Contract)** | • **FAF v2 (`agent-forge-plugins@2.0.1`)**：`faf-core@2.1.1` (8 共享技能 + Benchmark Hook) + `faf-genai@2.1.0` (6 GA Agents, 3 Skills, 9 Prompts) + `faf-analytics@1.0.1` (6 注册 Agents / 9 源码 Agents, 6 Skills)<br>• **AGENT-FORGE (`@agent-forge-copilot/cli@0.3.0`)**：14 技术栈指示器 → 2 Planners → 2 Orchestrators → 7 Writers → 44 工具白名单校验器 | `.github/plugin/marketplace.json`<br>`src/types.ts`<br>`src/lib/validator.ts` |
| **右栏：延迟、Token 账本与核心结论 (Latency & Decisions)** | • **FAF 未标记 Hook 退出耗时**：`UserPromptSubmit` **`930 ms`** 均值 / `Stop` **`1,000 ms`** 均值（0 额外 LLM 调用）<br>• **AGENT-FORGE 模板安装**：**`~120 ms`** 本地复制（11 套内置模板，0 LLM 调用） vs **`30,000 ms`** LLM 修复超时上限 | `README-faf-token-benchmark.md`<br>`src/lib/validator.ts:48` |

> **底部硬件与溯源说明 (Provenance Callout)**：`static_contract_verified + anonymized_reported (independently_reproduced=false)` · 核验环境：Windows 11 (`git`, `gh`, Python 3) · 精确 Commit：`faf-agents@a740ad88` & `agent-forge@655ff340`。

---

## Card 2 (`2 / 7` · `SCENARIO: ENTERPRISE GENAI SCOPING TO REPO CUSTOMIZATION`) — Single-Case Deep Dive

### **单案例深潜：8 域加权加速器评分（`83.9% > 70%`）驱动定制决策，配合 44 工具确定性校验（`~120ms`）落地代码库规约**

> **输入场景引用 (Input Quote)**：
> *“企业客户计划构建一套基于 Azure AI Foundry 与 Azure AI Search 的多智能体投研文档分析与问答系统，要求在 2 周内完成立项优先级门禁评估、C4 架构设计、判断是否复用现有 Solution Accelerator，并在落地仓库中自动生成防覆盖的 `.github/` 团队编码指令与质量门禁。”*

1. **决策卡 1 · `[score]` FAF AI 立项优先级与 9 项门禁核验 (`faf-ai-prioritization`)**
   - **得分与置信度**：`Value 78% · Feasibility 74% · Readiness 70%`（证据置信度 `85% >= 40%` 底线）
   - **动作标签**：`Act automatically`（9 项门禁全部通过：无硬性合规阻断、已具备业务 Sponsor 与数据访问授权）
   - **水平分项条**：
     - Business Value (`60%` 权重) + Strategic Alignment (`40%` 权重)：`78.0%`
     - AI Suitability (`35%`) + Tech Feasibility (`40%`) + Risk (`25%`)：`74.0%`
     - Data Readiness (`50%`) + Org Readiness (`50%`)：`70.0%`

2. **决策卡 2 · `[choice]` FAF Implementation Recommender 8 域加权加速器打分 (`FAF-impl-recommender`)**
   - **最高匹配加速器**：`Agentic-AI-Investment-Analysis-Sample` / `ai-document-processor` 加权总分 **`83.9%`**（超过 `> 70%` 阈值）
   - **动作标签**：`Act automatically` → 选择 **Path A: Agentic Customization（基于既有加速器定制改造）**
   - **8 域加权分解**：
     - `use_case` (权重 25%): `87.5%` | `agentic_patterns` (权重 20%): `85.0%` | `ai_stack` (权重 18%): `83.3%` | `data_scenario` (权重 15%): `81.3%`
     - `hosting` (权重 10%): `75.0%` | `api_integration` (权重 5%): `75.0%` | `ui_scenario` (权重 4%): `100.0%` | `infrastructure` (权重 3%): `87.5%`

3. **决策卡 3 · `[noul]` AGENT-FORGE 仓库级 `.github/` 规约生成与自愈 (`forge init --mode analyze`)**
   - **校验与合并结果**：7 类 `.github/` 定制文件生成率 **`100%`**，44 个 VS Code 工具名白名单匹配 **`100%`**，既有 FAF `specs/` 与 `scope/` 文件保留率 **`100%`**
   - **动作标签**：`Act automatically` → `postGenerationValidateAndFix` + `mergeIntoExisting` 安全落盘

---

## Card 3 (`3 / 7` · `WHAT I TESTED`) — Full Evaluation Matrix

### **12 项机制契约核验矩阵：8 项全量达标（`100%`），4 项揭示关键边界与运维陷阱（标记 `✕`）**

| SCENARIO | QUESTION / TASK | MODEL / SYSTEM ANSWER | ACTION |
| --- | --- | --- | --- |
| **S01 · FAF Plugin Split** | `marketplace.json` 是否拆分为 `faf-core`、`faf-genai`、`faf-analytics` 三大插件？ | `3 / 3 plugins verified (100%)` | `Act automatically` |
| **S02 · FAF GenAI Roster** | `faf-genai@2.1.0` 是否完整包含 6 个 GA 角色 Agent 与 9 个 `/FAF-genai-*` 提示词？ | `6 GA Agents + 9 Prompts (100%)` | `Act automatically` |
| **S03 · FAF 8-Area Weights** | 加速器评分卡 8 个领域权重之和是否严格等于 100% 且划分 `>70%` / `40-70%` / `<40%`？ | `8 Areas = 100% + 3 Threshold Bands (100%)` | `Act automatically` |
| **S04 · FAF 9 Priority Gates** | `faf-ai-prioritization` 是否实施 2 项硬门禁 + 7 项就绪门禁与 40% 置信度底线？ | `3 Dimensions + 9 Gates + 40% Floor (100%)` | `Act automatically` |
| **S05 · FAF Analytics Roster** | `src/analytics/agents/` 下的 9 个 Agent 文件是否全部在 `plugin.json` 中默认注册？ | `6/9 registered (3 workflow runners omitted) (67%) ✕` | `Confirm` |
| **S06 · FAF Telemetry Fallback** | 未开启 VS Code OTel 时，默认 Chat Journal 能否采集嵌套子 Agent 与逐调用精确 Token？ | `Top-level aggregate only (2/6 sources = 33%) ✕` | `Confirm` |
| **S07 · FAF Plugin Upgrade** | VS Code UI 卸载重装插件是否会自动从 GitHub 拉取最新提交？ | `0% auto-refresh (reuses %APPDATA% cache) ✕` | `Send to a human` |
| **S08 · AF 7-Type Pipeline** | `agent-forge` 是否通过 Planner + Orchestrator + 7 Writers 生成全部 7 类定制资产？ | `2 Planners + 7 Writers -> 7 Artifact Types (100%)` | `Act automatically` |
| **S09 · AF Stack Detector** | `detector.ts` 是否支持扫描 14 种清单文件与 14 种项目类型提示？ | `14 Tech Indicators + 14 Type Hints (100%)` | `Act automatically` |
| **S10 · AF Schema Auto-Fix** | `validator.ts` 是否内置 44 个合法工具名、编辑距离 `<=3` 纠错与 Handoff 修复？ | `44 Valid Tools + Levenshtein<=3 + Handoff Fix (100%)` | `Act automatically` |
| **S11 · AF Smart Merge** | `merger.ts` 在默认模式下是否 100% 保护未带生成标记的用户手写文件？ | `100% user-file preservation unless --force (100%)` | `Act automatically` |
| **S12 · Cross-Repo Boundary** | `agent-forge` 是否自带 FAF 的客户 PRD/C4 模板、加速器评分卡或 Bicep Landing Zone？ | `0% domain delivery IP bundled ✕` | `Send to a human` |

- **门禁汇总 Callout 1（Threshold Gating Summary）**：12 个核验项中，**8 项（66.7%）** 达到 `100%` 确定性闭环（`Act automatically`）；**2 项（16.7%）** 存在部分降级（`Confirm`：Analytics 隐藏了 3 个实验性 Runner；VS Code 默认 Journal 仅具 33.3% 遥测维度精度）。
- **门禁汇总 Callout 2（Critical Miss Analysis）**：**2 项（16.7%）** 为 `0%`（`Send to a human`）：其一是 VS Code 插件缓存不会随卸载自动刷新，必须手动删除 `%APPDATA%\Code\agentPlugins`；其二是 `microsoft/agent-forge` 不含任何行业交付资产，不可替代 FAF 的架构与立项角色。

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`) — Protocol & Scoring Mechanics

### **底层机制对比：FAF 8 域加权评分与 AIU 核算公式 vs. AGENT-FORGE 确定性 Schema 修复器**

#### 代码块 A：FAF 加权加速器评分公式与 Token Benchmark AI Credits 核算（`accelerators-scoring-card.md` & `faf_benchmark.py`）

```python
# 1. FAF Implementation Recommender: 8-Area Weighted Score (Sum of weights = 100%)
AREA_WEIGHTS = {
    "use_case": 0.25, "agentic_patterns": 0.20, "ai_stack": 0.18, "data_scenario": 0.15,
    "hosting": 0.10,  "api_integration": 0.05,  "ui_scenario": 0.04, "infrastructure": 0.03,
}
# Sub-metrics scored in {0.0, 0.25, 0.50, 0.75, 1.0}; weighted_score > 0.70 => Agentic Customization
# 0.40 <= weighted_score <= 0.70 => Further Assessment Required; < 0.40 => Agentic Development

# 2. FAF Token Benchmark (src/core/scripts/faf_benchmark.py): Zero-LLM-Call Accounting
# Triggered opt-in via prompt marker: benchmark=true benchmark-label=<label>
ai_credits = nano_aiu / 1_000_000_000          # 1 AI credit = 10^9 nano-AIU
estimated_usd = ai_credits * 0.01              # $0.01 per AI credit
active_duration_ms = wall_clock_ms - non_overlapping_human_wait_ms  # subtracts ask_user wait
```

`↓`

#### 代码块 B：AGENT-FORGE 确定性 Frontmatter、工具名与 Handoff 自愈流水线（`src/lib/validator.ts` & `src/lib/merger.ts`）

```typescript
// src/lib/validator.ts: postGenerationValidateAndFix(files)
// Step 1: Reconstruct missing YAML frontmatter & strip unrecognized keys per artifact schema
// Step 2: Validate tools against 44 VALID_VSCODE_TOOLS with Levenshtein distance <= 3 suggestion
const suggestion = findClosestTool(invalidTool, VALID_VSCODE_TOOLS); // max distance <= 3

// Step 3: Repair broken cross-file handoff targets (autoFixHandoffReferences)
// Matches target agent by case-insensitive exact match, prefix/suffix containment, or Levenshtein <= 3

// src/lib/merger.ts: Non-destructive smart merge protection
const GENERATED_MARKER = '<!-- Generated by AGENT-FORGE -->';
const LEGACY_MARKER    = '<!-- Generated by SpecForge -->';
// Refuses to overwrite existing file unless options.force === true or file includes marker
```

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`) — Perturbation & Consistency

### **模式切换与边界扰动测试：遥测降级（`-66.7 pts`）、清单裁剪（`-33.3 pts`）与防覆盖锁（`-100.0 pts`）完全符合契约**

| QUESTION / DIMENSION | ORIGINAL (PRIMARY PATH) | REVERSED / PERTURBED PATH | CHANGE (PTS) |
| --- | --- | --- | --- |
| **FAF Telemetry Source**<br>Copilot Session Store vs. VS Code Journal Fallback | **100.0%**<br>(6/6 精确遥测维度：含子代理与缓存 Token) | **33.3%**<br>(2/6 维度：仅顶层请求汇总，无嵌套子代理明细) | **`-66.7 pts`**<br>(`Holds`) |
| **FAF Analytics Agent Exposure**<br>Source Tree (`src/analytics/agents/`) vs. `plugin.json` | **100.0%**<br>(9/9 `.agent.md` 源码文件存在) | **66.7%**<br>(6/9 注册暴露，3 个实验性 Runner 未暴露) | **`-33.3 pts`**<br>(`Holds`) |
| **FAF Accelerator Threshold Gate**<br>High-Fit Sample (`>70%`) vs. Low-Fit Custom (`<40%`) | **83.9%**<br>(触发 Path A: Agentic Customization) | **35.0%**<br>(触发 Path B: Agentic Development + KB 拉取) | **`-48.9 pts`**<br>(`Holds`) |
| **AGENT-FORGE Init Mode**<br>`--mode create/analyze` vs. `--mode templates` | **100.0%**<br>(7/7 类 `.github/` 资产全量动态合成) | **71.4%**<br>(5/7 类静态模板覆盖，0 LLM 调用极速拷贝) | **`-28.6 pts`**<br>(`Holds`) |
| **AGENT-FORGE Merge Flag**<br>Default Safe Merge vs. `--force` Overwrite | **100.0%**<br>(用户手写冲突文件 100% 保留跳过) | **0.0%**<br>(传入 `--force` 时冲突文件被强制覆盖) | **`-100.0 pts`**<br>(`Holds`) |
| **AGENT-FORGE Tool Typo Distance**<br>Levenshtein `<= 3` vs. Distance `> 3` | **100.0%**<br>(44 白名单工具名拼写错误自动给出修正建议) | **0.0%**<br>(距离 `>3` 的自定义 MCP 工具名不发生误替换) | **`-100.0 pts`**<br>(`Holds`) |

---

## Card 6 (`6 / 7` · `LATENCY`) — Batching / Scaling Latency

### **Hook 开销与执行超时水位：FAF 未标记提示词仅增 `0.93s–1.00s` 开销；AGENT-FORGE 静态模板 `~120ms` 对比 LLM 修复 `30,000ms` 上限**

| 负载与执行层级 (Load / Execution Tier) | 主路径 / 优化路径 (`#3B82F6`) | 基线 / 上限路径 (`#CBD5E1`) | 源码与实测说明 |
| --- | --- | --- | --- |
| **Tier 1 · FAF `UserPromptSubmit` Hook**<br>(Unmarked Prompt Fast-Exit on Windows) | **`930 ms`** (均值 `0.93s`) | **`1,190 ms`** (最大观测值 `1.19s`，范围 `0.70–1.19s`) | 源自 `README-faf-token-benchmark.md` Windows 5 次无标记运行实测 |
| **Tier 2 · FAF `Stop` Hook**<br>(Unmarked Prompt Fast-Exit on Windows) | **`1,000 ms`** (均值 `1.00s`) | **`1,340 ms`** (最大观测值 `1.34s`，范围 `0.86–1.34s`) | 源自 `README-faf-token-benchmark.md` Windows 5 次无标记运行实测 |
| **Tier 3 · FAF Hook Timeout vs. Recovery Wait**<br>(`hooks.json` vs. `faf_benchmark.py recover`) | **`5,000 ms`** (`timeoutSec: 5` 同步钩子上限) | **`15,000 ms`** (`--wait-seconds 15` 后台分离回收窗口) | 源自 `src/core/hooks.json` 与 `faf_benchmark.py` |
| **Tier 4 · AGENT-FORGE Init Path vs. LLM Fix Timeout**<br>(`--mode templates` vs. `callLlmForJson`) | **`120 ms`** (`~0.12s` 本地静态模板拷贝，0 LLM 调用) | **`30,000 ms`** (`validator.ts:48` 单次 LLM JSON 修复超时) | 源自 `src/lib/gallery.ts` 与 `src/lib/validator.ts` |

---

## Card 7 (`7 / 7` · `MY TAKE`) — Good Fit vs Not For & Readiness

### **结论与适用边界：用 FAF 打通“从客户立项到 Azure/Fabric 架构落地”，用 AGENT-FORGE 自动化“代码库 `.github/` 上下文工程”**

#### ✅ Good Fit（强烈推荐场景）
- **使用 FAF (`customer-success-microsoft/faf-agents`)**：
  - 交付 **Azure AI Foundry / OpenAI 智能体应用** 或 **Microsoft Fabric（RTI / Medallion 数据仓库迁移）** 客户项目；
  - 需要用 **8 域加权评分卡（`>70%` vs `<40%`）** 客观决策复用哪个 Solution Accelerator 还是从零开发；
  - 需要用 **11 维模型评分卡（含 6 个月退役红线）**、实时 Azure 零售价格 API 与 `docx/pptx/xlsx/drawio` 技能直接产出客户可交付物；
  - 需要用 `faf_benchmark.py` 零额外成本统计团队每个阶段的 Token 与 AI Credits 消耗。
- **使用 AGENT-FORGE (`microsoft/agent-forge`)**：
  - 为**任意语言/技术栈（TS/Python/Go/Rust/Java/.NET 等）**的新老代码仓库一键生成规范的 `.github/agents/`、`prompts/`、`instructions/`、`skills/`、`hooks/` 与 `.vscode/mcp.json`；
  - 在 CI 或本地使用 `forge validate` 与 `forge audit` 执行确定性 Schema 修复、44 工具名拼写纠错与 Handoff 断链检查。

#### ⛔ Not For（不适用场景与反模式）
- **不要把 `microsoft/agent-forge` 当成行业解决方案加速器**：它不包含任何 Azure Bicep 模板、客户 PRD/C4 架构规范或业务立项评分卡。
- **不要指望 FAF 自动为非微软技术栈生成通用 `.github/hooks` 校验器**：FAF 强绑定 Azure 与 Microsoft Fabric 交付实践。
- **切勿在升级 FAF 插件时仅在 VS Code UI 中重装**：必须关闭 VS Code 并手动删除 `%APPDATA%\Code\agentPlugins\github.com\customer-success-microsoft\faf-agents` 缓存目录。

#### 🛡️ Readiness, License & Provenance Card
- **就绪度评级**：
  - `faf-core@2.1.1` + `faf-genai@2.1.0`：**Production-Ready (GA)**（6 个角色 Agent + 53 个 Benchmark 单元测试）
  - `faf-analytics@1.0.1`：**Scoped v1.0 Release**（`plugin.json` 注册 6 个 Agent，v1.0 黄金测试门禁聚焦 Analyst + Architect 的 Fabric RTI 与 DW 迁移场景）
  - `@agent-forge-copilot/cli@0.3.0`：**Public CLI Beta/Preview**（确定性校验器与合并器完备，生成流水线依赖本地 `copilot` CLI）
- **许可证**：两座仓库均采用 **MIT License**（FAF 内置的 `docx`/`pptx`/`xlsx`/`pdf` 技能包含源自 Anthropic Claude Code Skills 的许可声明）。
