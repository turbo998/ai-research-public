# 三重 MCP 达芬奇本地后期工作站（`willturner-maker/resolve-ai-workflow`）与官方页面核验科研基金雷达及多光标序列演示编排（`dryang21/Fundlark` & `ruvnet/mouse-swarm`）架构选型 FAQ

> **文档类型**：AI Solution Architect（AI 解决方案架构师）实战选型指南（六段式标准 FAQ）  
> **所属轮次**：2026-11-17 Night Round 51（Cumulative Round 475 Milestone）  
> **追踪目标**：
> - **`willturner-maker/resolve-ai-workflow`**（`★ 30`，Python / Splash 本地大模型 + OpenCode + 3 个 DaVinci Resolve Studio MCP Server + 无头 Blender Metal EXR 字幕管线，`MIT`）：100% 本地离线运行的专业影视后期工作站，通过持久化 SSD 前缀缓存让每次新会话直接复用 `~20k–45k` 缓存 Token（热启动 TTFT `~200 ms`，单流解码 `~170 tok/s`，并发峰值 `~375 tok/s`，标注 `anonymized_reported`），联动官方与社区 **3 大 DaVinci Resolve MCP**、无头 Blender 透明 EXR 渲染与 `ffprobe` 闭环自检
> - **`dryang21/Fundlark`**（`★ 30`，Python / 官方通知页截止日期核验科研经费与申报资格追踪器，适配 Claude Code / Codex / Cursor，`MIT`）& **`ruvnet/mouse-swarm`**（`★ 30`，JavaScript / 落地页 DOM 顺序生长与多 Agent 彩色光标编排展示器，`MIT`）：严格区分“研究方向相关”与“具备独立申报资格（Apply yourself vs 需机构提名）”并对不可达官网诚实标注 `Date to confirm` 的 **`Fundlark`**，配合将任意静态网页一键变成多 Agent 彩色光标协同搭建演示动画的 **`mouse-swarm`**  
> **计量审计 ID**：`CLAIM-20261117-R51-RESOLVEAI-FUNDLARK-MOUSESWARM`（本地硬件工作站与 DaVinci Resolve Studio 授权标记为 `not_measured`）

---

## 📌 一、核心结论速览（Executive Summary）

1. **为什么企业数字媒体后期中心、科研院所/高校 AI 创新实验室与开发者产品团队在落地“达芬奇（DaVinci Resolve）自动化剪辑包装”、“科研基金/产业专项申报筛选”与“多智能体协同搭建产品的酷炫视觉演示”时，常遭遇“保密视频素材不准上传云端 API 且单个 MCP 控制不完整”、“普通大模型查基金经常编造过期截止日期或忽略‘仅限机构提名’限制”、以及“为了拍一条多 Agent 同时改网页的宣传片要在视频软件里手K几百个假鼠标关键帧”三大痛点？**
   - **痛点一：专业后期剪辑的数据不出域红线与冷启动延迟**：企业宣传片与未公开产品视频严禁上传云端大模型；而在本机跑 Agent 调数十个剪辑工具时，如果每次新会话都要重新预填充（Prefill）几万字工具定义，首字延迟会慢得无法交互。
   - **痛点二：科研经费与专项基金检索的“资格错配”与“幻觉日期”**：让通用聊天 AI 找基金，它经常把必须由院系提名（Institutional Nomination）的项目推荐给个人博士后，或者凭记忆编造已经截止的日期。
   - **痛点三：多智能体产品演示页缺乏可交互的 DOM 生长编排**：想在官网直观展示“一群 AI Agent 正在协同构建页面”，手写动画代码或录屏剪辑极其繁琐。
   - **架构师黄金组合（`resolve-ai-workflow` MIT + `dryang21/Fundlark` MIT + `ruvnet/mouse-swarm` MIT）**：在本地影视后期工作站部署 **`willturner-maker/resolve-ai-workflow`**（基于 `Splash` 的持久化 SSD 前缀缓存直接复用 `20k–45k` Token 实现 `~200 ms` 极速响应，由 OpenCode 带着 `dry-run / confirm-token` 纪律同时操控 **3 个 DaVinci Resolve MCP**、无头 Blender Metal EXR 3D 字幕与 `ffprobe` 质检回读）；在科研与创新基金申报层接入 **`dryang21/Fundlark`**（强制去基金会官网核实截止时间，严格区分 `Apply yourself` 与机构限额，打不开的网页诚实标注 `Date to confirm`）；在产品首页与发布会演示层集成 **`ruvnet/mouse-swarm`**（将任意真实网页转化为按 DOM 顺序生长、多彩色 Agent 光标协同游走与逐字打字的可回放动画，并支持观察本地 Ruflo 集群实时状态）。
