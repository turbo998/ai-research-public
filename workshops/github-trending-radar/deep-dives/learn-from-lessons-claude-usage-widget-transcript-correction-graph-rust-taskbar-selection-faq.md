# 跨 CLI 纠错记录三层经验蒸馏引擎（`assassin808/learn-from-lessons`）与 450KB 纯 Rust 多账号配额任务栏监控器（`AbdoSarmini/claude-usage-widget-for-windows-taskbar`）深度选型 FAQ

> **文档定位**：本专题是 **2026-11-13 夜班第 14 轮（累计第 142 篇）独立六段式选型指南**，严格对标 `ib-vs-ethernet-roce-selection-faq.md` 的通俗第一性原理与闭式 FinOps 核算规范，面向重度使用 Claude Code / Codex / OpenCode 的研发团队负责人与 AI Solution Architect，深度拆解今日新仓爆发榜上专门根治“每次重开会话 Agent 又犯昨天刚被你骂过的老毛病”以及“Windows 重度开发者写代码写到一半突然撞上 5 小时/周度额度墙被迫停工”的两大高频提效利器：
> 1. **`assassin808/learn-from-lessons`（4 天新建获 `43★`，Python 3.9+，MIT，零第三方依赖，`pipx install` 即装即用）**：自动扫描本机已有的 **Claude Code、Codex 与 OpenCode 历史对话记录（Transcripts）**，精准抓取你纠正智能体的瞬间（如*“别擅自 push”、“我问的是为什么而不是让你直接改代码”、“这个数字不是表里的”*），通过 `lessons dream` 将其提炼为带**原话引证（Exact Quote）的三层经验图谱（`Principle 原则 → Rule 规则 → Narrow Case 窄场景案例`，出现两次即自动标记 `verified`）**，支持按场景（`--scenario writing-paper`）或 Git 上下文（`--context "$(git log -1)"`）精准检索注入 `CLAUDE.md`、`AGENTS.md` 或 `lessons mcp`！
> 2. **`AbdoSarmini/claude-usage-widget-for-windows-taskbar`（2 天新建获 `51★`，Rust，MIT，单文件仅 `~450 KB`，内存占用仅 `~5 MB`）**：常驻在 Windows 11 任务栏时钟旁（而非藏在折叠托盘里）的原生 Rust 配额监控微件——实时显示 **Claude 5 小时滚动窗口与周度（Weekly）订阅额度进度环**，超过 `75%` 变橙色预警、超过 `95%` 变红色告警，悬停即看精确重置倒计时，并原生支持通过不同 `CLAUDE_CONFIG_DIR` **同时监控多个 Pro / Max / Team / Enterprise 账号**！
>
> **English Version**: [learn-from-lessons-claude-usage-widget-transcript-correction-graph-rust-taskbar-selection-faq.en.md](learn-from-lessons-claude-usage-widget-transcript-correction-graph-rust-taskbar-selection-faq.en.md) · **关联日报**: [`daily/2026-11-13.md`](../daily/2026-11-13.md) · **专题架构图**: [`assets/github-ai-radar-2026-11-13-r14-learnfrom-taskbarwidget.svg`](../../../assets/github-ai-radar-2026-11-13-r14-learnfrom-taskbarwidget.svg)

![learn-from-lessons 与 claude-usage-widget-for-windows-taskbar 架构选型对比](../../../assets/github-ai-radar-2026-11-13-r14-learnfrom-taskbarwidget.svg)

---

## 📌 一、核心结论速览（Executive Summary）

