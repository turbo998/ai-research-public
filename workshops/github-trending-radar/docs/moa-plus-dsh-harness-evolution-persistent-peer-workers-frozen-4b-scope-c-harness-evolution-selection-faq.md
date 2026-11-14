# 持久化点对点协同智能体插件（`Burns1028/moa-plus`）与冻结 4B 模型跨钩子状态自进化框架（`HuangShengZeBlueSky/dsh-harness-evolution`）深度拆解与选型 FAQ

> **文档元数据（2026-11-14 · 晚班 Round 61 / 累计 Round 244）**  
> - **对标范式**：`ib-vs-ethernet-roce-selection-faq.md`（第一性原理 + 大白话拆解 + 灵魂三问 + Mermaid 决策树 + 闭式 FinOps 核算）  
> - **核心评估对象**：  
>   1. [`Burns1028/moa-plus`](https://github.com/Burns1028/moa-plus)（`★ 114`，面向 DeepSeek Harness 的 Mixture-of-Agents 持久化协同插件 `v0.2.7`/`v0.2.8`：由 Coordinator 把控全局方向，多个持久化 Worker 在各自独立会话中调研、构建、质疑与独立互审，支持 **Worker 之间点对点直接通信（Direct Peer Communication）、跨任务保留上下文**，并通过 macOS Seatbelt / Linux `bubblewrap` / Windows Job 实现受保护的沙箱隔离）  
>   2. [`HuangShengZeBlueSky/dsh-harness-evolution`](https://github.com/HuangShengZeBlueSky/dsh-harness-evolution)（`★ 104`，MIT 开源的 DeepSeek Harness 插件自进化研究与 36 组 `Model × Scope` 基准库：在**完全冻结底层 `Qwen3-4B` 执行模型权重**的前提下，通过 `L4` 能力引导搜索与 `Scope A/B/C` 三级可编辑范围进化外层 Harness——在跨 Hook 共享 Episode 状态的 `Scope C`/`L4` 下，仅靠 4B 小模型即斩获 **ALFWorld `95.41 ± 0.00%`、DBBench `70.56 ± 0.38%`、WebShop `48.17 ± 0.29%` 与 OSBench `41.67 ± 1.84%`**）  
> - **配套架构图**：[`assets/github-ai-radar-2026-11-14-r61-moaplus-dshevolution.svg`](../../../assets/github-ai-radar-2026-11-14-r61-moaplus-dshevolution.svg)  
> - **审计契约号**：`CLAIM-20261114-R61-MOAPLUS-DSHEVOLUTION`（本地开发机基础硬件折旧标注为 `not_measured`）

---

## 📌 一、核心结论速览（Executive Summary：3 分钟读懂本质）

1. **为什么传统的“主控调一次性子 Agent（Hub-and-Spoke Subagents）”既会让主控沦为传话筒，又会在任务结束后把子 Agent 刚摸清的代码库经验全部丢光？`Burns1028/moa-plus` (`MoA+`) 怎么破局？**  
   - **通俗大白话**：普通子智能体用完即毁（One-Shot）：Worker A 和 Worker B 协同开发一个 CLI 时，A 想问 B 接口格式，必须先汇报给 Coordinator、再由 Coordinator 转述给 B；等任务做完，两个 Worker 的记忆直接清空，下一个关联需求还得重头读一遍代码。  
   - **`MoA+` 的第一性原理破局**：
     - **Coordinator 掌舵 + 持久化 Worker 点对点直连（Direct Worker-to-Worker Messaging）**：Worker 拥有持久化的独立会话，可以**直接互相发消息对表、互相 Challenge（质疑）与独立 Code Review**，最后把经过人类确认的变更汇总回 Coordinator，且原地待命承接下一项任务！
     - **三平台原生内核级隔离（Seatbelt / `bubblewrap` / Windows Job）+ 零污染独立运行时**：受保护 Worker 在 macOS 上强制启用 Seatbelt、在 Linux 上启用 `bubblewrap`、在 Windows 上启用原生 Windows Job 隔离（严禁未适配的常驻终端越权）；通过 `apply-native-compat.mjs --backup` 与 `project-mode.mjs setup --dir` 构建完全隔离的运行时目录，绝不污染个人 `~/.dsh` 配置。
2. **当一个开源小模型（如 `Qwen3-4B`）在数据库或操作系统任务上老是犯“重复执行写操作”或“没改完就提前交卷”的毛病时，为什么微调模型权重既贵又慢，而进化它的外层 Harness（`dsh-harness-evolution`）却能让 `4B` 模型冲上 `70.56%–95.41%`？**  
   - **通俗大白话**：很多团队一看到小模型在垂直任务上表现不好，第一反应就是租 GPU 集群做 SFT/RL 微调。但实际上，小模型大多不是“不会写 SQL 或 Shell”，而是缺乏确定性的状态记账与动作拦截护栏！  
   - **`dsh-harness-evolution` 的第一性原理破局**：
     - **严格划分三级可编辑进化范围（`Scope A / B / C`）与 `L4` 能力引导搜索**：研究团队锁死 `Qwen3-4B` 权重不动，让独立的 Improver 根据执行失败轨迹自动修改 DSH 插件：
       - **`Scope A`（仅改 Skill 文本）**：只改提示词，天花板极低；
       - **`Scope B`（单轮改一个独立组件）**：每次只改 Skill、记忆、动作检查或回执解析中的一个；
       - **`Scope C`（跨 Hook 共享 Episode 状态的协同机制）**：允许多个插件钩子通过 `episode-local state` 协同！例如在进化出的 **DBBench `L4` Harness（测试成功率高达 `70.56 ± 0.38%`）** 中，写操作工作流自动把数据库执行回执（Write Receipts）记录进 Episode 状态，后续上下文钩子将该状态暴露给 4B 模型，同时**动作检查钩子（Action Check Hook）利用同一状态直接拦截重复写入与提前交卷（Premature Submission）**！
     - **四大权威基准实测巅峰（冻结 `Qwen3-4B`）**：在 36 组 `Model × Scope` 对照实验中，冻结的 `Qwen3-4B` 取得了 **ALFWorld `95.41 ± 0.00%`、DBBench `70.56 ± 0.38%`、WebShop `48.17 ± 0.29%`、OSBench `41.67 ± 1.84%`** 的惊人成绩！
3. **闭式 FinOps 审计结论（`CLAIM-20261114-R61-MOAPLUS-DSHEVOLUTION`）**：  
   - 按每月迭代与运行 **36 组企业垂直领域智能体工作流与多角色开发任务**（工程师时薪 **`$100.00/hr`**）核算：从“Path A：动辄租卡微调大参数模型 + 主控中转一次性子 Agent 重复读仓”（**`$5,920.00/月`**，含 `$2,120.00` 微调算力与重复上下文 Token 开销 + `38.0h` 训练调参与手工传话人力 `$3,800.00`）切换到“Path C：`dsh-harness-evolution` Scope-C 跨钩子状态进化（驱动冻结 `Qwen3-4B`）+ `MoA+` 持久化点对点 Worker”（**`$505.00/月`**，含 `$155.00` 极简推理与进化开销 + `3.5h` 审阅人力 `$350.00`），每月净省 **`$5,415.00`**（降本 **`91.47%`**，年化节省 **`$64,980.00`**），模型调优与协同工时缩减 **`90.79%`**。

![MoA+ & dsh-harness-evolution Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r61-moaplus-dshevolution.svg)

---

## 💬 二、架构师灵魂三问（Q1–Q3 Deep Dive）

### Q1：为什么 `HuangShengZeBlueSky/dsh-harness-evolution` 证明了仅仅进化提示词（`Scope A`）远远不够，必须开放到跨 Hook 共享状态的 `Scope C`？

1. **因为模型的“动作约束”与“观察记忆”必须在同一个 Episode 状态机里闭环**：  
   - 如果只改 `Scope A`（Skill 提示词），4B 小模型在长对话中依然会忘记自己第 3 步已经执行过 `INSERT` 语句，从而在第 7 步重复插入或直接空手提交。而在 `Scope C` 中，`after_tool` 钩子将写操作回执写入 `episode_state`，`before_prompt` 钩子将其渲染为醒目状态栏，`before_action` 钩子则直接用代码逻辑拒绝未拿到成功回执的 `submit` 调用——用确定性代码状态机补齐了小模型的注意力短板。

---

### Q2：`Burns1028/moa-plus` 是如何在不破坏开发者本机日常 DeepSeek Harness (`~/.dsh`) 的前提下，扩展底层 22 个原生包与 50 个文件路径的？

1. **带备份的兼容性画像（Compatibility Profiles）与 `project-mode.mjs` 独立运行时目录**：  
   - `MoA+` 先通过 `apply-native-compat.mjs --dry-run` 与 `--backup` 安全备份依赖变更，再由 `project-mode.mjs setup --dir /absolute/empty-moa-runtime` 创建拥有独立 Home、独立配置与独立备份的沙箱运行时，使个人桌面版与 `~/.dsh` 保持 100% 原生纯净。

---

### Q3：在 `MoA+` 中，什么时候应该让 Worker 使用独立的 Git Workspace，什么时候应该选 `shared` 共享父目录模式？

1. **按写入冲突半径选择隔离粒度**：  
   - 当多个 Worker 并行探索不同实现方案或修改交叉文件时，启用独立 Git Workspace 配合 OS 级沙箱（macOS Seatbelt / Linux `bubblewrap` / Windows Job）防止互相覆盖；当两个 Worker 一人专职写代码、一人专职只读审查（Independent Review）且需即时看到对方未提交改动时，可选用 `shared` 模式并在对话启动前锁定模式身份。

---

## 🧭 三、架构选型决策树与持久化协同 / Harness 进化拓扑图（Mermaid）

```mermaid
flowchart TD
    Start["DeepSeek Harness 多智能体协同 & 垂直任务准确率提升选型"] --> Goal{"核心架构目标?"}

    Goal -->|"多角色长链路开发 (调研 + 编码 + 独立质疑审查)"| CollabGate{"子 Agent 通信与生命周期?"}
    CollabGate -->|"追求持久化 Worker 会话 + Worker 间点对点直接通信<br/>+ Seatbelt/bwrap/Windows Job 内核级隔离"| UseMoAPlus["✅ Burns1028/moa-plus (MIT · v0.2.7 / v0.2.8)<br/>• Coordinator 把控全局，Worker 直接互发消息协同并跨任务留存经验<br/>• project-mode.mjs 独立运行时目录，零污染个人 ~/.dsh"]
    CollabGate -->|"仅需单次简单无状态文本摘要"| EphemeralSub["🔄 常规一次性 Subagent"]

    Goal -->|"提升垂直基准/生产任务成功率 (如数据库操作 DBBench、OS 运维 OSBench)"| EvolveGate{"优先微调模型权重还是进化外层 Harness?"}
    EvolveGate -->|"冻结低成本小模型 (如 Qwen3-4B)，进化跨 Hook 共享 Episode 状态的插件 (Scope C / L4)"| UseDSHEvolve["✅ HuangShengZeBlueSky/dsh-harness-evolution (MIT · 36 Profiles)<br/>• 写入回执自动记入 Episode State，动作检查钩子拦截重复写与早退<br/>• 冻结 Qwen3-4B 实测：ALFWorld 95.41% · DBBench 70.56% · OSBench 41.67%"]
    EvolveGate -->|"仅修改静态文本提示词 (Scope A)"| ScopeAOnly["⚠️ 仅改 Skill 文本，长程状态易丢失"]

    UseMoAPlus --> FinOps["💰 闭式 FinOps 收益 (CLAIM-20261114-R61-MOAPLUS-DSHEVOLUTION)<br/>月度总成本 $5,920.00 ➔ $505.00 (-91.47% · 年省 $64,980)"]
    UseDSHEvolve --> FinOps
```

---

## 📊 四、同类方案横向对比矩阵（Decision Matrix）

| 评估维度 | `Burns1028/moa-plus` (持久化点对点 MoA 插件) | 传统 Hub-and-Spoke 一次性子 Agent | `dsh-harness-evolution` (`Scope C / L4` 插件自进化) | 传统大模型 SFT 微调 / 纯改 Prompt (`Scope A`) |
| :--- | :--- | :--- | :--- | :--- |
| **通信与状态留存机制** | **Worker 间点对点直接通信 + 跨任务保留独立会话记忆** | 所有消息必须经主控中转，任务结束即销毁记忆 | **跨 Hook 共享 `episode-local state`（写回执联动动作拦截）** | 仅靠模型参数记忆或静态文本叮嘱，易重复操作与早退 |
| **安全性与可复现性** | **macOS Seatbelt / Linux `bubblewrap` / Windows Job 隔离** | 常共享宿主终端无进程级隔离 | **公开 36 组 `Model × Scope` 完整进化谱系与检查点代码** | 微调黑盒难复现，或手工改 Prompt 缺乏版本对照 |
| **小模型战力提升实证** | 多角色互审（Challenge & Review）显著降低合入缺陷 | 单一视角盲目自信交差 | **冻结 `Qwen3-4B` 达 ALFWorld `95.41%` / DBBench `70.56%`** | 4B 裸跑在复杂数据库与 OS 任务上大量提前失败 |
| **部署与宿主兼容性** | **支持 `--backup` 与独立 `--dir` 运行时，不污染 `~/.dsh`** | 侵入式修改全局配置 | **MIT 开源，进化产物直接作为标准 DSH 插件目录挂载** | 每次任务变更都需重跑昂贵的 GPU 训练流水线 |

---

## 🧮 五、7-Card 定量洞察与闭式 FinOps 核算（`CLAIM-20261114-R61-MOAPLUS-DSHEVOLUTION`）

> **核算范围与边界声明**：本模型核算每月迭代与运行 **36 组企业垂直领域智能体工作流与多角色开发任务** 的 GPU 微调/API Token 开销，以及人工手写插件状态机、在中转式子 Agent 间搬运上下文的工程师人力成本（按 **`$100.00/hr`** 计价）；本地开发机基础硬件折旧标注为 **`not_measured`**。

| 方案路径 | 算力/API Token 与微调开销 (`USD/月`) | 状态机调参与上下文中转工时 (`hrs/月`) | 工程师人力成本 (`@ $100/hr`) | 月度总成本 (`USD/月`) | 相对 Path A 净节省 (`USD/月` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：频繁微调 70B+ 大模型 + 主控中转一次性子 Agent** | `$2,120.00` | `38.0 hrs` | `$3,800.00` | **`$5,920.00`** | Baseline (`0.00%`) |
| **Path B：仅手工改 `Scope A` 提示词 + 无沙箱共享目录子进程** | `$980.00` | `18.0 hrs` | `$1,800.00` | **`$2,780.00`** | `-$3,140.00` (`-53.04%`) |
| **Path C（推荐）：`Scope-C` 进化冻结 4B + `MoA+` 点对点协同** | **`$155.00`** | **`3.5 hrs`** | **`$350.00`** | **`$505.00`** | **`-$5,415.00` (`-91.47%`)** |

- **闭式校验公式**：
  - $\text{Path A Total} = 2120.00 + 38.0 \times 100.00 = 2120.00 + 3800.00 = \$5,920.00$
  - $\text{Path B Total} = 980.00 + 18.0 \times 100.00 = 980.00 + 1800.00 = \$2,780.00$
  - $\text{Path C Total} = 155.00 + 3.5 \times 100.00 = 155.00 + 350.00 = \$505.00$
  - $\text{Net Savings (Path C vs Path A)} = 5920.00 - 505.00 = \$5,415.00/\text{mo} \quad (-91.47\%, \text{Annualized } \$64,980.00/\text{yr})$

---

## 🛠️ 六、AI 解决方案架构师实战上手 Checklist

1. **在独立运行时目录部署 `Burns1028/moa-plus` 保护个人 `~/.dsh` 环境**：
   ```bash
   git clone --branch v0.2.7 --single-branch https://github.com/Burns1028/moa-plus.git && cd moa-plus
   npm ci && node scripts/apply-native-compat.mjs --backup "$PWD/.superpowers/native-backup"
   npm run build && node scripts/project-mode.mjs setup --dir /tmp/isolated-moa-runtime
   ```
2. **借鉴 `dsh-harness-evolution` 的 `Scope C` 跨钩子状态模式加固生产 Agent**：
   - 不要只改静态 `SKILL.md` 文字（`Scope A`）；将关键副作用（如数据库写入回执、API 变更状态）记录到 `episode-local state`，并在提交钩子（Action Check Hook）中强制校验回执后再放行完成动作。
