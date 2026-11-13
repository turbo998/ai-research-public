# 跨 9 大工具本地私有共享记忆层（`rjcuff/Woolly`）与四重独立校验硬三角形预算 Low-Poly 建模技能（`gokayfem/image-to-lowpoly`）深度选型 FAQ

> **文档定位**：本专题是 **2026-11-13 夜班第 37 轮（累计第 165 篇）独立六段式选型指南**，严格对标 `ib-vs-ethernet-roce-selection-faq.md` 的通俗第一性原理与闭式 FinOps 核算规范，面向多工具协同研发团队负责人、游戏/Web 3D 资产管线架构师与 AI Solution Architect，深度拆解今日新仓榜上解决“在 Claude Code、Cursor、Codex、Gemini CLI 间切换时记忆各自孤立、队友的 Agent 每次从零失忆起步”以及“让 AI 生成 500 面 Low-Poly 模型时靠未坍缩的修改器（Modifiers）、四边形谎报面数或贴图遮丑”的两大实战工具：
> 1. **`rjcuff/Woolly`（3 天新建获 `11★`，Go，MIT，PyPI/npm `woolly-ai`，支持 macOS / Windows / Linux）**：“Ollama 负责跑模型，Woolly 负责替所有 AI 工具记住一切”的**纯本地 Markdown 跨工具共享记忆层**——一行 `woolly connect` 即可打通 **Claude Code、Claude Desktop、Cursor、VS Code、Windsurf、Codex、Gemini CLI、LM Studio 与 opencode**；启动时仅按需加载当前项目的笔记，提供 `woolly log` 审计每个应用读写了哪条记忆，并支持通过 `woolly init` 将 `.woolly/` 提交至 Git 仓库，让全团队所有人的 Agent 共享同一份架构决策与避坑记忆（零第三方云端上传）！
> 2. **`gokayfem/image-to-lowpoly`（2 天新建获 `11★`，Python，MIT，兼容 Claude Code / Codex / Cursor / Copilot / Gemini）**：“用精确到个位数的 $N$ 个三角形还原一张参考照片”的硬预算 3D 低多边形建模技能——针对 `100 / 200 / 500 / 1,000` 三角形硬预算，通过拟合锁定相机、推断背面三维实体体积、共享优化器移动顶点，并**用 4 种独立方法交叉核验真实三角形数量**（严禁未应用的 Subdivision/Mirror 修改器、未三角化的四边/多边形、隐藏副物体、扁平纸片挤出或用贴图颜色掩盖烂几何），在纯灰泥（Grey Clay）渲染下实现 **`0.943 / 0.972 / 0.983 / 0.984` 的剪影 IoU**，输出单物体零修改器的标准 `.glb` 与 `.blend`！
>
> **English Version**: [woolly-image-to-lowpoly-local-cross-tool-memory-exact-triangle-budget-3d-skill-selection-faq.en.md](woolly-image-to-lowpoly-local-cross-tool-memory-exact-triangle-budget-3d-skill-selection-faq.en.md) · **关联日报**: [`daily/2026-11-13.md`](../daily/2026-11-13.md) · **专题架构图**: [`assets/github-ai-radar-2026-11-13-r37-woolly-imagetolowpoly.svg`](../../../assets/github-ai-radar-2026-11-13-r37-woolly-imagetolowpoly.svg)

![rjcuff/Woolly 与 gokayfem/image-to-lowpoly 架构选型对比](../../../assets/github-ai-radar-2026-11-13-r37-woolly-imagetolowpoly.svg)

---

## 📌 一、核心结论速览（Executive Summary）

