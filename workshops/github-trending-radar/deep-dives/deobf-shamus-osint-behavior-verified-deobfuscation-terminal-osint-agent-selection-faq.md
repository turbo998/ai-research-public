# 四阶段行为证明反混淆逆向技能（`memcpython/deobf`）与 12 工具 `(Y/n)` 边界受控终端 OSINT 侦察智能体（`RouteInferno/shamus-osint-ai-agent`）深度选型 FAQ

> **文档定位**：本专题是 **2026-11-13 夜班第 24 轮（累计第 152 篇）独立六段式选型指南**，严格对标 `ib-vs-ethernet-roce-selection-faq.md` 的通俗第一性原理与闭式 FinOps 核算规范，面向企业安全威胁情报负责人、恶意代码逆向工程专家与 AI Solution Architect，深度拆解今日新仓榜上解决“大模型逆向混淆代码时靠猜函数名编造看似合理的假源码”与“威胁情报侦察在 20 个网页工具间手工切标签页或盲目发散查询”的两大安全利器：
> 1. **`memcpython/deobf`（2 天新建获 `26★`，MIT，零运行态依赖单文件 `SKILL.md`，兼容 Claude Code / Codex / Agent Skills）**：确立**“别猜源码，还原行为（Don't guess the source. Recover the behavior.）”**铁律的四阶段反混淆与逆向工程技能（`extract → decode → lift → verify`）——覆盖 **Lua / LuaJIT / Luau、JavaScript、原生 PE/ELF/Mach-O 二进制与自定义虚拟机（Custom VMs）**，强制 Agent 编写可复用的解码器与语义提升器（Lifter），严禁把未知的 VM Opcode 假装成无操作（No-op）或给分发器改个漂亮名字就谎称“已完全反混淆”，并强制将**已观测事实（Observed Facts）、假设（Hypotheses）与已验证结果（Verified Results）**及未解边界显式分离！
> 2. **`RouteInferno/shamus-osint-ai-agent`（当日新建获 `41★`，JavaScript，MIT，`v1.4.0`）**：常驻终端（PowerShell / CLI）的开源情报（OSINT）侦察智能体——内置 **`whois`、`dns`、`archive` 等 12 款侦察工具**，一行命令即可自动打印侦察计划、逐步调用工具、在步骤间记录自省笔记，并在**扩大搜索半径前主动暂停以 `(Y/n)` 征求人工确认**，最终输出可管道化、可定时调度的结构化案卷文件（Case File）！
>
> **English Version**: [deobf-shamus-osint-behavior-verified-deobfuscation-terminal-osint-agent-selection-faq.en.md](deobf-shamus-osint-behavior-verified-deobfuscation-terminal-osint-agent-selection-faq.en.md) · **关联日报**: [`daily/2026-11-13.md`](../daily/2026-11-13.md) · **专题架构图**: [`assets/github-ai-radar-2026-11-13-r24-deobf-shamus.svg`](../../../assets/github-ai-radar-2026-11-13-r24-deobf-shamus.svg)

![memcpython/deobf 与 RouteInferno/shamus-osint-ai-agent 架构选型对比](../../../assets/github-ai-radar-2026-11-13-r24-deobf-shamus.svg)

---

## 📌 一、核心结论速览（Executive Summary）

1. **一句话大白话讲透这两个项目到底解决了什么痛点？**
   - **终结“把一段加了虚拟化保护的 LuaJIT 或控制流平坦化的 JS 扔给大模型，模型解出两个字符串、给 VM 分发器重命名一下、脑补出 3 个长得很整洁的假函数，就敢拍胸脯说‘已经完整还原源码’”的痛点（`memcpython/deobf`）**：那根本不是逆向工程，那是看图说话编故事（*"A prettier VM is still a VM. A runnable guess is still a guess."*）！`deobf` 用零依赖单文件 `SKILL.md` 给 Claude Code 和 Codex 戴上四道紧箍咒（`extract → decode → lift → verify`）：不许猜“看着像 Base64”而必须实测解码例程；不许手改几个函数交差而必须写出覆盖全程序的转换脚本；遇到没还原出来的指令**必须原样标为未解（Unresolved Boundary）绝不许脑补成空指令**，且每一步必须通过运行态行为与副作用校验！
   - **终结“安全分析师查一个可疑C2域名时，要在浏览器里开十几个 Whois / DNS / 历史快照网页来回复制粘贴，或者跑自动化侦察脚本时因为没有边界确认把无关子域全扫了一遍”的痛点（`RouteInferno/shamus-osint-ai-agent`）**：`Shamus`（`v1.4.0`）直接住在终端里，自带 12 把 OSINT 工具；它先打出侦察计划，每调完一个工具就读输出、写条简短推理笔记决定下一步，而且**一旦需要扩大搜索范围（Widen the Search），必定停下来弹出 `(Y/n)` 等你点头**，最后自动汇总成标准案卷文件！