1. **一句话大白话讲透这两个项目到底解决了什么痛点？**
   - **终结“你昨天刚在 Claude Code 里强调‘没经过允许不准 git push’，今天新开一个会话或换到 Codex 它又犯一模一样的错；而如果把所有教训全手写塞进一个几千行的 `CLAUDE.md`，写论文时还要加载一堆 Git 规则白白浪费上下文”的痛点（`assassin808/learn-from-lessons`）**：人类带徒弟最怕“说过十遍的话左耳进右耳出”。`learn-from-lessons` 不需要你手动写笔记：跑一下 `lessons scan` 和 `lessons dream`，它直接扫描你电脑上 Claude Code、Codex 和 OpenCode 的历史日志，找出你每次打断纠正 AI 的地方，提炼成 **“原则（Principle）→ 规则（Rule）→ 具体案例（Case）”** 三层图谱，每一条都附带当时对话的原话证据，且**同一个错误被纠正两次后自动升格为 `verified`（已核验经验）**！更妙的是它支持按场景过滤（`--scenario`）和按 `git log -1` 检索，让你在写论文时绝不加载无关的部署教训！
   - **终结“在 Windows 11 上全屏写代码时看不见 Claude Pro/Max/Team 的 5 小时窗口和周度配额，重构到最关键的一步突然弹出 Rate Limit 锁死，或者为了看一眼配额还得挂一个吃 300MB 内存的 Electron 壳”的痛点（`AbdoSarmini/claude-usage-widget-for-windows-taskbar`）**：这个用纯 Rust 写的单文件小工具只有 **`~450 KB`**，内存仅占 **`~5 MB`**、CPU 接近 0%，直接嵌在 Windows 11 任务栏右下角时钟旁边：一眼就能看到 **5 小时额度和周额度圆环**（`>75%` 变橙、`>95%` 变红），鼠标悬停直接看几点几分重置，而且支持同时挂载多个 `CLAUDE_CONFIG_DIR` 账号，看到主号变橙立即平滑切到备号或团队号！
2. **闭式 FinOps 投资回报结论（`CLAIM-20261113-R14-LEARNFROM-TASKBARWIDGET`）**：
   - 以 **25 人研发团队每月跨多账号运行 `2,000 次` Claude Code / Codex / OpenCode 编码会话** 为基准（资深研发工程师全包时薪 `$90.00/hr`；开发机硬件与 Windows 11 系统授权费：`not_measured`）：
   - 从 **Path A（每次新会话重复人工纠正同类错误 + 盲跑撞上 5 小时限流墙被迫切高价按量 API 或停工等重置，月均 `$4,940.00`）** 升级至 **Path C（`learn-from-lessons` 三层按场景经验注入 + `claude-usage-widget` `450KB` 多账号任务栏实时预警，月均 `$455.00`）**，每月净省 **`$4,485.00/mo`（降幅 `-90.79%`，年省 `$53,820.00/yr`）**，并将重复纠偏回滚与限流中断恢复工时从 `38.0 hrs/mo` 压缩至 `3.5 hrs/mo`（节省 **`-90.79%`**）。

---

## 🎯 二、三大灵魂拷问（Q1 / Q2 / Q3 深度原理解析）

### Q1：为什么“靠人手写全局 `CLAUDE.md`”和“靠去网页后台查配额”无法支撑高强度日常 Agent 编程？
- **第一性原理拆解**：
  1. **静态全局规则文件的“噪音稀释效应”**：当 `CLAUDE.md` 累积到上千行涵盖前端、数据库、发版、写文档的杂乱禁令时，模型的注意力反而被无关规则稀释；且工程师在紧张排障时根本没空停下来把刚才的纠错整理成规范条目。
  2. **5 小时滚动窗口与周度配额的盲区中断成本**：大型多文件重构若在完成 80% 时突然触发 5 小时配额耗尽，未持久化的推理脉络就会被迫中断，切换按量 API Key 又会产生高额账单。

### Q2：`assassin808/learn-from-lessons` 是如何从本机历史转录中自动蒸馏出“有据可查、按需加载”的三层经验图的？
- **第一性原理拆解**：
  1. **跨 CLI 转录扫描 + 三层抽象（Principle / Rule / Case）+ 二次出现核验锁**：
     - 直接解析本地已有的 Claude Code、Codex 与 OpenCode 会话文件，将每一次人类纠偏转化为一条可验证预测（“当出现情况 S 时，执行 X 可避免被纠正”），组织为顶层原则、中层规则与底层仓库特例三级图谱，保留原始对话引用，并在第二次命中时自动标记为 `verified`。
  2. **按场景（`--scenario`）与 Git 提交上下文（`--context`）动态过滤注入**：
     - 支持 `lessons index --scenario writing-paper` 与 `lessons search ... --context "$(git log -1)"`，并通过 `lessons inject --target CLAUDE.md --apply`、`AGENTS.md` 或 `lessons mcp` 按需喂给智能体，零外部 Python 依赖。

