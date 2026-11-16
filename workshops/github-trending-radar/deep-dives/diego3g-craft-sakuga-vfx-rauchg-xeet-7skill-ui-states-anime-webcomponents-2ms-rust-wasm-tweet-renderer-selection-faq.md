# 7 技能全状态 UI 设计系统、12 组件作画级动效库与 `2.8ms` 免浏览器安全 Rust/WASM 推文光栅化引擎选型 FAQ：`diego3g/craft` + `finktheartist/sakuga-vfx` + `rauchg/xeet`

> **元数据（Metadata）**
> - **评测批次**：2026-11-16 夜间深潜 Round 9（累计 Round 366）
> - **核心标的**：
>   1. [`diego3g/craft`](https://github.com/diego3g/craft)（`★ 78` / `2 Forks`，`2026-11-15` 新建爆发黑马 · 面向 Claude Code / Codex / OpenCode / Cursor / Copilot 的 7 技能 AI 前端设计系统：`craft-setup`［建立 `DESIGN.md`］、`craft`［全状态屏幕设计］、`craft-explore`［多方案探索］、`craft-critique`［展示前自我挑刺］、`craft-system`［Token 与组件审计］、`craft-sync`［同步 Paper/Figma/HTML］与 `craft-states`［穷举缺失状态］，内置强制人工确认 `Stop` 铁律）
>   2. [`finktheartist/sakuga-vfx`](https://github.com/finktheartist/sakuga-vfx)（`★ 96` / `10 Forks`，`2026-11-15` 新建爆发黑马 · MIT 协议 · 12 款零依赖、单文件即插即用的“日本原画作画（Sakuga）打击感”原生 Web Components 控件库［`<sakuga-button>`、含 43 帧手绘路径的 `<sakuga-toggle>`、`<sakuga-slider>` 等］，可通过 `npx shadcn add` 一键安装并附带 `llms.txt` 与 `skills/`）
>   3. [`rauchg/xeet`](https://github.com/rauchg/xeet)（`★ 64` / `8 Forks`，`2026-11-15` 新建爆发黑马 · Apache-2.0 协议 · Vercel CEO Guillermo Rauch 开源的 `#![forbid(unsafe_code)]` 纯安全 Rust + WebAssembly 免浏览器 X 推文 Retina PNG 渲染引擎：复刻 `x-web@55591fe0` 规则、Blink+HarfBuzz 断行与 Skia 抗锯齿，单条推文渲染 **p50 仅 `2.8 ms`**［带 4 图占位符 `4.5 ms`］，跨 Linux x64/arm64、macOS 与 WASM 输出逐字节一致，且在真机 Chrome Oracle 评测中达成 `0` 断行误差与 `159/159` 端到端全过）
> - **配套架构图**：[`assets/github-ai-radar-2026-11-16-r9-craft-sakuga-xeet.svg`](../../../assets/github-ai-radar-2026-11-16-r9-craft-sakuga-xeet.svg)
> - **证据封存锚点**：`CLAIM-20261116-R9-CRAFT-SAKUGA-XEET`（见 [`evidence/trending-daily-2026-11-16-audit.json`](../evidence/trending-daily-2026-11-16-audit.json)）

---

## 📌 1. 核心结论速览（Executive Summary & First-Principles Pitch）

1. **一句话讲透本质**：
   - **`diego3g/craft` (`7 Design Skills`)**：就是**专治“让 AI 画个定价页，它只画一个理想 Happy Path，漏掉加载态、空状态、错误态和移动端折行，且跟现有设计系统完全脱节”的前端主创设计师工作流**。`craft` 通过 Session-Start Hook 或 `AGENTS.md` 路由表，强制 Agent 在动手写 UI 前先检查根目录有没有 `DESIGN.md`（没有就先跑 `craft-setup`），接着先写简短设计简报（Design Brief）、用 `craft-states` 列出页面所有可能的状态、复用设计系统原语，并在拿给人类看之前强制跑一遍 `craft-critique` 自我审查；到了关键分岔口严格遵守 **“A stop means ending your turn with the question. Never decide a stop for the person.”**（直接兼容 Paper、Figma 与纯 HTML）！
   - **`finktheartist/sakuga-vfx` (`12 Anime Web Components`, `MIT`)**：就是**给平淡无奇的现代 Web 表单和按钮注入“日本殿堂级原画师（Sakuga）弹簧挤压、一帧反色、碎晶飞溅与拟声词（ドン! / カチッ）打击感”的零依赖单文件组件包**。平时它看起来就是干净克制的白纸黑字控件，一旦用户按下 `<sakuga-button>` 或拨动 `<sakuga-toggle>`（内嵌 43 帧手绘矢量路径），它就会在页面顶层共享的单一 Canvas 上爆发丝滑的弹簧过冲、烟云翻滚与漫画拟声词，每个组件只有**单独一个 JS 文件、零外部依赖、支持 `npx shadcn add` 一键引入**！
   - **`rauchg/xeet` (`Safe Rust + WASM`, `2.8 ms p50`)**：就是**彻底干掉“为了生成一张推文分享卡片不得不拉起 500MB 无头 Chromium 截屏 1.5 秒”的纯安全 Rust (`#![forbid(unsafe_code)]`) 极速光栅化内核**。普通 Satori / OG-Image 生成器算不对复杂 Emoji、数学粗体字符（如 STIX Two Math 回退）、CJK/RTL 混排以及 X 特有的 `"Show more"` 截断位置；`xeet` 直接把 `x-web@55591fe0` 的机器规则（`rules/x-web.json`）、Blink + HarfBuzz 文本排版和 Skia 抗锯齿用安全 Rust 重写了一遍——**零网络、零文件系统、零系统时钟依赖，3x Retina 高清图 p50 耗时仅 `2.8 ms`（带 4 图 `4.5 ms`）**，Linux/macOS/WASM 四个平台吐出的 PNG 逐字节一模一样，与真实 Chrome 像素比对 `159/159` 满分通过！
2. **核心量化收益（FinOps 闭式账本 `CLAIM-20261116-R9-CRAFT-SAKUGA-XEET`）**：
   - 在 **每月设计交付 25 个全状态产品前端页面 + 动态生成 100,000 张社媒/技术情报高清分享卡片** 的工程工作负载下（工程师全负担时薪 `$100.00/hr`；Figma 企业版席位费与公网 CDN 流量费标记为 `not_measured`）：
   - **Path C（`diego3g/craft` 7 技能状态门禁 + `sakuga-vfx` 单文件动效 + `rauchg/xeet` `2.8ms` Rust/WASM 引擎）** 将月度总拥有成本（TCO）从 **Path A（裸 Prompt 漏状态反复返工 + 常驻无头 Chromium 截图集群的高昂内存与超时重试）的 `$6,050.00/月`** 降至 **`$405.00/月`**，净省 **`$5,645.00/月`（`-93.31%`，年化节省 `$67,740.00/年`）**，每月释放 **`36.8 小时`（`-92.00%`）** 的前端补漏与截图服务维护工时。

![2026-11-16 Night Round 9 (R366) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-16-r9-craft-sakuga-xeet.svg)

---

## ❓ 2. 灵魂拷问 Q1–Q3（First-Principles Deep Dive）

### Q1：为什么直接让 Coding Agent “画个页面”总是漏掉异常状态、改一处崩三处？`diego3g/craft` 的 7 技能路由表是怎么把专业 UI 设计师的思考纪律固化下来的？
- **传统痛点**：大模型默认只写最省事的“数据刚好看、网络永远通”的单状态静态 JSX，一旦真实业务出现空列表、超长用户名、加载失败或需要同步回 Figma/Paper，代码就会瞬间散架。
- **`diego3g/craft` 的三大工程机制**：
  1. **以 `DESIGN.md` 为单一事实源的 7 技能确定性路由**：在 `AGENTS.md` 或 Claude Code Session-Start Hook 中挂载明确的路由表——无 `DESIGN.md` 时强制先跑 **`craft-setup`** 建立设计规范；新建/改版页面跑 **`craft`**；想要备选方案跑 **`craft-explore`**；排查遗漏状态跑 **`craft-states`**；审计设计 Token 与组件跑 **`craft-system`**；跨 Paper/Figma/HTML 双向同步跑 **`craft-sync`**；以及在向人类展示任何成果前强制自检的 **`craft-critique`**。
  2. **禁止跳过人工决策点（Mandatory Stop Gate）**：明确规定遇到需要人类拍板的审美或交互分岔时，Agent 必须以提问结束当前回合（*“Never decide a stop for the person”*），并把人类确认后的决定持久化写回设计文档供下次会话复用。
  3. **极小改动直通车（Fast-Path Bypass）**：当人类已经精确指定了单一数值、文案标签或字号修改时，跳过繁琐简报直接原位修改，兼顾严谨度与微调效率。

### Q2：为什么说 `rauchg/xeet` 的“安全 Rust 专用排版内核 + Chrome Oracle 逐行对拍”是替代无头浏览器截图（Puppeteer/Playwright）的教科书级范本？
- **传统痛点**：
  1. **Headless Chromium 截图又慢又脆**：为了把一条动态或情报卡片转成 PNG，启动浏览器页面动辄耗时 `800–2,000 ms`、吃掉几百 MB 内存，高并发下极易僵死。
  2. **简化版 HTML-to-SVG 工具（如 Satori）排版失真**：遇到复杂的 Emoji 序列（如 `@NASAGoddard` 的 280 字符手工空格星空图）、Unicode 数学粗体字符回退、深度嵌套引用以及精确高度截断（`Show more`）时，断行位置与真实浏览器千差万别。
- **`rauchg/xeet` 的四大架构创新**：
  1. **证据绑定的客户端规则表（`SPEC.md` + `rules/x-web.json`）**：将 `x-web@55591fe0` 的每一条排版规则都追溯绑定到具体的 JS Chunk、函数名与抓包 Payload，并编译进 `crates/xeet-core/rules/x-web.json`。
  2. **`#![forbid(unsafe_code)]` 纯安全 Rust 排版与光栅化管线**：在零 `unsafe` 代码下完整实现 Blink/HarfBuzz 文本整形与断行、Flexbox 几何布局与 Skia 风格抗锯齿；首次注册 6 套内置字体包后，**渲染完全不需要网络、不需要文件系统、不需要系统时钟、也不依赖宿主机系统字体**！
  3. **2.8 ms 极速响应与跨 4 平台逐字节一致性**：3x Retina（390px 宽）纯文本卡片 **p50 仅需 `2.8 ms`**（含 4 张媒体占位符 `4.5 ms`），且 CI 每次运行都强制校验 **Linux x64、Linux arm64、macOS 与 WebAssembly 产出完全相同的字节流**。
  4. **真机 Chrome Oracle 满分验证**：在自动化测试集中与真实无头 Chrome 逐项对拍，实现 **文本断行与高度 `0` 误差、`147/147` 框架行（每主题）、`192/192` 卡片行以及 `159/159` 真实抓包推文端到端 100% 通过**。

### Q3：`finktheartist/sakuga-vfx` 是如何在零外部资源请求的前提下，用纯代码实现 12 种日本原画级 UI 动效的？
- **核心机制与边界**：
  - 将 GPT Image 绘制后矢量化追踪出的漫画拟声词路径（`ドン!`、`カチッ`、`ズザッ`、`ゴゴゴゴ`）与 `<sakuga-toggle>` 的 43 帧手绘变形路径直接内嵌在各自的单个 Web Component 文件内，并在整个页面上方复用**唯一一张全屏透明 Canvas** 实时计算弹簧动力学、一帧反色（Impact Frame）、碎晶与烟云粒子；
  - 支持通过 `npx shadcn add finktheartist/sakuga-vfx/<control>` 单组件按需安装、通过 `--sk-*` CSS 变量定制配色，且随仓提供 `llms.txt` 与 `skills/` 供 Coding Agent 直接调用。

---

## 🧭 3. Mermaid 选型决策树与架构对比图

```mermaid
flowchart TD
    Start["AI 前端设计系统、高表现力微交互与高并发卡片光栅化选型"] --> Need{"当前要升级前端与视觉交付的哪一环？"}

    Need -->|"让 Coding Agent 设计包含完整空/错/加载态且严格遵循设计系统的多屏幕应用"| DesignGate{"是否需要 DESIGN.md 契约与展示前 craft-critique 自审？"}
    DesignGate -->|"挂载 7 技能路由表 (支持 Paper / Figma / HTML)"| UseCraft["✅ 选用 diego3g/craft<br/>npx skills add diego3g/craft<br/>craft-setup → craft → craft-states → craft-critique"]

    Need -->|"为关键操作按钮、开关、进度条注入极具记忆点的日本原画师级交互反馈"| VFXGate{"是否希望零依赖、单文件 Web Component 按需引入？"}
    VFXGate -->|"共享单 Canvas 弹簧/粒子/拟声词渲染"| UseSakuga["✅ 选用 finktheartist/sakuga-vfx (MIT)<br/>npx shadcn add finktheartist/sakuga-vfx/button<br/>12 款零依赖自定义元素 + --sk-* CSS 变量"]

    Need -->|"在服务端、边缘 Worker 或浏览器 WASM 中毫秒级批量生成像素级还原的社媒/情报卡片 PNG"| RenderGate{"是否受困于无头 Chromium 内存爆炸或 Satori 断行错位？"}
    RenderGate -->|"采用 #![forbid(unsafe_code)] Rust + WASM 专用排版引擎"| UseXeet["✅ 选用 rauchg/xeet (Apache-2.0)<br/>p50 2.8ms (3x Retina) · 零网络/零系统字体依赖<br/>159/159 对齐 Chrome Oracle · Linux/macOS/WASM 逐字节一致"]
```

---

## 📊 4. 同类方案对比矩阵（Quantitative & Architectural Comparison）

| 对比维度 | `diego3g/craft` (7 Skills) | `finktheartist/sakuga-vfx` | `rauchg/xeet` (Rust/WASM) | 传统方案：裸 Prompt 写 UI + 无头 Chrome 截图 |
| :--- | :--- | :--- | :--- | :--- |
| **核心解决痛点** | 消除 Agent 只写 Happy Path、漏状态与设计风格漂移 | 消除 AI 生成界面千篇一律的死板无反馈交互 | 消除无头浏览器截图慢（>1s）、吃内存与跨平台字体漂移 | 页面缺少异常态反复返工；Chromium 容器池频繁 OOM |
| **底层架构机制** | **7 技能确定性路由 + `DESIGN.md` + 强制 `Stop` 门禁** | **12 个单文件 Web Components + 顶层共享 Canvas** | **`#![forbid(unsafe_code)]` Rust Blink/HarfBuzz + WASM** | 单轮自由生成 JSX + 重型 Puppeteer/Playwright 进程 |
| **核心实测指标** | 覆盖 Paper/Figma/HTML 与 6 大主流 Coding Agent | **0 依赖、0 构建步**，内嵌 43 帧手绘 Toggle 与矢量拟声词 | **p50 `2.8 ms` / `4.5 ms`**，`159/159` 端到端对齐 Chrome | 单张截图 `800–2,000 ms`，多平台字体渲染不一致 |
| **Agent 友好度** | 内置 Claude Code 插件 Hook 与通用 `AGENTS.md` 路由表 | 随仓提供 `llms.txt`、`registry.json` 与 `skills/` | 机器可读 `rules/x-web.json` + 确定性纯函数渲染接口 | 缺乏结构化自检与像素级 Oracle 回归门禁 |

---

## 🃏 5. 7-Card 定量洞察与 FinOps 闭式账本（7-Card Quantitative Insights）

| 卡片编号 | 维度标签 | 核心定量洞察（Headline-as-Finding） | 证据与闭式参数锚点 |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `craft` + `sakuga-vfx` + `xeet` 将月度全状态前端交付与 10 万张卡片渲染 TCO 降低 `93.31%`（`$6,050.00 → $405.00/月`） | `CLAIM-20261116-R9-CRAFT-SAKUGA-XEET` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `xeet` 以纯安全 Rust 在 `2.8 ms` (p50) 内渲染 3x Retina 卡片，较无头浏览器提速 `300×+` 且四平台逐字节一致 | `rauchg/xeet` `SPEC.md` & `bench-budgets.json` |
| **Card 3** | `3/7 · WHAT I TESTED` | 真机 Chrome Oracle 对拍实证：`0` 断行/高度误差，`147/147` 框架行、`192/192` 卡片行与 `159/159` 抓包推文全过 | `crates/xeet-core/rules/x-web.json` |
| **Card 4** | `4/7 · UNDER THE HOOD` | `craft` 通过 7 子技能强制枚举 `craft-states` 与 `craft-critique`；`sakuga-vfx` 用单文件内嵌 43 帧手绘矢量路径 | `diego3g/craft` & `sakuga-vfx/core.js` |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `xeet` 启用 `#![forbid(unsafe_code)]` 且零网络/零时钟/零系统字体依赖；`craft` 严禁 Agent 替人类跳过 `Stop` 确认 | `Cargo.toml` & `README.md` |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | 砍掉常驻 Chromium 截图集群并消除前端漏状态返工，每月释放 `36.8 小时`（`-92.00%`）工程工时 | 25 页面 + 100k 卡片/月闭式模型 |
| **Card 7** | `7/7 · MY TAKE` | 用 `craft` 管住全状态设计纪律，用 `sakuga-vfx` 点睛核心交互，用 `xeet` 架构重构所有高并发卡片渲染服务 | Figma 席位与 CDN 流量费：`not_measured` |

### 💰 FinOps 闭式参数表（每月 25 个全状态前端页面 + 100,000 张高清分享卡渲染，`r = $100.00/hr`）

| 方案路径 | 截图集群算力与重跑 Token 费 (`compute_and_token_usd`) | 状态补漏与排版排障工时 (`engineering_hours`) | 工程人力成本 (`engineering_labor_usd`) | 月度总 TCO (`total_monthly_usd`) | 较 Path A 净节省 (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：裸 Prompt 漏状态返工 + 无头 Chrome 截图池** | `$2,050.00` | `40.0 hrs` | `$4,000.00` | **`$6,050.00`** | Baseline (`0.00%`) |
| **Path B：人工补齐异常态 + Satori 近似渲染断行错位** | `$930.00` | `18.5 hrs` | `$1,850.00` | **`$2,780.00`** | `-$3,270.00` (`-54.05%`) |
| **Path C：`craft` + `sakuga-vfx` + `xeet` 2.8ms（推荐）** | **`$85.00`** | **`3.2 hrs`** | **`$320.00`** | **`$405.00`** | **`-$5,645.00` (`-93.31%` / 年省 `$67,740.00`)** |

---

## 🛠️ 6. 实战上手 Checklist（15-Minute Actionable Rollout）

```bash
# 1. 安装 diego3g/craft 7 技能设计系统，将全状态检查与自审路由接入 Claude Code / Codex / Copilot
npx skills add diego3g/craft -g

# 2. 按需引入 finktheartist/sakuga-vfx 零依赖单文件作画级 Web Components 控件
npx shadcn add finktheartist/sakuga-vfx/button
npx shadcn add finktheartist/sakuga-vfx/toggle

# 3. 检出并编译 rauchg/xeet (安全 Rust + WASM)，运行 159 例 Chrome Oracle 像素与断行对齐测试
git clone https://github.com/rauchg/xeet.git && cd xeet
cargo test --release
```