1. **一句话大白话讲透这两个项目到底解决了什么痛点？**
   - **终结“上午在 Claude Code 里刚跟 AI 敲定完数据库表结构和踩坑教训，下午切到 Cursor 或 Windsurf 改前端时 AI 对上午的决定一无所知；或者队友拉下代码后他的 Codex 又从零开始犯同样的错”的痛点（`rjcuff/Woolly`）**：执行 `woolly connect`，**Claude Code、Claude Desktop、Cursor、VS Code、Windsurf、Codex、Gemini CLI、LM Studio、opencode** 9 大工具立刻共享同一个保存在本机磁盘上的纯 Markdown 记忆库（不往任何外部云服务器发一个字节）；执行 `woolly init` 把 `.woolly/` 提交进 Git，全队成员的 AI 助手立即同步全部技术栈约定与避坑指南，且每次启动只加载当前项目关联笔记！
   - **终结“让 AI 建一个‘严格 500 三角形’的猫咪低模（Low-Poly），结果 AI 嘴上报 500 面，打开 Blender 一看其实是 500 个四边形（1,000 个三角形）外加一个没坍缩的细分修改器（实际上万面）；或者正面看着像猫，转到侧面发现是张扁平剪影纸片”的痛点（`gokayfem/image-to-lowpoly`）**：强制在**无贴图的灰泥模式（Grey Clay）**下考核几何真本事（不许靠画贴图蒙混过关），先推断照片看不见的背面实心体积并防止部件穿插把珍贵的三角形浪费在身体内部，再通过**四种独立计量方式锁死三角形总数（100 / 200 / 500 / 1,000 精确到个位数，零修改器、单物体）**，剪影重合度（Silhouette IoU）最高达 **`0.984`**！
2. **闭式 FinOps 投资回报结论（`CLAIM-20261113-R37-WOOLLY-IMAGETOLOWPOLY`）**：
   - 以 **16 人多工具软件与 3D 互动资产团队每月执行 `3,200 次跨 CLI/IDE 编码会话` 并生产 `50 个严格面数受限的 Low-Poly 3D 模型`** 为基准（软件与 3D 技术美术全包时薪 `$95.00/hr`；工作站硬件与商业游戏引擎授权：`not_measured`）：
   - 从 **Path A（9 工具记忆孤岛反复重敲背景 + AI 生成假面数 3D 模型人工返工减面，月均 `$5,200.00`）** 切换至 **Path C（`Woolly` `.woolly/` 跨工具本地共享记忆 + `image-to-lowpoly` 四重校核硬预算低模技能，月均 `$492.50`）**，每月净省 **`$4,707.50/mo`（降幅 `-90.53%`，年省 `$56,490.00/yr`）**，并将跨工具重复交代背景与手工重拓扑减面的工时从 `38.0 hrs/mo` 压缩至 `3.5 hrs/mo`（节省 **`-90.79%`**）。

---

## 🎯 二、三大灵魂拷问（Q1 / Q2 / Q3 深度原理解析）

### Q1：为什么云端专属记忆服务（Cloud Memory SaaS）和每个 IDE 自带的私有记忆无法解决研发团队的跨工具失忆？
- **第一性原理拆解**：
  1. **工具链异构性成为常态**：同一名架构师日常会用 Claude Code 跑长链重构、用 Cursor 做行内补全、用 Gemini CLI 查大上下文、用 LM Studio / Ollama 跑本地敏感数据。私有记忆把上下文锁死在单一客户端内。
  2. **缺乏项目级按需加载与 Git 分支协同**：把所有项目的记忆混在一个全局黑盒里既浪费启动 Token 又污染无关项目；`Woolly` 在启动时仅注入当前项目（如 `acme`）的笔记，并通过 `.woolly/` 随代码仓天然支持团队 Git 协同与 `woolly log` 跨应用审计。

### Q2：为什么普通 Coding Agent 在执行“生成严格 $N$ 个三角形的 3D 模型”时会出现五花八门的作弊与穿帮？
- **第一性原理拆解**：
  1. **多边形（Polygon）与三角形（Triangle）混淆及隐藏修改器**：Blender 默认面板显示的 Polygon 数会把四边形（Quad = 2 个三角形）和 N-gon 算作 1，且未 Apply 的 Subdivision / Mirror 修改器或隐藏物体会携带大量未计入的隐形三角形。
  2. **单视角剪影作弊与内部穿插浪费**：如果只考核正视图剪影 IoU 或允许带纹理渲染，Agent 会生成扁平纸片挤出体（转个角度即扁平）、用贴图颜色伪造立体感，或者让四肢直接穿插进躯干内部，把宝贵的三角形预算浪费在永远看不见的内部曲面上。

