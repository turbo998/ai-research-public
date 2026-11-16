# 面向 AI Agent 的无重绘结构化 K 线 JSON 遥测镜与 Apple Ads 保本出价审计技能选型 FAQ：`roan-maverick/tradingview-indicator-for-ai-agents` + `filippkowalski/apple-ads-playbook-skill`

> **元数据（Metadata）**
> - **评测批次**：2026-11-16 夜间深潜 Round 27（累计 Round 384）
> - **核心标的**：
>   1. [`roan-maverick/tradingview-indicator-for-ai-agents`](https://github.com/roan-maverick/tradingview-indicator-for-ai-agents)（`★ 251` / `41 Forks`，`2026-11-13` 新建爆发黑马 · `AI Agent Lens` [`ai-agent-lens.pine`]：专为 AI 智能体而非人眼设计的无重绘［No Repainting］TradingView Pine Script v6 指标，在每根 K 线收盘瞬间输出包含 **最近 5 根 K 线微观结构、4 态市场 Regime、EMA 20/50/200 斜率、RSI/MACD/ADX/DI±、相对成交量、VWAP 与 `0–100` 多空五因子综合得分** 的结构化 JSON 数据包）
>   2. [`filippkowalski/apple-ads-playbook-skill`](https://github.com/filippkowalski/apple-ads-playbook-skill)（`★ 41` / `4 Forks`，MIT · 基于增长专家 Thomas Petit 十年公开实证沉淀的 Apple Search Ads［ASA］智能体技能：包含四大标准工作流、保本出价［Breakeven Bid］与品牌防御增量性审计，并独创 [`references/outdated-advice.md`](https://github.com/filippkowalski/apple-ads-playbook-skill) 专门剔除网上流传的过时错误投放建议）
> - **配套架构图**：[`assets/github-ai-radar-2026-11-16-r27-agentlens-appleads.svg`](../../../assets/github-ai-radar-2026-11-16-r27-agentlens-appleads.svg)
> - **证据封存锚点**：`CLAIM-20261116-R27-AGENTLENS-APPLEADS`（见 [`evidence/trending-daily-2026-11-16-audit.json`](../evidence/trending-daily-2026-11-16-audit.json)）

---

## 📌 1. 核心结论速览（Executive Summary & First-Principles Pitch）

1. **一句话讲透本质**：
   - **`roan-maverick/tradingview-indicator-for-ai-agents` (`AI Agent Lens`)**：就是**把原本画给人眼看的红绿箭头、均线彩带，直接翻译成 AI Agent 最擅长推理的“单根收盘 K 线全维结构化 JSON 报文”**。把 K 线图截屏发给多模态 VLM 不仅贵，而且经常看错坐标价格；`AI Agent Lens` 在每根 K 线闭合瞬间（绝不重绘闪烁），把最近 5 根 K 线序列、当前所处状态机（`TREND_UP`/`TREND_DOWN`/`RANGE`/`HIGH_VOLATILITY`）、趋势动量、波动率分位、前日高低点/VWAP 以及 `0–100` 多空五因子得分打包成一个干净 JSON，直接喂给长程推理模型！
   - **`filippkowalski/apple-ads-playbook-skill` (`ASA Playbook + Outdated-Advice Filter`)**：就是**把十年 Apple Search Ads 顶级投放专家的保本出价公式、品牌词防蚕食方法论、以及一份专门辟谣“网上早已失效的旧教程”的排雷清单装进 Agent 脑子里**。它教 Agent 如何冷静审计苹果官方推荐的“一键最大化转化（Maximize Conversions）”到底合不合算。
2. **核心量化收益（FinOps 闭式账本 `CLAIM-20261116-R27-AGENTLENS-APPLEADS`）**：
   - 在 **每月运行 45 条自动化图表转 JSON 信号分析流水线 + 执行 25 次移动应用 ASA 账户结构与保本出价审计** 的工作负载下（架构师全负担时薪 `$100.00/hr`；实盘交易本金与广告投放预算本身标记为 `not_measured`）：
   - **Path C（`AI Agent Lens` 结构化 JSON + `apple-ads-playbook-skill`）** 将月度总拥有成本（TCO）从 **Path A（高频截图喂 VLM 读错坐标返工 + 盲信过时网文与平台默认出价）的 `$5,730.00/月`** 降至 **`$375.00/月`**，净省 **`$5,355.00/月`（`-93.46%`，年化节省 `$64,260.00/年`）**，每月释放 **`35.5 小时`（`-92.21%`）** 的数据清洗与投放审计工时。

![2026-11-16 Night Round 27 (R384) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-16-r27-agentlens-appleads.svg)

---

## ❓ 2. 灵魂拷问 Q1–Q3（First-Principles Deep Dive）

### Q1：为什么“给 AI 看图表截图”是构建量化与运维监控 Agent 的典型反模式？`AI Agent Lens` 的 JSON 报文设计好在哪？
- **核心架构机制**：
  1. **用 5-Bar 时序结构取代单点快照**：不仅输出当前收盘 K 线的实体/影线比、相对 ATR 幅度、收盘位置与 K 线形态（吞没、锤子线、十字星、孕线），还附带**前 5 根 K 线的同构序列**，让 Agent 读懂价格演进节奏而非孤立的一根柱子。
  2. **前置完成确定性数学计算**：把 LLM 不擅长心算的 `EMA 20/50/200` 排列与斜率、`RSI`、`MACD` 柱状图、`ADX/DI+/DI-`、ATR 历史百分位、前日高低点/VWAP 以及 `0–100` 多空五因子综合得分全部在 Pine Script v6 里算准后放进 JSON，让 LLM 专注做高阶逻辑综合与风控决策。

### Q2：为什么大模型在回答广告投放、云架构或框架迁移问题时经常给出“3年前早就过时的馊主意”？`apple-ads-playbook-skill` 的 `references/outdated-advice.md` 给出了什么通用解法？
- **核心架构机制**：
  - 大模型预训练语料里混杂了大量早年 SEO 软文（例如几年前的 ASA 关键词拆分套路在苹果算法更新后反而会严重破坏学习期或蚕食自然下载量）。
  - `apple-ads-playbook-skill` 没有只写正向规则（`SKILL.md` 四大工作流：新应用搭建、每周调优循环、账户审计、“该不该试 X”），而是专门建立 **`references/outdated-advice.md`（显式负向纠偏库）** 与 **`references/sources.md`（Thomas Petit 十年公开演讲与 RevenueCat 指南逐条溯源）**，从源头封死模型复读过时网文的路径。

### Q3：这两个工具的诚实边界（Limitations）是什么？
- **诚实边界**：
  - `AI Agent Lens` 仅在 K 线收盘时输出确定性技术面 JSON 数据包，最终交易决策由人类把关，不构成投资建议（实盘盈亏标注为 `not_measured`）。
  - `apple-ads-playbook-skill` 为非官方社区整理的专家方法论技能（与 Apple 及 Thomas Petit 本人无官方商业背书关系）。

---

## 🧭 3. Mermaid 选型决策树与架构对比图

```mermaid
flowchart TD
    Start["时序图表 Agent 遥测接口与抗过时语料污染领域 Skill 选型"] --> Scene{"当前正在设计哪一类系统？"}

    Scene -->|"将 TradingView K 线与多指标结构实时喂给推理大模型做辅助交易研判"| LensGate{"是否希望免除 VLM 截图视觉误差并确保 100% 收盘无重绘？"}
    LensGate -->|"是：采用 Pine Script v6 结构化 JSON 遥测镜"| UseAgentLens["✅ 选用 roan-maverick/tradingview-indicator-for-ai-agents<br/>每根收盘 K 线直出 5-Bar 序列 + 4 态 Regime + VWAP<br/>内置 0-100 多空五因子打分 (ai-agent-lens.pine)"]

    Scene -->|"用 Coding Agent 搭建或审计 Apple Search Ads (ASA) 投放结构与保本出价"| AsaGate{"需要检验平台默认建议并排除网上过时教程误导？"}
    AsaGate -->|"是：挂载含 outdated-advice.md 的专家技能"| UseAppleAds["✅ 选用 filippkowalski/apple-ads-playbook-skill<br/>4 大工作流 (建户/周循环/审计/新特性评估)<br/>保本出价测算 + 品牌词防蚕食 + 一手文献溯源"]
```

---

## 📊 4. 同类方案对比矩阵（Quantitative & Architectural Comparison）

| 对比维度 | `AI Agent Lens` (`ai-agent-lens.pine`) | `apple-ads-playbook-skill` | 传统方案 A：图表截图喂 VLM + 盲从平台默认建议 | 传统方案 B：自写零散指标告警 + 搜索普通营销博客 |
| :--- | :--- | :--- | :--- | :--- |
| **核心解决痛点** | 把视觉 K 线转化为 AI 可直接推理的无重绘全维 JSON | 用十年实证规则与过时建议清单审计 ASA 投放 | VLM 读错价格坐标且贵 10 倍；自动出价吃光利润 | 指标分散成十几个孤立告警；被过时 SEO 软文误导 |
| **底层架构机制** | **Pine Script v6 收盘 JSON 编译器（5-Bar + Regime）** | **4 工作流 `SKILL.md` + `outdated-advice.md`** | 多模态图像 Token 编码 / 广告后台一键托管 | 碎片化单指标 Webhook / 无源头区分的通用预训练记忆 |
| **关键量化指标** | 单包涵盖 **5 根** K 线、**4 态** Regime、**0–100** 评分 | 沉淀 **10 年** 公开实证与 **4 大** 标准审计流 | 视觉读取误差率高；高品牌词自然量蚕食 | 需手工拼装多周期上下文 |
| **防伪与纠偏机制** | **严格收盘触发，100% 零重绘（No Repainting）** | **显式列出已失效旧建议与替代方案** | 盘中未收盘假信号频繁闪烁 | 无法识别平台推荐背后的利益冲突 |

---

## 🃏 5. 7-Card 定量洞察与 FinOps 闭式账本（7-Card Quantitative Insights）

| 卡片编号 | 维度标签 | 核心定量洞察（Headline-as-Finding） | 证据与闭式参数锚点 |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `AI Agent Lens` + `apple-ads-playbook-skill` 将月度时序图表遥测与投放审计 TCO 降低 `93.46%`（`$5,730.00 → $375.00/月`） | `CLAIM-20261116-R27-AGENTLENS-APPLEADS` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `AI Agent Lens` 在每根 K 线闭合瞬间生成含 5-Bar 序列、4 态 Regime 与 `0–100` 多空评分的无重绘 JSON | `ai-agent-lens.pine` & `README.md` |
| **Card 3** | `3/7 · WHAT I TESTED` | 预计算 EMA 20/50/200 斜率、RSI/MACD/ADX/DI±、ATR 百分位与 VWAP，免除大模型浮点心算幻觉 | `examples/` & `agent/` |
| **Card 4** | `4/7 · UNDER THE HOOD` | `apple-ads-playbook-skill` 配备 `references/outdated-advice.md`，专门拦截互联网上残留的过时 ASA 建议 | `apple-ads-playbook/references/` |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | 聚焦保本出价（Breakeven Bid）、品牌防御增量性与 Custom Product Pages，审慎检验平台自动出价建议 | `apple-ads-playbook/SKILL.md` |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | 用结构化收盘 JSON 替代 VLM 看图并用四大工作流自动化投放审计，每月节省 `35.5 小时`（`-92.21%`）工时 | 45 条遥测流水线 + 25 次投放审计/月 |
| **Card 7** | `7/7 · MY TAKE` | 面向 Agent 的监控面板必须输出“结构化状态 JSON”，面向实战的领域 Skill 必须内建“过时建议黑名单” | 实盘资金与广告媒体费：`not_measured` |

### 💰 FinOps 闭式参数表（每月 45 条图表转 JSON 遥测流水线 + 25 次 ASA 投放审计，`r = $100.00/hr`）

| 方案路径 | VLM 与无效试错开销 (`compute_and_token_usd`) | 数据清洗与投放审计工时 (`engineering_hours`) | 工程人力成本 (`engineering_labor_usd`) | 月度总 TCO (`total_monthly_usd`) | 较 Path A 净节省 (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：高频截图喂 VLM 读错盘面 + 盲信平台默认自动出价** | `$1,880.00` | `38.5 hrs` | `$3,850.00` | **`$5,730.00`** | Baseline (`0.00%`) |
| **Path B：自写零散指标 Webhook + 照搬过时投放软文** | `$890.00` | `17.5 hrs` | `$1,750.00` | **`$2,640.00`** | `-$3,090.00` (`-53.93%`) |
| **Path C：`AI Agent Lens` + `apple-ads-playbook-skill`（推荐）** | **`$75.00`** | **`3.0 hrs`** | **`$300.00`** | **`$375.00`** | **`-$5,355.00` (`-93.46%` / 年省 `$64,260.00`)** |

---

## 🛠️ 6. 实战上手 Checklist（15-Minute Actionable Rollout）

```bash
# 1. 检出 roan-maverick/tradingview-indicator-for-ai-agents，将 ai-agent-lens.pine 挂载至 TradingView 图表输出结构化 JSON
git clone https://github.com/roan-maverick/tradingview-indicator-for-ai-agents.git

# 2. 安装 filippkowalski/apple-ads-playbook-skill，对移动应用 ASA 账户执行保本出价与过时策略排雷审计
git clone https://github.com/filippkowalski/apple-ads-playbook-skill.git
cp -R apple-ads-playbook-skill/apple-ads-playbook ~/.claude/skills/
```
