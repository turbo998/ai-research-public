# 分钟级零前视偏差投研智能体（`jackson-cmd/risk-aware-trading-agents`）与开源金融图表 MCP 组件库（`funnest-xyz/funnest-charts`）架构选型 FAQ

> **文档类型**：AI Solution Architect（AI 解决方案架构师）实战选型指南（六段式标准 FAQ）  
> **所属轮次**：2026-11-17 Night Round 21（Cumulative Round 445 Milestone）  
> **追踪目标**：
> - **`jackson-cmd/risk-aware-trading-agents`**（`★ 220`，Python 3.10+ / PyPI `0.8.0` / MCP / Hugging Face `rta-bench-1`，`MIT`）：按新闻发布的精确分钟重放历史行情、次日开盘撮合且每次回测自动执行前视偏差检查（Look-Ahead Check）的美股投研智能体与基准平台（含匿名盲测 vs 实名、训练截断日前后分离计分、VIX + FOMC/CPI 宏观日历门禁与 `30%` 现金安全垫），并附带同作者期权终端参考架构 **`jackson-cmd/zeus-options-terminal`**（`★ 112`）
> - **`funnest-xyz/funnest-charts`**（`★ 88`，TypeScript / `@funnest/charts-react` / `@funnest/charts-cli` / `@funnest/charts-mcp`，`Apache-2.0`）：免 iframe 原生嵌入、支持图表上直接拖拽改单（Drag-to-Modify Orders）、服务端安全渲染（SSR SVG）且自带 CLI 与 MCP Server 的开源金融看盘与投研图表组件库  
> **计量审计 ID**：`CLAIM-20261117-R21-RISKAWARE-FUNNEST`（底层商业实时行情数据源牌照费标记为 `not_measured`）

---

## 📌 一、核心结论速览（Executive Summary）

1. **为什么企业金融机构与财富管理团队在落地“大模型智能投研（AI Quant / Wealth-Tech）”时，90% 的内部新闻回测都是虚假高收益，且前端看盘组件深陷商业闭源 SDK 锁定？**
   - **投研回测的两大“作弊”假象**：① **日历日对齐导致盘后新闻盘中买（Post-Close Look-Ahead Bias）**：绝大多数开源回测脚本按“日历日期（Calendar Date）”把新闻标题与当日收盘价拼接，导致当天盘后 16:30 发布的财报利好被 Agent 在当天 16:00 收盘价“穿越买入”；② **大模型背诵历史股票代码（Pre-Cutoff Memorization）**：用 2024 年训练完的模型去测 2020–2022 年的实名 `NVDA` / `AAPL`，模型直接靠先验记忆作弊，一上真实未知行情就巨亏。
   - **投研前端的“iframe 割裂与高昂授权费”**：商业专业 K 线图表库（如 TradingView 高级商业版或专有金融图表 SDK）不仅授权费昂贵、强制套在隔离的 `iframe` 里无法跟随宿主设计系统的 CSS 变量，而且 AI Agent 无法直接通过 MCP 协议把策略信号渲染成带持仓/挂单标记的可交互图表或 PNG/SVG 报告。
   - **架构师黄金组合（`risk-aware-trading-agents` MIT + `funnest-charts` Apache-2.0）**：在后端投研与风控执行层部署 **`jackson-cmd/risk-aware-trading-agents`**（新闻按发布精确分钟重放、次日开盘成交、每次运行强制过 Look-Ahead Check、支持股票代码匿名盲测与训练截断日前后分离打分，内置 VIX + FOMC/CPI 宏观风控与 `30%` 现金底线并通过 MCP 暴露）；在前端投顾工作台与报告生成层部署 **`funnest-xyz/funnest-charts`**（免 iframe 原生 `<FnChart />` 支持图表拖拽改单、SSR SVG 组合图表，以及 `@funnest/charts-mcp` 让 Agent 一键把 JSON Spec 渲染成 PNG/SVG/HTML/React 代码）。
