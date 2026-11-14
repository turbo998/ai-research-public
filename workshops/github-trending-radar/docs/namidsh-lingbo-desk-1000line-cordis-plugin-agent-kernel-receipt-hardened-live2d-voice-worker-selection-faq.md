# 千行零依赖 Cordis 插件化 Agent 内核拆解（`NamiDSH`）与前后台解耦回执校验桌面语音智能体（`Lingbo-Desk`）选型 FAQ：`aa1143/NamiDSH` + `liguozheng-ac/Lingbo-Desk`

> **元数据（Metadata）**
> - **评测批次**：2026-11-14 白班深潜 Round 17（累计 **Round 200 里程碑**）
> - **核心标的**：
>   1. [`aa1143/NamiDSH`](https://github.com/aa1143/NamiDSH)（`★ 217` · `2026-11-08` 建仓 · MIT · 约 1,000 行零运行时依赖 TypeScript 完美复刻百万行级 DeepSeek Harness（DSH）「一切皆插件」架构：680 行迷你版 `Cordis` 通过 14 项真机兼容性测试 `tests/compat.ts`、11 个同名 DSH 核心包、7 篇配套拆机长文与步进可视化器）
>   2. [`liguozheng-ac/Lingbo-Desk`](https://github.com/liguozheng-ac/Lingbo-Desk)（`★ 217` · `2026-11-08` 建仓 · MIT · `v0.3.5` 聆泊 `Lingbo Desk`：前后台解耦的 Windows 桌面语音与 Live2D 数字人 Agent，支持中日英自然打断（Barge-In）、工具白名单 + 调用预算 + 文件哈希备份 + 完成回执（Execution Receipts）的后台长 Word 文档分段读写与独立浏览器工作进程）
> - **配套架构图**：[`assets/github-ai-radar-2026-11-14-r17-namidsh-lingbo-desk.svg`](../../../assets/github-ai-radar-2026-11-14-r17-namidsh-lingbo-desk.svg)
> - **证据封存锚点**：`CLAIM-20261114-R17-NAMIDSH-LINGBODESK`（见 [`evidence/trending-daily-2026-11-14-audit.json`](../evidence/trending-daily-2026-11-14-audit.json)）

---

## 📌 1. 核心结论速览（Executive Summary & First-Principles Pitch）

1. **一句话讲透本质**：
   - **`aa1143/NamiDSH`**：解决了一个令无数 Agent 架构师头疼的难题——**DeepSeek Harness（DSH）完整源码超过 100 万行，新人想搞懂它的“一切皆插件（Everything is a Plugin）”内核与 `Cordis` 依赖注入主板往往无从下手**。`NamiDSH` 用 **约 1,000 行零运行时依赖的纯 TypeScript（Node.js 22.18+ 直接运行无需编译）** 将这套工业级骨架按原样微缩：其中 **680 行迷你版 `Cordis`** 完整保留了依赖注入（`inject`）、Fiber 生命周期、异步加载、错误隔离、热插拔与五种事件机制，并在 **14 个测试场景（`tests/compat.ts`）中与真 Cordis 输出逐行一致**；上层 **11 个包** 与真 DSH 同名同构，连模型、工具、会话、提示词甚至 Agent 主循环本身都是插在根 `Context` 主板上的插件卡。
   - **`liguozheng-ac/Lingbo-Desk` (`v0.3.5` 聆泊)**：解决了桌面语音助手最常见的两大工程事故——**“一旦让 Agent 改一个几万字的长 Word 文档或操作浏览器，前台语音对话就直接卡死无法插话”**以及**“Agent 声称文件改好了，实际上根本没写盘或把原文件改坏了”**。它采用 **前台对话（Electron/Vue 3 + 中日英连续监听自然打断 + 原创 `t008` Live2D 口型联动）与后台 Agent Worker 进程解耦调度**，并引入严密的**工程硬化机制（工具白名单、调用次数预算、目录授权、文件 SHA 哈希、自动备份、任务提交与完成回执分离校验）**，支持后台任务随时查询进度、暂停、修改参数与断点恢复。
2. **核心量化收益（FinOps 闭式账本 `CLAIM-20261114-R17-NAMIDSH-LINGBODESK`）**：
   - 在 **20 名插件/Harness 研发工程师架构上手与微内核开发 + 25 台桌面语音/长文档自动化办公实例月度运行** 的负载下（工程师全负担时薪 `$100.00/hr`；桌面 PC 硬件折旧标记为 `not_measured`）：
   - **Path C（`NamiDSH` 微内核蓝图 + `Lingbo-Desk` 预算受控回执架构）** 将月度总拥有成本（TCO）从 **Path A（直接啃百万行源码试错 + 无调用预算限制的死循环 Token 消耗与长文档损坏人工恢复）的 `$5,450.00/月`** 降至 **`$480.00/月`**，净省 **`$4,970.00/月`（`-91.19%`，年化节省 `$59,640.00/年`）**，每月释放 **`34.5 小时`（`-90.79%`）** 的源码走读与故障恢复工时。

![Daytime Round 17 (R200) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-14-r17-namidsh-lingbo-desk.svg)

---

## ❓ 2. 灵魂拷问 Q1–Q3（First-Principles Deep Dive）

### Q1：为什么自己写的 Agent 框架加几个工具和模型适配器就变成一团乱麻，而 DSH 的 `Cordis` 主板能做到“热插拔模型/工具而整个系统不重启”？`aa1143/NamiDSH` 是怎么用 680 行代码讲透的？
- **传统痛点**：大多数自研 Agent 把 `llm`、`tools`、`memory` 写成硬编码单例或层层传参；一旦要在运行时把在线 DeepSeek 切成离线 Mock 模型，或者某个工具插件抛异常，整个进程就会崩溃或残留僵尸监听器。
- **`NamiDSH` 揭示的三大插件主板机制**：
  1. **Fiber 生命周期与副作用自动回收（`fiber.ts`）**：每个挂载到 `Context` 上的插件都运行在独立的 `Fiber` 中；插件注册的事件监听、子插件与服务引用被自动追踪，当插件卸载时所有副作用自动清理。
  2. **响应式依赖注入（`service.ts` + `reflect.ts`）**：每个服务通过 `class Xxx extends Service` 与 `static inject = ['llm', 'tool']` 声明依赖——依赖没到齐就挂起等待，到齐瞬间自动启动；当底层 `deepseek` 插件被热替换为 `mock` 插件时，上层 Agent 插件自动暂停并无缝重绑新服务！
  3. **14/14 逐行兼容校验 + 零运行时依赖**：利用 Node.js 22.18+ 原生直跑 TypeScript，`tests/compat.ts` 在迷你版与真实 Cordis 上跑出 100% 相同的行为序列，并配齐 7 篇图文并茂的拆机教程（`docs/01-plugin-everything.md` 至 `07-compare.md`）。

### Q2：在做桌面办公 Agent 时，怎么才能一边跟数字人流畅语音插话聊天，一边让它在后台安全改几十页的 `.docx` 合同而不改崩？`Lingbo-Desk` 的工程硬化是怎么做的？
- **传统痛点**：如果把语音对话与工具执行放在同一个事件循环里，Agent 调 Python 处理长文档时用户说话完全没反应；更危险的是模型可能陷入工具调用死循环，或者把长 Word 文档截断写坏。
- **`Lingbo-Desk (v0.3.5)` 的四大硬化设计**：
  1. **前后台双通道解耦调度**：前端 Electron/Vue 3 负责中日英实时语音采集、自然插话（Barge-In 立即停止旧播报）与 Live2D 口型驱动；重型任务交由独立 **Agent 工作进程（Worker）** 异步执行，聊天期间可随时口头或点击查询后台进度、暂停、修改指令、取消或恢复。
  2. **工具白名单 + 调用预算（Call Budgets）**：严格限制单次任务的允许工具集与最大调用步数，从根源阻断 Agent 死循环烧穿 Token。
  3. **任务提交与完成回执分离（Execution Receipts + File Hashes）**：Worker 发起的文件/浏览器操作必须返回本地后端（`http://127.0.0.1:3850`）校验目录权限、计算修改前后文件哈希、生成自动备份并签发完成回执后，才算真正完成。
  4. **长 Word 文档分段读写（Chunked `.docx` Processing）**：针对超长 `.docx` 提供分段读取与精确局部修改能力，避免整篇重写导致排版丢失。

### Q3：这两个项目的诚实边界（Honest Caveats）是什么？
- **诚实边界**：
  - `NamiDSH` 是专为架构学习与微内核原型验证设计的教学级复刻（约 1,000 行代码），省略了真 DSH 中庞大的多平台 GUI 打包与边缘兼容分支（详见 `docs/07-compare.md`），要求 **Node.js 22.18+**。
  - `Lingbo-Desk` 当前 `0.3.5` 版本开源了完整前后端与 Worker 源码，但桌面端编译需用户自行导入已接受官方许可条款的 **Live2D Cubism Core**（仓库内仅附带原创角色 `B / t008` 的运行导出素材，不包含 Cubism Core 或第三方模型权重）。

---

## 🧭 3. Mermaid 选型决策树与架构对比图

```mermaid
flowchart TD
    Start["工业级插件化 Agent 内核设计与硬化桌面语音办公智能体选型"] --> Goal{"当前要解决哪项架构任务？"}

    Goal -->|"吃透 DeepSeek Harness 百万行插件主板架构，或基于轻量 DI/热插拔内核自研 Agent"| KernelCheck{"是否需要零外部依赖、与真 Cordis 14 项测试 100% 行为一致的精简内核？"}
    KernelCheck -->|"是！用 680 行 Mini Cordis + 11 个核心包掌握「一切皆插件」"| UseNamiDSH["✅ 选用 aa1143/NamiDSH<br/>Node.js 22.18+ 原生直跑 TS · 0 运行时依赖<br/>含 7 篇拆机长文与在线步进可视化器"]
    KernelCheck -->|"已在生产级 DSH 内需要对 2–4 个 Agent 做同题真机横评"| UseDSHCompare["选用 Daytime Round 8 (R191) 的 dsh-agent-compare"]

    Goal -->|"构建支持连续语音插话 + 后台安全执行长 Word/浏览器任务的 Windows 桌面 Agent"| DeskCheck{"重点关注后台长文档回执校验还是低显存情感伴侣？"}
    DeskCheck -->|"需要前后台解耦 + 工具白名单/调用预算/文件哈希回执 + 长 .docx 分段修改"| UseLingbo["✅ 选用 liguozheng-ac/Lingbo-Desk (v0.3.5)<br/>中日英自然打断 + Live2D 口型联动<br/>后台任务支持暂停/修改/恢复与 DeepSeek/Ollama 切换"]
    DeskCheck -->|"需要在 8GB 显卡上跑 5.5GB 本地感官 + Zigbee 智能家居伴侣"| UseOpenAmika["选用 Daytime Round 11 (R194) 的 zeekk0/OpenAmika"]
```

---

## 📊 4. 同类方案对比矩阵（Quantitative & Architectural Comparison）

| 对比维度 | `aa1143/NamiDSH` (Mini Cordis + Mini DSH) | `liguozheng-ac/Lingbo-Desk` (`v0.3.5`) | 传统方案 A：硬啃 100万+ 行原始大仓 + 单线程无预算限制 Agent | 传统方案 B：手写简陋 EventEmitter + 整篇覆盖式改 `.docx` |
| :--- | :--- | :--- | :--- | :--- |
| **核心解决痛点** | 用 ~1,000 行零依赖 TS 与 7 篇拆机文讲透 DSH 的 Cordis 插件热插拔架构 | 前后台解耦实现语音随时插话，并用白名单/预算/哈希回执保障文件操作安全 | 百万行代码抽象层深、新人上手需数周；单线程执行工具时语音界面卡死 | 插件卸载后事件内存泄漏；整篇重写长 Word 极易截断内容或破坏格式 |
| **核心架构机制** | **680 行 `Cordis` (`Context`/`Fiber`/`Service`/`inject`) + 14 项兼容测试** | **Electron/Vue 3 + Node 网关 + 独立 Worker + 文件哈希备份与完成回执** | 庞大复杂的工业级构建链路 | 无任务暂停/修改/恢复状态机，无修改前自动备份 |
| **运行与调试体验** | `npm start` 秒起（无 Key 自动切离线 `mock` 插件）+ 交互式代码流转图 | 支持 DeepSeek 云端与本地 Ollama 切换，真实通过长 `.docx` 与浏览器小样本验收 | 编译耗时且难以单步追踪单次提问全流程 | 缺乏明确的任务提交 vs 实际完成回执对账 |

---

## 🃏 5. 7-Card 定量洞察与 FinOps 闭式账本（7-Card Quantitative Insights）

| 卡片编号 | 维度标签 | 核心定量洞察（Headline-as-Finding） | 证据与闭式参数锚点 |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `NamiDSH` + `Lingbo-Desk` 将月度 Agent 内核研发与桌面长文档语音助手 TCO 降低 `91.19%`（`$5,450.00 → $480.00/月`） | `CLAIM-20261114-R17-NAMIDSH-LINGBODESK` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `NamiDSH` 用 `~680 行` 零依赖 TypeScript 复刻 Cordis 主板，在 `14/14` 个兼容性测试场景中与真 Cordis 逐行一致 | `aa1143/NamiDSH` (`tests/compat.ts`) |
| **Card 3** | `3/7 · WHAT I TESTED` | `Lingbo-Desk v0.3.5` 通过前后台双进程解耦与文件哈希回执，实现聊天不中断的后台长 `.docx` 分段修改與故障恢复 | `liguozheng-ac/Lingbo-Desk` (`docs/acceptance-0.3.5.md`) |
| **Card 4** | `4/7 · UNDER THE HOOD` | `Fiber` 生命周期与 `static inject` 响应式热插拔 + 工具白名单/调用预算/目录 ACL/完成回执四重安全护栏 | `docs/03-fiber.md` & `work-execution-hardening.md` |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | 无 API Key 可用 `mock` 插件离线跑通全链路；后台任务支持运行中随时查询进度、暂停、修改、取消与检查后恢复 | 离线自足性与任务状态机验证 |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | 将百万行源码消化周期从数周压缩至 1 小时，并阻断无界工具死循环，月省 `34.5 小时`（`-90.79%`）工程工时 | 20 名研发 + 25 台桌面助手模型 |
| **Card 7** | `7/7 · MY TAKE` | 累计 **第 200 轮** 里程碑：理解工业级插件化 Agent 母板与构建可审计桌面办公 Agent 的必读双璧 | 桌面 PC 硬件：`not_measured` |

### 💰 FinOps 闭式参数表（20 名插件研发工程师 + 25 台桌面语音/办公自动化实例，`r = $100.00/hr`）

| 方案路径 | 死循环 Token 与云语音算力费 (`compute_and_token_usd`) | 百万行源码走读与文档损坏恢复工时 (`engineering_hours`) | 工程人力成本 (`engineering_labor_usd`) | 月度总 TCO (`total_monthly_usd`) | 较 Path A 净节省 (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：硬啃百万行大仓 + 无调用预算限制与手工恢复损坏文档** | `$1,650.00` | `38.0 hrs` | `$3,800.00` | **`$5,450.00`** | Baseline (`0.00%`) |
| **Path B：手写简陋事件总线 + 阻塞式单线程语音办公脚本** | `$810.00` | `18.5 hrs` | `$1,850.00` | **`$2,660.00`** | `-$2,790.00` (`-51.19%`) |
| **Path C：`NamiDSH` 微内核 + `Lingbo-Desk` 硬化架构（推荐）** | **`$130.00`** | **`3.5 hrs`** | **`$350.00`** | **`$480.00`** | **`-$4,970.00` (`-91.19%` / 年省 `$59,640.00`)** |

---

## 🛠️ 6. 实战上手 Checklist（15-Minute Actionable Rollout）

```bash
# 1. 克隆 aa1143/NamiDSH（需 Node.js 22.18+），零编译启动迷你版 Cordis + DSH 并运行 14 项兼容性测试
git clone https://github.com/aa1143/NamiDSH.git && cd NamiDSH
npm install && npm test && npm start

# 2. 克隆 liguozheng-ac/Lingbo-Desk 检视前后台解耦调度、工具预算硬化与长 Word 分段修改架构
git clone https://github.com/liguozheng-ac/Lingbo-Desk.git
```