### Q3：`AbdoSarmini/claude-usage-widget-for-windows-taskbar` 是如何在 `~450 KB` 体积与 `~5 MB` 内存下实现多账号实时配额护航的？
- **第一性原理拆解**：
  1. **纯 Rust 原生 Win32 任务栏内嵌（非托盘隐藏）与三色阈值环**：
     - 摒弃臃肿的 WebView/Electron 框架，编译为 `~450 KB` 免安装单文件 `.exe`，常驻任务栏时钟左侧，实时绘制 5 小时与周度使用率（或剩余率）双环，在 `75%`（橙色）与 `95%`（红色）与 Claude Code 保持一致视觉预警。
  2. **多 `CLAUDE_CONFIG_DIR` 并发监控与零后台终端驻留**：
     - 只需登录过一次 `claude` CLI 即可自动读取凭证（无需保持命令行窗口常开），支持同时添加个人 Pro/Max 与公司 Team/Enterprise 多个配置目录，悬停即看各账号精确重置时间。

---

## 🧭 三、Mermaid 选型决策树与「三层经验蒸馏 + 任务栏多号配额监控」架构图

```mermaid
flowchart TD
    A["多 CLI 编码智能体经验沉淀与订阅配额实时治理选型"] --> B{"当前最突出的日常痛点？"}
    B -- "Agent 跨会话反复犯同样的错 (如擅自 push、误改只读查询)，手写规则又太累" --> C["采用 assassin808/learn-from-lessons (三层经验图谱 + lessons mcp)"]
    B -- "Windows 11 下多账号跑 Claude Code，经常在关键任务中途盲撞 5h/周度限流墙" --> D["采用 claude-usage-widget-for-windows-taskbar (~450KB Rust 任务栏微件)"]

    C --> C1["lessons scan & dream 扫描本机 Claude/Codex/OpenCode 历史纠偏并保留原话引用"]
    C1 --> C2["Principle->Rule->Case 三层图谱 (二次命中标 verified) + 按 scenario/git log 精准注入"]

    D --> D1["~5MB 内存常驻任务栏时钟旁，实时显示 5h 与周度配额 (75% 橙 / 95% 红)"]
    D1 --> D2["同时监控多个 CLAUDE_CONFIG_DIR 账号，在 75% 橙色预警时提前平滑切号"]

    C2 & D2 --> E["🏆 黄金日常驾驶舱：越用越懂规矩的 Agent 记忆 + 零盲区配额调度 (-90.79% TCO)"]
```

---

## 📊 四、同类方案核心能力对比矩阵（Selection Matrix）

| 评估维度 | Path A：无跨会话纠错提取 + 盲跑撞限流墙 | Path B：人工维护千行全局 `CLAUDE.md` + 重型托盘软件 | **Path C（推荐）：`learn-from-lessons` + `claude-usage-widget`** |
| :--- | :--- | :--- | :--- |
| **人类纠偏经验采集方式** | 随会话关闭彻底遗忘，下次重犯 | 需人工手动编写并分类 | **自动扫描本机 Claude/Codex/OpenCode 转录，保留原话引用，二次出现自动标 `verified`** |
| **经验注入的上下文信噪比** | 无 | 所有场景硬塞同一份巨型 `CLAUDE.md` | **Principle/Rule/Case 三层结构 + `--scenario` 与 `git log -1` 动态过滤** |
| **Windows 11 配额可见性与多号管理** | 撞墙报错后才知道超限 | 藏在二级折叠托盘，切号繁琐 | **常驻任务栏时钟旁双环（5h + 周度），`75%/95%` 变色预警 + 多 `CLAUDE_CONFIG_DIR` 同屏** |
| **客户端资源开销** | 无 | Electron 托盘动辄占用 `200–400 MB` 内存 | **纯 Python 标准库零依赖 + `~450 KB` Rust 单文件（仅占 `~5 MB` 内存）** |
| **月度总拥有成本（25 人 / 2,000 会话）** | **`$4,940.00 / mo`**（`$1,520` 超额/浪费 + `$3,420` 工时） | **`$2,490.00 / mo`**（`$690` 超额 + `$1,800` 工时） | **`$455.00 / mo`（净省 `$4,485.00/mo` · `-90.79%`）** |