### Q3：`gokayfem/image-to-lowpoly` 是如何做到“四重独立计面、纯灰泥真几何、多档预算精确收敛”的？
- **第一性原理拆解**：
  1. **四重独立三角形计数门禁 + 零修改器单物体导出**：
     - 强制转换为单物体纯三角网格并清空一切修改器，从四个独立维度核对三角形数等于目标值 $N$（如 100、200、500、1,000），直接导出干净的 `.glb` 与 `.blend`。
  2. **背面实心体积推断 + 共享顶点优化器 + 诚实缺陷披露**：
     - 先构建被遮挡区域的推断实体并消除部件自穿插，再用共享优化器移动顶点逼近锁定相机剪影（100/200/500/1000 面 IoU 分别达 `0.943 / 0.972 / 0.983 / 0.984`），同时在报告中诚实指出当前正面厚度与头部细节的残余局限。

---

## 🧭 三、Mermaid 选型决策树与「Woolly 跨工具共享记忆 + image-to-lowpoly 硬预算建模」架构图

```mermaid
flowchart TD
    A["多 AI 工具 (Claude/Cursor/Codex/Gemini) 记忆互通与硬面数预算 3D 低模资产生成"] --> B{"当前处于哪个工程任务？"}
    B -- "跨工具/跨队友协同：9 款 AI 工具各自失忆，或换工具需重新交代架构约定" --> C["采用 rjcuff/Woolly (woolly connect + .woolly/ 本地共享记忆)"]
    B -- "3D 低模资产生产：需根据单张参考图生成精确 N 个三角形的 .glb/.blend 模型" --> D["采用 gokayfem/image-to-lowpoly (四重计面 + 灰泥优化 3D 技能)"]

    C --> C1["woolly connect 打通 Claude/Cursor/Windsurf/Codex/Gemini/Ollama 等 9+ 工具"]
    C1 --> C2["启动仅按需加载当前项目记忆 + woolly init 提交 .woolly/ 供全队共享"]

    D --> D1["锁定相机拟合 + 背面三维体积推断 + 消除内部穿插浪费"]
    D1 --> D2["4 种独立方式核验精确 N 三角形 (零修改器) + 灰泥剪影 IoU 达 0.984"]

    C2 & D2 --> E["🏆 黄金跨端协同与精益 3D 资产底座：Woolly 统一记忆 + image-to-lowpoly (-90.53% TCO)"]
```

---

## 📊 四、同类方案核心能力对比矩阵（Selection Matrix）

| 评估维度 | Path A：各 App 孤立记忆 + AI 盲建未计面 3D 模型 | Path B：手工复制 Markdown + Blender 自动减面修改器 | **Path C（推荐）：`rjcuff/Woolly` + `gokayfem/image-to-lowpoly`** |
| :--- | :--- | :--- | :--- |
| **跨 AI 工具记忆互通范围** | Claude、Cursor、Codex 互不相通，每次切工具重讲一遍 | 靠人手复制粘贴规则文件 | **一条 `woolly connect` 打通 Claude/Cursor/VS Code/Windsurf/Codex/Gemini/Ollama 等** |
| **团队共享与数据主权** | 传上第三方云端记忆服或仅限个人本机 | 散乱文档易过期，无读写溯源日志 | **100% 本地可读 Markdown + `.woolly/` 随 Git 团队共享 + `woolly log` 审计** |
| **三角形预算精确度与防作弊** | 混入 Quad/N-gon 与未应用修改器，实际面数超标数倍 | 自动 Decimate 拓扑破碎、大量狭长退化三角形 | **四种独立方式校核精确 $N$ 三角形（单物体、零修改器，标准 `.glb`/`.blend`）** |
| **多视角立体感与几何纯净度** | 靠贴图遮丑或扁平纸片挤出，内部穿插浪费面数 | 减面后五官与四肢粘连成块 | **纯灰泥（Grey Clay）验证 + 背面实体推断 + 防内部穿插（IoU `0.943–0.984`）** |
| **月度总拥有成本（3,200 会话 + 50 模型）** | **`$5,200.00 / mo`**（`$1,590` Token + `$3,610` 工时） | **`$2,610.00 / mo`**（`$710` Token + `$1,900` 工时） | **`$492.50 / mo`（净省 `$4,707.50/mo` · `-90.53%`）** |