2. **闭式 FinOps 量化收益（25 名影视后期工程师、科研项目申报负责人与产品演示开发者，每月执行 450 次达芬奇/Blender 自动化成片、官方基金资格核查与多光标交互演示制作，综合时薪 `$95.00/hr`）**：
   - 从 **Path A（云端视频代理 API + 付费基金库与人工手K演示光标，`$5,660.00/月`）** 切换至 **Path C（`resolve-ai-workflow` 本地三 MCP 工作站 + `Fundlark` 核验追踪 + `mouse-swarm` 光标编排，`$336.00/月`）**，每月净省 **`$5,324.00/月`（降幅 `-94.06%`，年化节省 `$63,888.00/年`）**，手工拉时间线渲染字幕、核对基金细则与手调多鼠标动画工时从 `36.0 小时/月` 降至 `2.8 小时/月`（节省 **`92.22%`**）。

![Resolve AI Workflow + Fundlark + Mouse Swarm Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r51-resolve-fundlark-mouseswarm.svg)

---

## 💬 二、灵魂拷问 Q1–Q3（大白话拆解应用场景与架构本质）

### Q1：`willturner-maker/resolve-ai-workflow` 是如何在一台本地工作站上用“持久化 SSD 前缀缓存 + 三重达芬奇 MCP + 无头 Blender + `ffprobe` 自检”跑通全自动后期的？
- **大白话本质定义**：`resolve-ai-workflow`（`MIT`）是**“数据 100% 不出本机、靠 SSD 缓存实现 0.2 秒极速响应、左手用 3 个 MCP 操作达芬奇剪辑调色、右手调无头 Blender 渲染透明 3D 字幕、最后自己用 `ffprobe` 验片的本地 AI 后期工作站蓝图”**。
- **四大核心工程支柱（实测性能数据标注为 `anonymized_reported, independently_reproduced=false`）**：
  1. **持久化 SSD 前缀缓存（`Splash` + `Qwen3.8-Flash-Next IQ3_S` `262k` 上下文）**：将 `20,000–45,000` 个系统与 MCP 工具定义 Token 持久化缓存在 SSD 上，新开会话直接命中缓存，热启动首字延迟（TTFT）仅 **`~200 ms`**，单流解码 **`~170 tok/s`**，并发总吞吐达 **`~375 tok/s`**；
  2. **三重互补的 DaVinci Resolve Studio 21.2 MCP 矩阵**：
     - 社区 Python `davinci-resolve` MCP（约 36 个实时媒体池、时间线、波纹剪辑与护栏工具）；
     - 社区 Node `davinci-resolve-advanced` MCP（负责离线数据库、DRX 调色静帧、DRT 时间线模板与 QC）；
     - Blackmagic 官方内置 `DaVinci Resolve` MCP（Studio 21.1+ 原生随附）；
  3. **Dry-Run / Confirm-Token 安全纪律 + `ffprobe` 闭环读回验证**：OpenCode 在修改时间线前强制执行预演与确认令牌纪律，并在渲染后调用 `ffmpeg / ffprobe` 读取真实帧率、编码与抽帧自检；
  4. **无头 Blender Cycles Metal 透明 EXR 字幕流水线**：后台自动调用 Blender（Metal 硬件加速 + `film_transparent`）渲染高品质 EXR 序列并自动导入达芬奇时间线。

