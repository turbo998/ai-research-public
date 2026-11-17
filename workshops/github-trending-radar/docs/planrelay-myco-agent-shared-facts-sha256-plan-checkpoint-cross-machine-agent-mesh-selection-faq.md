# SHA-256 绑定计划审批工作台（`ineedfoundmyway/planrelay`）与跨机 Agent 委托网络及双端核验事实库（`chenhg5/myco` & `agent-shared-facts`）架构选型 FAQ

> **文档类型**：AI Solution Architect（AI 解决方案架构师）实战选型指南（六段式标准 FAQ）  
> **所属轮次**：2026-11-17 Night Round 34（Cumulative Round 458）  
> **追踪目标**：
> - **`ineedfoundmyway/planrelay`**（`★ 78`，TypeScript / Node.js 22+ 零依赖审查伴侣，`MIT OR Apache-2.0`）：以 **“内容一旦变动，旧审批自动失效（Different Content, Different Review）”** 为核心铁律的本地计划与代码审查工作台，将每条批注与审批决定严格绑定至 **SHA-256 快照、行号、严重度与解决状态**，提供 CLI `check` 门禁验证最新修订版是否已获批准
> - **`chenhg5/myco`**（`★ 93`，Go 单二进制跨平台客户端，`MIT`）& **`siwen-121/agent-shared-facts`**（`★ 68`，Python 3.12+ / Git + 只读 MCP，`MIT`）：打通云端（`claude.ai` / VPS）与本地开发机及队友 Claude Code / Codex 的跨机任务委托网格（`myco`），配合严格区分“离线草稿 / 审阅候选 / 已发布事实”且强制要求**第二台设备拉取核验后才签发发布回执**的跨端事实同步架构（`agent-shared-facts`）  
> **计量审计 ID**：`CLAIM-20261117-R34-PLANRELAY-MYCO`（底层 Tailscale / Cloudflare 隧道基础网络标记为 `not_measured`）

---

## 📌 一、核心结论速览（Executive Summary）

1. **为什么分布式工程团队在跨多台设备（Windows 工作站、Mac 笔记本、云端 VPS）协同运行多个 AI 编程 Agent 时，经常发生“计划改了但旧的‘同意’还留在聊天里导致 Agent 按未审新版乱写”、“人在云端 Agent 与本地 CLI 之间当人肉复制粘贴总线”以及“某台机器上 Agent 产生的未证实假设直接污染全团队共享记忆库”三大事故？**
   - **事故一（聊天室里的“过期批准 Stale Approval”漏洞）**：在普通对话流里，人类对 V1 版计划回了一句 `Looks good`，随后 Agent 根据新上下文微调了计划（或漏掉了回滚步骤），但历史里的批准语义依然残留，导致未经重新审批的新计划被直接执行。
   - **事故二（工程师沦为“人肉消息总线”）**：云端 `claude.ai` 或远端服务器上的 Agent 需要读取你本地机器才有的内网数据库、已登录 CLI 或本地编译链；或者你的 Agent 需要请队友的 Agent 协助排查接口——结果全靠人类在两个窗口间复制 Prompt、重讲背景、粘贴报错。
   - **事故三（跨设备共享记忆的“草稿污染真相”）**：多台电脑上的不同 Agent（Claude Code、Codex、Kimi、DeepSeek）如果直接往同一个共享向量库或网盘里写记忆，未经核实的离线草稿会瞬间被其他设备当成既定事实引用。
   - **架构师黄金组合（`planrelay` + `myco` + `agent-shared-facts`）**：在计划审批门禁层部署零依赖的 **`ineedfoundmyway/planrelay`**（将每次批注与审批绑定至精确 SHA-256 内容哈希，内容一改立即生成 Pending 新修订版，Agent 动工前必须跑通 CLI `check`）；在跨机互联层部署单 Go 二进制的 **`chenhg5/myco`**（让云端 Agent 在同一对话中直接调用你本机已配置好的 Claude Code / Codex 或队友节点）；在跨设备知识沉淀层采用 **`siwen-121/agent-shared-facts`**（以 Git Commit SHA 区分草稿、候选与已发布事实，强制第二台设备拉取核验并仅通过只读 MCP 暴露已批准摘要）。