2. **闭式 FinOps 投资回报结论（`CLAIM-20261113-R24-DEOBF-SHAMUS`）**：
   - 以 **安全威胁情报与逆向团队每月分析 `30 个混淆样本（LuaJIT/JS/VM/PE-ELF）` 并开展 `120 次外部攻击面/C2 归属 OSINT 调查`** 为基准（安全逆向分析师全包时薪 `$105.00/hr`；商业 IDA Pro / Binary Ninja 席位费与企业级 SIEM 存储采购：`not_measured`）：
   - 从 **Path A（裸用大模型脑补假反编译源码 + 浏览器手工开十几个标签页拼凑 OSINT 报告，月均 `$5,670.00`）** 升级至 **Path C（`deobf` 四阶段可复用解码/提升管线 + `Shamus v1.4.0` 12 工具 `(Y/n)` 受控终端 OSINT 智能体，月均 `$542.50`）**，每月净省 **`$5,127.50/mo`（降幅 `-90.43%`，年省 `$61,530.00/yr`）**，并将排查脑补假代码误导与手工整理 OSINT 案卷的工时从 `38.0 hrs/mo` 压缩至 `3.5 hrs/mo`（节省 **`-90.79%`**）。

---

## 🎯 二、三大灵魂拷问（Q1 / Q2 / Q3 深度原理解析）

### Q1：为什么直接让通用 Coding Agent 反混淆代码会出现严重的“合理故事幻觉（Plausible Story Hallucination）”？
- **第一性原理拆解**：
  1. **用表象美化替代语义提升（Renaming vs. Lifting）**：LLM 天生倾向于输出可读性高的代码。面对自定义字节码 VM 或控制流平坦化时，它会给 `switch(opcode)` 改名叫 `executeBusinessLogic()`，并把看不懂的分支直接删掉或当成 No-op，生成一份能编译但行为完全错误的假代码。
  2. **忽略惰性解码与运行时自修改（Lazy Decoding & Runtime Mutation）**：静态一次性 Dump 往往漏掉运行期动态解密的常量池与有符号整数溢出边界。

### Q2：`memcpython/deobf` 是如何用 `extract → decode → lift → verify` 四步强制逆向工程证据链的？
- **第一性原理拆解**：
  1. **先立契约再做转换（Establish the Contract Before Transforming）**：
     - `extract` 识别容器、加载器与运行时；`decode` 用可复用脚本恢复字节、常量与指令原型；`lift` 翻译 handler 语义、剥离 VM 状态机并重建控制流；`verify` 检验实际输出与副作用。
  2. **显式标出未解边界与三态事实分离**：
     - 严格区分**已观测事实（Observed Facts）、假设（Hypotheses）与已验证结果（Verified Results）**；任何未能 100% 证实语义的指令必须保留为显式未解标记，帮助分析师精准聚焦剩余硬骨头。

### Q3：`RouteInferno/shamus-osint-ai-agent` (`v1.4.0`) 是如何在终端内兼顾“自主多步推理”与“受控侦察范围”的？
- **第一性原理拆解**：
  1. **12 工具链式自省与案卷自动生成**：
     - 不同于死板的批处理脚本，`Shamus` 根据前一步 `whois` / `dns` / `archive` 的返回内容动态决定下一步工具，并在步骤间留下简短自省笔记，最终输出完整 Case File。
  2. **`(Y/n)` 扩圈审批闸门**：
     - 在向外关联新域名、历史归档或更大范围目标前，强制暂停等待终端用户输入 `(Y/n)`，避免侦察范围失控或打草惊蛇。

---

## 🧭 三、Mermaid 选型决策树与「deobf 反混淆提取 + Shamus 终端 OSINT 归因」联动架构图

```mermaid
flowchart TD
    A["可疑混淆样本 (LuaJIT/JS/VM/PE-ELF) 逆向与外部 C2 基础设施 OSINT 调查"] --> B{"当前处于安全分析哪个阶段？"}
    B -- "阶段 1：样本反混淆与行为还原 (防止大模型脑补假源码与漏掉未知 Opcode)" --> C["采用 memcpython/deobf (extract -> decode -> lift -> verify)"]
    B -- "阶段 2：提取出的域名/IP/指纹外部侦察与案卷归档 (防止网页切换与无界发散)" --> D["采用 RouteInferno/shamus-osint-ai-agent (v1.4.0 12 工具终端 Agent)"]

    C --> C1["编写可复用解码器与 VM Lifter 脚本 + 验证运行时副作用"]
    C1 --> C2["严格分离事实/假设/验证结果 + 显式保留未解指令边界，提取真实 C2 指标"]

    D --> D1["终端内自动规划并调用 whois/dns/archive 等 12 款工具 + 步骤间记笔记"]
    D1 --> D2["扩大搜索半径前强制 (Y/n) 人工确认 + 自动输出结构化 Case File"]

    C2 & D2 --> E["🏆 黄金端到端威胁分析链路：deobf 行为保真逆向 + Shamus 终端侦察案卷 (-90.43% TCO)"]
```

---

## 📊 四、同类方案核心能力对比矩阵（Selection Matrix）