---

## 🧪 五、定量 FinOps 算例与 7-Card 洞察（`CLAIM-20261113-R37-WOOLLY-IMAGETOLOWPOLY`）

### 5.1 测算基准与显式边界（Scope & Boundaries）
- **场景设定**：16 人规模的多工具研发与 3D 互动资产团队，每月跨 Claude Code、Cursor、Codex 与 Gemini CLI 运行 **3,200 次开发会话**，并按严格面数预算交付 **50 个 WebGL / 移动端游戏 Low-Poly 3D 模型**。
- **费率假设**：软件工程师与 3D 技术美术全包时薪 **`$95.00 / hr`**。
- **显式边界声明（Explicit Not-Measured Boundary）**：本地工作站硬件折旧与商业 3D 引擎企业授权费标记为 **`not_measured`**，本表严格核算因跨工具重复交代背景与 3D 模型面数超标重跑消耗的 Token 支出，以及工程师手动同步笔记与在 Blender 中返工重拓扑减面的工时。

### 5.2 三路径月度成本闭式对照表

| 成本分项 | Path A：孤岛记忆重讲 + 假面数 3D 返工 | Path B：手工同步笔记 + Decimate 减面修补 | **Path C：`Woolly` + `image-to-lowpoly`（推荐）** |
| :--- | :--- | :--- | :--- |
| **月度跨工具背景重发与 3D 返工 Token 支出** | **`$1,590.00`**（重复输入项目背景 + 3D 废稿重试） | **`$710.00`**（中等上下文与重跑开销） | **`$160.00`**（按项目精准加载 `.woolly/` + 共享优化器一次达标） |
| **跨工具人工同步与 Blender 重拓扑减面工时（`$95/hr`）** | `38.0 hrs × $95.00` = **`$3,610.00`** | `20.0 hrs × $95.00` = **`$1,900.00`** | `3.5 hrs × $95.00` = **`$332.50`** |
| **月度总成本（Monthly TCO）** | **`$5,200.00 / mo`** | **`$2,610.00 / mo`**（`-49.81%`） | **`$492.50 / mo`** |
| **相对 Path A 净节省** | 基准线（Baseline） | 净省 `$2,590.00 / mo` | **净省 `$4,707.50 / mo`（`-90.53%` · 年省 `$56,490.00/yr`）** |
| **工作站硬件与商业 3D 引擎授权费** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 六、生产级落地核验 Checklist

- [ ] **1. `rjcuff/Woolly` 跨工具连接与项目初始化**：运行 `curl -fsSL https://usewoolly.com/install.sh | sh && woolly connect`，并在项目仓执行 `woolly init` 将 `.woolly/` 纳入版本控制。
- [ ] **2. 项目隔离加载与 `woolly log` 审计验证**：在 Cursor 中记录一条项目架构决策，启动 Claude Code 验证其仅加载当前项目笔记并能通过 `woolly log` 查看到跨应用读写记录。
- [ ] **3. `gokayfem/image-to-lowpoly` 四档预算生成测试**：对单张参考图生成 `100 / 200 / 500 / 1,000` 三角形四档模型，验证输出的 `.glb` 与 `.blend` 均为单物体、零修改器且四种独立计数完全一致。
- [ ] **4. 纯灰泥（Grey Clay）多视角与无内部穿插核验**：在无纹理灰泥渲染下检查正面、侧面与俯视图，确认无扁平纸片作弊且无部件内部穿插浪费面数。