2. **闭式 FinOps 量化收益（35 名分布式工程师与架构师、每月执行 40,000 次跨机 Agent 计划审查、远程委托与共享架构事实更新，综合时薪 `$95.00/hr`）**：
   - 从 **Path A（聊天框口头批计划 + 人肉跨窗复制粘贴中转 + 无版本共享记忆，`$5,560.00/月`）** 切换至 **Path C（`PlanRelay` SHA-256 计划门禁 + `Myco` 跨机委托网 + `agent-shared-facts` 双端核验事实库，`$341.00/月`）**，每月净省 **`$5,219.00/月`（降幅 `-93.87%`，年化节省 `$62,628.00/年`）**，过期计划推倒重做、人肉充当消息总线与清理脏记忆工时从 `36.0 小时/月` 降至 `2.8 小时/月`（节省 **`92.22%`**）。

![PlanRelay + Myco + Shared Facts Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r34-planrelay-myco-shared-facts.svg)

---

## 💬 二、灵魂拷问 Q1–Q3（大白话拆解应用场景与架构本质）

### Q1：`ineedfoundmyway/planrelay` 是如何用“SHA-256 哈希绑定”彻底消灭 AI 编程中的“过期批准（Stale Approvals）”的？
- **大白话本质定义**：`PlanRelay`（`MIT OR Apache-2.0`，Node.js 22+ 零外部依赖）是立在“Agent 写完计划”与“Agent 开始改代码”之间的**“防篡改、防过期 SHA-256 版本审批闸机”**。
- **三大核心架构设计**：
  1. **内容变一字，审批即重置（`Different Content, Different Review`）**：当 Agent 更新了实施方案并以相同任务 ID 重新导入时，系统自动计算 SHA-256 并创建一条处于 `Pending` 状态的全新修订版（Revision）——早期版本的历史批注与决定完整保留供对比，但**旧版本的 `Approved` 状态绝不会继承给新版本**；
  2. **行级锚定与阻塞项闭环（Snapshot + Line + Severity + Resolution）**：人类审阅者的每条评论都精确锚定在具体快照版本、行号与严重级别（如缺失回滚步骤、越权假设或漏写验证命令），未解决的 Blocker 一目了然；
  3. **零依赖本地运行与双格式导出（JSON for Agents + Markdown for Humans）**：无需安装任何 npm 第三方包、无需配 API Key，直接用系统 Node 22+ 读写本地 JSON 工作区；支持 CLI `check` 命令在 CI 或 Agent Pre-Tool Hook 中硬性检查“当前最新 SHA-256 修订版是否已获批准”。

### Q2：`chenhg5/myco` 与 `siwen-121/agent-shared-facts` 如何让跨机器、跨系统的多个 Agent 像菌丝网络（Mycelium）一样安全协同？
- **`chenhg5/myco`（单 Go 二进制打通云端、本机与队友的 Agent 菌丝网络，`MIT`）**：
  1. **让云端 Agent 直接借用你本机的工具链**：当你在 `claude.ai` 网页或云端 VPS 上的 Agent 需要访问只有你笔记本上才有的内网数据库、本地 Git 配置或已登录 CLI 时，通过 `myco` 可在同一对话中直接把子任务委派给你本机的 Shell 节点或本机已配好的 Claude Code / Codex 执行并拿回结果；
  2. **跨队友 Agent 直接协作**：不再需要人肉把同事的报错截图发给自己的 Agent——你的 Agent 可通过 `myco` Hub 发现队友授权暴露的 Agent 节点、委派联调任务并接收结构化回复。
