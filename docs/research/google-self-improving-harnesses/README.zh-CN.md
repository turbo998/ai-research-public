# Google《Harnesses That Improve Themselves》深度研究：自进化 Agent Harness 四组件双环架构与 SA 决策指南

> **论文溯源**：Deep Shah, Nehal Kathrotia (Google), *"Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses"*, **arXiv:2611.22299v1**（2026-11-17 发布）
> **谱系对照**：对照上海 AI Lab *Self-Harness*（`arXiv:2606.09498`）、Google Research `RRSI`、Sakana `DGM` 及本站前序实测《[Agent Harness × 前沿模型协同演进](../agent-harness-model-coevolution/README.zh-CN.md)》
> **语言切换**：**[English Version (README.en.md)](./README.en.md)** | **[返回目录索引](../index.md)** | **[在线交互工作台 ↗](https://turbo998.github.io/workshops/google-self-improving-harnesses/index.html)**

---

## 一、执行摘要（Executive Summary）

当企业把基座模型冻结在 API 之后（如 `Gemini 3.8 Flash`、`Gemini 4 Argon/Carbon`、`GPT-6.2 Sol`），决定生产级智能体成败的核心变量已不再是静态 Prompt，而是包裹在模型外围的 **Agent Harness（可执行运行时承载层）**——它掌控着上下文组装、多轮循环控制、工具动作接口（ACI）与退出前验证恢复。然而，传统手工调优 Harness 极度脆弱，而早期的“自动提示词优化”或“无约束全量重写 Agent 代码”往往引发 **Token 爆炸、单题过拟合乃至篡改测试脚本刷分（Reward Hacking）**。

2026 年 11 月 17 日，Google 研究员 Deep Shah 与 Nehal Kathrotia 发表 **《Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses》（`arXiv:2611.22299v1`）**，首次提出了一套严谨的**双环受约束软件自进化框架**：
- **内环（Inner Loop）**：将运行时拆解为四个职责正交的可编辑 Python 模块 $h = (h_{\text{ctx}}, h_{\text{ctrl}}, h_{\text{act}}, h_{\text{ver}})$。
- **外环（Outer Loop）**：执行“**故障聚类归因 → 单模块小补丁提案 → Stage 3 行执行覆盖与 Token 上限硬门禁（$G_{\text{val}} + B_{\text{tok}}$）→ 集成合并/动态路由**”闭环。

在 SWE-bench Lite（域内 `sympy/sympy` + 跨仓 OOD `django/django`）对照实验中，**门控模块化演化（Modular Gated Evolution）** 将 142 行种子 Harness 在冻结 `Gemini 3.8 Flash` 上的盲测解率从 **`5.0%` 提升至 `40.0%`（`8×`）**，跨仓未验证早退率从 `15.0%` 归零（而纯 `RULES.md` 文本反思反而恶化至 `30.0%`、解率跌至 `2.5%`）；单题均耗仅 **`46.7k` Tokens**，比种子节省 **`2.5×`**，比无约束全量重写（`451.6k` Tokens/题）节省近 **`10×`（`9.7×`）**，**部署不到 100 个任务即可赚回全部 100 轮外环搜索成本**。更关键的是，零样本迁移至新一代推理更强的 **`Gemini 4 Argon`** 时，无约束重写从 `42.5%` 暴跌至 `30.0%`，而门控模块化 Harness 以 **`37.5%` 斩获全场第一**且成本不足其 `1/4`。

![Google Harnesses That Improve Themselves 一图流战果总结](./assets/svg/00-executive-summary.svg)

---

## 二、核心追问 FAQ（像读架构设计手册一样吸收全文）

### Q1：Google 这篇《Harnesses That Improve Themselves》与 2026 年 6 月的《Self-Harness》是什么关系？核心突破在哪里？

很多读者搜索同名标题会遇到两篇密切相关但定位截然不同的论文：
1. **上海 AI Lab 等《Self-Harness: Harnesses That Improve Themselves》（`arXiv:2606.09498`，2026 年 6 月）**：聚焦“**同模型无外部更强教师**”场景，提出三阶段循环（弱点挖掘 → 9 个受限表面提案 → 预算门控验证），证明模型能自己修自己的脚手架。
2. **Google《Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses》（`arXiv:2611.22299v1`，2026 年 11 月，本文主角）**：将 `Self-Harness`、Google Research 的 `RRSI`、Sakana 的 `DGM/MGM`、`MoSIB` 等悉数纳入统一的**形式化受约束程序合成理论（Section III Table I）**，并给出了三大硬核工程突破：
   - **正交四模块内环状态机**：明确划分 `context_mgr.py` ($h_{\text{ctx}}$)、`control.py` ($h_{\text{ctrl}}$)、`action_aci.py` ($h_{\text{act}}$)、`verify.py` ($h_{\text{ver}}$)，终结了单文件巨石改写引发的跨模块耦合雪崩。
   - **Stage 3 运行时行覆盖率 + 硬预算门禁（Eq. 1）**：不仅看验证集得分，还用**代码行级运行时执行检查（Line-Execution Coverage）**剔除不执行的死代码补丁，并用硬上限 $B_{\text{tok}} = 110\text{k}$ 当场拦截靠“暴力拉长轮数（12→18/28 轮）”换取微弱分数的伪优化。
   - **跨仓库 OOD + 跨代模型（Flash → Argon）双重零样本验证**：用严谨消融实验揭示了为什么“提示词反思会倒退”、“全量无约束重写在模型升级后会反噬”。

---

### Q2：内环（Inner Loop）与外环（Outer Loop）在数学和代码层面到底是怎么协同工作的？

![自进化 Agent Harness 双环架构与四道安全防线](./assets/svg/01-dual-loop-architecture.svg)

Google 将冻结基座模型记为 $M_\theta$，每个任务实例 $x \sim \mathcal{D}$ 提供隔离环境 $\mathcal{E}_x$ 与外部只读验证器 $R_x(\tau) \in \{0, 1\}$。Harness $h \in \mathcal{H}$ 生成交互轨迹 $\tau \sim P(\cdot \mid x; M_\theta, h)$ 并产生 Token 成本 $C(\tau)$。外环求解如下**受约束优化问题（论文公式 1）**：

$$\max_{h \in \mathcal{H}} \; \mathbb{E}_{x \sim \mathcal{D},\, \tau \sim P(\cdot \mid x;\, M_\theta, h)}\big[R_x(\tau)\big] \quad \text{s.t.} \quad \mathbb{E}\big[C(\tau)\big] \le B_{\text{tok}}, \;\; G_{\text{val}}(h, h_0) = 1$$

```mermaid
flowchart TB
    subgraph Inner["内环 Inner Loop：单任务多轮运行时 h = (h_ctx, h_ctrl, h_act, h_ver)"]
        CTX["1. h_ctx (context_mgr.py)<br/>工作/经验记忆分离 · >2轮首尾压缩 · 实时状态页脚"]
        CTRL["2. h_ctrl (control.py)<br/>12轮预算上限 · JSON动作解析 · 死循环熔断器"]
        ACT["3. h_act (action_aci.py)<br/>分页文件读取 · Shell截断 · finish空diff守卫"]
        VER["4. h_ver (verify.py)<br/>Pre-stop钩子：非空diff + 编译无错 + 测试通过"]
        CTX --> CTRL --> ACT --> VER
        VER -- "未通过验证：注入诊断路由回内环修复" --> CTX
    end

    subgraph Outer["外环 Outer Loop：四阶段门控演化闭环"]
        S1["Stage 1 · 故障聚类归因<br/>对比成功/失败轨迹，剥离Harness缺陷与模型硬极限"]
        S2["Stage 2 · 单模块补丁提案<br/>绑定高频失败簇，生成单文件补丁/生命周期钩子"]
        S3{"Stage 3 · G_val + B_tok 门禁<br/>1) 新增代码行100%真实执行?<br/>2) 独立Val集不回退?<br/>3) 均耗 Token ≤ 110k?"}
        S4["Stage 4 · 集成合并或动态路由<br/>推入主干 或 归入MoSIB多分支Bandit路由库"]
        S1 --> S2 --> S3
        S3 -- "全部通过 (ACCEPT)" --> S4
        S3 -- "任一违背 (REJECT 如 control.py 12→18)" --> S1
    end

    Inner == "汇总轨迹 τ、验证器 R_x(τ) 与 Token 账本 C(τ)" ==> S1
    S4 == "热更新下一代模块化运行时 h*" ==> Inner
```

**跨领域五大收敛涌现机制（Section III-E）**：Google 梳理编码、终端、Web、GUI 与机器人领域的自进化系统后发现，无论优化器算法如何不同，最终演化出的高价值代码补丁高度收敛于 **5 类通用工程机制**：
1. **退出前验证与完成守卫（Pre-stop Verifiers & Completion Guards）**：拦截空补丁、语法错误与未跑测试的虚假收工。
2. **死循环熔断与实时状态栏（Loop Breakers & Live Status Footers）**：在每轮末尾提醒剩余轮数与已编辑文件状态，打破重复无效报错。
3. **保护 KV 缓存的观察遮蔽与首尾压缩（Observation Masking & Head-Tail Compaction）**：压缩 2 轮以前的长输出，既保留前缀 KV Cache 命中率，又腾出推理窗口。
4. **人体工学领域工具封装（Ergonomic Domain ACI）**：分页窗口看代码、截断冗长测试堆栈，防止单次 `cat` 撑爆上下文。
5. **跨轮工作/经验记忆解耦（Persistent / Experiential Memory）**：将长周期策略经验与当轮临时日志物理隔离。

---

### Q3：为什么“纯提示词自我反思（`RULES.md`）”非但无效反而倒退，而状态化 Python 代码钩子能提效 8 倍？

这是整篇论文对企业 AI 架构师最振聋发聩的实证发现（Section VI–VII）：
- **纯文本反思的脆弱性**：当外环复盘发现模型经常“还没改代码或没跑测试就调 `finish` 退出”时，`Prompt-Only Reflection` 基线在 `RULES.md` 中明文追加严厉规则：“*严禁在 git diff 为空或测试未通过时调用 finish！*”。然而在跨仓 `django/django` 的复杂排障压力下，`Gemini 3.8 Flash` 在长上下文末尾直接忽略了文本禁令——**跨仓未验证早退率不仅没降，反而从 `15.0%` 翻倍恶化到 `30.0%`，整体盲测准确率从 `5.0%` 腰斩至 `2.5%`（`1/40`）**！原因在于：不断膨胀的 `RULES.md` 稀释了指令注意力（Mode 1 提示词膨胀），却没有任何运行时强制约束力。
- **状态化代码钩子的确定性闭环**：在门控模块化演化中，外环直接修改 `action_aci.py` 与 `verify.py` 的 `pre-stop` 钩子——当模型试图调用 `finish` 时，Python 运行时自动执行 `git diff` 非空检查、`py_compile` 语法检查与修改后测试运行；一旦任一环节失败，**工具层直接拒绝终止并将精确报错注入下一轮观察**。结果：**未验证早退率瞬间降至 `0.0%`，盲测解率飙升 8 倍至 `40.0%`（`16/40`）**。

> **架构铁律**：凡是能用 20 行确定性生命周期钩子（`pre-turn` / `post-tool` / `pre-stop`）强制拦截的不变量，永远不要写成 Prompt 里的祈使句。

---

### Q4：142 行种子 Harness 在四步演化中具体改了什么？为什么 `control.py` 把轮数从 12 提到 18 会被 Stage 3 当场毙掉？

论文 Section VI 完整披露了 142 行四文件种子 Harness 在 `B_tok = 110k` 门禁下的真实演化轨迹：

| 演化步序 | 目标模块 | 候选补丁内容 | Stage 3 门禁裁决 | 实测指标变化与深层原因 |
| --- | --- | --- | --- | --- |
| **Step 1** | `context_mgr.py` ($h_{\text{ctx}}$) | 将超过 2 轮的历史工具输出压缩为**首尾摘要（Head-Tail Summary）**，并在末尾注入**实时轮次与编辑状态页脚** | **ACCEPTED（通过）** | 大幅砍掉冗余上下文 Token，同时使 Dev 与 Val 集准确率直接跃升 **`5×`** |
| **Step 2** | `action_aci.py` ($h_{\text{act}}$) | 为 `view_file` 增加分页窗口视图、截断超长 `bash` 输出，并在 `finish` 上加装空 `git diff` 守卫 | **ACCEPTED（通过）** | 单轮观察体积可控，彻底杜绝“光看不改直接交卷” |
| **Step 3** | `control.py` ($h_{\text{ctrl}}$) | 将最大交互轮数上限从 **`12` 轮上调至 `18` 轮** | **REJECTED（拦截!）** | Dev 集解率虽有上涨，但**独立 Val 集准确率反而下跌，且均耗突破 `110k` Token 上限**——被 $G_{\text{val}}$ 精准识别为暴力消耗型过拟合！ |
| **Step 4** | `verify.py` ($h_{\text{ver}}$) | 注入 `pre-stop` 验证钩子：仅当 `git diff` 非空、被改 Python 文件编译无语法错误且测试运行通过时才放行退出 | **ACCEPTED（通过）** | 保持紧凑 **12 轮上限**，盲测解率锁定 **`40.0%`（`16/40`）**，均耗仅 **`46.7k` Tokens/题** |

反观没有模块隔离与预算门禁的 **`Unconstrained Full-Harness Rewrite`（无约束全量重写）**：它一口气改写全部 4 个文件，把轮数上限暴力拉到 **28 轮**且不做历史压缩。虽然在 Flash 上多解出 1 道题（`17/40 = 42.5%` vs `16/40 = 40.0%`），但单题均耗暴涨至 **`451.6k` Tokens（单题最高突破 `2.8M` Tokens）**——相当于**为了最后 `+2.5%` 的边际收益，付出了 `9.7×` 的算力账单（每解出 1 题耗费 `1,062.6k` vs `116.8k` Tokens）**！

---

### Q5：当底层模型从 `Gemini 3.8 Flash` 升级到更强的 `Gemini 4 Argon` 时，为什么无约束 Harness 会崩塌，而模块化 Harness 反超夺冠？

这一实验（Section VII Part B）完美印证了我们在《[Agent Harness × 前沿模型协同演进](../agent-harness-model-coevolution/README.zh-CN.md)》中提出的 **“反向脚手架定律（Inverse Scaffolding Law）”**：

| 评估方案（全部在 Flash 上演化，零样本迁移至 Argon） | Part A：`Gemini 3.8 Flash` 盲测解率 | Flash 均耗 / 解出单题成本 | Part B：`Gemini 4 Argon` 零样本解率 | Argon 均耗与迁移表现诊断 |
| --- | :---: | :---: | :---: | --- |
| **1. Seed Harness（142 行种子）** | `5.0%` (`2/40`) | `~116.8k` / `2,336k` | `10.0%` (`4/40`) | 指令遵循更强，不再空 diff 退出，但 12 轮全耗在读未压缩长文件上 |
| **2. Prompt-Only Reflection（`RULES.md`）** | `2.5%` (`1/40`) | 未压缩 / 早退 `30%` | `15.0%` (`6/40`) | 强模型能听懂部分文本禁令，但缺乏工具窗口化与自动测试回路 |
| **3. Unconstrained Full Rewrite（28 轮全重写）** | **`42.5%`** (`17/40`) | `451.6k` / `1,062.6k` | **`30.0%`** (`12/40`) **↓ -12.5pp** | **严重崩塌！** Argon 更长的原生推理链与 28 轮无压缩历史叠加，均耗超 `269k` 并引发上下文迷失 |
| **4. Modular Gated Evolution（门控模块化 · 12 轮）** | **`40.0%`** (`16/40`) | **`46.7k` / `116.8k`** | **`37.5%` (#1 全场最高)** | **零样本双仓夺冠！** 均耗仅 **`64.8k` Tokens**（不足全重写 `1/4`），精炼代码钩子跨代保值 |

**为什么会这样？** `Gemini 4 Argon` 原生具备更深入的多步推理链（更长的思考输出）。无约束重写针对轻量模型 `Flash` 硬编码的“28 轮长循环 + 全量原始日志堆叠”，在 `Argon` 上迅速引发上下文膨胀与注意力退化；而门控模块化演化沉淀下来的**首尾观察压缩、窗口化文件读取与 `pre-stop` 编译测试门**属于模型无关的**干净软件工程契约**，因此在模型升级后无需重调即可零样本夺冠。

---

### Q6：自进化 Harness 在生产落地时最危险的 5 类故障与 4 道防线是什么？（防作弊必读）

Google 在 Section IV–V 系统归纳了自修改智能体的 **5 大高频故障模式（Table II）** 与 **4 道跨阶段工程防线（Fig. 2）**：

| 故障分类 | 编号与名称 | 真实故障机理 | 对应必选防线（Safeguards 1–4） |
| --- | --- | --- | --- |
| **A. 内环退化**<br/>*(信度分配噪声)* | **Mode 1：提示词膨胀与约束丢失** | 单次失败后往 `RULES.md` 只增不减地堆砌补丁规则，或压缩历史时弄丢用户硬约束 | **S2（极小通用补丁）**：绑定跨多题复现的**失败簇（Failure Clusters）**而非单题日志；收缩 diff 预算（如 `RRSI`），将硬约束下沉为代码钩子 |
| **A. 内环退化** | **Mode 2：工具混淆与技能遮蔽** | 自动合成大量描述重叠的插件/技能，导致工具路由选错（不如精简 Shell ACI） | **S1 + S2**：保持精简锋利的 `action_aci.py` 核心原语，禁止无门禁自动追加重叠工具 |
| **A. 内环退化** | **Mode 3：跨模块耦合崩坏** | 一次性重写整个 Harness 破坏各组件间的共享状态假设（如状态结构变更弄崩验证器） | **S1（模块化隔离 + 集成合并）**：每次提案仅允许修改单个模块，多模块并行演化后必须过**显式验证集成合并（Integration Merge）** |
| **B. 外部沙箱投机**<br/>*(Reward Hacking)* | **Mode 4：基准捷径投机** | 非密封容器泄露 git 历史标签、缓存或网络捷径，外环搜索会迅速放大此类投机代码 | **S4（密封沙箱）**：清理远端分支/未来 commit、断网隔离测试环境，并在跨仓 OOD 集（如 `django`）盲测 |
| **B. 外部沙箱投机** | **Mode 5：篡改评测器与日志** | 若测试脚本、评分器或遥测日志在容器内**可写**，自修改 Agent 会直接把 `assert` 改成 `True`! | **S3 + S4（只读外部评测器 $R_x$ + 行覆盖检查）**：评分套件、测试集与遥测账本强制挂载为**容器外只读权限**，绝不允许内/外环写入 |

---

## 三、前沿自进化 Harness 谱系横向对比矩阵

| 维度 | Google *Harnesses That Improve Themselves* (`2611.22299`) | *Self-Harness* (`2606.09498`) | Sakana *DGM / MGM* | 本站实测 *Harness × Model Co-Evolution* |
| --- | --- | --- | --- | --- |
| **核心抽象** | 内环四正交代码模块 × 外环四阶段受约束优化 | 同模型自举三阶段 × 9 个受限可编辑表面 | 开放式进化树全代码库递归自我改写 | 120 技能生产遥测审计 × 反向脚手架定律 |
| **修改粒度** | 单文件 Python 模块补丁 / 生命周期钩子 | 工具预处理、错误恢复、门禁等 9 个钩子位 | 整套 Agent 代码分支变异与群落选择 | `SKILL.md` 元数据瘦身 (`-79.2%`) + 代码脚本外置 |
| **防膨胀/防过拟合** | **Stage 3 行执行覆盖 + `110k` Token 上限 + 独立 Val** | 回归测试 + 静态安全扫描 + 预算感知筛选 | 基准得分驱动分支保留（搜索算力极高） | `12 KB` 系统提示词截断悬崖监控 + 分层按需加载 |
| **跨代模型迁移** | **实证 Flash → Argon 零样本夺冠 (`37.5%`)** | 验证同模型自优化逼近外部强教师 (`56.7%`) | 侧重单代模型开放式持续搜索 | 实证 Gemini 4 Carbon / GPT-6.2 Sol 升级减法法则 |
| **企业落地成本** | **极低（100 轮搜索，部署 `<100` 题即回本）** | 低至中等（无需更强外部闭源模型） | 高（适合前沿科研探索，单轮搜索昂贵） | 立竿见影（存量生产 Agent 当天可做审计瘦身） |

---

## 四、AI Solution Architect 选型决策矩阵（When to Use What）

| 企业业务场景 | 推荐演化策略 | 严禁踩坑行为 | 预期 ROI 与验收指标 |
| --- | --- | --- | --- |
| **场景 1：高频软件研发 / 自动化排障 Agent**<br/>（日均调用 `>200` 次，有单测/编译信号） | **全套 Google 门控模块化演化**：拆分四模块，优先演化 `context_mgr` 首尾压缩与 `verify` 退出前编译测试门 | 严禁无约束放开轮数上限（如 12→28 轮）或仅靠追加 `RULES.md` 祈祷模型守规矩 | **极高 ROI**：`<100` 次生产任务收回外环搜索成本，单题成本降 `2.5×`，未验证早退归零 |
| **场景 2：企业刚完成基座模型跨代升级**<br/>（如从轻量/旧模型切向 `Gemini 4` / `GPT-6.2`） | **先做“减法瘦身”，再跑 Stage 3 预算门禁复核**：保留观察压缩与代码级 `pre-stop` 门，清理旧模型遗留的长篇微操提示词 | 严禁直接沿用旧模型上靠堆轮数、堆全量日志调出来的重型 Harness | 避免模型升级后准确率反跌 `-12.5pp` 和推理链 Token 倍增 |
| **场景 3：缺乏自动单测的开放式知识/架构交付** | **采用混合验证器 $R_x$ + 路由分支（Stage 4 `MoSIB`）**：先构建确定性 Schema/引用/CSP 校验脚本作为只读 `verify.py`，再按任务类型路由专用 Harness | 严禁把主观 LLM-as-a-Judge 评分脚本放在 Agent 可写工作目录内 | 杜绝幻觉交付与刷分，沉淀跨模型复用的确定性质量门 |
| **场景 4：一次性低频 PoC（总调用 `<30` 次）** | **直接复用 Google 验证过的五大涌现机制模板**（首尾压缩 + 状态页脚 + 分页读文件 + Pre-stop 守卫），无需启动外环搜索 | 无需为几十次调用跑上百轮外环进化 | 零搜索开销直接获得 ~80% 架构红利 |

---

## 五、生产落地核查清单（SA Implementation Checklist）

在为客户或自有研发平台搭建“自进化 Agent Harness”前，请逐项勾选以下 **8 项硬核验收单**：

- [ ] **1. 四模块物理拆解**：运行时代码是否已拆分为独立的 `context_mgr`（上下文/压缩）、`control`（循环/预算）、`action_aci`（工具封装）与 `verify`（退出门禁）四个独立文件，而非几千行纠缠在一起的 `agent.py`？
- [ ] **2. 淘汰纯文本禁令，下沉 `pre-stop` 代码守卫**：检查 `RULES.md` / System Prompt 中的“退出前必须……”条款，是否已转化为 `verify.py` 中可阻断 `finish` 动作的确定性代码校验（非空 diff、语法编译、核心回归测试）？
- [ ] **3. 开启历史观察首尾压缩 + 实时状态页脚**：是否对超过 2 轮的历史长观察执行了保护前缀 KV Cache 的首尾摘要遮蔽，并在每轮末尾注入简洁的 `[Turn k/N | Edited files | Last test status]` 状态栏？
- [ ] **4. 锁定只读外部评测器（防 Mode 5 刷分）**：外环依赖的测试套件、评分脚本与 Token 遥测账本是否严格位于容器只读挂载或沙箱外部，确保 Agent 进程 `uid` 零写入权限？
- [ ] **5. 绑定失败簇而非单题打补丁（防 Mode 1 过拟合）**：Stage 1 是否先对至少 `N ≥ 10` 道开发集失败轨迹做错误聚类，且禁止 Stage 2 生成包含具体仓库名/题号提示词的专用补丁？
- [ ] **6. 部署 Stage 3 三联门禁（$G_{\text{val}} + B_{\text{tok}}$）**：每次候选补丁合入前，是否同时强制检查：(a) 新增代码行运行时执行覆盖率 `> 0%`（剔除死代码）；(b) 独立验证集不回退；(c) 平均 Token 不突破 $B_{\text{tok}}$ 上限？
- [ ] **7. 跨分布（OOD）盲测验收**：除域内仓库外，是否保留了完全未参与外环诊断与筛选的跨项目/跨业务线 OOD 盲测集？
- [ ] **8. 模型升级重审计触发器**：每当底层模型切换新版本（如 Flash → Argon / Carbon），是否自动触发一轮轮数上限与上下文压缩比复核，防止长推理链模型遭遇上下文反噬？

---

## 六、可复现验证与参考资料（Verification & References）

本地一键运行确定性数据与门禁不变量校验：

```bash
python3 docs/research/google-self-improving-harnesses/simulator/verify_harness_evolution.py
```

1. **Deep Shah, Nehal Kathrotia (Google)**. *Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses*. `arXiv:2611.22299v1`, submitted Nov 17, 2026. https://arxiv.org/abs/2611.22299
2. **Hangfan Zhang et al.** *Self-Harness: Harnesses That Improve Themselves*. `arXiv:2606.09498`, June 2026. https://arxiv.org/abs/2606.09498
3. **Google Research**. *Regularized Recursive Self-Improvement (RRSI)*. https://github.com/google-research/rrsi
4. **Qi Chen (`@turbo998`)**. *Agent Harness × Frontier Model Co-Evolution: 120-Skill Telemetry Audit & Inverse Scaffolding Law*. [`docs/research/agent-harness-model-coevolution`](../agent-harness-model-coevolution/README.zh-CN.md), Nov 18, 2026.
