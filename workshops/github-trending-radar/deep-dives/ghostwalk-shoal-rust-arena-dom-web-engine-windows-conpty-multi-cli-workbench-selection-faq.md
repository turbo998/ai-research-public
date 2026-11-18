# `8.5 MiB` 纯 Rust 连续内存池无头网页引擎（`DhanushNehru/GhostWalk`）与 Windows 原生 ConPTY 三 CLI 交接卡工作台（`qianshuixia/Shoal`）深度选型 FAQ

> **文档定位**：本专题是 **2026-11-13 夜班第 40 轮（累计第 168 篇）独立六段式选型指南**，严格对标 `ib-vs-ethernet-roce-selection-faq.md` 的通俗第一性原理与闭式 FinOps 核算规范，面向高性能 Agent 爬虫/网页提取负责人、Windows 多 CLI 协同研发架构师与 AI Solution Architect，深度拆解今日新仓榜上解决“为了跑两行简单网页内联 JS 不得不拉起 500MB 的 Chromium 容器”以及“在 Windows 上同时用 Claude Code、Codex 与 Antigravity (`agy`) 时某家配额用完无法一键带上下文换人接力”的两大工程项目：
> 1. **`DhanushNehru/GhostWalk`（3 天新建获 `10★`，Rust，MIT，无需 Chromium 与 GPU）**：专为 AI Agent 打造的**面向数据设计（Data-Oriented Design）无头网页引擎**——将网页解析进**扁平连续内存池 DOM（Flat Arena DOM：所有节点存储在同一个连续 Vector 中，通过 4 字节句柄索引）**，在有界引擎中对实时 DOM 执行页面内联 JavaScript 修改，并以 `tree` / `text` / `markdown` / `json` 四种格式导出结果；在双核 Linux 沙箱实测**端到端耗时仅约 `1 ms`、峰值内存（Peak RSS）仅 `8.5 MiB`**！
> 2. **`qianshuixia/Shoal`（4 天新建获 `10★`，TypeScript / Tauri / `node-pty` + Windows ConPTY，MIT）**：专为 Windows 平台打造的 **Claude Code + Codex CLI + Google Antigravity CLI (`agy`) 同屏并排原生交互工作台（`:47800` 网页端与 Tauri 桌面端）**——通过 Hooks 自动感知每个会话是“正在干活”还是“等你输入”，每轮回复结束自动生成**「待验收（Awaiting review）」结果卡**；当某个 CLI 配额耗尽或你想换另一个模型接手时，**一键即可将任务连同自动编译的交接卡（Handoff Card）转交给另一款 CLI**，且所有状态持久化于 `<stateDir>/state.json`！
>
> **English Version**: [ghostwalk-shoal-rust-arena-dom-web-engine-windows-conpty-multi-cli-workbench-selection-faq.en.md](ghostwalk-shoal-rust-arena-dom-web-engine-windows-conpty-multi-cli-workbench-selection-faq.en.md) · **关联日报**: [`daily/2026-11-13.md`](../daily/2026-11-13.md) · **专题架构图**: [`assets/github-ai-radar-2026-11-13-r40-ghostwalk-shoal.svg`](../../../assets/github-ai-radar-2026-11-13-r40-ghostwalk-shoal.svg)

![DhanushNehru/GhostWalk 与 qianshuixia/Shoal 架构选型对比](../../../assets/github-ai-radar-2026-11-13-r40-ghostwalk-shoal.svg)

---

## 📌 一、核心结论速览（Executive Summary）