2. **闭式 FinOps 量化收益（15 个量化投研与智能投顾席位、每月执行 500 次无前视偏差策略回测并生成 30,000 次客户组合/交易图表视图，量化工程师综合时薪 `$95.00/hr`）**：
   - 从 **Path A（商业量化回测 SaaS + 专有商业金融图表 SDK 席位，`$6,030.00/月`）** 切换至 **Path C（`risk-aware-trading-agents` MIT 零前视偏差引擎 + `funnest-charts` Apache-2.0 原生图表与 MCP，`$370.00/月`）**，每月净省 **`$5,660.00/月`（降幅 `-93.86%`，年化节省 `$67,920.00/年`）**，穿越大数排查、盲测清洗与图表桥接开发工时从 `38.0 小时/月` 降至 `3.0 小时/月`（节省 **`92.11%`**）。

![risk-aware-trading-agents + Funnest Charts Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r21-risk-aware-funnest-charts.svg)

---

## 💬 二、灵魂拷问 Q1–Q3（大白话拆解应用场景与架构本质）

### Q1：`jackson-cmd/risk-aware-trading-agents` 是怎么彻底堵死大模型回测中的“偷看未来新闻”与“背诵历史牛股代码”两大漏洞的？
- **大白话本质定义**：这是一套**“物理上无法偷看未来的美股大模型交易试验场与实盘/模拟盘风控智能体”**（PyPI `0.8.0`，内置英文与 `--lang zh` 中文双语 CLI 与 `:8501` 看板）。
- **四大防作弊与机构级风控机制**：
  1. **分钟级新闻到达 + 次日开盘撮合 + 自动前视检查（Look-Ahead Check）**：新闻严格按发布的精确分钟进入视野，盘后发布的新闻只能触发次日开盘（Next Open）订单；每次执行 `riskaware research run -s swing_trend --period 2022` 时，引擎自动运行确定性的 Look-Ahead Check 并保存完整运行审计记录。
  2. **三段冻结市场 × 匿名盲测（Blind Mode）× 截断日前后分离计分**：内置 **2020 熔断崩盘、2022 熊市、2026 最新行情** 三个标准冻结数据集（Hugging Face `rta-bench-llm-trading-benchmark`），对 Llama、GPT、Claude、Gemini 分别在**隐藏股票真实名称的盲测模式**与实名模式下跑 3 个随机种子，并严格按各模型训练知识截断日（Training Cutoff）前后分开统计得分。
  3. **硬核宏观与仓位风控门禁**：买入前强制检查 VIX 恐慌指数、FOMC 议息 / CPI 通胀 / 非农就业宏观日历、财报窗口期以及多源交叉验证新闻（支持接入免费 SEC 8-K 公告或自有新闻 CSV），并硬性锁定 **`30%` 最低现金安全垫（30% Cash Floor）**。
  4. **原生 MCP Server 与期权扩展参考**：一条命令启动 MCP 服务（`docker run -i --rm ghcr.io/jackson-cmd/risk-aware-trading-agents mcp`），支持 10 家券商模拟盘/实盘；若涉及美股期权 Greeks 与四源双语财经快讯，还可参考同作者的 **`zeus-options-terminal`**（注：Zeus 采用 `PolyForm Noncommercial` 协议，供个人学习与内部架构参考）。

### Q2：为什么财富管理与投研 App 越来越抗拒传统 iframe 图表插件？`funnest-xyz/funnest-charts` 带来了什么架构升级？
- **传统金融图表方案的痛点**：iframe 嵌套的图表无法直接读取宿主 React 应用的字体、背景与暗黑模式 Token，移动端手势（双指缩放、长按十字光标、惯性滚动）经常卡顿，且无法让 AI Agent 直接在对话或自动化日报中生成高颜值金融图表。
- **`funnest-charts`（`Apache-2.0`）的三大核心能力**：
  1. **免 iframe 原生 `<FnChart />` 专业交易画布 + 图表直接拖拽改单**：直接运行在宿主页面 DOM/Canvas 中，原生支持在 K 线上展示实时持仓（Positions）、挂单（Open Orders）与成交点（Fills），并支持鼠标**直接在图表上拖拽修改止盈/止损挂单价格**；通过单一 `Datafeed` 接口即可对接任意券商或内部行情源，且自动适配全球（绿涨红跌）与亚洲/韩国市场（红涨蓝跌）配色习惯。
  2. **SSR 安全的轻量 SVG 投顾看板组件库**：提供 `LineChart`、`AreaChart`、`BarChart`、`CandlestickChart`、`DonutChart`（资产配置环图）、`TreemapChart`（市值涨跌热力树图）与 `PercentageBarChart`（多空权重条），支持服务端无头渲染。
  3. **AI 原生 CLI 与 MCP Server（`@funnest/charts-mcp`）**：执行 `claude mcp add funnest-charts -- npx -y @funnest/charts-mcp` 即可让 Claude Code 或 Cursor 直接调用 MCP 渲染图表，或通过 `npx @funnest/charts-cli render spec.json --out chart.png` 将 JSON 规范一键输出为 PNG、SVG、独立 HTML 或 React `.tsx` 组件代码。

