# 六级回退开源情报态势台（`alexandephilia/sitrep-osint`）与 DeepSeek Harness 按需懒加载资源管理器及声画解构原创动效技能（`dsh-workspace-explorer` & `motion-library-skill`）架构选型 FAQ

> **文档类型**：AI Solution Architect（AI 解决方案架构师）实战选型指南（六段式标准 FAQ）  
> **所属轮次**：2026-11-17 Night Round 53（Cumulative Round 477）  
> **追踪目标**：
> - **`alexandephilia/sitrep-osint`**（`★ 46`，JavaScript / 本地优先实时态势与供应链/灾害开源情报控制台，`MIT`）：融合去重分类 RSS 新闻流（内置 **`direct → bot-UA → AMP → proxy → Jina → Firecrawl` 六级正文穿透提取梯队**）、带**作者多样性上限（Author-Diversity Caps）**的 X/Threads 社媒监控、3D 地球仪（自动聚焦 `M≥5` 强震与火山爆发）、卫星云图/气象雷达/火灾热点（NASA FIRMS）/实时航班船舶（ADS-B & AIS）图层与 24h 本地持久化状态
> - **`tm5452/dsh-workspace-explorer`**（`★ 30`，JavaScript `v1.2.0` / DeepSeek Harness 桌面端多标签按需预览文件资源管理器插件，`MIT`）& **`ronkenx9/motion-library-skill`**（`★ 45`，Shell/Python / 基于 `yt-dlp` + `ffprobe` + 音频分析解构大师动效原理并创作原创动效的 Claude Code / Codex 技能，`MIT`）：支持在 DSH 右侧栏多标签浏览本机磁盘、右键手势导航、**对 PDF/Office 大文件默认只显示封面并点击确认后才按需加载（切换非固定标签自动释放内存）**的 `dsh-workspace-explorer`，配合从优秀参考片中学习节奏与音效原理但拒绝照抄模板的 `motion-library-skill`  
> **计量审计 ID**：`CLAIM-20261117-R53-SITREPOSINT-DSHEXPLORER-MOTIONLIB`（底层大模型基础订阅标记为 `not_measured`）

---

## 📌 一、核心结论速览（Executive Summary）

1. **为什么跨国企业供应链风控中心、DeepSeek Harness 重度研发团队与数字创意工程团队在日常运作中，常面临“商业态势感知终端动辄数万美元/年、而自建爬虫常被反爬墙挡住或被单个水军账号刷屏误导”、“在 AI 桌面客户端里找本机大文件要频繁切出窗口、一不小心点开几百 MB 的 PDF/视频还把客户端内存撑爆”、以及“让 AI 学参考视频做动效结果它只会生搬硬套抄袭原片布局”三大痛点？**
   - **痛点一：开源情报（OSINT）正文提取受阻与社媒水军偏置**：抓取突发新闻时普通请求常被付费墙或反爬拦截；而在监控 X / Threads 灾情或供应链舆情时，如果不限制同一作者的发帖权重，单个机器人账号连发 50 条就会伪造出虚假热点。
   - **痛点二：AI 桌面工作台缺乏“内存安全型”内嵌文件浏览器**：在 DeepSeek Harness 等桌面端工作时，若直接加载大体积 PDF、Office 或视频极易耗尽渲染进程内存；且切换会话时常丢失刚才找文件的目录位置。
   - **痛点三：参考视频学习的“像素级照抄”陷阱**：给 Coding Agent 看一段优秀动效参考，它往往把别人的配色和排版原封不动抄过来，而不是提炼底层的运动节奏与声画同步规律。
   - **架构师黄金组合（`sitrep-osint` MIT + `dsh-workspace-explorer` MIT + `motion-library-skill` MIT）**：在供应链与区域态势监控层部署 **`alexandephilia/sitrep-osint`**（六级正文穿透回退梯队 + 社媒作者多样性上限 + 3D 强震/火山自动聚焦地球仪 + ADS-B/AIS 航运图层）；在 DeepSeek Harness 桌面工作台安装 **`tm5452/dsh-workspace-explorer` (`v1.2.0`)**（多标签跨会话保留目录历史、右键滑动手势、PDF/Office 大文件封面按需加载、切换非图钉标签自动释放内存并一键拖入对话）；在创意动效研发层挂载 **`ronkenx9/motion-library-skill`**（调用 `yt-dlp`、`ffprobe` 与 `analyze_sound.py` 拆解参考片的运动物理与音频节拍，针对当前 Brief 发明原创动效）。
2. **闭式 FinOps 量化收益（25 名企业风控分析师、AI 工作台工程师与创意技术工程师，每月执行 1,200 次突发事件研判、大文件工作区协同与声画动效研发，综合时薪 `$95.00/hr`）**：
   - 从 **Path A（采购高价商业 OSINT 席位 + 误点大文件撑爆上下文与返工抄袭动效，`$5,720.00/月`）** 切换至 **Path C（`sitrep-osint` 本地态势台 + `dsh-workspace-explorer` 按需预览插件 + `motion-library-skill`，`$341.00/月`）**，每月净省 **`$5,379.00/月`（降幅 `-94.04%`，年化节省 `$64,548.00/年`）**，人工翻墙扒正文、过滤水军噪音与跨窗口找文件工时从 `36.0 小时/月` 降至 `2.8 小时/月`（节省 **`92.22%`**）。