### Q2：`dryang21/Fundlark` 是如何帮科研人员与创新团队避开“假截止日期”与“无资格白写申请书”两大深坑的？
- **三大诚实核验机制（支持网页端、任意联网聊天助手与 Claude Code / Codex / Cursor 技能，`MIT`）**：
  1. **严格区分“课题相关（Relevant）”与“符合申报资格（Eligible）”**：明确核查博士毕业年限、入职时间窗口、所属机构资质（如 HHMI 准入名单、学会会员要求），并标明是个人可直接申报（*Apply yourself*）还是必须经校方/导师提名；
  2. **官网直连核验 + `Date to confirm` 零幻觉降级**：每条推荐必须附带资助方官方原始链接与精确到时区的截止时间；若官网暂时无法访问，**严禁猜测日期，强制归入 `Date to confirm`（待确认日期）栏**；
  3. **内置申报看板（Tracker）**：支持在浏览器中按学科、职业阶段与关键词标签筛选并保存拟申报清单。

### Q3：`ruvnet/mouse-swarm` 如何把静态落地页秒变“多智能体协同搭建”的视觉盛宴？
- **双模式多光标编排引擎（`MIT`，支持 Claude Code 与 Codex 技能一键安装）**：
  - **模式一（Sequential DOM Reveal 视觉编排）**：按文档流顺序依次浮现页面元素、为叶节点文字添加打字机效果，并驱动一群带不同颜色与名称标签的 Agent 光标围绕元素移动、框选与构建（支持 `replay / pause / resume / skip` 完整播放控制）；
  - **模式二（Ruflo 本地集群实时观测）**：可读取并可视化本机 CLI Agent 的注册与上报状态，且严格保持只读展示（绝不越权控制电脑或偷启后台进程）。

---

## 🧭 三、端到端集成参考架构与选型决策树（Mermaid）

```mermaid
flowchart TD
    subgraph ResolveWorkstation["100% 本地 AI 后期工作站：resolve-ai-workflow (★30, MIT)"]
        A[Splash 本地引擎 Qwen3.8-Flash-Next 262k<br/>SSD 持久化前缀缓存复用 20k–45k Token · TTFT ~200ms] --> B[OpenCode 算子 + dry-run/confirm-token 纪律]
        B --> C[3 大 DaVinci Resolve MCP 协同<br/>官方 MCP + 实时剪辑 MCP + 离线 DRX/DRT/DB MCP]
        C --> D[无头 Blender Metal 渲染透明 EXR 字幕<br/>+ ffmpeg/ffprobe 闭环读回质检]
    end

    subgraph FundAndSwarm["官方核验科研基金与多光标演示：Fundlark (★30, MIT) + mouse-swarm (★30, MIT)"]
        E[dryang21/Fundlark 基金发现技能<br/>区分 Apply yourself 资格 + 官网核验截止日 + Date to confirm 防幻觉]
        F[ruvnet/mouse-swarm 落地页多光标编排<br/>DOM 顺序生长 + 彩色 Agent 光标协同 + Ruflo 状态观测]
    end
```

---

## 📊 四、同赛道方案横向选型对比矩阵（Decision Matrix）

| 评估维度 | 方案 A：上传云端视频 API + 通用 AI 盲搜基金 + 手K多鼠标动画 | 方案 B：单 MCP 无缓存脚本 + 手工维护基金 Excel | **方案 C（推荐）：`resolve-ai-workflow` + `Fundlark` + `mouse-swarm` (MIT)** |
| :--- | :--- | :--- | :--- |
| **后期剪辑数据隐私、工具覆盖度与首字响应** | ❌ 机密素材外传泄密且按分钟高价计费 | ⚠️ 单一 MCP 缺离线调色/模板能力，无 SSD 缓存每次冷启动慢 | ✅ **100% 本地闭环、SSD 缓存复用 `20k–45k` Token（`~200ms` TTFT）、3 MCP + Blender EXR** |
| **科研基金/专项申报的资格匹配与日期准确性** | ❌ 常把“仅限机构提名”推给个人，或编造过期日期 | ⚠️ 手工翻几十个基金会网站耗时极长 | ✅ **强制核对官网并标注 `Apply yourself` 资格，不可达网页诚实标 `Date to confirm`** |
| **多 Agent 协同构建落地页的视觉演示成本** | ❌ 在 AE/Premiere 里手K十几个光标轨迹耗费数天 | ⚠️ 静态截图缺乏多智能体并发协作的视觉冲击力 | ✅ **`mouse-swarm` 自动按 DOM 顺序生长并编排多色光标与打字动画，支持交互回放** |
| **月度总拥有成本（TCO，25 人 / 450 次工作流）** | **`$5,660.00 / 月`**（含 `$2,240` 云视频/数据库费 + `36.0h` 人工） | **`$2,400.00 / 月`**（含 `$880` API 费 + `16.0h` 手工核对） | **`$336.00 / 月`**（**净省 `-94.06%`**，仅 `$70` 本地缓存存储与 `2.8h` 确认令牌/资格终审） |

