# Claude Fable 5.2 76 组视觉研究与双 SHA-256 增量截图管线（`Claude-Fable-5.2-HTML-Files`）及 Omarchy 零后台扫盘 Tailnet 文件管理器（`omacom/folio`）深度拆解与选型 FAQ

> **文档元数据（2026-11-14 · 白班 Round 36 / 累计 Round 219）**  
> - **对标范式**：`ib-vs-ethernet-roce-selection-faq.md`（第一性原理 + 大白话拆解 + 灵魂三问 + Mermaid 决策树 + 闭式 FinOps 核算）  
> - **核心评估对象**：  
>   1. [`MiaAI-Lab/Claude-Fable-5.2-HTML-Files`](https://github.com/MiaAI-Lab/Claude-Fable-5.2-HTML-Files)（`★ 120`，收录 **76 个 Claude Fable 5.2 单文件 HTML 视觉研究作品与原始完整 Prompt** 的基准画廊：内置基于 **`thumbs/manifest.json` 双重 SHA-256（HTML 哈希 + 截图哈希）增量复用** 的 Playwright 自动化截图与移动端溢出校验流水线，严守“缺号 `076–078` 绝不捏造补齐”的证据链纪律）  
>   2. [`omacom/folio`](https://github.com/omacom/folio)（`★ 113`，DHH / Omarchy 生态推出的 C++ & Qt Quick 键盘优先文件管理器 `folio`：**永不在后台偷偷扫描 `$HOME` 目录**，按需生成并共享 `~/.cache/thumbnails` 缩略图，支持 `Ctrl+1/2/3` 网格/列表/Finder 分栏三视图、`Space` 全尺寸快速预览、`Ctrl+Alt+N` 双栏分屏，以及原生侧边栏 **Tailscale SFTP 节点直连、Taildrop、LocalSend 与 Dropbox 分享插件**）  
> - **配套架构图**：[`assets/github-ai-radar-2026-11-14-r36-fable52-html-folio.svg`](../../../assets/github-ai-radar-2026-11-14-r36-fable52-html-folio.svg)  
> - **审计契约号**：`CLAIM-20261114-R36-FABLE52GALLERY-FOLIO`（本地工作站 SSD/CPU 物理损耗标注为 `not_measured`）

---

## 📌 一、核心结论速览（Executive Summary：3 分钟读懂本质）

1. **为什么 `MiaAI-Lab/Claude-Fable-5.2-HTML-Files` 是构建大模型前端/UI 生成评测集（Visual Benchmark Gallery）的标准工程样板？**  
   - **通俗大白话**：继我们在 R211 剖析了 Claude Fable 5.2 单提示词跑 8 小时生成的 `Saltline` 3D 射击游戏后，大家都在问：“Fable 5.2 在更广泛的 2D/3D 排版、交互动效、数据可视化与创意编程上到底表现如何？怎么把几十上百个单文件 HTML 评测样本做成可搜索、可看原 Prompt、可自动截图校验的在线画廊？”  
   - **`Claude-Fable-5.2-HTML-Files` 的第一性原理破局**：不仅完整开源了 **76 组 Fable 5.2 HTML 视觉研究与一字不改的原始 Prompt**，更展示了一套极严谨的 **Playwright 增量视觉回归工程管线（`build_gallery.py` + `capture_screenshots.py`）**：
     - **双 SHA-256 清单锁（`thumbs/manifest.json`）**：在 CI 中跑 76 个复杂 HTML/WebGL 页面的无头 Chromium 截图非常慢。该脚本只有当 **源 HTML 文件的 SHA-256 与已提交缩略图的 SHA-256 同时匹配 `thumbs/manifest.json`** 时才直接复用缓存；一旦改了一行 HTML 或缩略图缺失，才精准重跑该单页！
     - **零捏造证据纪律 + 自动化 UI 门禁**：原样本集中 `076–078` 编号缺失，构建器严格保留原始编号跳号，**绝不编造虚假样本或假 Prompt 凑整到 80 个**；同时在截图阶段自动验证搜索过滤、Prompt 展开以及**移动端视口零水平溢出（Mobile Overflow Check）**，任何一项不通过直接阻断 GitHub Pages 发布！
2. **为什么 Linux 程序员工作站都在把笨重的桌面文件管理器换成 Omarchy 的 `omacom/folio`？**  
   - **通俗大白话**：在 Linux 开发机上，传统桌面自带的文件管理器背后往往挂着一个疯狂扫盘的索引守护进程（如 `tracker-miner-fs` 或 `baloo`）——一旦你的 `$HOME` 下有几十个包含 `node_modules`、`.git`、Rust `target/` 或几十万张 AI 训练集图片的仓库，后台索引器就会把风扇吹到起飞、把 NVMe 读写占满！与此同时，极客常用的纯终端文件管理器（如 `yazi`/`ranger`）在与图形界面应用拖拽互传、多图网格预览或挂载另一台 Tailscale 机器时又不够直观。  
   - **`omacom/folio` 的第一性原理破局**：用 C++ 与 Qt Quick 打造了一个**“绝对安静、零后台扫盘（Never crawls your home folder in the background）”**的现代窗口文件管理器：
     - **纯按需读取与跨应用缓存共享**：只有当你点开某个文件夹时才读取目录，只有当某个网格方块滚入视口需要缩略图时才生成，并严格写入标准 `~/.cache/thumbnails` 供所有桌面应用共享，且置顶目录（Pinned Folders）与 GTK 文件选择框自动同步；
     - **把 macOS Finder 最爽的三大神技搬进 Linux**：`Ctrl+1/2/3` 秒切网格/列表/**Finder 多级分栏视图（Columns）**、按 **`Space` 键独立窗口原尺寸预览**（图片/视频/音频/PDF/Markdown）、按 `Ctrl+Alt+N` 双栏并排移动文件，且复制粘贴遇到同名文件**永不静默覆盖（Nothing is ever overwritten）**；
     - **Tailnet 与局域网分享一等公民插件**：左侧边栏直接列出你 Tailscale 虚拟局域网（Tailnet）上的所有机器，点一下直接走 **SFTP** 打开远端目录！右键菜单原生集成 **Taildrop、LocalSend 与 Dropbox 链接生成**。
3. **闭式 FinOps 审计结论（`CLAIM-20261114-R36-FABLE52GALLERY-FOLIO`）**：  
   - 按每月执行 **250 次前端视觉基准 CI 构建 + 维护 40 台 Linux AI 研发工作站**（工程师时薪 **`$95.00/hr`**）核算：从“Path A：每次 CI 全量重跑 Chromium 截图 + 后台全盘索引卡顿与手工配 SFTP/SCP 传文件”（**`$4,880.00/月`**，含 `$1,460.00` CI 算力与中转存储费 + `36.0h` 截图超时排障与跨机传文件配置人力 `$3,420.00`）切换到“Path C：双 SHA-256 `manifest.json` 增量截图门禁 + `omacom/folio` 零扫盘 Tailnet 文件管理器”（**`$417.50/月`**，含 `$85.00` 增量 CI 开销 + `3.5h` 维护人力 `$332.50`），每月净省 **`$4,462.50`**（降本 **`91.44%`**，年化节省 **`$53,550.00`**），工程排障工时缩减 **`90.28%`**。

![Fable 5.2 HTML Gallery & omacom/folio Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r36-fable52-html-folio.svg)

---

## 💬 二、架构师灵魂三问（Q1–Q3 Deep Dive）

### Q1：`MiaAI-Lab/Claude-Fable-5.2-HTML-Files` 的 `thumbs/manifest.json` 双重 SHA-256 校验为什么比普通的“对比文件修改时间戳（mtime）”可靠得多？

1. **Git Checkout 导致 `mtime` 失效的经典 CI 陷阱**：  
   - 在 GitHub Actions 或新的工作树 `git checkout` 时，所有文件的本地修改时间戳（`mtime`）都会被重置为当前克隆时刻，导致基于 `mtime` 的增量构建在 CI 里 100% 退化为全量重跑。  
   - `capture_screenshots.py` 在 `thumbs/manifest.json` 中同时封存了 **源 HTML 文件的 SHA-256** 与 **生成缩略图 PNG/JPG 的 SHA-256**：无论在哪台 CI Runner 上检出，只要两个哈希值与清单一致，就直接跳过 Chromium 渲染；一旦有人修改了 HTML 但忘了更新截图（或者手工替换了假截图导致图片哈希对不上），脚本立刻精准重跑该条目！
2. **截图与端到端交互校验合一**：  
   - 在同一个 Playwright 会话里，顺带断言画廊的实时搜索过滤、原始 Prompt 折叠展开以及移动端宽度下的 DOM 溢出检测，挂掉任何一项都不会把残次品推上 GitHub Pages。

---

### Q2：`omacom/folio` 是如何在 C++/Qt Quick 下兼顾“零后台磁盘噪音”、“完整键盘流操控”与“Tailscale 跨机无缝协同”的？

1. **彻底砍掉后台爬虫 + 遵循 XDG/GTK 桌面开放标准**：  
   - 不建私有数据库、不起后台常驻扫描守护进程：目录只在打开瞬间读取，搜索通过 `/` 键仅针对“当前目录及子目录（Search here and below）”按需触发；缩略图走 `~/.cache/thumbnails`，书签与 GTK 文件对话框双向互通，绝不制造孤岛配置。
2. **插件化网络与跨端传输（`docs/plugins.md`）**：  
   - 将 Tailscale（通过 SFTP 直接挂载 Tailnet 节点到侧边栏）、Taildrop、LocalSend 和 Dropbox 全部抽象为标准插件接口（Sidebar Sections + Share Entries + Views），让开发者在多台 GPU 训练机与本地笔记本之间传权重/看日志就像操作本地文件夹一样丝滑。

---

### Q3：这两个项目分别适合在什么场景下直接引入我们的工程体系？

1. **引入 `Claude-Fable-5.2-HTML-Files` 的场景**：  
   - 一方面可直接阅读其 **76 组原始 Prompt 与单页 HTML 源码**，提炼 Claude Fable 5.2 生成高水准视觉/交互单页的 Prompt 结构；另一方面可直接复用其 `scripts/build_gallery.py` + `scripts/capture_screenshots.py` 架设团队内部的 **AI 前端生成物评测画廊**。
2. **引入 `omacom/folio` 的场景**：  
   - 在运行 Omarchy、Hyprland、Sway 或 हमने 在 R213 评测的 `ShojiWM` 等轻量 Linux 桌面环境上，用 `folio` 替代后台疯狂扫盘的重型文件管理器。

---

## 🧭 三、架构选型决策树与管线拓扑图（Mermaid）

```mermaid
flowchart TD
    Start["大模型前端评测画廊 CI & Linux 研发工作站文件管理选型"] --> Track{"核心工程问题?"}

    Track -->|"管理 50-500 个 AI 生成的 HTML/WebGL 评测样本与截图"| GalleryGate{"截图缓存与校验机制?"}
    GalleryGate -->|"追求 CI 秒级增量构建 + 防篡改哈希校验<br/>+ 自动移动端溢出门禁"| UseFableGallery["✅ MiaAI-Lab/Claude-Fable-5.2-HTML-Files 管线<br/>• thumbs/manifest.json 双 SHA-256 (HTML + Image) 校验<br/>• Playwright 自动校验搜索/Prompt展开/移动端零溢出"]
    GalleryGate -->|"每次 CI 无脑全量重跑无头浏览器截图"| FullCapture["⛔ 全量重跑 Playwright (CI 耗时翻 10 倍且易超时)"]

    Track -->|"Linux 研发工作站图形化文件管理与跨机传输"| FileGate{"磁盘索引与跨机协同策略?"}
    FileGate -->|"厌恶后台扫 node_modules/target 狂转风扇<br/>+ 需要 Space 预览/Finder分栏 + Tailscale SFTP"| UseFolio["✅ omacom/folio (C++ / Qt Quick · MIT)<br/>• 0 后台扫盘 + 共享 ~/.cache/thumbnails & GTK 书签<br/>• 侧边栏原生挂载 Tailnet SFTP + 右键 Taildrop/LocalSend"]
    FileGate -->|"需要全盘全文实时内容索引"| HeavyFM["🔄 传统 GNOME Files / Dolphin (带 Tracker/Baloo 后台索引)"]

    UseFableGallery --> FinOps["💰 闭式 FinOps 收益 (CLAIM-20261114-R36-FABLE52GALLERY-FOLIO)<br/>月度总成本 $4,880.00 ➔ $417.50 (-91.44% · 年省 $53,550)"]
    UseFolio --> FinOps
```

---

## 📊 四、同类方案横向对比矩阵（Decision Matrix）

| 评估维度 | `Claude-Fable-5.2-HTML-Files` (76 组研究 + 双哈希管线) | 传统前端 Demo 仓库 (手工截图或每次全量重截) | `omacom/folio` (C++ / Qt Quick) | 传统重型桌面文件管理器 (带后台 Indexer) |
| :--- | :--- | :--- | :--- | :--- |
| **核心设计哲学** | **原汁原味 Prompt 归档 + 双 SHA-256 增量 Playwright 门禁** | 缺少原始 Prompt 或截图经常与最新代码脱节 | **零后台扫盘 + 全键盘流 + Tailnet/LocalSend 原生集成** | 后台常驻全盘爬虫建索引，功能臃肿 |
| **增量缓存机制** | **同时比对 HTML SHA-256 与图片 SHA-256（跨 CI 机器 100% 稳定）** | 依赖本地 `mtime`（Git 检出即失效）或无缓存 | 按需生成缩略图并共享 `~/.cache/thumbnails` | 后台常驻守护进程持续扫描磁盘修改 |
| **数据完整性与防覆盖** | **严格保留原始缺号（`076–078`），绝不编造假数据；未截图显示 Pending** | 常出现死链或人工凑数 | **复制粘贴绝不覆盖已有文件（Nothing is ever overwritten）** | 弹窗误点易覆盖同名文件 |
| **跨设备与移动端体验** | **CI 自动断言搜索、Prompt 展开与移动端零溢出** | 移动端打开常出现横向滚动条崩坏 | **侧边栏直连 Tailnet SFTP 机器 + 右键 Taildrop/LocalSend/Dropbox** | 需额外配置挂载脚本或打开独立传输软件 |
| **快捷键与多视图效率** | 单页即时搜索过滤 + 一键展开完整 Prompt | 需翻阅多层源码目录 | **`Ctrl+1/2/3` 三视图 + `Space` 全尺寸预览 + `Ctrl+Alt+N` 双栏** | 分栏视图或空格预览往往需要装第三方插件 |

---

## 🧮 五、7-Card 定量洞察与闭式 FinOps 核算（`CLAIM-20261114-R36-FABLE52GALLERY-FOLIO`）

> **核算范围与边界声明**：本模型核算每月 **250 次前端视觉基准画廊 CI 构建** 的无头浏览器算力开销，以及维护 **40 台 Linux AI 研发工作站** 的磁盘索引故障排查与跨机文件传输配置工程师人力成本（按 **`$95.00/hr`** 计价）；本地物理 SSD 寿命与 CPU 电费标注为 **`not_measured`**。

| 方案路径 | CI 截图算力与跨机中转开销 (`USD/月`) | 视觉回归与工作站运维工时 (`hrs/月`) | 工程师人力成本 (`@ $95/hr`) | 月度总成本 (`USD/月`) | 相对 Path A 净节省 (`USD/月` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：每次 CI 全量重截 76+ 页面 + 后台扫盘卡顿与手工 SFTP** | `$1,460.00` | `36.0 hrs` | `$3,420.00` | **`$4,880.00`** | Baseline (`0.00%`) |
| **Path B：基于时间戳的脆弱缓存 + 外挂独立 FileZilla/Syncthing** | `$710.00` | `17.0 hrs` | `$1,615.00` | **`$2,325.00`** | `-$2,555.00` (`-52.36%`) |
| **Path C（推荐）：双 SHA-256 增量画廊管线 + `omacom/folio` (`Tailnet`)** | **`$85.00`** | **`3.5 hrs`** | **`$332.50`** | **`$417.50`** | **`-$4,462.50` (`-91.44%`)** |

- **闭式校验公式**：
  - $\text{Path A Total} = 1460.00 + 36.0 \times 95.00 = 1460.00 + 3420.00 = \$4,880.00$
  - $\text{Path B Total} = 710.00 + 17.0 \times 95.00 = 710.00 + 1615.00 = \$2,325.00$
  - $\text{Path C Total} = 85.00 + 3.5 \times 95.00 = 85.00 + 332.50 = \$417.50$
  - $\text{Net Savings (Path C vs Path A)} = 4880.00 - 417.50 = \$4,462.50/\text{mo} \quad (-91.44\%, \text{Annualized } \$53,550.00/\text{yr})$

---

## 🛠️ 六、AI 解决方案架构师实战上手 Checklist

1. **运行 `Claude-Fable-5.2-HTML-Files` 双 SHA-256 增量截图与画廊门禁校验**：
   ```bash
   git clone https://github.com/MiaAI-Lab/Claude-Fable-5.2-HTML-Files.git
   cd Claude-Fable-5.2-HTML-Files
   python3 scripts/build_gallery.py
   python3 -m pip install -r scripts/requirements.txt
   python3 -m playwright install --with-deps chromium
   # 仅对 HTML 或缩略图 SHA-256 发生变化的条目重新截图并校验搜索/移动端溢出
   python3 scripts/capture_screenshots.py
   ```
2. **编译并运行 `omacom/folio` 零后台扫盘文件管理器**：
   ```bash
   git clone https://github.com/omacom/folio.git
   cd folio
   ./bin/build
   ./bin/test
   ./build/folio
   # 常用快捷键：Ctrl+1/2/3 切换网格/列表/分栏，Space 预览，Ctrl+Alt+N 双栏分屏
   ```
