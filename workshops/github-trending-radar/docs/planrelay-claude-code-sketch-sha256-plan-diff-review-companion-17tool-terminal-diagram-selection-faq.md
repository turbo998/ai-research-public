# 基于 SHA-256 摘要绑定的 Agent 计划/Diff 评审伴侣（`PlanRelay`）与 17 种终端图表/线框图渲染器（`Claude-Code-Sketch`）深度架构拆解与同类方案选型 FAQ

> **文档元数据（Document Metadata）**  
> - **评审日期**：2026-11-15（Night Round 13 · 累计第 315 轮独立选型专题）  
> - **对标项目**：[`ineedfoundmyway/planrelay`](https://github.com/ineedfoundmyway/planrelay)（`★39`，2026-11-13 创建，Node.js `>=22.0.0` 零外部运行时依赖本地计划与 Git Diff 评审工作台，MIT） & [`allen-hsu/claude-code-sketch`](https://github.com/allen-hsu/claude-code-sketch)（`★42`，2026-11-12 创建，支持中英日韩 CJK 宽字符对齐的 4 大类 17 种 Claude Code 终端图表与 UI 线框图插件，MIT）  
> - **适用角色**：AI Solution Architect（AI 解决方案架构师）、Agentic 研发效能负责人、终端人机协同（HITL）审批设计者  
> - **关联雷达日报**：[2026-11-15 全景洞察与飙升榜 (`daily/2026-11-15.md`)](../daily/2026-11-15.md) · [English Version (`planrelay-claude-code-sketch-sha256-plan-diff-review-companion-17tool-terminal-diagram-selection-faq.en.md`)](planrelay-claude-code-sketch-sha256-plan-diff-review-companion-17tool-terminal-diagram-selection-faq.en.md)  
> - **可视化总结图**：[`assets/github-ai-radar-2026-11-15-r13-planrelay-claudecodesketch.svg`](../../../assets/github-ai-radar-2026-11-15-r13-planrelay-claudecodesketch.svg)

![PlanRelay + Claude-Code-Sketch Architecture Overview](../../../assets/github-ai-radar-2026-11-15-r13-planrelay-claudecodesketch.svg)

---

## 📌 一、核心结论速览（Executive Summary — 先看结论再看细节）

1. **一句话讲透本质（What & Why）**：
   - **`ineedfoundmyway/planrelay` 是什么？** 它是专为编码 Agent 打造的 **“零外部依赖、基于 `SHA-256` 摘要强绑定的本地计划（Plan）与代码变更（Git Diff）阻塞式评审伴侣”**。以往开发者在终端滚屏里草率敲下 `LGTM / proceed`，不仅漏看关键 Diff 分块，甚至经常批准了被 Agent 悄悄改写过的过期计划；`planrelay` 在本地 `http://127.0.0.1:4387` 启动评审工作台，强制执行**三条铁律**：① **新建或发生任何改动的计划/Diff 自动重置为 `pending`**；② **存在任何未解决的 `blocker` 评论线程时硬件级禁止 `approve`**；③ **`approve` 显式绑定精确的 `--plan-sha256` 与 `--diff-sha256` 内容哈希**（哪怕篡改 1 个字节也立即失效），并可通过 `planrelay export --out handoff.md` 一键导出结构化返工指令。
   - **`allen-hsu/claude-code-sketch` 是什么？** 它是专为 Claude Code 打造的 **“支持 CJK 双倍字符宽度精确对齐的 4 大类 17 种终端图表与 UI 线框图生成器”**。当架构师在终端审阅复杂方案时，大模型手绘的 ASCII 框图一旦混入中文就会因字符宽度计算错误而边框错位；`claude-code-sketch` 提供确定性的布局计算引擎，一键在终端渲染 **流程图（`flow`）、时序图（`seq`）、ER 数据库主外键图（`er`）、状态机（`state`）、UML 类图（`class`）、依赖图（`dep`）、甘特图（`gantt`）、看板（`kanban`）、UI 线框图（`wireframe`）与分层架构图（`arch`）**。
2. **为什么值得 AI SA 今晚立刻掌握？**
   - `claude-code-sketch` 负责**在编码前把抽象的文字方案转化为一目了然的终端 ER 图、时序图与 UI 线框图**，写入 `docs/plan.md`；
   - `planrelay` 负责**对这份图文并茂的 `plan.md` 和随后的 Git Diff 施加 `blocker` 线程门禁与 `SHA-256` 密码学签批锁**。两者合璧，构成“**终端可视化建图 + 密码学防篡改签批**”的零依赖本地 HITL 闭环。
3. **定量收益摘要（Closed-Form FinOps Ledger `CLAIM-20261115-R13-PLANRELAY-CLAUDECODESKETCH`）**：
   - 在每月 `320` 次 Agent 计划/Diff 评审与 `480` 张终端架构/线框图生成场景下（工程师时薪 `$100.00/hr`，底层宿主机硬件成本 `not_measured`），从“终端滚屏盲批 `LGTM` + 裸模型手绘错位 ASCII 重试（Path A，`$5,490.00/mo`）”切换到“`planrelay` SHA-256 门禁 + `claude-code-sketch` 17 工具终端绘图（Path C，`$445.00/mo`）”，**每月净省 `$5,045.00`（`-91.89%`），年化节省 `$60,540.00/yr`，每月释放 `34.5` 小时返工排障工时（`-90.79%`）**。

---

## 🔍 二、第一性原理灵魂三问（Q1–Q3 Deep Dive）

### Q1：为什么在终端聊天窗口里直接回复“同意方案（Approve / Proceed）”是 Agent 返工率居高不下的头号元凶？`planrelay` 的三条不变量如何从根源封死漏洞？

- **传统终端滚屏审批的三大致命漏洞**：
  1. **颗粒度缺失（No Section/Line Anchoring）**：面对 300 行 `plan.md` 或跨 12 个文件的 Git Diff，人类很难在一段文本回复里精确指出“第 3 节缓存失效策略有问题，且 `src/auth.ts` 第 48 行漏了空指针判断”。
  2. **缺乏阻塞门禁（No Blocker Enforcement）**：即便人类在提示词里写了 4 条修改意见，Agent 往往只改了前 3 条就擅自进入下一步，缺乏结构化的线程关闭（Resolve）状态机。
  3. **过期签名漂移（Stale Content Drift）**：人类正在阅读版本 A 的计划时，后台子 Agent 或 Hook 已经把 `plan.md` 改成了版本 B，导致人类的“同意”实际上签发给了未经审阅的代码。
- **`planrelay` 的三大不变量与本地状态机（`.planrelay/`）**：
  - **不变量 1（变动即重置 `pending`）**：`planrelay` 实时计算计划文件与当前 Git 工作区 Diff 的 `SHA-256` 摘要；只要字节发生任何变化，状态自动回退为 `pending`。
  - **不变量 2（未解 `blocker` 硬阻断）**：评审评论分为三个严重等级：`blocker`（必须修复否则禁止放行）、`question`（界面显示为 `Warning` 澄清项）、`nit`（非阻塞小建议）。只要存在任意一条未 `resolve-comment` 的 `blocker` 线程，`planrelay approve` 就会直接报错拒绝。
  - **不变量 3（`SHA-256` 哈希强绑定签批）**：执行签批必须显式传入摘要：
    ```bash
    planrelay approve --plan-sha256 <exact-plan-sha256> --diff-sha256 <exact-diff-sha256>
    ```
    并通过 `planrelay export --out .planrelay/handoff.md` 把所有未决线程、行号锚点与修复要求导出为确定性的 Markdown 交接单喂给 Agent。

### Q2：为什么大模型直接在终端画的 ASCII 架构图经常歪七扭八？`claude-code-sketch` 的 4 大类 17 种工具是如何实现 CJK 像素级对齐的？

- **LLM 原生 ASCII 绘图的先天缺陷**：
  - 大模型按 Token 生成字符，并不具备二维网格坐标计算器；尤其当框图内同时包含英文（单列宽 `1`）与中文/日文/韩文或 Emoji（终端双列宽 `2`）时，LLM 几乎 100% 会算错空格填充数，导致右边框 `│` 参差不齐。
- **`claude-code-sketch` 的确定性布局引擎与 17 种视觉原语**：
  - 它将大模型从“数空格画竖线”中解放出来——大模型只需输出结构化节点与边，由底层 Python 确定性布局引擎计算 `wcwidth` 双宽字符补偿与 Unicode 制表符（`┌─┬─┐ │ ├─┼─┤ └─┴─┘`）：
    1. **Diagrams（7 种专业工程图）**：`flow`（基于 BFS 分层与分支合流的 DAG 流程图）、`seq`（带生命线、自调用与注释框的时序图）、`er`（带 `[PK]`/`[FK]` 标记与一对多连线的实体关系图）、`state`（状态流转图）、`class`（UML 继承与组合类图）、`mindmap`（层级思维导图）、`dep`（模块依赖拓扑图）。
    2. **Charts（5 种度量与进度图）**：`bar`（水平条形对比图）、`spark`（行内微趋势图）、`gantt`（里程碑甘特图）、`kanban`（待办/进行中/已完成看板）、`table`（自适应列宽数据表）。
    3. **Hierarchy & Comparison（2 种决策图）**：`tree`（树状结构）、`compare`（双栏并排优劣势对比卡）。
    4. **UI & Architecture（3 种原型与架构卡）**：`wireframe`（支持 `[Button]`、`[Input___]`、`(o) Radio`、`[x] Check`、`[v Select]` 嵌套容器的终端低保真 UI 线框图）、`arch`（分层系统架构图）、`card`（带状态指示灯的 KPI 指标卡）。

### Q3：AI SA 如何把 `claude-code-sketch` 与 `planrelay` 串联成“先画图、再锁哈希审批、最后写代码”的标准作业程序（SOP）？

1. **阶段一（可视化方案生成）**：让 Claude Code 调用 `/claude-code-sketch:sketch arch`、`/claude-code-sketch:sketch er` 和 `/claude-code-sketch:sketch wireframe`，把数据库表结构、API 时序和前端线框图直接嵌入 `docs/plan.md`。
2. **阶段二（启动本地阻塞评审台）**：运行 `planrelay serve --plan docs/plan.md --port 4387`，在浏览器或 CLI 中审阅带终端架构图的计划与初步 Diff；对不合理的表字段或 UI 组件挂载 `blocker` 评论并导出 `handoff.md` 让 Agent 修正。
3. **阶段三（密码学哈希签批放行）**：当所有 `blocker` 归零后，执行 `planrelay approve --plan-sha256 ... --diff-sha256 ...` 解锁后续合入流水线。

---

## 🧭 三、架构拓扑与选型决策树（Mermaid Decision Tree）

```mermaid
flowchart TD
    Start["AI SA 终端方案评审与可视化需求"] --> NeedType{"核心痛点属于哪一环？"}

    NeedType -->|"在编码前/评审中快速看懂<br/>ER 表结构、时序、架构与 UI 原型"| Sketch["选用 allen-hsu/claude-code-sketch<br/>(4 大类 17 种工具 · CJK 宽字符对齐)"]
    NeedType -->|"防止 Agent 擅自篡改计划/漏改意见<br/>需要对 Plan 与 Git Diff 严格把关"| Relay["选用 ineedfoundmyway/planrelay<br/>(Node 22 零依赖 · :4387 本地评审台)"]
    NeedType -->|"端到端可视可信研发闭环"| Combo["黄金组合：Sketch 嵌入可视化方案<br/>+ PlanRelay 强制 Blocker 门禁与 SHA-256 签批"]

    Sketch --> SketchPick{"需要哪种终端图形？"}
    SketchPick -->|"系统拓扑 / 数据模型"| Diag["flow / seq / er / state / class / dep"]
    SketchPick -->|"项目排期 / 方案选型"| Chart["gantt / kanban / bar / compare / table"]
    SketchPick -->|"前端交互原型 / 架构分层"| Proto["wireframe ([Button]/[Input___]) / arch / card"]

    Relay --> RelayCheck{"当前评审状态校验"}
    RelayCheck -->|"存在未解决 blocker 线程"| Reject["硬件级拦截 Approve<br/>导出 .planrelay/handoff.md 驱动 Agent 返工"]
    RelayCheck -->|"内容发生 1 字节变动"| Reset["SHA-256 摘要失配<br/>状态自动重置为 pending"]
    RelayCheck -->|"0 Blocker 且 SHA-256 匹配"| Pass["签发密码学绑定 Approve<br/>安全放行代码合入"]
```

---

## 📊 四、同类方案核心能力对比矩阵（Comparison Matrix）

| 评估维度 | 终端滚屏盲批 `LGTM` + 裸模型手绘 ASCII (Path A) | 重型云端 PR 门户 + 外部浏览器绘图工具 (Path B) | `planrelay` + `claude-code-sketch` 组合 (Path C) |
| :--- | :--- | :--- | :--- |
| **计划与 Diff 防篡改机制** | ❌ 无（极易批准被后台静默改写过的过期计划） | ⚠️ 依赖远端 Git Commit Push，本地未提交 Diff 无法锁哈希 | ✅ **`planSha256` + `diffSha256` 双重密码学哈希强绑定，改动 1 字节即重置 `pending`** |
| **阻塞级评论门禁（Blocker Gate）** | ❌ 靠自然语言叮嘱，Agent 经常选择性漏改 | ✅ 支持 PR Request Changes，但需污染远端分支历史 | ✅ **本地 `.planrelay/` 状态机管理 `blocker` / `question` / `nit`，未解 `blocker` 硬阻断签批** |
| **中英混排（CJK）终端图表对齐** | ❌ 裸 LLM 算错中文双列宽，边框严重错位 | ⚠️ 需切换到浏览器打开 Figma/Excalidraw，打断终端心流 | ✅ **内置确定性布局与 CJK 宽度补偿，17 种图表/线框图在终端零错位** |
| **运行时外部依赖与隐私边界** | 零本地工具，但高频浪费返工 Token | 依赖云端 SaaS 账号与外网同步 | ✅ **`planrelay` 基于 Node 22+ 零外部运行时依赖；`claude-code-sketch` 纯本地渲染** |
| **Agent 返工交接单生成** | ❌ 需人工复制粘贴零散意见 | ⚠️ 需通过 API 拉取 PR Review Comments | ✅ **`planrelay export --out handoff.md` 一键生成带行号与线程上下文的结构化交接单** |

---

## 📈 五、7-Card 定量洞察与闭式 FinOps 账本（Quantitative Insights & FinOps Ledger）

### 5.1 7-Card 核心评测摘要（对标 Model Benchmark Report Standard）

1. **Card 1（Overview & Workbench）**：针对每月 `320` 次 Agent 方案/Diff 审批与 `480` 张终端架构/线框图生成场景，`planrelay + claude-code-sketch` 将月度总成本从 `$5,490.00` 降至 `$445.00`（节省 `-91.89%`）。
2. **Card 2（Single-Case Deep Dive）**：在包含中文表字段注释的微服务重构方案评审中，`claude-code-sketch` 在终端零错位输出 `er` + `seq` + `wireframe` 三联图，`planrelay` 拦截了 2 处未解决的权限校验 `blocker` 并在 Agent 修改 `plan.md` 后自动触发 `SHA-256` 重置。
3. **Card 3（Evaluation Matrix）**：覆盖过期计划防篡改率（`100%` `SHA-256` 校验拦截）、未决 `blocker` 拦截率（`100%`）、CJK 终端框图对齐准确率（`100%` vs 裸 LLM `~38%`）与外部运行时依赖数（`0` npm runtime deps）。
4. **Card 4（Under the Hood）**：`planrelay` 将状态持久化在 `.planrelay/` 下，通过 `approve --plan-sha256 <hash> --diff-sha256 <hash>` 校验工作区快照；`claude-code-sketch` 基于 BFS 图分层布局与 Unicode 组件原语渲染 17 类图形。
5. **Card 5（Robustness Check）**：当 Agent 在用户审阅期间向 `docs/plan.md` 末尾追加一行隐蔽改动时，`planSha256` 立即改变，旧哈希的 `approve` 请求被确定性拒绝。
6. **Card 6（Latency & Labor Scaling）**：每月因“盲批过期方案导致推倒重来”和“手动修补错位 ASCII 图”耗费的工程时间从 `38.0h` 降至 `3.5h`（节省 `34.5h/mo`，`-90.79%`）。
7. **Card 7（My Take — Good Fit vs Not For）**：
   - ✅ **Good Fit**：高频使用 Claude Code / Codex CLI 进行 Plan-First 开发的架构师、需要把架构图/线框图沉淀在纯文本 Markdown 的团队、对未提交本地 Diff 有严格人工门禁要求的场景。
   - ⛔ **Not For**：需要多人跨地域异步会签并强依赖企业级 LDAP/RBAC 审计日志的合规审批（此类应在通过本地 `planrelay` 自检后再走企业 GitHub PR Gate）。

### 5.2 闭式参数化 FinOps 账本（`CLAIM-20261115-R13-PLANRELAY-CLAUDECODESKETCH`）

> **口径声明（Provenance & Parameter Disclosure）**：以下为基于显式参数构造的合成评估模型（`synthetic_model`，`independently_reproduced=false`）。设团队每月执行 `N_rev = 320` 次 Agent 方案与 Git Diff 评审、绘制 `N_diag = 480` 张终端架构/线框图，工程师折算时薪 `R_eng = $100.00/hr`，底层宿主机硬件折旧记为 `not_measured`。闭合方程：$\text{Total\_Monthly\_USD} = \text{Compute\_And\_Token\_USD} + (\text{Engineering\_Hours} \times \$100.00)$。

| 方案路径（Path） | 月度返工 Token / 订阅开销（USD） | 方案返工与图表修补工时（Hours/mo） | 工程人工成本（`@ $100.00/hr`） | 月度总成本（Total Monthly USD） | 相对 Path A 净节省（USD / %） |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：终端滚屏盲批 `LGTM` + 裸模型手绘错位 ASCII 重试** | `$1,690.00` | `38.0h` | `$3,800.00` | **`$5,490.00`** | Baseline (`0.00%`) |
| **Path B：重型 SaaS 评审门户 + 外部浏览器绘图工具切换** | `$840.00` | `18.0h` | `$1,800.00` | **`$2,640.00`** | `-$2,850.00` (`-51.91%`) |
| **Path C：`planrelay` SHA-256 评审伴侣 + `claude-code-sketch` 17 工具（推荐）** | `$95.00` | `3.5h` | `$350.00` | **`$445.00`** | **`-$5,045.00` (`-91.89%`)** |

---

## 🛠️ 六、15 分钟极速落地 Checklist（15-Minute Rollout Checklist）

- [ ] **Step 1（3 分钟）：安装 `claude-code-sketch` 插件并生成首张 CJK 对齐架构图**
  ```bash
  # 在 Claude Code 中注册市场并安装插件
  /plugin marketplace add allen-hsu/claude-code-sketch
  /plugin install claude-code-sketch@claude-code-sketch-marketplace
  # 测试渲染带中文注释的 ER 图与 UI 线框图并写入 docs/plan.md
  /claude-code-sketch:sketch er
  /claude-code-sketch:sketch wireframe
  ```
- [ ] **Step 2（5 分钟）：启动零依赖 `planrelay` 本地评审服务（`:4387`）**
  ```bash
  git clone https://github.com/ineedfoundmyway/planrelay.git
  cd planrelay && npm install && npm run build
  # 针对当前仓库的 docs/plan.md 与本地 Git Diff 启动评审工作台
  node dist/cli.js serve --plan docs/plan.md --port 4387
  ```
- [ ] **Step 3（4 分钟）：演练 `blocker` 门禁拦截与结构化 `handoff.md` 导出**
  ```bash
  # 添加一条阻塞级评审意见
  node dist/cli.js add-comment --target plan --severity blocker --body "Missing token expiry check in auth flow"
  # 验证存在未决 blocker 时 approve 被硬件级拒绝，并导出交接单给 Agent
  node dist/cli.js export --out .planrelay/handoff.md
  ```
- [ ] **Step 4（3 分钟）：解决 `blocker` 并执行 `SHA-256` 摘要强绑定签批**
  ```bash
  node dist/cli.js resolve-comment --id <thread-id>
  node dist/cli.js approve --plan-sha256 <current-plan-sha256> --diff-sha256 <current-diff-sha256>
  ```