---

## 🧮 五、7-Card 定量洞察与闭式 FinOps 核算（`CLAIM-20261117-R51-RESOLVEAI-FUNDLARK-MOUSESWARM`）

> **核算范围与边界声明**：面向 25 名影视后期工程师、科研项目申报负责人与产品演示开发者团队，每月执行 **450 次 DaVinci Resolve/Blender 后期成片、官方基金资格核查与多光标交互演示制作**（综合时薪 `$95.00/hr`；本地硬件工作站与 Resolve Studio 永久授权标记为 `not_measured`）：

$$\text{Total Monthly TCO} = \text{Cloud Video/Grant SaaS Spend} + (\text{Manual Timeline/Grant/Demo Hours} \times \$95.00)$$

| 成本构成项 | Path A：云端视频 API + 盲搜基金 + 手K光标 | Path B：无缓存单 MCP + 手工表格 | **Path C：`resolve-ai` + `Fundlark` + `mouse-swarm`** |
| :--- | :---: | :---: | :---: |
| **月度云端视频代理 API 与商业基金数据库开销** | `$2,240.00` | `$880.00` | **`$70.00`** |
| **月度手拉时间线、逐站查基金细则与手K光标工时** | `36.0 hrs` | `16.0 hrs` | **`2.8 hrs`**（直降 **`92.22%`**） |
| **月度后期、科研与前端工程师人工成本（`@ $95.00/hr`）** | `$3,420.00` | `$1,520.00` | **`$266.00`** |
| **月度总拥有成本（Monthly TCO）** | **`$5,660.00`** | **`$2,400.00`**（`-57.60%`） | **`$336.00`**（**`-94.06%`**） |
| **相对 Path A 净节省（月度 / 年化）** | 基线（`$0.00`） | `$3,260.00 / 月`（`$39,120/年`） | **`$5,324.00 / 月`（`$63,888.00 / 年`）** |

---

## ✅ 六、AI 解决方案架构师实战上手 Checklist（SA Action Checklist）

- [ ] **Step 1 — 部署 `willturner-maker/resolve-ai-workflow` 搭建零上云达芬奇工作站**：启用 `Splash` 持久化 SSD 前缀缓存（复用 `20k–45k` Token），挂载官方 + 社区实时 + 社区离线 3 个 Resolve MCP，并开启 `dry-run / confirm-token` 与 `ffprobe` 读回自检。
- [ ] **Step 2 — 集成无头 Blender Metal EXR 字幕管线**：将片头与技术图解交由无头 Blender Cycles 渲染为 `film_transparent` EXR 序列并自动置入 Resolve 时间线。
- [ ] **Step 3 — 安装 `dryang21/Fundlark` 技能规范科研与创新项目申报**：要求所有申报立项必须通过 `Fundlark` 核查官网实时截止时间、明确 `Apply yourself` 资格并对不可达页面诚实标注 `Date to confirm`。
- [ ] **Step 4 — 使用 `ruvnet/mouse-swarm` 为产品官网与发布会制作多光标构建动画**：安装 Claude Code / Codex 技能一键为静态落地页注入 DOM 顺序生长与多智能体光标协同动效。