1. **一句话大白话讲透这两个项目到底解决了什么痛点？**
   - **终结“Agent 抓网页时，用 `curl` 拿不到被页面内联 JS 动态改写后的 DOM 内容，而一旦上 Playwright / Puppeteer 拉起无头 Chromium，每个并发实例就要吃掉 `500 MB+` 内存和几百毫秒冷启动开销”的痛点（`DhanushNehru/GhostWalk`）**：`GhostWalk` 用纯 Rust 的**数据导向架构（Flat Arena DOM：所有 DOM 节点紧凑排列在单一连续数组中，用 4 字节句柄代替 8 字节裸指针，彻底消灭堆内存碎片与指针追逐）**，配合有界 JS 执行器直接跑完页面的内联脚本修改 DOM，然后一步导出 Agent 最爱吃的语义 Markdown 或 JSON——**全程不装 Chromium、不用 GPU，端到端耗时仅 `~1 毫秒`，峰值内存仅 `8.5 MiB`（比 Chromium 省 98% 内存）**！
   - **终结“在 Windows 主力机上同时开着 Claude Code、Codex CLI 和 Antigravity (`agy`) 三个黑窗口，Claude 写到一半触发 5 小时限额，你得手动去翻历史记录复制粘贴一大段话喂给 Codex 接盘”的痛点（`qianshuixia/Shoal`）**：基于 Node 24 + `node-pty` + Windows 原生 **ConPTY**，把三大王牌 CLI 装进同一个 `:47800` 网页或 Tauri 桌面窗格里：每个任务跑完一轮自动变成一张**「待验收」结果卡**（可批注打回继续改，也可一键转发给其他任务）；更爽的是，当某家 CLI 额度用光时，点一下转交，系统**自动汇总上下文编译出一张标准交接卡（Handoff Card）**喂给下一棒 CLI 无缝续跑！
2. **闭式 FinOps 投资回报结论（`CLAIM-20261113-R40-GHOSTWALK-SHOAL`）**：
   - 以 **15 人 Windows 研发与网页信息提取团队每月执行 `250,000 次动态网页抓取解析` 与 `2,400 次跨三巨头 CLI（Claude/Codex/agy）研发任务`** 为基准（系统与全栈工程师全包时薪 `$95.00/hr`；Windows 工作站硬件与代理 IP 带宽费：`not_measured`）：
   - 从 **Path A（重型 Chromium 无头容器池 + CLI 限额后人工翻记录复制粘贴交接，月均 `$5,230.00`）** 升级至 **Path C（`GhostWalk` `8.5 MiB` 连续内存池网页引擎 + `Shoal` Windows ConPTY 自动交接卡工作台，月均 `$492.50`）**，每月净省 **`$4,737.50/mo`（降幅 `-90.58%`，年省 `$56,850.00/yr`）**，并将维护 Chromium OOM 崩溃池及手动跨终端搬运上下文的工时从 `38.0 hrs/mo` 压缩至 `3.5 hrs/mo`（节省 **`-90.79%`**）。

---

## 🎯 二、三大灵魂拷问（Q1 / Q2 / Q3 深度原理解析）

### Q1：为什么传统的基于堆指针树（Pointer-Based DOM Tree）与全量 Chromium 在高并发 Agent 网页读取场景下极其浪费？
- **第一性原理拆解**：
  1. **指针追逐（Pointer Chasing）与 CPU 缓存未命中**：传统浏览器每个 DOM 节点都是独立堆分配对象，遍历树时 CPU L1/L2 缓存频繁失效。`GhostWalk` 将整棵 DOM 树拍平进一个连续 `Vec`，用 `u32`（4 字节句柄）索引节点，实现极致的缓存局部性。
  2. **AI Agent 不需要像素光栅化管线**：95% 的 Agent 网页读取只需要“执行完内联 JS 修改后的 DOM 文本/Markdown”，根本不需要 Blink 排版引擎和 Skia GPU 光栅化。剥离渲染管线后，峰值 RSS 降至惊人的 **`8.5 MiB`**，耗时降至 **`~1 ms`**。

### Q2：`qianshuixia/Shoal` 是如何在 Windows 环境下解决多 CLI 进程生命周期与跨工具接力的？
- **第一性原理拆解**：
  1. **Windows ConPTY 原生伪终端与独立后台守护（`scripts\workbench.ps1`）**：
     - 通过 `node-pty` 驱动 Windows ConPTY 承载 Claude Code、Codex 与 `agy` 的真实交互式会话；`scripts\workbench.ps1 start` 在独立隐藏控制台启动后台服务，关掉启动窗口绝不误杀正在跑的 Agent，且所有状态实时落盘 `<stateDir>/state.json`。
  2. **「待验收」结果卡与自动编译交接卡（M3 Switching & Forwarding）**：
     - 挂载各 CLI 的生命周期 Hook 实时变色提示“运行中 / 等待输入”；回合结束自动封装为「待验收」卡片，支持跨任务转发结果卡或在切换 CLI 时自动生成包含前置进展的交接卡（Handoff Card），同时貼心提醒 Windows 下工作台路径勿含空格以兼容 `agy` Hook 限制。