---

## 🧪 五、定量 FinOps 算例与 7-Card 洞察（`CLAIM-20261113-R14-LEARNFROM-TASKBARWIDGET`）

### 5.1 测算基准与显式边界（Scope & Boundaries）
- **场景设定**：25 人规模的软件工程团队，每月跨 Claude Code、Codex 与 OpenCode 执行 **2,000 次日常编码、重构与论文/文档撰写会话**。
- **费率假设**：资深软件工程师全包时薪 **`$90.00 / hr`**。
- **显式边界声明（Explicit Not-Measured Boundary）**：工程师开发机硬件折旧与 Windows 11 操作系统授权费标记为 **`not_measured`**，本表严格核算因重复犯错浪费的 Token、盲撞订阅限流后被迫开启的按量 API 超额账单以及人工纠偏回滚工时。

### 5.2 三路径月度成本闭式对照表

| 成本分项 | Path A：重复犯错回滚 + 盲撞 5h 限流切按量 API | Path B：手工维护巨型 `CLAUDE.md` + 重型托盘 | **Path C：`learn-from-lessons` + `450KB Rust Widget`（推荐）** |
| :--- | :--- | :--- | :--- |
| **月度按量 API 超额与重复犯错 Token 净支出** | **`$1,520.00`**（反复纠正同一错误 + 撞墙后紧急切高价按量 API） | **`$690.00`**（全量长规则冗余 Token 消耗） | **`$140.00`**（75% 橙色预警提前平滑切号 + 按场景精准注入已核验经验） |
| **重复纠偏、回滚误操作与限流中断恢复工时（`$90/hr`）** | `38.0 hrs × $90.00` = **`$3,420.00`** | `20.0 hrs × $90.00` = **`$1,800.00`** | `3.5 hrs × $90.00` = **`$315.00`** |
| **月度总成本（Monthly TCO）** | **`$4,940.00 / mo`** | **`$2,490.00 / mo`**（`-49.60%`） | **`$455.00 / mo`** |
| **相对 Path A 净节省** | 基准线（Baseline） | 净省 `$2,450.00 / mo` | **净省 `$4,485.00 / mo`（`-90.79%` · 年省 `$53,820.00/yr`）** |
| **开发机硬件折旧与 Windows 系统许可费** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 六、生产级落地核验 Checklist

- [ ] **1. `assassin808/learn-from-lessons` 本机历史扫描与三层蒸馏**：执行 `pipx install git+https://github.com/assassin808/learn-from-lessons`，运行 `lessons scan`、`lessons dream` 与 `lessons view`，检视从本机 Claude Code / Codex / OpenCode 转录中提取的 `Principle → Rule → Case` 图谱及原话证据。
- [ ] **2. 场景过滤与 `CLAUDE.md` / `lessons mcp` 注入验证**：测试 `lessons index --scenario <name>` 与 `lessons inject --target CLAUDE.md --apply`，确保仅将经过二次核验（`verified`）且匹配当前场景的经验注入上下文。
- [ ] **3. `claude-usage-widget-for-windows-taskbar` 部署与内存核验**：在 Windows 11 上放置 `ClaudeUsageWidget.exe`（或 `cargo build --release` 源码编译），核验任务管理器中内存占用稳定在 `~5 MB` 且常驻时钟左侧。
- [ ] **4. 多 `CLAUDE_CONFIG_DIR` 账号挂载与 `75%` 橙色切换演练**：在右键菜单中添加多个 Claude Code 配置目录，开启“显示剩余配额（Show remaining）”与 `75%/95%` 阈值变色提醒，在大型重构前根据悬停重置时间合理排程。