- **`siwen-121/agent-shared-facts`（Git Commit SHA 绑定 + 双设备拉取核验的跨端事实库，`MIT`）**：
  1. **三态严格隔离（离线草稿 vs 审阅中候选 vs 已生效事实）**：每条共享事实在指定 Git 分支上拥有固定 ID 与文件路径，Agent 读取时同时获取精确的 `commit SHA`；
  2. **第二设备读回确认机制（Two-Device Publication Receipt）**：Agent 可以在离线或单机上整理候选事实（Candidate），但必须经过对照审阅并合入主分支，且**由第二台设备从上游真实拉取并核对内容一致后，才签发最终“发布回执”**；
  3. **只传获准摘要与只读 MCP 暴露**：原始机密文件、PII 与凭据严格留在源设备本地，共享仓库只提交获准公开的摘要与可追溯证据 ID，并通过 stdio 或带鉴权的 Streamable HTTP **只读 MCP 服务**供 Claude Code、Codex、Kimi、DeepSeek 等读取。

### Q3：企业 AI 架构师如何将这三者整合为分布式团队的 Agent 协同基座？
- **计划准入层（`PlanRelay`）**：所有跨模块架构变更计划必须导入 `PlanRelay`，跑通 CLI `check` 确认最新 SHA-256 快照无未决 Blocker 且处于 `Approved` 状态；
- **跨机执行层（`Myco`）**：协调者 Agent 通过 `myco` 将已批准计划中的子任务分发至 macOS、Windows 与内网测试机上的 Claude Code / Codex 节点；
- **知识固化层（`agent-shared-facts`）**：各节点执行完毕后提炼出的接口契约与环境事实，经审阅合并与第二设备核验后写入 `agent-shared-facts` 只读 MCP 供全员消费。

---

## 🧭 三、端到端集成参考架构与选型决策树（Mermaid）

```mermaid
flowchart TD
    subgraph PlanGate["SHA-256 计划审批闸机：ineedfoundmyway/planrelay (Node 22+ 0-Dep)"]
        A[Agent 生成或更新实施方案] --> B[导入 PlanRelay 计算内容 SHA-256<br/>内容变动自动置为 Pending 新修订版]
        B --> C[人类行级批注 Severity / Blocker<br/>导出 Agent JSON 与人类 Markdown]
        C --> D{CLI check 最新版本已 Approved?}
    end

    subgraph MeshAndFacts["跨机执行与双端核验事实库：myco (★93, Go) + agent-shared-facts (★68, MIT)"]
        D -->|Yes| E[chenhg5/myco 跨机菌丝网络<br/>云端 Agent 委派任务至本地/队友 Claude Code &amp; Codex]
        E --> F[各设备产出候选事实 Candidate<br/>原始机密留本地 · 仅提炼摘要与证据 ID]
        F --> G[siwen-121/agent-shared-facts 审阅合入 Git 分支<br/>第二设备拉取核验 → 签发发布回执 → 暴露只读 MCP]
    end
```

---

## 📊 四、同赛道方案横向选型对比矩阵（Decision Matrix）

| 评估维度 | 方案 A：聊天框口头说“同意” + 人肉跨窗复制粘贴 + 共享网盘记忆 | 方案 B：普通 GitHub PR 审 Markdown + 手写 SSH 脚本 | **方案 C（推荐）：`PlanRelay` + `Myco` + `agent-shared-facts`** |
| :--- | :--- | :--- | :--- |
| **防计划微调后沿用旧批准（Stale Approval）** | ❌ 聊天记录里的旧 `LGTM` 无法随计划内容变动自动作废 | ⚠️ PR 审批重、耗时长，不适合本地高频迭代的 Agent 计划 | ✅ **基于 SHA-256 快照：内容一改即创建 Pending 新版，CLI `check` 硬性拦截未批新版** |
| **云端 Agent 与本机/队友 CLI 跨机联动** | ❌ 工程师充当人肉消息总线，在多个窗口间来回复制粘贴 | ⚠️ 手写 SSH 隧道配置繁琐，无跨队友 Agent 自动发现与委派 UI | ✅ **单 Go 二进制 `myco` 一键组网，云端会话直接调用本机工具链或委派队友 Agent** |
| **跨设备共享记忆防污染与隐私边界** | ❌ 某台机器的错误草稿直接写进共享向量库，且易泄露本地密钥 | ⚠️ 缺乏“第二设备拉取回执”与只读 MCP 标准封装 | ✅ **严格区分草稿/候选/已发布（带 Commit SHA），强制双设备核验回执且敏感原件不出本机** |
| **月度总拥有成本（TCO，35 人 / 4 万次协同操作）** | **`$5,560.00 / 月`**（含 `$2,140` 过期计划重跑 + `36.0h` 人肉中转） | **`$2,410.00 / 月`**（含 `$890` 中继维护 + `16.0h` 手工同步） | **`$341.00 / 月`**（**净省 `-93.87%`**，仅 `$75` 轻量 Go/Git 节点 + `2.8h` 修订与事实签批） |