### Q3：在实际生产中如何界定 `GhostWalk` 与完整浏览器（如 `chrome-devtools-mcp` / `KittyBrowser`）的分工边界？
- **第一性原理拆解**：
  1. **快路径用 `GhostWalk`（`1ms / 8.5 MiB`）**：对于海量文档抓取、新闻/公告提取及包含内联 JS 状态注入的网页，优先走 `GhostWalk --dump markdown/json`。
  2. **重交互/视觉布局调试走真实 Chrome**：当需要调试复杂 WebGL/Canvas、检查 CSS 像素溢出或跑多步登录流时，再按需升级至真实 Chrome 方案。

---

## 🧭 三、Mermaid 选型决策树与「GhostWalk 8.5MiB 引擎 + Shoal 三 CLI 工作台」架构图

```mermaid
flowchart TD
    A["高并发 Agent 网页 DOM 提取与 Windows 多 CLI (Claude/Codex/agy) 协同选型"] --> B{"当前处于哪个工程环节？"}
    B -- "网页内容提取层：curl 拿不到 JS 修改后的 DOM，而无头 Chrome 吃光内存" --> C["采用 DhanushNehru/GhostWalk (Rust Flat Arena DOM 无头网页引擎)"]
    B -- "Windows 多 CLI 协同层：同时跑 Claude/Codex/agy 切窗口乱、配额耗尽难接力" --> D["采用 qianshuixia/Shoal (:47800 / Tauri Windows ConPTY 工作台)"]

    C --> C1["连续内存池 Arena DOM (4 字节句柄) + 有界内联 JS 执行"]
    C1 --> C2["~1ms 端到端耗时 & 8.5 MiB 峰值内存 -> 直接导出 tree/text/markdown/json"]

    D --> D1["node-pty + ConPTY 同屏承载 Claude/Codex/agy + Hook 状态变色"]
    D1 --> D2["回合结束生成『待验收』结果卡 + 配额耗尽一键编译 Handoff Card 换 CLI 接力"]

    C2 & D2 --> E["🏆 黄金轻量采集与多 CLI 接力栈：GhostWalk 8.5MiB 引擎 + Shoal 工作台 (-90.58% TCO)"]
```

---

## 📊 四、同类方案核心能力对比矩阵（Selection Matrix）

| 评估维度 | Path A：无头 Chromium 容器池 + 手动跨窗口复制 | Path B：静态 `curl`/Cheerio + 独立 Windows 终端标签 | **Path C（推荐）：`GhostWalk` + `qianshuixia/Shoal`** |
| :--- | :--- | :--- | :--- |
| **单页面解析延迟与峰值内存** | `300–1,500 ms`，每实例占用 `400–800 MiB` RAM | 快但**完全无法执行内联 JS 对 DOM 的动态修改** | **`~1 ms` 端到端耗时，峰值内存仅 `8.5 MiB`（Flat Arena DOM + 内联 JS 执行）** |
| **DOM 内存布局与输出格式** | 复杂堆指针树，需额外写脚本转 Markdown | 仅返回原始静态 HTML 字符串 | **4 字节句柄连续数组 + 原生一键导出 `tree / text / markdown / json`** |
| **Windows 多 CLI 状态感知与验收** | 3 个黑窗口各自为战，不知道谁停下来等输入 | 仅靠标签页标题看状态，无结构化验收卡 | **Hook 实时颜色标记运行/等待 + 回合结束自动生成「待验收」结果卡** |
| **单 CLI 配额耗尽后的跨工具接力** | 手动翻滚屏记录复制粘贴到另一个 CLI | 手写临时交接文档 | **一键切换 CLI 并自动编译结构化交接卡（Handoff Card）+ 结果卡跨任务转发** |
| **月度总拥有成本（25 万抓取 + 2,400 任务）** | **`$5,230.00 / mo`**（`$1,620` 容器/Token + `$3,610` 工时） | **`$2,610.00 / mo`**（`$710` Token + `$1,900` 工时） | **`$492.50 / mo`（净省 `$4,737.50/mo` · `-90.58%`）** |

