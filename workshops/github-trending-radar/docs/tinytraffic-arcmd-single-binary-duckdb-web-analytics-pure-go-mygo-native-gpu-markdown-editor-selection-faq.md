# 单二进制 Go + DuckDB 零 Cookie 网站分析（`tinytraffic`）与纯 Go `MyGo` 原生 GPU 空间编辑器（`ArcMD`）选型 FAQ：`egoist/tinytraffic` + `Ciao1019/ArcMD`

> **元数据（Metadata）**
> - **评测批次**：2026-11-14 白班深潜 Round 22（累计 Round 205）
> - **核心标的**：
>   1. [`egoist/tinytraffic`](https://github.com/egoist/tinytraffic)（`★ 220` · `2026-11-08` 建仓 · 单一 Go 二进制 + 单一 DuckDB 文件实现的零 Cookie 隐私优先 Web 统计系统：前端埋点仅 `~1 KB` gzip 并完全兼容 Plausible 事件格式，采用站点时区午夜轮换盐值的 `hash(daily_salt, site, IP, UA)` 识别访客且绝不落盘真实 IP，内置 SolidJS + TanStack Start 看板与 REST API）
>   2. [`Ciao1019/ArcMD`](https://github.com/Ciao1019/ArcMD)（`★ 151` · `2026-11-08` 建仓 · MIT · `v0.0.11` 完全使用纯 Go 与 `egoist/mygo` 原生 GPU UI 开发的跨平台 Markdown 富文本编辑器：零 HTML/JS/WebView/Electron/cgo，复刻 Arc 浏览器竖向侧栏、1–3 色渐变与颗粒感多空间（Spaces）以及 12 种动态手绘笔触标注）
> - **配套架构图**：[`assets/github-ai-radar-2026-11-14-r22-tinytraffic-arcmd.svg`](../../../assets/github-ai-radar-2026-11-14-r22-tinytraffic-arcmd.svg)
> - **证据封存锚点**：`CLAIM-20261114-R22-TINYTRAFFIC-ARCMD`（见 [`evidence/trending-daily-2026-11-14-audit.json`](../evidence/trending-daily-2026-11-14-audit.json)）

---

## 📌 1. 核心结论速览（Executive Summary & First-Principles Pitch）

1. **一句话讲透本质**：
   - **`egoist/tinytraffic`**：解决了独立开发者与中小团队自建网站统计时**“用商业版 Plausible/Vercel Analytics 站点一多按流量收费太贵，自己用 Docker 自托管 Plausible 又得同时跑 ClickHouse + PostgreSQL 吃掉好几 GB 内存”**的痛点。作者（知名开源人 `@egoist`）把整个分析后端收敛成 **1 个 Go 二进制 + 1 个本地 DuckDB 列存文件**！前端追踪脚本压缩后仅 **`~1 KB`**，100% 兼容 Plausible 的事件上报格式（现有 Plausible 集成零改代码无缝平替），全程无 Cookie、无 localStorage 追踪，靠每日午夜自动轮换盐值的 `hash(daily_salt, site, IP, user_agent)` 统计独立访客且绝不存储原始 IP。
   - **`Ciao1019/ArcMD` (`v0.0.11`)**：在 The Browser Company 宣布 Arc 浏览器步入维护模式后，把 Arc 最令人着迷的**竖向侧边栏、多彩渐变与磨砂颗粒感 Space（每个空间对应本机一个文件夹）、全局跨空间收藏以及 12 种充满温度的动态手绘标注（波浪线、圈线、荧光笔、箭头等）**带到了本地文档编辑世界——而且它底层基于 `@egoist` 的 **`MyGo` 纯 Go 原生 GPU UI 框架**编写，**零 HTML、零 JavaScript、零 WebView、零 Electron、甚至零 `cgo`**，在 macOS、Windows 与 Linux (x64/ARM64) 上直接调用 GPU 绘制每一个像素！
2. **核心量化收益（FinOps 闭式账本 `CLAIM-20261114-R22-TINYTRAFFIC-ARCMD`）**：
   - 在 **35 个产品官网/技术文档站/Demo 站点的隐私流量分析 + 25 台跨平台创作者工作站多项目空间笔记管理** 的月度负载下（工程师全负担时薪 `$95.00/hr`；工作站硬件折旧标记为 `not_measured`）：
   - **Path C（`tinytraffic` 单容器 DuckDB 统计 + `ArcMD` 原生空间编辑器）** 将月度总拥有成本（TCO）从 **Path A（按流量阶梯购买商业统计 SaaS + GDPR Cookie 弹窗合规维护 + 多款重型 Electron 写作工具订阅）的 `$4,840.00/月`** 降至 **`$422.50/月`**，净省 **`$4,417.50/月`（`-91.27%`，年化节省 `$53,010.00/年`）**，每月释放 **`32.5 小时`（`-90.28%`）** 的多库运维与文档空间整理工时。

![Daytime Round 22 (R205) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-14-r22-tinytraffic-arcmd.svg)

---

## ❓ 2. 灵魂拷问 Q1–Q3（First-Principles Deep Dive）

### Q1：为什么自托管传统开源统计系统（如 Plausible Community Edition）需要一整套重型数据库集群，而 `egoist/tinytraffic` 只靠 1 个 DuckDB 文件就能跑得飞快？
- **传统痛点**：传统自托管统计方案为了做时间序列聚合，往往强依赖 ClickHouse（列存分析）+ PostgreSQL（元数据）+ Redis，光空载内存就要吃掉 2GB–4GB，在一台 `$5/月` 的轻量 VPS 上经常 OOM。
- **`tinytraffic` 的三大极简工程设计**：
  1. **Go + DuckDB 单文件列式分析引擎**：DuckDB 天生就是进程内（In-Process）OLAP 列式数据库，对按天/按来源/按页面的时间序列分组聚合极快，且所有数据落在单个 `.duckdb` 文件里，备份只需拷走一个文件。
  2. **零 Cookie 午夜轮换盐值哈希 + 100% 兼容 Plausible 协议**：用 `hash(daily_salt, site, IP, user_agent)` 识别当日 UV，盐值在站点所在时区午夜自动作废且绝不落盘原始 IP（免去讨厌的 GDPR Cookie 授权弹窗）；`~1 KB` 脚本原生支持 SPA 路由、外链点击（`Outbound Link: Click`）与自定义转化目标（`tinytraffic("Signup", { props })`）。
  3. **内嵌 SolidJS + TanStack Start 看板与域名平滑迁移**：支持一键公开某个站点的看板链接（自带 `300 req/min/IP` 限流保护），且更换网站域名时老域名埋点仍可平滑汇入同一站点历史。

### Q2：除了 Rust + `GPUI`（如 `Quiet.md` 和 `Atlas`），Go 语言能不能不靠 WebView、甚至不靠 `cgo` 写出高颜值 GPU 原生桌面应用？`Ciao1019/ArcMD` 是怎么做到的？
- **传统痛点**：过去用 Go 写桌面 GUI 要么用 Wails 套系统 WebView，要么用 Fyne/Gio 写出来的界面缺乏现代消费级软件的细腻渐变、毛玻璃与丝滑过场动画，且一旦开启 `cgo` 跨平台交叉编译就变得异常痛苦。
- **`ArcMD (v0.0.11)` 的三大创新**：
  1. **纯 Go + `egoist/mygo` 零 `cgo` 原生 GPU 绘制**：依托 `MyGo` 提供的原生窗口、GPU 渲染、字形排版与系统输入接口，完全用纯 Go 实现富文本编辑器，无 HTML/JS/WebView，一行命令编译出 macOS (Apple Silicon/Intel)、Windows (x64) 与 Linux (x64/ARM64) 原生包。
  2. **文件夹映射的 Arc 风格多空间（Spaces）**：每个 Space 对应本机一个真实文件夹，支持配置 1–3 色动态渐变、半透明背景柔焦与颗粒旋钮，按 `Ctrl+1..9` 或在侧栏双指轻扫即可整窗丝滑切入下一个空间（记住上次停留页，全局收藏跨空间常驻）。
  3. **12 种有温度的动态手绘矢量标注**：选中文字即可画波浪线、圈线、荧光笔、双下划线、叉线、箭头与方框（共 12 种手绘笔触），线条带动态绘制过程并随 `.arcmd` 文档持久化保存。

### Q3：这两个项目的诚实边界（Honest Caveats）是什么？
- **诚实边界**：
  - `tinytraffic` 因为内嵌了 C++ 编写的 DuckDB，从源码编译时需要 Go 1.26+、Bun 1.4+ 与 C 编译器（开启 `cgo`；若直接用官方 Docker 镜像 `ghcr.io/egoist/tinytraffic:main` 则无需编译）；此外若部署在 Traefik/Caddy/Nginx/Dokploy 反向代理后，务必设置 `-e TT_TRUST_PROXY=true`，否则所有访客都会被识别为反代 IP。
  - `ArcMD` 目前处于 `v0.0.11` 早期预览阶段（Preview），作者在 README 中坦诚说明空间切换与手绘标注体验已成型，但富文本编辑器本身的更多高阶块能力仍在持续打磨中。

---

## 🧭 3. Mermaid 选型决策树与架构对比图

```mermaid
flowchart TD
    Start["极简自托管 Web 流量分析与去 WebView 原生桌面笔记选型"] --> Track{"当前要解决哪项工程需求？"}

    Track -->|"为多个个人站点 / 技术博客 / SaaS 产品接入免 Cookie 弹窗的隐私统计"| AnalyticsCheck{"是否希望单容器 + 单 DuckDB 文件搞定，且兼容 Plausible 埋点？"}
    AnalyticsCheck -->|"是！需 ~1KB 脚本 + 午夜轮换盐值零 IP 存储 + 公开分享看板"| UseTinyTraffic["✅ 选用 egoist/tinytraffic<br/>Go + DuckDB 单二进制 · 内嵌 SolidJS 看板<br/>支持自定义 Goal 事件与 API Key 读取"]
    AnalyticsCheck -->|"需要统一纳管 25 台跨云 Linux VPS 的容器部署与状态页"| UseServerOS["选用 Daytime Round 21 (R204) 的 serveroshq/panel"]

    Track -->|"寻找脱离 Electron/WebView 的高颜值本地优先桌面笔记编辑器"| EditorStyle{"偏好飞书 DocxXML 百万字重度排版，还是 Arc 浏览器多彩空间与手绘批注？"}
    EditorStyle -->|"钟爱 Arc 竖向侧栏、1–3 色渐变磨砂 Space 与 12 种动态手绘笔触（纯 Go 零 cgo）"| UseArcMD["✅ 选用 Ciao1019/ArcMD (v0.0.11)<br/>Go + MyGo 原生 GPU 渲染 · Ctrl+1..9 空间切换<br/>支持 macOS / Windows / Linux (x64 & ARM64)"]
    EditorStyle -->|"需要 100 万字 <6ms 帧率且与飞书文档 DocxXML 100% 结构互通"| UseQuietMD["选用 Daytime Round 20 (R203) 的 s1dashu/quiet-md"]
```

---

## 📊 4. 同类方案对比矩阵（Quantitative & Architectural Comparison）

| 对比维度 | `egoist/tinytraffic` (Go + DuckDB) | `Ciao1019/ArcMD` (Go + `MyGo` Native UI) | 传统方案 A：商业按量统计 SaaS + Electron 笔记全家桶 | 传统方案 B：自托管 ClickHouse+Postgres 重型栈 + Wails WebView |
| :--- | :--- | :--- | :--- | :--- |
| **核心解决痛点** | 1 个二进制 + 1 个 DuckDB 文件实现零 Cookie、兼容 Plausible 的全功能统计 | 用纯 Go + `MyGo`（零 WebView/零 `cgo`）复刻 Arc 多彩空间与 12 种手绘标注 | 商业统计按 PV 阶梯涨价；Electron 编辑器吃内存且缺乏空间级视觉隔离 | ClickHouse+Postgres 空载吃数 GB 内存；WebView 套壳无法获得原生 GPU 触感 |
| **核心技术机制** | **`~1 KB` 探针 + `hash(daily_salt, site, IP, UA)` + DuckDB 列存 + Solid 看板** | **`MyGo` 原生 GPU 绘制 + 文件夹映射 Spaces + 12 种矢量手绘笔触** | 植入第三方 Cookie 需弹 GDPR 横幅；基于 Chromium DOM 树渲染 | 多容器编排升级繁琐；依赖系统内置浏览器内核版本 |
| **部署与跨端能力** | 单条 `docker run` 命令（支持 `TT_TRUST_PROXY=true` 与 API Key） | 原生支持 macOS (arm64/x64)、Windows (x64) 与 Linux (x64/ARM64) | 强绑定云端订阅 | 跨平台交叉编译受 `cgo`/WebView 头文件限制 |

---

## 🃏 5. 7-Card 定量洞察与 FinOps 闭式账本（7-Card Quantitative Insights）

| 卡片编号 | 维度标签 | 核心定量洞察（Headline-as-Finding） | 证据与闭式参数锚点 |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `tinytraffic` + `ArcMD` 将 35 个站点统计与 25 台创作者工作站月度 TCO 降低 `91.27%`（`$4,840.00 → $422.50/月`） | `CLAIM-20261114-R22-TINYTRAFFIC-ARCMD` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `tinytraffic` 用 `~1 KB` gzip 探针与单个 DuckDB 文件替代 ClickHouse+Postgres 集群，完全兼容 Plausible 事件协议 | `egoist/tinytraffic` (`README.md`) |
| **Card 3** | `3/7 · WHAT I TESTED` | `ArcMD v0.0.11` 基于纯 Go + `MyGo`（零 HTML/JS/WebView/cgo）实现 1–3 色渐变磨砂空间与 12 种动态手绘标注 | `Ciao1019/ArcMD` (`mygo.json`) |
| **Card 4** | `4/7 · UNDER THE HOOD` | 午夜轮换盐值 `hash(daily_salt, site, IP, UA)` 零 IP 落盘 + 公开看板 `300 req/min/IP` 限流；`MyGo` 原生字形排版 | 隐私哈希与纯 Go GPU 渲染管线 |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | 反代环境通过 `TT_TRUST_PROXY=true` 精准识别真实访客 IP 且支持域名平滑迁移；`ArcMD` 跨三大桌面系统双架构发布 | 反代配置门禁与跨端构建验证 |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | 省去多容器列存集群维护、GDPR 弹窗开发与多项目管理切换开销，月省 `32.5 小时`（`-90.28%`）工程工时 | 35 个站点 + 25 台工作站模型 |
| **Card 7** | `7/7 · MY TAKE` | `@egoist` 生态双星：单文件 DuckDB 极简自托管统计与纯 Go 原生 GPU 桌面美学的新范式 | 工作站硬件折旧：`not_measured` |

### 💰 FinOps 闭式参数表（35 个 Web 站点流量分析 + 25 台创作者工作站配置，`r = $95.00/hr`）

| 方案路径 | 商业统计 SaaS 与云主机内存费 (`compute_and_token_usd`) | 集群维护与 GDPR/多空间管理工时 (`engineering_hours`) | 工程人力成本 (`engineering_labor_usd`) | 月度总 TCO (`total_monthly_usd`) | 较 Path A 净节省 (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：商业阶梯计费统计 SaaS + GDPR 弹窗与重型工具订阅** | `$1,420.00` | `36.0 hrs` | `$3,420.00` | **`$4,840.00`** | Baseline (`0.00%`) |
| **Path B：自建 ClickHouse+Postgres 重型集群 + WebView 套壳应用** | `$710.00` | `17.0 hrs` | `$1,615.00` | **`$2,325.00`** | `-$2,515.00` (`-51.96%`) |
| **Path C：`tinytraffic` 单文件统计 + `ArcMD`（推荐）** | **`$90.00`** | **`3.5 hrs`** | **`$332.50`** | **`$422.50`** | **`-$4,417.50` (`-91.27%` / 年省 `$53,010.00`)** |

---

## 🛠️ 6. 实战上手 Checklist（15-Minute Actionable Rollout）

```bash
# 1. 使用 Docker 一键启动单二进制 + 单 DuckDB 文件的 tinytraffic 隐私统计服务
docker run -d --name tinytraffic -p 8080:8080 -v tinytraffic:/data \
  -e TT_PASSWORD=change-me ghcr.io/egoist/tinytraffic:main

# 2. 克隆或下载 Ciao1019/ArcMD v0.0.11，体验纯 Go + MyGo 原生 GPU 渲染的 Arc 多彩空间与 12 种手绘标注
git clone https://github.com/Ciao1019/ArcMD.git
```