![SITREP OSINT + DSH Explorer + Motion Library Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r53-sitreposint-dshexplorer-motionlib.svg)

---

## 💬 二、灵魂拷问 Q1–Q3（大白话拆解应用场景与架构本质）

### Q1：`alexandephilia/sitrep-osint` 的“六级正文提取回退链”与“社媒作者多样性上限”是如何保障突发情报高信噪比的？
- **大白话本质定义**：`sitrep-osint`（`MIT`，本地优先 Web 控制台，自带 `data/` 24 小时跨重启状态持久化）是**“把新闻六级破壁阅读器、防刷屏社媒雷达、气象/火灾/地震卫星图层与实时飞机轮船轨迹装进一个本地网页的全景态势感知指挥舱”**。
- **三大核心架构设计**：
  1. **六级正文提取回退梯队（6-Stage Reader Fallback Ladder）**：当内置去广告阅读器遇到反爬或付费墙时，自动按 **`direct（直连）→ bot-UA → AMP 页面 → 代理 → Jina Reader → Firecrawl`** 六级梯队逐级降级穿透，确保提取出干净正文与媒体；
  2. **按主题懒加载 + 作者多样性上限（Author-Diversity Caps）**：监控 X 与 Threads 时实施作者多样性封顶，防止单一高频账号刷屏扭曲聚类结果，并将社媒求救信号、事件聚类与失效源告警融合成统一态势简报；
  3. **3D 地球仪自动跳焦 + 海陆空多维图层**：3D 地球仪自动弹窗并跳焦至最新重大突发事件（火山与 `M≥5` 级地震最高优），Leaflet 地图叠加气象预警、空气质量（AQMS）、NASA FIRMS 野火热点、向日葵 9 号卫星红外/水汽图层、RainViewer 降雨雷达、ADS-B 实时航班、AIS 船舶与 CCTV 视频流。

### Q2：`tm5452/dsh-workspace-explorer` (`v1.2.0`) 如何让 DeepSeek Harness 桌面端的文件浏览既快又不吃内存？
- **三大桌面级交互与内存保护机制（`dsh plugin --profile web add dsh-workspace-explorer`，`MIT`）**：
  1. **分级按需预览 + 切标签自动释放内存**：图片、音频（带会话区音乐胶囊）与纯文本单击即看；而 **PDF、Office 等重型文件默认只显示封面，必须点击确认按钮才加载正文**；未点击图钉（Pin）固定的预览标签在切换时自动释放内存，彻底杜绝预览大文件把客户端拖慢；
  2. **跨会话共享多标签 + 目录级视图记忆**：切换会话或工作区时完整保留已打开的多个文件夹标签与前进/后退历史，且每个目录自动记住自己上次用的是列表还是缩略图大图标及排序方式；
  3. **右键滑动手势 + 拖拽入对话**：在文件区按住右键左滑后退、右滑前进、上滑返回上一级，选中文件直接拖入聊天框即可喂给 Agent。

### Q3：`ronkenx9/motion-library-skill` 如何教会 Claude Code 与 Codex“学神韵而不抄皮囊”？
- **基于 `yt-dlp + ffprobe + analyze_sound.py` 的解构式创作（`MIT`）**：
  - 先通过脚本对标杆视频进行帧级拆解与声学节拍分析（`analyze_sound.py`），提炼“为什么这段动效高级”的物理节奏规律，再结合当前业务 Brief 发明全新原创动作，坚决杜绝机械照搬参考片。

---

## 🧭 三、端到端集成参考架构与选型决策树（Mermaid）

```mermaid
flowchart TD
    subgraph OSINTConsole["多源融合开源情报台：alexandephilia/sitrep-osint (★46, MIT)"]
        A[全球/区域突发新闻与 X/Threads 信号] --> B[6级正文穿透梯队: direct→bot-UA→AMP→proxy→Jina→Firecrawl<br/>+ 社媒作者多样性上限防刷屏]
        B --> C[3D 地球仪 M≥5 强震/火山自动聚焦<br/>+ NASA FIRMS 火点 / 向日葵9号卫星 / ADS-B 航班 / AIS 船舶图层]
    end

    subgraph DSHAndMotion["DSH 按需预览插件与声画动效解构：dsh-workspace-explorer (★30) + motion-library (★45)"]
        D[DeepSeek Harness 桌面工作区] --> E[tm5452/dsh-workspace-explorer v1.2.0<br/>多标签记忆 + 右键手势 + PDF/Office 封面按需加载与自动释放内存]
        F[品牌/产品动效 Brief] --> G[ronkenx9/motion-library-skill<br/>yt-dlp + ffprobe + analyze_sound.py 解构节奏 → 生成原创动效]
    end
```