---

## 🧮 五、7-Card 定量洞察与闭式 FinOps 核算（`CLAIM-20261117-R34-PLANRELAY-MYCO`）

> **核算范围与边界声明**：面向 35 名跨地域/跨设备协同的工程师与架构师团队，每月执行 **40,000 次 Agent 计划版本审查、跨机任务委托与共享架构事实同步**（综合时薪 `$95.00/hr`；底层基础 Tailscale / Cloudflare 隧道网络标记为 `not_measured`）：

$$\text{Total Monthly TCO} = \text{Stale-Plan Re-Run \& Relay Spend} + (\text{Manual Copy-Paste Bus \& Fact Cleanup Hours} \times \$95.00)$$

| 成本构成项 | Path A：聊天口头批准 + 人肉复制粘贴中转 | Path B：静态 PR 审计划 + 自写 SSH 脚本 | **Path C：`PlanRelay` + `Myco` + `shared-facts`** |
| :--- | :---: | :---: | :---: |
| **月度过期计划误执行重跑 Token 与中继宿主开销** | `$2,140.00` | `$890.00` | **`$75.00`** |
| **月度人肉跨机搬运上下文、计划回滚与脏记忆清理工时** | `36.0 hrs` | `16.0 hrs` | **`2.8 hrs`**（直降 **`92.22%`**） |
| **月度研发与架构师人工成本（`@ $95.00/hr`）** | `$3,420.00` | `$1,520.00` | **`$266.00`** |
| **月度总拥有成本（Monthly TCO）** | **`$5,560.00`** | **`$2,410.00`**（`-56.65%`） | **`$341.00`**（**`-93.87%`**） |
| **相对 Path A 净节省（月度 / 年化）** | 基线（`$0.00`） | `$3,150.00 / 月`（`$37,800/年`） | **`$5,219.00 / 月`（`$62,628.00 / 年`）** |

---

## ✅ 六、AI 解决方案架构师实战上手 Checklist（SA Action Checklist）

- [ ] **Step 1 — 部署零依赖 `PlanRelay` 并将 CLI `check` 写入编码启动钩子**：使用 Node.js 22+ 启动 `ineedfoundmyway/planrelay`，规定任何跨文件 Agent 计划修改后必须重新导入生成新修订版，并在 CLI `check` 返回 `Approved` 后才允许进入编码阶段。
- [ ] **Step 2 — 安装单二进制 `chenhg5/myco` 打通云端与本地/队友 Agent 节点**：在开发机与内网测试机安装 `myco`，将本地 Claude Code、Codex 与受控 Shell 节点接入同一项目网络，彻底告别跨窗口复制粘贴。
- [ ] **Step 3 — 用 `siwen-121/agent-shared-facts` 建立双端核验的团队事实库**：运行 `setup.cmd` / `setup.sh` 初始化私有 Git 事实仓库，跑通 `python -m unittest discover -s tests -v` 双克隆合成测试。
- [ ] **Step 4 — 强制执行“原件留本机、摘要进 Git、只读 MCP 消费”铁律**：禁止将含 PII 或密钥的原始文件推入共享分支，仅提交经审阅合并且由第二台设备拉取确认的摘要与证据 ID，并通过只读 MCP 暴露给各端 Agent。