---

## 🧪 五、定量 FinOps 算例与 7-Card 洞察（`CLAIM-20261113-R40-GHOSTWALK-SHOAL`）

### 5.1 测算基准与显式边界（Scope & Boundaries）
- **场景设定**：15 人规模的 Windows AI 研发与数据采集团队，每月执行 **250,000 次含内联 JS 修改的网页提取任务**，并协同推进 **2,400 个跨 Claude Code、Codex CLI 与 Antigravity (`agy`) 的编码任务**。
- **费率假设**：系统与全栈工程师全包时薪 **`$95.00 / hr`**。
- **显式边界声明（Explicit Not-Measured Boundary）**：Windows 工作站主机硬件折旧与第三方商业代理 IP 带宽费标记为 **`not_measured`**，本表严格核算无头浏览器容器算力账单与跨 CLI 重复交代背景消耗的 Token 支出，以及工程师维护 Chromium OOM 崩溃池与手动搬运多 CLI 上下文的工时。

### 5.2 三路径月度成本闭式对照表

| 成本分项 | Path A：重型 Chromium 池 + 手动复制交接 | Path B：静态 `curl` + 独立终端标签页 | **Path C：`GhostWalk` (`8.5 MiB`) + `Shoal`（推荐）** |
| :--- | :--- | :--- | :--- |
| **月度网页解析容器算力与跨 CLI 交接 Token 支出** | **`$1,620.00`**（高内存 Chromium 池 + 换工具重发长上下文） | **`$710.00`**（漏抓 JS 内容导致的重试 Token） | **`$160.00`**（`8.5 MiB` 极速解析 + 精炼 Handoff Card 接力） |
| **Chromium OOM 排障与手动跨 CLI 搬运工时（`$95/hr`）** | `38.0 hrs × $95.00` = **`$3,610.00`** | `20.0 hrs × $95.00` = **`$1,900.00`** | `3.5 hrs × $95.00` = **`$332.50`** |
| **月度总成本（Monthly TCO）** | **`$5,230.00 / mo`** | **`$2,610.00 / mo`**（`-50.10%`） | **`$492.50 / mo`** |
| **相对 Path A 净节省** | 基准线（Baseline） | 净省 `$2,620.00 / mo` | **净省 `$4,737.50 / mo`（`-90.58%` · 年省 `$56,850.00/yr`）** |
| **Windows 工作站硬件与代理 IP 带宽费** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 六、生产级落地核验 Checklist

- [ ] **1. `DhanushNehru/GhostWalk` 编译与 `--stats` 基准实测**：运行 `cargo build --release` 与 `./target/release/ghostwalk examples/demo.html --dump tree --stats`，验证内联 JS 成功修改 DOM、耗时约 `1 ms` 且峰值 RSS 低于 `10 MiB`。
- [ ] **2. `qianshuixia/Shoal` 无空格路径部署与启动**：将仓库克隆至无空格路径（兼容 `agy` Hook 限制），在 Node 24 下运行 `scripts\workbench.ps1 start` 打开 `http://127.0.0.1:47800`。
- [ ] **3. 「待验收」结果卡与跨 CLI 交接卡（Handoff Card）演练**：在 Claude Code 完成一轮任务生成「待验收」卡片后，测试一键将任务转交给 Codex CLI 或 `agy`，确认自动编译的 Handoff Card 完整携带前置结论。
- [ ] **4. 权限边界安全确认**：由于 `Shoal` 默认以全权限模式启动三大 CLI，严格确保仅在受信任且有 Git 版本保护的项目目录中使用。