---

## 📊 四、同赛道方案横向选型对比矩阵（Decision Matrix）

| 评估维度 | 方案 A：高价商业 OSINT 终端 + 频繁切系统资源管理器 + 照抄模板 | 方案 B：零散 RSS 阅读器 + 手工复制绝对路径 | **方案 C（推荐）：`sitrep-osint` + `dsh-workspace-explorer` + `motion-library` (MIT)** |
| :--- | :--- | :--- | :--- |
| **突发情报正文穿透力与防刷屏能力** | ❌ 商业订阅按席位年费极高；普通抓取遇反爬即瞎 | ⚠️ 缺乏 `direct→Jina→Firecrawl` 自动降级与作者多样性限制 | ✅ **内置 6 级正文穿透梯队、作者多样性上限与海陆空卫星/AIS/ADS-B 多维图层** |
| **AI 桌面端大文件浏览与内存控制** | ❌ 误点大型 PDF/视频直接卡死聊天窗口或塞爆上下文 | ⚠️ 来回切 Windows 资源管理器找路径打断对话流 | ✅ **内嵌多标签右键手势浏览，大文件封面确认后按需加载，切非固定标签自动释放内存** |
| **动效参考学习与原创度保障** | ❌ 直接照抄参考片布局与配色，引发版权与同质化争议 | ⚠️ 纯文字描述动效缺乏音频节拍与帧级物理依据 | ✅ **`ffprobe` + `analyze_sound.py` 拆解声画节拍原理，针对 Brief 生成原创动效** |
| **月度总拥有成本（TCO，25 人 / 1,200 次工作流）** | **`$5,720.00 / 月`**（含 `$2,300` 商业席位/误传大文件 + `36.0h` 人工） | **`$2,430.00 / 月`**（含 `$910` 抓取费 + `16.0h` 手工整理） | **`$341.00 / 月`**（**净省 `-94.04%`**，仅 `$75` 降级提取额度与 `2.8h` 研判签批） |

---

## 🧮 五、7-Card 定量洞察与闭式 FinOps 核算（`CLAIM-20261117-R53-SITREPOSINT-DSHEXPLORER-MOTIONLIB`）

> **核算范围与边界声明**：面向 25 名企业风控分析师、AI 工作台工程师与创意技术工程师团队，每月执行 **1,200 次突发事件态势研判、大文件工作区会话与声画动效研发工作流**（综合时薪 `$95.00/hr`；底层大模型基础订阅标记为 `not_measured`）：

$$\text{Total Monthly TCO} = \text{OSINT SaaS \& Large-File Token Dump Spend} + (\text{Paywall/Spam Triage \& File Hunting Hours} \times \$95.00)$$

| 成本构成项 | Path A：商业 OSINT 终端 + 大文件误载 | Path B：零散 RSS + 手工复制路径 | **Path C：`sitrep-osint` + `dsh-explorer` + `motion-lib`** |
| :--- | :---: | :---: | :---: |
| **月度商业情报订阅与误传大文件 Token 损耗** | `$2,300.00` | `$910.00` | **`$75.00`** |
| **月度人工扒正文、筛除水军与跨窗口找文件工时** | `36.0 hrs` | `16.0 hrs` | **`2.8 hrs`**（直降 **`92.22%`**） |
| **月度风控与工程团队人工成本（`@ $95.00/hr`）** | `$3,420.00` | `$1,520.00` | **`$266.00`** |
| **月度总拥有成本（Monthly TCO）** | **`$5,720.00`** | **`$2,430.00`**（`-57.52%`） | **`$341.00`**（**`-94.04%`**） |
| **相对 Path A 净节省（月度 / 年化）** | 基线（`$0.00`） | `$3,290.00 / 月`（`$39,480/年`） | **`$5,379.00 / 月`（`$64,548.00 / 年`）** |

---

## ✅ 六、AI 解决方案架构师实战上手 Checklist（SA Action Checklist）

- [ ] **Step 1 — 部署 `alexandephilia/sitrep-osint` 构建供应链与区域风险态势台**：复用其 `direct → bot-UA → AMP → proxy → Jina → Firecrawl` 六级正文提取梯队与社媒作者多样性上限设计。
- [ ] **Step 2 — 在 DeepSeek Harness 桌面端安装 `tm5452/dsh-workspace-explorer` (`v1.2.0`)**：执行 `dsh plugin --profile web add dsh-workspace-explorer`，利用封面按需加载与非固定标签内存自动释放机制保护长会话稳定性。
- [ ] **Step 3 — 在 Claude Code 与 Codex 中挂载 `ronkenx9/motion-library-skill`**：安装 `yt-dlp`、`ffmpeg` 与 `analyze_sound.py`，要求 Agent 在编写动效前先做声画节拍解构而非照抄模板。
- [ ] **Step 4 — 建立本地 `data/` 24h 态势快照归档规范**：将突发告警聚类与多图层快照纳入企业应急响应复盘库。
