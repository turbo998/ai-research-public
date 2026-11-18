# 免训练权重空间直接编程三剑客选型 FAQ：`brianbell-x/codehygiene` (13KB) + `brianbell-x/ssd-ransomware-guard` (89KB) + `Eppy-EpHard/AHA`

> **元数据（Metadata）**
> - **评测批次**：2026-11-16 夜间深潜 Round 5（累计 Round 362）
> - **核心标的**：
>   1. [`brianbell-x/codehygiene`](https://github.com/brianbell-x/codehygiene)（`★ 87` / `5 Forks`，`2026-11-15` 新建爆发黑马 · `13.0 KiB` `1.58-bit` 三值 `{-1, 0, +1}` 权重空间直接编译的 `574K` 参数 System-1 代码可读性与反 AI Slop 检测模型：纯 NumPy CPU 单次前向仅需 **`~10 ms`**，统一覆盖 11 种编程语言并输出 6 维子评分与行级波浪线诊断 `Squiggle`，附带 `12.97 KiB` 纯浏览器 Web Worker + Circuit X-ray 交互工作台）
>   2. [`brianbell-x/ssd-ransomware-guard`](https://github.com/brianbell-x/ssd-ransomware-guard)（`★ 53` / `6 Forks`，`2026-11-15` 新建爆发黑马 · MIT 协议 · 驻留在 **SSD 闪存主控片上 SRAM（`189.02 KB`）** 内的 **`88.75 KB`（`363,520` trits）** 三值 System-1 勒索软件零字节丢失回滚引擎：纯 C11 零浮点、零动态内存分配，每 `128` 次写入仅耗 **`4.0 ms`**，遇袭立即冻结 GC 垃圾回收并翻转 `L2P` 逻辑到物理页映射表，在 `9/9` QEMU NVMe `ext4` 实战攻击中实现 **`0 B` 数据丢失** 并通过 **`7/7` `Z3 QF_LIA` `UNSAT` 形式化验证**）
>   3. [`Eppy-EpHard/AHA`](https://github.com/Eppy-EpHard/AHA)（`★ 40` / `7 Forks`，`2026-11-15` 新建爆发黑马 · MIT 协议 · **无需任何外部大模型（No LLM）的自监督权重空间编程框架**：通过模型自身同前缀配对采样分支（Matched Pairs）与 Barry 线性规划，对两层 MLP `down_proj` 施加秩-1 稀疏修正 $W' = W + u v^\top$［每层仅改 8 列、`<= 8,192` 个权重］，零梯度下降将 `Qwen3.5-0.8B` 的 GSM8K 从 **`14.0%` 暴涨至 `71.2%` (`+57.2`)**、MATH-500 从 **`9.8%` 升至 `51.8%` (`+42.0`)**、分布外 IFEval 从 **`19.6%` 升至 `62.7%` (`+43.1`)**）
> - **配套架构图**：[`assets/github-ai-radar-2026-11-16-r5-weightspace-trio.svg`](../../../assets/github-ai-radar-2026-11-16-r5-weightspace-trio.svg)
> - **证据封存锚点**：`CLAIM-20261116-R5-WEIGHTSPACE-TRIO`（见 [`evidence/trending-daily-2026-11-16-audit.json`](../evidence/trending-daily-2026-11-16-audit.json)）

---

## 📌 1. 核心结论速览（Executive Summary & First-Principles Pitch）

1. **一句话讲透本质**：
   - **`brianbell-x/codehygiene` (`13.0 KiB`, `574K` 参数)**：就是**把“资深架构师一眼看出 AI Slop 烂代码的直觉（System 1）”直接用数学公式编译进 13 KB 三值权重里的毫秒级代码门禁**。传统 Linter（Ruff/ESLint）只能抓语法错误，拦不住层层缩进、满屏废话注释和吞掉异常的 AI 垃圾代码；而每次提交调大模型做 Code Review 又贵又慢。`codehygiene` 不用一丁点训练数据和梯度下降，直接在 `compile.py` 里把数学特征电路编译成 `569,662` 个严格取值为 `{-1, 0, +1}` 的三值权重（每字节压 5 个 Trit，总包仅 **`13.0 KiB`**），在 CPU 上 **`~10 ms`** 扫完 11 种语言的源码，直接标出 `[noisy_comment]`、`[deep_nesting]` 与 `[swallowed_error]` 行级波浪线！
   - **`brianbell-x/ssd-ransomware-guard` (`88.75 KB` 权重 / `189.02 KB` SRAM)**：就是**利用 SSD 闪存“永不原地覆写”的物理第一性原理，把三值 AI 防护网直接塞进硬盘主控 SRAM 里的“零字节丢失时光机”**。操作系统层的杀毒软件（EDR）一旦被内核 Rootkit 绕过，勒索软件就会加密全盘；但在 SSD 内部，新写入的密文其实写在了全新的 Flash 页上，**原本的明文数据依然完好无损地躺在硅片旧页上，直到垃圾回收（GC）把它擦除**！该项目将 `363,520` 个三值权重（`88.75 KB`）编译进 `189.02 KB` 的无操作系统 C11 引擎，每 `128` 次 NVMe 块写入仅耗时 **`4.0 ms`** 完成零浮点整数推理：一旦识破加密特征，立即在硬件层冻结 GC、锁死 `TRIM`/擦除指令，并直接把 `L2P`（逻辑到物理块映射表）指针拨回旧明文页——**`9/9` 次真实 Linux NVMe 勒索与擦除攻击 `0 字节` 丢失，甚至在 85% 满盘攻击中途拔掉电源，也能靠 `3.79 KB` 超级电容日志 100% 救回全部 `1,500/1,500` 个文件**！
   - **`Eppy-EpHard/AHA` (`Self-Supervised Weight-Space Programming`)**：就是**不用请昂贵的外部大模型当外科医生，让小模型“自己给自己做微创脑科手术”治好无限复读死循环**。小尺寸推理模型（如 `Qwen3.5-0.8B`/`2B`）经常自己跟自己车轱辘话复读到 Token 耗尽。此前做权重空间编程（Weight-Space Programming）需要依赖 Frontier 大模型 Agent 去读写权重；`AHA` 证明完全不需要外部 LLM：只要在模型开始复读前 8 个 Token 处截断，从同一前缀采样 8 条分支，把“不复读的正常分支”与“最早陷入复读的分支”在同一层的残差流均值相减得到方向向量 $u$，再用线性规划选出仅含 8 个非零神经元的触发向量 $v$，对两层 MLP `down_proj` 加上秩-1 修正 $W' = W + u v^\top$（在 0.8B 模型中每层最多只改 `8,192` 个权重），就能让 `Qwen3.5-0.8B` 的 GSM8K 从 **`14.0%` 飙升到 `71.2%`**！
2. **核心量化收益（FinOps 闭式账本 `CLAIM-20261116-R5-WEIGHTSPACE-TRIO`）**：
   - 在 **每月执行 50,000 次 PR 代码卫生门禁 + 守护 40 个核心 NVMe 存储节点 + 完成 15 款端侧小模型去复读外科修正** 的企业工作负载下（工程师全负担时薪 `$100.00/hr`；物理 NVMe 盘片采购与机柜电费标记为 `not_measured`）：
   - **Path C（`codehygiene` + `ssd-ransomware-guard` + `AHA` 权重空间编程三剑客）** 将月度总拥有成本（TCO）从 **Path A（全量调云端 LLM 审代码 + 依赖 OS 层 EDR 事后恢复 + 调 Frontier Agent 或全量微调救小模型）的 `$6,220.00/月`** 降至 **`$395.00/月`**，净省 **`$5,825.00/月`（`-93.65%`，年化节省 `$69,900.00/年`）**，每月释放 **`37.8 小时`（`-92.20%`）** 的工程维护工时。

![2026-11-16 Night Round 5 (R362) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-16-r5-weightspace-trio.svg)

---

## ❓ 2. 灵魂拷问 Q1–Q3（First-Principles Deep Dive）

### Q1：为什么不需要任何训练数据和梯度下降，就能在 `compile.py` 里“手搓”出 574K 参数的代码卫生神经网络和 363K 参数的 SSD 防勒索网络？
- **第一性原理拆解**：
  1. **System-1 快思考本质上是可组合的局部特征电路**：无论是识别代码里的“复读机式废话注释 / 6 层嵌套 `if` / 空 `except:` 吞异常”，还是识别 NVMe 写入流里的“文件头魔法字节被高熵密文覆盖 + 冷数据块突遭顺序覆写”，其底层判据都是明确的代数与时序局部模式。
  2. **`codehygiene` 的 13.0 KiB 三值编译架构**：在 `compile.py` 中直接将字节网格掩码（Block 0）、局部卷积、因果注意力与通道缩放偏置构造为严格取值于 `{-1, 0, +1}` 的 `569,662` 个 Trit（按 `5 trits/byte` 紧凑打包）加上 `4,103` 个一维通道缩放/偏置参数，总计仅 **`13.0 KiB`**。不生成任何废话 Token，单次前向传播（CPU `~10 ms`）直接输出校准后的 `0.0–1.0` 卫生总分、`flatness`/`naming`/`simplicity`/`comments`/`error_handling`/`layout` 6 个子维度得分、风格原型（如 `style: slop (98%)`）以及精确到行号的 `Squiggle` 诊断。
  3. **`ssd-ransomware-guard` 的 88.75 KB 零浮点片上 C11 引擎 + Z3 形式化证明**：将 `128` 种文件头语法、差分转换门、4 头因果注意力与步长滤波器直接解析编译为 `363,520` 个三值权重（`88.75 KB` @ `2 bits/trit`）。在脱离操作系统的 `189.02 KB` 静态 C11 中仅使用无分支整数运算（`int8`/`int16`/`int32`，零浮点、零 `malloc`），通过 `500` 个窗口的 C11/Python 逐比特一致性测试与 **`7/7` 项 `Z3 QF_LIA` 白盒形式化不可满足（`UNSAT`）证明**！

### Q2：`Eppy-EpHard/AHA` 是如何在完全不调用外部 LLM、也不跑梯度下降的情况下，把 `Qwen3.5-0.8B` 的 GSM8K 准确率从 `14.0%` 拉升到 `71.2%` 的？
- **传统痛点**：小参数推理模型在生成思维链时极易卡在局部吸引子（无限重复同一句话直到耗尽 `max_tokens`）。以往要用权重空间编程修复它，必须让 Claude/GPT 等昂贵的外部 Agent 反复探查并修改模型权重。
- **`AHA` 的三步自监督秩-1 手术（$W' = W + u v^\top$）**：
  1. **Step 1 — 同前缀配对提取推力方向 $u$（Matched Pairs）**：取一条发生死循环复读的基础回答，用检测器找到复读起点（Loop Onset），退后 8 个 Token 截断；从这**完全相同的前缀**采样 8 条最长 3,072 Token 的续写分支。只要其中既有复读分支又有正常走完的分支，就将“最早开始复读的分支”与“最长有效产出的分支”配成一对，在未修改模型上跑前向，取复读起点后 64 Token 开始的 160 个 Token 残差流均值相减——因为前缀、题目、位置与长度完全相同，相减后剩下的纯粹是“走出死循环 vs. 陷入死循环”的行为方向 $u$！
  2. **Step 2 — 线性规划求解稀疏触发神经元 $v$（Barry's Linear Program）**：通过最小化 $\sum |v_j|$ 线性规划选出仅含 **8 个非零条目**的向量 $v$（意味着在 `Qwen3.5-0.8B` 的单层 `down_proj` 中最多只改动 **8 列、`8,192` 个权重**）。
  3. **Step 3 — 跨分布零样本泛化验证**：仅利用 GSM8K-train 与 MATH-train 轨迹构造的秩-1 修改，在**完全未进入流水线的分布外指令遵循基准 IFEval（541 题）** 上，将 `Qwen3.5-0.8B` 从 **`19.6%` 提升至 `62.7%`（`+43.1 pts`，`14.4 s.e.`）**，将 `Qwen3.5-2B`（自动搜索选定第 2 层与第 4 层）从 **`61.4%` 提升至 `77.1%`（`+15.7 pts`）**，全面超越 Barry 均值差分法 `2.3–5.8` 个百分点并追平外部 Frontier Agent 手工调权！

### Q3：这三个项目各自的诚实边界（Limitations）在哪里？
- **诚实边界**：
  - `codehygiene` 评估的是**代码表面结构与可读性卫生（System-1 风格直觉）**，不替代编译器类型检查、单元测试或深层业务逻辑的形式化验证。
  - `ssd-ransomware-guard` 目前端到端闭环已在 Linux `ext4`（基于 QEMU NVMe/NBD）、85% 满盘 CoW FTL 模拟器与独立 C11 上实证通过，但针对 Windows `NTFS`、真实物理商业主控 ASIC 固件流片以及慢速潜伏型低频加密的扩展仍在路线图中。
  - `AHA` 作者在 `docs/RESULTS.md` 中极为诚实地指出：在 `0.8B` 上 AHA 的成绩是**追平（Parity，差距在 `1 s.e.` / `3.0` 分以内）** 外部 Agent 权重编辑而非大幅超越，且完整公开了所有未奏效的负向实验记录。

---

## 🧭 3. Mermaid 选型决策树与架构对比图

```mermaid
flowchart TD
    Start["权重空间直接编程 (Weight-Space Programming) 三大落地场景选型"] --> Scene{"你要解决哪一层面的问题？"}

    Scene -->|"在 CI 或 Coding Agent 提交前以毫秒级拦截深层嵌套、废话注释与吞异常的 AI Slop 代码"| CodeGate{"是否希望零 GPU、零 Token 跨 11 语言统一打分？"}
    CodeGate -->|"采用 13.0 KiB 1.58-bit 三值编译网络 (~10ms CPU)"| UseCodeHygiene["✅ 选用 brianbell-x/codehygiene<br/>npx skills add brianbell-x/codehygiene -g<br/>6 维子评分 + 行级 Squiggle + 12.97 KiB 浏览器 X-ray"]

    Scene -->|"在存储底层防御绕过操作系统内核的勒索软件与全盘 Wiper 擦除攻击"| StorageGate{"如何实现真正的 0 字节丢失与断电秒级恢复？"}
    StorageGate -->|"利用 NAND 异地写物理特性 + 189 KB 片上 SRAM 三值模型"| UseSSDGuard["✅ 选用 brianbell-x/ssd-ransomware-guard<br/>88.75 KB 三值权重 + 4.0ms/128写 无分支 C11<br/>冻结 GC 翻转 L2P 回滚 + 7/7 Z3 QF_LIA UNSAT"]

    Scene -->|"修复端侧小推理模型 (0.8B/2B) 思维链无限复读死循环，且不想跑微调或调昂贵外部 LLM"| ModelGate{"是否采用同前缀分支配对 + 线性规划秩-1 权重修改？"}
    ModelGate -->|"仅改两层 down_proj 各 8 列 (W' = W + u v^T)"| UseAHA["✅ 选用 Eppy-EpHard/AHA<br/>Qwen3.5-0.8B GSM8K 14.0%→71.2% · IFEval 19.6%→62.7%<br/>100% 自监督零梯度、零外部 LLM 参与"]
```

---

## 📊 4. 同类方案对比矩阵（Quantitative & Architectural Comparison）

| 对比维度 | `brianbell-x/codehygiene` | `brianbell-x/ssd-ransomware-guard` | `Eppy-EpHard/AHA` | 传统方案：LLM Judge / OS 杀软 / 全量微调 |
| :--- | :--- | :--- | :--- | :--- |
| **模型体积 / 改动量** | **`13.0 KiB`**（`569,662` trits @ `1.58-bit`） | **`88.75 KB`** 权重（驻留 `189.02 KB` SRAM） | 仅改 **2 层 × 8 列**（`0.8B` 每层 `<= 8,192` 权重） | 数十 GB 权重 / 全参数梯度更新 |
| **推理/求解耗时** | CPU 单次前向 **`~10 ms`**（零 Token 生成） | 每 128 次写入 **`4.0 ms`**（纯整数 C11） | 单机采样配对 + 线性规划秒级求解 | 每次调用数秒至数十秒 / GPU 训练数小时 |
| **核心实证指标** | 跨 **11 种语言**输出 6 维可读性分与行级波浪线 | `9/9` 勒索攻击 **`0 B` 丢失** · `7/7` Z3 `UNSAT` | `0.8B` GSM8K **`+57.2`** · MATH **`+42.0`** · IFEval **`+43.1`** | 易受 Prompt 抖动、Rootkit 绕过或灾难性遗忘影响 |
| **外部 LLM / 训练依赖** | **0 训练数据、0 梯度下降、0 外部 API** | **0 训练数据、0 浮点、0 操作系统依赖** | **0 外部 LLM、0 梯度下降、0 人工标注** | 强依赖昂贵云端 API 与标注数据集 |

---

## 🃏 5. 7-Card 定量洞察与 FinOps 闭式账本（7-Card Quantitative Insights）

| 卡片编号 | 维度标签 | 核心定量洞察（Headline-as-Finding） | 证据与闭式参数锚点 |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | 权重空间直接编程三剑客将月度代码卫生门禁、防勒索与小模型修复 TCO 降低 `93.65%`（`$6,220.00 → $395.00/月`） | `CLAIM-20261116-R5-WEIGHTSPACE-TRIO` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `codehygiene` 将 `574K` 参数压入 `13.0 KiB` 三值权重，CPU `~10 ms` 跨 11 语言精准揪出 AI Slop | `compile.py` & `docs/` Web Worker |
| **Card 3** | `3/7 · WHAT I TESTED` | `ssd-ransomware-guard` 在 `189.02 KB` SRAM 中 `4.0 ms` 判定攻击并翻转 `L2P`，`9/9` 实战攻击 `0 B` 丢失 | `QEMU_REDTEAM_VERIFIER_REPORT.md` |
| **Card 4** | `4/7 · UNDER THE HOOD` | `AHA` 用同前缀复读/正常配对残差差值 $u$ + 8 列线性规划 $v$ 实现 $W' = W + u v^\top$ 免 LLM 外科修正 | `Eppy-EpHard/AHA` `README.md` |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `ssd-ransomware-guard` 断电恢复 `1,500/1,500` 文件且 `7/7` Z3 `UNSAT`；`AHA` 在分布外 IFEval 暴涨 `+43.1` 分 | `verification/smt_verify.py` & `RESULTS.md` |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | 剥离 50,000 次慢速 LLM 审代码 Token 与全量微调算力，每月节省 `37.8 小时`（`-92.20%`）排障与恢复工时 | 50k PR 检查 + 40 节点 + 15 模型/月 |
| **Card 7** | `7/7 · MY TAKE` | 标志着“免训练解析编译三值小模型 + 自监督秩-1 权重手术”正式成为端侧与硬件级 AI 的黄金利器 | 物理硬盘与机柜硬件费：`not_measured` |

### 💰 FinOps 闭式参数表（每月 50,000 次代码卫生检查 + 40 个存储节点守护 + 15 款小模型修复，`r = $100.00/hr`）

| 方案路径 | API Token、GPU 微调与备份开销 (`compute_and_token_usd`) | 规则维护、勒索恢复与调参工时 (`engineering_hours`) | 工程人力成本 (`engineering_labor_usd`) | 月度总 TCO (`total_monthly_usd`) | 较 Path A 净节省 (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：云端 LLM 审代码 + OS 级 EDR + 全量微调/外部 Agent** | `$2,120.00` | `41.0 hrs` | `$4,100.00` | **`$6,220.00`** | Baseline (`0.00%`) |
| **Path B：11 套语言 AST 规则 + 定时快照备份 + 惩罚系数盲调** | `$960.00` | `19.0 hrs` | `$1,900.00` | **`$2,860.00`** | `-$3,360.00` (`-54.02%`) |
| **Path C：`codehygiene` + `ssd-guard` + `AHA` 权重编程（推荐）** | **`$75.00`** | **`3.2 hrs`** | **`$320.00`** | **`$395.00`** | **`-$5,825.00` (`-93.65%` / 年省 `$69,900.00`)** |

---

## 🛠️ 6. 实战上手 Checklist（15-Minute Actionable Rollout）

```bash
# 1. 全局安装 brianbell-x/codehygiene (13.0 KiB 三值模型)，对当前仓库执行 ~10ms 反 AI Slop 门禁检查
npx skills add brianbell-x/codehygiene -g
uvx --from git+https://github.com/brianbell-x/codehygiene codehygiene . --check

# 2. 编译验证 brianbell-x/ssd-ransomware-guard (88.75 KB 权重 + C11 引擎 + 7/7 Z3 QF_LIA 形式化证明)
git clone https://github.com/brianbell-x/ssd-ransomware-guard.git && cd ssd-ransomware-guard
pip install -e . && make weights c_lib test smt

# 3. 运行 Eppy-EpHard/AHA 自监督秩-1 权重修正流水线，消除 Qwen3.5-0.8B / 2B 复读死循环
git clone https://github.com/Eppy-EpHard/AHA.git && cd AHA
uv sync && uv run python -m src.cli --help
```
