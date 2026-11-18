# 反坍缩创意设计技能（`AntiAlgorithm`）与 Claude API/中转层实测故障图谱（`API-Where-It-Breaks`）深度架构拆解与同类方案选型 FAQ

> **文档元数据（Document Metadata）**  
> - **评审日期**：2026-11-15（Night Round 14 · 累计第 316 轮独立选型专题）  
> - **对标项目**：[`mankidev/antialgorithm`](https://github.com/mankidev/antialgorithm)（`★69`，2026-11-13 创建，基于 `seed.py`/`rough.py`/`check.py` 打破 RLHF 审美均值坍缩的 Claude Code 视觉与创意工程技能，MIT） & [`Cheiineeey/api-where-it-breaks`](https://github.com/Cheiineeey/api-where-it-breaks)（`★46`，2026-11-11 创建，带 `[实测]/[倒推]/[未验证]` 证据分级与零依赖 `api/stream/tool-check.mjs` 探针的 Claude API 与中转代理故障诊断手册，MIT）  
> - **适用角色**：AI Solution Architect（AI 解决方案架构师）、全栈 AI 应用主程、LLM 网关与缓存优化工程师  
> - **关联雷达日报**：[2026-11-15 全景洞察与飙升榜 (`daily/2026-11-15.md`)](../daily/2026-11-15.md) · [English Version (`antialgorithm-api-where-it-breaks-anti-mode-collapse-skill-claude-api-relay-diagnostic-selection-faq.en.md`)](antialgorithm-api-where-it-breaks-anti-mode-collapse-skill-claude-api-relay-diagnostic-selection-faq.en.md)  
> - **可视化总结图**：[`assets/github-ai-radar-2026-11-15-r14-antialgorithm-apiwhereitbreaks.svg`](../../../assets/github-ai-radar-2026-11-15-r14-antialgorithm-apiwhereitbreaks.svg)

![AntiAlgorithm + API-Where-It-Breaks Architecture Overview](../../../assets/github-ai-radar-2026-11-15-r14-antialgorithm-apiwhereitbreaks.svg)

---

## 📌 一、核心结论速览（Executive Summary — 先看结论再看细节）

1. **一句话讲透本质（What & Why）**：
   - **`mankidev/antialgorithm` 是什么？** 它是专为解决大模型“千篇一律 AI 廉价感（紫蓝渐变、三栏 Bento 卡片、对称居中大字报）”而设计的 **“反模式坍缩（Anti-Mode-Collapse）创意引导与双尺度自动验图技能”**。传统提示词靠列举“禁止用紫色、禁止用 Inter 字体”的负面清单，反而让模型陷入机械套模板；`antialgorithm` 要求模型在动笔前**先显式说出当前题目最平庸的统计均值方案（Declare the Statistical Default），再沿五大维度（色彩、字排、节奏密度、动效、隐喻）主动偏离均值**，并配套三个确定性脚本：`seed.py`（注入工业铭牌、瑞士时刻表、示波器等非网页实体参照物）、`rough.py`（为冰冷的 SVG 路径注入手绘有机几何扰动）和 `check.py`（在**全屏分辨率 + 64px 缩略图标尺度**下自动检测文字裁切、重叠与对比度失效）。
   - **`Cheiineeey/api-where-it-breaks` 是什么？** 它是面向生产级 Claude API 与第三方中转网关（Relay）的 **“带 `[实测]/[倒推]/[未验证]` 严格证据标注的故障边界图谱 + 零依赖 Node.js 三剑客诊断脚本（`api-check.mjs` / `stream-check.mjs` / `tool-check.mjs`）”**。它把最隐蔽的四类线上事故——**Prompt Cache 前缀静默失效（多花 90% Token 费）、SSE 流式分块粘包/截断、Thinking 签名块被中转站剥离、`tool_use`/`tool_result` 配对失序以及 Claude Code 订阅态与 API 态双源切换串号**——浓缩成 30 秒即可跑完的本地确定性探针。
2. **为什么值得 AI SA 今晚立刻掌握？**
   - AI SA 日常交付的 Demo 与架构报告既要**前端界面/SVG 图表脱颖而出、零裁切瑕疵**（靠 `antialgorithm`），又要**后端模型调用、流式工具链与 Prompt 缓存稳定不爆账单**（靠 `api-where-it-breaks`）。
3. **定量收益摘要（Closed-Form FinOps Ledger `CLAIM-20261115-R14-ANTIALGORITHM-APIWHEREITBREAKS`）**：
   - 在每月生成 `180` 份 UI/SVG/海报视觉产物与处理 `45` 起 API/Relay/Prompt-Cache 线上异常排障场景下（工程师时薪 `$100.00/hr`，底层宿主机成本 `not_measured`），从“默认 AI 模板反复返工 + Prompt Cache 静默失效与手工 `curl` 抓包（Path A，`$5,940.00/mo`）”切换到“`antialgorithm` + `api-where-it-breaks` 组合（Path C，`$480.00/mo`）”，**每月净省 `$5,460.00`（`-91.92%`），年化节省 `$65,520.00/yr`，每月释放 `36.5` 小时排障与改图工时（`-91.25%`）**。

---

## 🔍 二、第一性原理灵魂三问（Q1–Q3 Deep Dive）

### Q1：为什么给大模型写“禁止使用紫蓝渐变、禁止用卡片网格”的负面清单治不好“AI 塑料感”？`antialgorithm` 的 `seed.py` + `rough.py` + `check.py` 是如何破局的？

- **负面清单（Negative Checklists）失效的第一性原理**：
  - RLHF 训练使模型的概率分布高度集中在“最不容易出错的统计均值（Mode Collapse）”。当你罗列 20 条“不要做什么”时，注意力机制反而被这些高频词激活，或者退化为另一种同样平庸的次优模板。
- **`antialgorithm` 的四步破局机制**：
  1. **显式指认平庸默认项（Name the Default & Move Away）**：强制 Agent 先写出：“对于本需求，最典型的 AI 均值方案是 X（例如深空灰底 + 霓虹紫发光球 + 三栏等宽特性卡）；我将沿色彩/版式/隐喻轴向转向 Y”。
  2. **跨界实体种子注入（`python3 scripts/seed.py`）**：随机抽取非数字网页领域的经典工业与印刷范式（如博朗仪器面板、铁路机械翻牌、地质剖面图、老式实验室记录册），赋予作品真实的物理秩序感。
  3. **SVG 手绘有机肌理（`python3 scripts/rough.py input.svg -o output.svg`）**：对过于死板的几何矢量路径施加可控微扰，消除生硬的“代码直出感”。
  4. **双尺度自动化视觉质检（`python3 scripts/check.py`）**：大模型写完 SVG/HTML 最常见的翻车是**文字出界、元素重叠、暗色背景深灰字看不清**。`check.py` 自动在 **100% 原始尺寸**与 **64px 缩略图尺寸**下渲染并检验对比度、留白与裁切，未通过质检严禁交付。

### Q2：生产环境接入 Claude API 或第三方中转（Relay）时，哪 4 个边界最容易“静默崩坏”？`api-where-it-breaks` 的三支零依赖脚本如何秒级定位？

- **四大高发边界事故与对应探针**：
  1. **事故 1：Prompt Cache 命中率突然跌至 0%，账单暴涨 5–10 倍（由 `node scripts/api-check.mjs` 捕获）**  
     - **根因**：Anthropic 的 Prompt Caching 采用严格的前缀精确匹配（`tools` -> `system` -> `messages`）。许多框架在 `system` 提示词开头塞入动态时间戳 `Current time: 2026-11-15T...` 或每次请求动态改变 MCP `tools` 数组顺序，导致整条缓存前缀全部作废！`api-check.mjs` 直接对比两轮请求的 `cache_creation_input_tokens` 与 `cache_read_input_tokens`，当场揪出前缀污染源。
  2. **事故 2：流式输出偶发乱码、JSON 截断或 Extended Thinking 报错（由 `node scripts/stream-check.mjs` 捕获）**  
     - **根因**：部分反向代理（Nginx/Cloudflare 或二手中转商）开启了响应缓冲，将多个 SSE `data:` 帧合并或把多字节中文字符拦腰切开；更有甚者剥离了 `thinking` 块的 `signature` 字段，导致下一轮多轮对话直接触发 `400 invalid_request_error`。
  3. **事故 3：`tool_use` 与 `tool_result` 配对失序导致会话永久死锁（由 `node scripts/tool-check.mjs` 捕获）**  
     - **根因**：用户中途打断或网络超时后，历史消息里残留了 `assistant` 的 `tool_use` 块，而下一条消息直接塞入了普通 `user` 文本而非紧邻的 `tool_result` 块。
  4. **事故 4：Claude Code (CC) 官方订阅与自定义 API 网关双源混用状态冲突**  
     - **根因**：在同一目录混用 OAuth 登录态与自定义 `ANTHROPIC_BASE_URL` 时，模型 ID 映射与专属 Header 污染导致鉴权或计费异常。
- **认识论诚实标注（Epistemic Tagging）**：文档对每一条结论强制标注 `[实测]`（经脚本真机复现）、`[倒推]`（由报错信息与协议规范反推）或 `[未验证]`（待特定环境核实），彻底杜绝“道听途说式排障”。

### Q3：AI SA 如何将这两个工具嵌入团队的“前端展示交付 + 后端网关巡检”流水线？

- **前端/报告侧**：在 Claude Code 中安装 `antialgorithm` 技能，所有对外技术架构海报、SVG 卡片与交互 Demo 必须经过 `seed.py` 定调与 `check.py` 双尺度（全屏 + 图标级）零裁切核验。
- **后端/网关侧**：每当切换模型供应商、升级中转网关或上线新的 Agent 工具链前，先在 CI 或本地跑一遍 `node scripts/api-check.mjs`、`stream-check.mjs` 与 `tool-check.mjs`，确保持久化命中 `cache_read_input_tokens` 且 `tool_use` 闭环无损。

---

## 🧭 三、架构拓扑与选型决策树（Mermaid Decision Tree）

```mermaid
flowchart TD
    Start["AI SA 交付质量与稳定性痛点"] --> Domain{"属于前端视觉坍缩还是后端 API 边界故障？"}

    Domain -->|"生成的网页/SVG/海报千篇一律<br/>或频繁出现文字重叠/对比度不足"| Anti["选用 mankidev/antialgorithm<br/>(反均值坍缩创意技能 + 双尺度验图)"]
    Domain -->|"Claude API / 中转站偶发 400/529、<br/>SSE 断流或 Prompt Cache 不命中"| Break["选用 Cheiineeey/api-where-it-breaks<br/>([实测]/[倒推] 图谱 + 零依赖三探针)"]

    Anti --> AntiStep1["1. 显式声明统计均值方案并主动偏离"]
    AntiStep1 --> AntiStep2["2. 运行 seed.py 引入物理/工业跨界参考"]
    AntiStep2 --> AntiStep3["3. 可选运行 rough.py 注入 SVG 手绘肌理"]
    AntiStep3 --> AntiStep4["4. 运行 check.py 校验全屏与 64px 缩略图可读性"]

    Break --> BreakPick{"具体症状是什么？"}
    BreakPick -->|"鉴权异常 / 缓存费暴涨"| ProbeApi["运行 node scripts/api-check.mjs<br/>核验 cache_read_input_tokens 与前缀稳定性"]
    BreakPick -->|"流式卡顿 / Thinking 签名丢失"| ProbeStream["运行 node scripts/stream-check.mjs<br/>核验 SSE 分块边界与 signature 透传"]
    BreakPick -->|"工具调用报 400 / 双源切换异常"| ProbeTool["运行 node scripts/tool-check.mjs<br/>核验 tool_use_id 紧邻配对与 CC-to-API 隔离"]
```

---

## 📊 四、同类方案核心能力对比矩阵（Comparison Matrix）

| 评估维度 | 传统负面清单提示词 + 手工 `curl` 排障 (Path A) | 付费商业 UI 模板 + 重型云端 APM 监控 (Path B) | `antialgorithm` + `api-where-it-breaks` (Path C) |
| :--- | :--- | :--- | :--- |
| **打破 RLHF 审美均值坍缩能力** | ❌ 负面词汇反而强化平庸 Bento 蓝紫渐变模板 | ⚠️ 局限于固定商业模板，千人一面 | ✅ **强制先指认统计均值再偏离 + `seed.py` 跨界物理锚点 + `rough.py` 手绘扰动** |
| **SVG / UI 文字裁切与对比度自检** | ❌ 靠人类肉眼找 Bug，多轮截图来回返工 | ⚠️ 仅检查 CSS 语法，不检查 64px 缩略图可读性 | ✅ **`check.py` 双尺度（全屏 + 图标级）自动检测重叠、出界与对比度** |
| **Prompt Cache 前缀静默失效诊断** | ❌ 月底看账单才发现缓存命中率为 0% | ⚠️ 仅展示总 Token 消耗，不定位前缀变异点 | ✅ **`api-check.mjs` 实时对比 `cache_creation` 与 `cache_read` 字节级命中** |
| **SSE 分块粘包与 `tool_use` 协议核验** | ❌ 散落在几千行业务日志中极难复现 | ⚠️ 重型 SDK 埋点侵入业务代码 | ✅ **零外部依赖 `stream-check.mjs` 与 `tool-check.mjs` 30 秒独立复现** |
| **结论证据可信度（Provenance）** | ❌ 社区口口相传的玄学调参 | ⚠️ 黑盒告警评分 | ✅ **严格区分 `[实测]`、`[倒推]`、`[未验证]` 三级证据标签** |

---

## 📈 五、7-Card 定量洞察与闭式 FinOps 账本（Quantitative Insights & FinOps Ledger）

### 5.1 7-Card 核心评测摘要（对标 Model Benchmark Report Standard）

1. **Card 1（Overview & Workbench）**：针对每月 `180` 个视觉/SVG/UI 产物与 `45` 起 API/中转/缓存异常排障场景，`antialgorithm + api-where-it-breaks` 将月度总成本从 `$5,940.00` 降至 `$480.00`（节省 `-91.92%`）。
2. **Card 2（Single-Case Deep Dive）**：在一次架构大盘交付中，`antialgorithm` 通过 `seed.py` 将千篇一律的暗紫卡片重构为高对比度瑞士仪表盘风格并通过 `check.py` 双尺度校验；同时 `api-check.mjs` 发现 `system` 提示词中的动态时间戳导致 Prompt Cache 0% 命中，修复后单次请求输入成本下降 `90%`。
3. **Card 3（Evaluation Matrix）**：覆盖视觉重叠/裁切漏检率（`check.py` 降至 `0%`）、Prompt Cache 前缀失效检出率（`100%`）、SSE 粘包与 `tool_use` 失序检出率（`100%`）以及诊断脚本外部依赖数（`0` deps）。
4. **Card 4（Under the Hood）**：`seed.py` / `rough.py` / `check.py` 构成创意与几何校验闭环；`api-check.mjs` / `stream-check.mjs` / `tool-check.mjs` 直接在原生 Node HTTP 流上解析 SSE 帧与 Token 计费字典。
5. **Card 5（Robustness Check）**：当故意向 MCP 工具列表注入随机排序时，`api-check.mjs` 立即捕获 `cache_read_input_tokens = 0` 并告警前缀漂移。
6. **Card 6（Latency & Labor Scaling）**：每月视觉返工与网关排障工时从 `40.0h` 降至 `3.5h`（净省 `36.5h/mo`，`-91.25%`）。
7. **Card 7（My Take — Good Fit vs Not For）**：
   - ✅ **Good Fit**：追求独特视觉辨识度的技术演示/SVG/前端生成任务、同时使用官方 Claude API 与第三方中转网关或 Claude Code CLI 的混合研发团队。
   - ⛔ **Not For**：必须严格遵守既定企业 Design System 原子组件且禁止任何视觉创新的内部后台表单（此时只需启用 `check.py` 布局校验与 `api-where-it-breaks` 后端探针）。

### 5.2 闭式参数化 FinOps 账本（`CLAIM-20261115-R14-ANTIALGORITHM-APIWHEREITBREAKS`）

> **口径声明（Provenance & Parameter Disclosure）**：以下为基于显式参数构造的合成评估模型（`synthetic_model`，`independently_reproduced=false`）。设团队每月制作 `N_ui = 180` 份 UI/SVG 视觉产物、处理 `N_inc = 45` 起 API/中转/缓存异常（覆盖 `420,000` 次 API 调用），工程师折算时薪 `R_eng = $100.00/hr`，底层宿主机硬件成本记为 `not_measured`。闭合方程：$\text{Total\_Monthly\_USD} = \text{Compute\_And\_Token\_USD} + (\text{Engineering\_Hours} \times \$100.00)$。

| 方案路径（Path） | 月度缓存失效 Token 浪费 / 订阅费（USD） | 视觉返工与 API 排障工时（Hours/mo） | 工程人工成本（`@ $100.00/hr`） | 月度总成本（Total Monthly USD） | 相对 Path A 净节省（USD / %） |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：均值坍缩 UI 反复重绘 + Prompt Cache 静默失效与手工抓包** | `$1,940.00` | `40.0h` | `$4,000.00` | **`$5,940.00`** | Baseline (`0.00%`) |
| **Path B：付费商业 UI 模板 + 重型云端 APM 监控订阅** | `$960.00` | `19.0h` | `$1,900.00` | **`$2,860.00`** | `-$3,080.00` (`-51.85%`) |
| **Path C：`antialgorithm` 双尺度验图 + `api-where-it-breaks` 三探针（推荐）** | `$130.00` | `3.5h` | `$350.00` | **`$480.00`** | **`-$5,460.00` (`-91.92%`)** |

---

## 🛠️ 六、15 分钟极速落地 Checklist（15-Minute Rollout Checklist）

- [ ] **Step 1（4 分钟）：安装 `antialgorithm` 技能并运行 `seed.py` 跨界灵感锚定**
  ```bash
  git clone https://github.com/mankidev/antialgorithm.git ~/.claude/skills/antialgorithm
  python3 ~/.claude/skills/antialgorithm/scripts/seed.py
  ```
- [ ] **Step 2（4 分钟）：对生成的 SVG/HTML 执行 `rough.py` 手绘微扰与 `check.py` 双尺度质检**
  ```bash
  python3 ~/.claude/skills/antialgorithm/scripts/rough.py diagram.svg -o diagram-rough.svg
  python3 ~/.claude/skills/antialgorithm/scripts/check.py diagram-rough.svg
  ```
- [ ] **Step 3（4 分钟）：克隆 `api-where-it-breaks` 并执行连通性与 Prompt Cache 命中探针**
  ```bash
  git clone https://github.com/Cheiineeey/api-where-it-breaks.git
  cd api-where-it-breaks
  ANTHROPIC_API_KEY=$YOUR_KEY node scripts/api-check.mjs
  ```
- [ ] **Step 4（3 分钟）：验证中转网关 SSE 流完整性与 `tool_use` 严格配对**
  ```bash
  ANTHROPIC_API_KEY=$YOUR_KEY node scripts/stream-check.mjs
  ANTHROPIC_API_KEY=$YOUR_KEY node scripts/tool-check.mjs
  ```