| 评估维度 | Path A：裸 Prompt 反混淆 + 浏览器手工查 OSINT | Path B：手写零散正则解码 + 无门禁批量侦察脚本 | **Path C（推荐）：`memcpython/deobf` + `Shamus v1.4.0`** |
| :--- | :--- | :--- | :--- |
| **反混淆真实性与防脑补能力** | 极易重命名几个函数编造“看似合理”的假源码 | 仅能处理简单字符串替换，遇自定义 VM 即卡死 | **四阶段 `extract→decode→lift→verify`，强制可复用 Lifter 脚本与行为校验** |
| **未知指令与未解边界处理** | 偷偷把未知的 Opcode 当作无操作忽略掉 | 脚本直接报错崩溃 | **显式标出所有未解边界（Unresolved Boundaries），严格区分事实、假设与验证结果** |
| **OSINT 侦察工作流与工具集成** | 浏览器开 20 个网页手动复制粘贴 | 死板跑完固定命令，不会根据输出动态追查 | **终端原生集成 12 款工具，按上一步输出动态调整计划并记录推理笔记** |
| **侦察范围控制与案卷沉淀** | 人工随时可能漏记或误扫无关资产 | 无暂停机制，容易过度发散消耗配额 | **扩大搜索前强制 `(Y/n)` 人工确认 + 自动汇编标准 Case File 支持管道调度** |
| **月度总拥有成本（30 样本 + 120 调查/月）** | **`$5,670.00 / mo`**（`$1,680` 算力 + `$3,990` 工时） | **`$2,860.00 / mo`**（`$760` 算力 + `$2,100` 工时） | **`$542.50 / mo`（净省 `$5,127.50/mo` · `-90.43%`）** |

---

## 🧪 五、定量 FinOps 算例与 7-Card 洞察（`CLAIM-20261113-R24-DEOBF-SHAMUS`）

### 5.1 测算基准与显式边界（Scope & Boundaries）
- **场景设定**：安全威胁情报与逆向工程团队每月分析 **30 个多层混淆样本（LuaJIT / JavaScript / 自定义字节码 VM / 加壳 PE-ELF）**，并针对提取出的 IOC 开展 **120 次 OSINT 外部侦察调查**。
- **费率假设**：安全逆向与威胁情报分析师全包时薪 **`$105.00 / hr`**。
- **显式边界声明（Explicit Not-Measured Boundary）**：商业反编译器（IDA Pro / Binary Ninja）年度席位费与企业级 SIEM 集群长期存储采购标记为 **`not_measured`**，本表严格核算逆向与侦察 Agent 的 LLM / API 消耗，以及分析师花在甄别大模型脑补假代码、手写一次性解码器与手工整理 OSINT 案卷上的工时。

### 5.2 三路径月度成本闭式对照表

| 成本分项 | Path A：大模型脑补反混淆 + 网页手工侦察 | Path B：手写零散脚本 + 无界自动扫描 | **Path C：`deobf` + `Shamus v1.4.0`（推荐）** |
| :--- | :--- | :--- | :--- |
| **月度逆向/侦察 LLM Token 与查询 API 支出** | **`$1,680.00`**（反复追问脑补假代码 + 冗余查询） | **`$760.00`**（无门禁发散扫描开销） | **`$175.00`**（脚本化解码/Lifter 省 Token + `(Y/n)` 精准控圈） |
| **假代码排障、VM 逆向与案卷汇编工时（`$105/hr`）** | `38.0 hrs × $105.00` = **`$3,990.00`** | `20.0 hrs × $105.00` = **`$2,100.00`** | `3.5 hrs × $105.00` = **`$367.50`** |
| **月度总成本（Monthly TCO）** | **`$5,670.00 / mo`** | **`$2,860.00 / mo`**（`-49.56%`） | **`$542.50 / mo`** |
| **相对 Path A 净节省** | 基准线（Baseline） | 净省 `$2,810.00 / mo` | **净省 `$5,127.50 / mo`（`-90.43%` · 年省 `$61,530.00/yr`）** |
| **商业 IDA Pro 席位与企业 SIEM 存储采购** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 六、生产级落地核验 Checklist

- [ ] **1. `memcpython/deobf` 技能部署**：将 `SKILL.md` 复制到 `.claude/skills/deobf/SKILL.md` 或 `.agents/skills/deobf/SKILL.md`，重启会话并显式调用 `deobf` 分析混淆样本。
- [ ] **2. 四阶段可复用解码器与未解边界核验**：确认 Agent 产出了独立的解码器/Lifter 脚本、验证了运行时输出与副作用，并将未能确定的 VM 指令显式标记为 `Unresolved` 而非伪造逻辑。
- [ ] **3. `RouteInferno/shamus-osint-ai-agent` (`v1.4.0`) 终端部署**：在 Windows PowerShell 或终端环境中配置 `Shamus`，核验 12 款内置 OSINT 工具（`whois`、`dns`、`archive` 等）连通性。
- [ ] **4. `(Y/n)` 扩圈门禁与案卷归档验证**：对测试域名发起侦察，验证 Agent 在扩大搜索范围前暂停等待 `(Y/n)` 确认，并检查最终生成的 Case File 结构完整性。
