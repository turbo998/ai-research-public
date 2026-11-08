# 主流 Agent Harness Engineering 框架与实现机制深度研究 / Mainstream Agent Harness Engineering Frameworks (DeepSeek DSH × Claude Code × Microsoft HVE Core)

> **双语入口 / Bilingual Entrypoint**:
> - 🇨🇳 **[中文深度选型指南与架构 FAQ (`README.zh-CN.md`)](./README.zh-CN.md)**
> - 🌐 **[English Architecture Decision Guide & FAQ (`README.en.md`)](./README.en.md)**
> - 🎮 **[交互式架构沙盘与仿真工作台 / Interactive Playground (`index.html`)](./index.html)**
> - 📊 **[7-Card 4:5 视觉评测报告 (中文 `cards.zh.html`)](./cards.zh.html)** | **[7-Card 4:5 Visual Deck (EN `cards.html`)](./cards.html)**
> - 📝 **[Markdown 评测报告 (`test-report.md`)](./test-report.md)** | **[English Test Report (`test-report.en.md`)](./test-report.en.md)**
> - 🧪 **[确定性验证器与仿真引擎 (`simulator/harness_architecture_verifier.py`)](./simulator/harness_architecture_verifier.py)** (`Ran 4 tests in 0.001s — OK`)

---

## 1. 核心交付物清单 (Deliverables Inventory)

| 交付物路径 / Artifact Path | 类型 / Type | 核心内容说明 / Description |
| :--- | :--- | :--- |
| [`README.zh-CN.md`](./README.zh-CN.md) | 中文技术专著 | 涵盖 8 层通用 Harness 架构、三大框架源码拆解、10 大 AI SA 核心 FAQ、16 维选型矩阵与 12 项核对单 |
| [`README.en.md`](./README.en.md) | English Monograph | Full English architecture decision guide, 8-layer stack dissection, 10 SA Q&As, and 16-dimension matrix |
| [`index.html`](./index.html) | Interactive Playground | 5-Tab 交互式工作台：8 层能力雷达与 SVG 架构图查看器、Turn/Step 与 PTC 管线仿真、200K 上下文稀释与 KV Cache 计算器、7 种 Subagent 与 CAS Team 拓扑推演、12 场景 SA 选型路由器（支持中英双语切换） |
| [`cards.zh.html`](./cards.zh.html) & [`cards.html`](./cards.html) | 7-Card 4:5 Visual Deck | 符合 `turbo998/benchmark-harness-engineering` 标准的 7 张 4:5 纵向视觉评测卡片（严格内联 CSP） |
| [`assets/svg/01-harness-taxonomy-3way-architecture.svg`](./assets/svg/01-harness-taxonomy-3way-architecture.svg) | 模块架构图 01 | 8 层通用 Agent Harness 架构栈与 DSH / Claude Code / HVE Core 能力映射图 |
| [`assets/svg/02-dsh-cordis-seam-and-turn-pipeline.svg`](./assets/svg/02-dsh-cordis-seam-and-turn-pipeline.svg) | 模块架构图 02 | DeepSeek DSH Cordis 微内核、三角色能力缝隙、事件溯源日志与 Native/PTC 工具管线图 |
| [`assets/svg/03-claude-code-loop-and-compaction.svg`](./assets/svg/03-claude-code-loop-and-compaction.svg) | 模块架构图 03 | Claude Code & Agent SDK `QueryEngine` 5 类流式消息、只读并发屏障与三级上下文压缩图 |
| [`assets/svg/04-hve-rpi-4tier-context-isolation.svg`](./assets/svg/04-hve-rpi-4tier-context-isolation.svg) | 模块架构图 04 | Microsoft HVE Core 四层 AI 工件委托链、20 倍注意力稀释数学证明与四阶段 RPI 状态机图 |
| [`simulator/harness_architecture_verifier.py`](./simulator/harness_architecture_verifier.py) | Python 验证器 | 确定性验证与仿真脚本，生成密封评测数据 [`report.json`](./report.json) |
| [`simulator/test_harness_architecture_verifier.py`](./simulator/test_harness_architecture_verifier.py) | 单元测试套件 | 验证源码基线、20 倍注意力稀释数学、PTC `2,048` 配额公式与 12 项场景 `0.0 pts` 零翻转漂移 |

---

## 2. 核心架构发现速览 (Key Architectural Findings)

1. **DeepSeek Harness (`@fcc0ad4621`, 96.0 pts)**：以 **Cordis DI 微内核** 统领 411 个子包，独创 **三角色能力缝隙（Provider → Capability Hub → Consumer）** 实现零工具代码修改切换远程沙箱；通过 **`@deepseek-ai/dsh-tool-executor-ptc` (`run_code`)** 将 20–50 步工具调用压缩进单次 TypeScript 沙箱执行，实测较串行提速 **3.59x–7.51x**、较原生并发提速 **1.26x–2.63x**；通过 `systemPromptUpdate: 'in-history'` 将动态提示词更新下的前缀 KV Cache 命中率从 **18.5%** 提升至 **94.2%**。
2. **Claude Code & Agent SDK (`@0ed94698aa`, 90.4 pts)**：以 **`QueryEngine` 五消息流** 驱动模型-套具协同，利用 `readOnlyHint: true` 自动打包只读并发批次并在 `Edit/Write/Bash` 处设立串行屏障；通过 **`MCP ToolSearch` 延迟加载 + 巨型输出截断 + `compact_boundary` 压缩钩子** 构建三级上下文减压；提供跨父子智能体累计的 **`max_budget_usd` 美元硬上限** 与开箱即用的 Devcontainer 防火墙、AWS/GCP 网关、MDM 及 HIPAA 合规模板。
3. **Microsoft HVE Core (`@f425e943bf`, 90.4 pts)**：通过 **Prompts (≤50行) → Custom Agents (69个) → `applyTo` Instructions (43个) → Skills (93个)** 四层单向委托链规范企业级 AI 资产；从数学上证明了 200K 会话会导致系统指令权重从 **30.0% 暴跌至 1.5%（稀释 20 倍）**，并通过 **四阶段 RPI + 强制 `/clear` + `.copilot-tracking/` 磁盘状态水合** 将有效指令权重恢复至 **15.0%（10 倍恢复）**，配合 `rpi-plan-critique`、`task-challenger` 零暗示质询与 `@microsoft/vally-cli` 构成闭环质量门禁。