### Q3：企业 AI 架构师如何把 `risk-aware-trading-agents` 与 `funnest-charts` 组装成端到端智能投研工作台？
- **策略验证与信号生成层（后端 MCP）**：Claude / Codex 通过 `risk-aware-trading-agents` MCP Server 查询当日 VIX/FOMC 宏观状态（`riskaware regime`）、交叉验证 SEC 8-K 新闻并运行带前视检查的策略回测；
- **可视化交付与交易交互层（前端 React + 图表 MCP）**：Agent 将回测净值曲线、买卖成交点与行业市值热力图拼装为 JSON Spec，交由 `@funnest/charts-mcp` 渲染为高清投研日报 PNG/SVG，并在 Web 投顾终端通过 `<FnChart />` 呈现可拖拽改单的交互式 K 线。

---

## 🧭 三、端到端集成参考架构与选型决策树（Mermaid）

```mermaid
flowchart LR
    subgraph QuantBackend["零前视偏差投研内核：risk-aware-trading-agents (MIT, PyPI 0.8.0)"]
        A[SEC 8-K / 精确到分钟历史新闻 + 行情] --> B[分钟级重放引擎 + 次日开盘撮合<br/>每次运行强制执行 Look-Ahead Check]
        B --> C[rta-bench-1 评估矩阵<br/>2020/2022/2026 × 匿名盲测 vs 实名 × 截断日前后分离]
        C --> D[实盘/模拟盘风控门禁<br/>VIX + FOMC/CPI 日历 + 财报规避 + 30% 现金安全垫]
        D --> E[riskaware MCP Server]
    end

    subgraph ChartFrontend["原生金融图表与 MCP 交付：funnest-xyz/funnest-charts (Apache-2.0)"]
        E --> F[Claude / 投研 Agent 编排器]
        F -->|@funnest/charts-mcp &amp; CLI| G[一键生成投研报告 PNG / SVG / HTML / React 代码]
        F -->|Datafeed 实时流| H[免 iframe 原生 &lt;FnChart /&gt; 交易画布<br/>持仓/挂单叠加 + 图表直接拖拽改单 + SSR SVG 看板]
    end
```

---

## 📊 四、同赛道方案横向选型对比矩阵（Decision Matrix）

| 评估维度 | 方案 A：商业量化回测 SaaS + 闭源商业金融图表 SDK | 方案 B：自写日历日 Pandas 脚本 + 通用 ECharts 封装 | **方案 C（推荐）：`risk-aware-trading-agents` (MIT) + `funnest-charts` (Apache-2.0)** |
| :--- | :--- | :--- | :--- |
| **防止盘后新闻穿越与代码记忆作弊** | ⚠️ 多数按日度聚合新闻，缺乏针对大模型训练截断日的盲测拆分 | ❌ 日历日对齐极易将 16:30 盘后财报在 16:00 收盘价穿越买入 | ✅ **精确到分钟重放 + 次日开盘撮合 + 自动 Look-Ahead Check + 匿名盲测与截断日分离** |
| **宏观日历与底线仓位风控** | ⚠️ 需额外编写复杂的宏观事件过滤器 | ❌ 纯技术指标容易在 FOMC/CPI 发布日或熊市满仓踏雷 | ✅ **内置 VIX + FOMC/CPI/非农日历检查 + 财报期过滤 + 硬性 `30%` 现金底线** |
| **前端交易图表原生度与拖拽改单** | ⚠️ 商业图表常封装在 iframe 中，定制主题难且按席位/域名高价收费 | ❌ 通用图表库手写 K 线缩放、十字光标与挂单拖拽极易卡顿 | ✅ **免 iframe 原生嵌入、支持图表拖拽改单、内置 SSR SVG 环图/热力树图且 `Apache-2.0` 免费商用** |
| **AI Agent (MCP / CLI) 原生可调用性** | ❌ 闭源黑盒，无官方 MCP 接口 | ❌ 需手动写胶水脚本截图生成报告 | ✅ **前后端均内置标准 MCP Server（`riskaware mcp` + `@funnest/charts-mcp`）与 `/llms.txt`** |
| **月度总拥有成本（TCO，15 席位 / 500 回测 / 3 万视图）** | **`$6,030.00 / 月`**（含 `$2,420` 商业授权 + `38.0h` 穿越审计与桥接） | **`$2,660.00 / 月`**（含 `$950` 算力 + `18.0h` 手写图表交互与清洗） | **`$370.00 / 月`**（**净省 `-93.86%`**，仅 `$85` 容器宿主 + `3.0h` 策略复核） |

---

## 🧮 五、7-Card 定量洞察与闭式 FinOps 核算（`CLAIM-20261117-R21-RISKAWARE-FUNNEST`）

> **核算范围与边界声明**：面向 15 名量化研究员与智能投顾工程师团队，每月执行 **500 次分钟级点对点策略回测并渲染 30,000 次客户资产组合/交易图表视图**（工程师综合时薪 `$95.00/hr`；底层交易所商业实时 Level-1/Level-2 行情牌照费标记为 `not_measured`）：

$$\text{Total Monthly TCO} = \text{Backtest/Charting SDK Spend} + (\text{Look-Ahead Audit \& Chart Integration Hours} \times \$95.00)$$

| 成本构成项 | Path A：商业量化 SaaS + 商业图表 SDK | Path B：自写日度 Pandas + 通用 ECharts | **Path C：`risk-aware` (MIT) + `funnest-charts` (Apache-2.0)** |
| :--- | :---: | :---: | :---: |
| **月度回测平台与金融图表 SDK 授权 / 容器算力费** | `$2,420.00` | `$950.00` | **`$85.00`** |
| **月度前视偏差排查、盲测清洗与图表拖拽交互开发工时** | `38.0 hrs` | `18.0 hrs` | **`3.0 hrs`**（直降 **`92.11%`**） |
| **月度量化与前端工程师人工成本（`@ $95.00/hr`）** | `$3,610.00` | `$1,710.00` | **`$285.00`** |
| **月度总拥有成本（Monthly TCO）** | **`$6,030.00`** | **`$2,660.00`**（`-55.89%`） | **`$370.00`**（**`-93.86%`**） |
| **相对 Path A 净节省（月度 / 年化）** | 基线（`$0.00`） | `$3,370.00 / 月`（`$40,440/年`） | **`$5,660.00 / 月`（`$67,920.00 / 年`）** |

---

## ✅ 六、AI 解决方案架构师实战上手 Checklist（SA Action Checklist）

- [ ] **Step 1 — 部署 `risk-aware-trading-agents` 并跑通三段冻结市场前视检查**：执行 `pip install "risk-aware-trading-agents[dashboard,mcp]"`，运行 `riskaware research run -s swing_trend --period 2022 --lang zh` 验证分钟级新闻回放、次日开盘撮合与自动 Look-Ahead Check。
- [ ] **Step 2 — 强制执行“匿名盲测（Blind Mode）+ 训练截断日前后分离评估”**：在评估任何大模型选股或择时 Agent 时，必须对比隐藏股票代码后的盲测收益与模型训练截断日之后（Post-Cutoff）的样本外表现，并开启 `30%` 现金安全垫。
- [ ] **Step 3 — 在投顾前端集成 `@funnest/charts-react` 免 iframe 图表组件**：通过 `npm i @funnest/charts-react` 引入 `<FnChart />`（对接内部 `Datafeed` 并开启挂单拖拽修改）与 SSR 安全的 `DonutChart` / `TreemapChart`。
- [ ] **Step 4 — 将 `riskaware mcp` 与 `@funnest/charts-mcp` 挂载至投研 Agent**：执行 `claude mcp add funnest-charts -- npx -y @funnest/charts-mcp` 并连接 `ghcr.io/jackson-cmd/risk-aware-trading-agents mcp`，实现从宏观扫描、回测验真到自动渲染 PNG/SVG 投研图表的全链路闭环。
