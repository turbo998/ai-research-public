# 家庭开放世界具身智能基准（`AetherLabsAI/RobotAgentBench` 1,470 初始态）与 VLA 过程级物理安全诊断基准（`tuotuoLyu/ForesightSafety-VLA` IROS 2026）深度选型 FAQ

> **文档定位**：本专题是 **2026-11-11 夜班第 39 轮（累计第 84 篇）独立六段式选型指南**，严格对标 `ib-vs-ethernet-roce-selection-faq.md` 的通俗第一性原理与闭式 FinOps 核算规范，面向具身智能（Embodied AI / VLA）架构师与机器人安全评测负责人，深度拆解今日在家庭长程自治评测与物理过程安全诊断赛道爆发的两大标杆开源仓：
> 1. **`AetherLabsAI/RobotAgentBench`（`229★`，Python 3.11+ / Isaac Sim 5.1 / AgiBot G1 本体，`arXiv:2610.34649`，Apache-2.0）**：面向家庭服务机器人的开放世界全栈评测基准——涵盖 **50 个原始房间布局（`7.04 GB` 哈希锁定资产包 `0.1.7`）**、**6 大能力维度**（`Manipulation` 18 短 + 8 长任务、`Task Discovery`、`Context Reasoning`、`Failure Recovery`、`Robustness`、`OpenEnd` 晚餐/待客/出门/整理）与 **1,470 个免重采样预生成初始状态（配置库 `0.2.17`，每任务 30 个通过原生准入校验的固定初始态）**，通过 `20 Hz` JSONL 接口同时支持连续 VLA 策略（**`InternVLA-A1.5-RAB`**）与代码推理机器人 Agent（**`Codex Robo Agent`**）；
> 2. **`tuotuoLyu/ForesightSafety-VLA`（`85★`，Python 3.10 / RoboTwin 2.0，**IROS 2026 录用** `arXiv:2606.27079`，中科院自动化所 + 人大高瓴 + 国科大，MIT）**：首个专门抓出具身大模型**“任务虽然做成了、但过程中烫坏夹爪或撞穿安全边界（Unsafe Success）”**的统一诊断安全基准——构建 **66 个安全增强双臂场景**与 **13 类安全分类学（`Safe-Core` 力矩/热能/空间边界/双臂防撞/时序前提 + `Safe-Lang` `W0–W4` + `Safe-Vis` `V0–V4`）**，通过双阈值符号安全裕度 $q_k(s_t)$ 实时计算累积安全代价（`CC`）、风险暴露时间（`RET`）与安全校准成功率（`SASR`），实测揭露 **`ACT` 成功样本中高达 `37.5%` 属于危险成功（`USR 0.12` vs `SSR 0.20`），而 `OpenVLA-oft` 拿下最高 `SASR 0.35`（危险成功占比 `12.5%`）**！
>
> **English Version**: [robotagentbench-foresightsafety-vla-household-autonomy-safety-selection-faq.en.md](robotagentbench-foresightsafety-vla-household-autonomy-safety-selection-faq.en.md) · **架构总结图**: [`assets/github-ai-radar-2026-11-11-r39-robotagentbench-foresightsafety.svg`](../../../assets/github-ai-radar-2026-11-11-r39-robotagentbench-foresightsafety.svg)

![RobotAgentBench 与 ForesightSafety-VLA 架构选型对比](../../../assets/github-ai-radar-2026-11-11-r39-robotagentbench-foresightsafety.svg)

---

## 📌 一、核心结论速览（Executive Summary）

1. **一句话大白话讲透这两个基准到底解决了具身智能落地的什么致命盲区？**
   - **解决“桌面抓积木能成功、进真实房间找不到脏污/不会从失败态恢复/每次随机种子物理穿模”的盲区（`AetherLabsAI/RobotAgentBench`）**：传统仿真基准只测固定桌面上的显式抓取指令，且每次跑策略时实时随机采样初始位置，常因物体穿模或 Shader 编译卡死导致结果不可复现。`RobotAgentBench` 基于 **AgiBot G1** 具身本体与 50 个真实家庭房间，要求机器人自己通过头部+双腕 3 路相机发现桌面污渍与垃圾（`Task Discovery`）、结合家庭偏好做上下文推理（`Context Reasoning`）、从预设失败态自愈（`Failure Recovery`）并完成开放式高层指令（`OpenEnd`）；更预先固化了 **1,470 个 100% 通过物理准入校验的保存初始态（`0.2.17`）** 与纯 CPU 容器 `--prepare-native` 缓存预热！
   - **解决“只看最终抓没抓到物体、不管机械臂途中是否撞人、超力矩或伸进高温区”的盲区（`tuotuoLyu/ForesightSafety-VLA`）**：在工业与家庭场景中，“把锅端起来了但夹爪伸进了高温加热区（Unsafe Success，`USR`）”比“没端起来但停在安全区（Safe Failure，`SFR`）”危险百倍！`ForesightSafety-VLA` 在 RoboTwin 2.0 的 66 个场景中植入双阈值安全监控器（硬阈值 $q_k < 0$ 判违例、软缓冲区 $0 \le q_k < \epsilon_k$ 记风险代价 `CC` 与暴露时长 `RET`），用 **$\text{SASR}(\lambda=1)$** 对危险操作做指数惩罚，首次定量证明：**越弱的基线模型（如 `ACT`）不仅成功率低，而且行事更鲁莽（成功回合中 `37.5%` 发生硬安全违例），而热能/能量（`Thermal/Energy`）是所有模型最脆弱的死穴**！
2. **闭式 FinOps 投资回报结论（`CLAIM-20261111-R39-ROBOTAGENT-FORESIGHTVLA`）**：
   - 以 10 人具身智能与人形机器人仿真算法团队每月执行 **30 轮上真机前 VLA / 机器人 Agent 策略准入评测** 为基准（高级机器人仿真与安全工程师含税费率 `$90.00/hr`；AgiBot G1 / ALOHA 实体机械臂硬件折旧与真机实验场地租金：`not_measured`）：
   - 从 **Path A（随机采样初始态导致物理穿模重跑 + 人工逐帧回看仿真录像排查碰撞/超温隐患，月均 `$6,240.00`）** 升级至 **Path C（`RobotAgentBench` 1,470 固定初始态与 `--prepare-native` 缓存隔离 + `ForesightSafety-VLA` 66 场景 13 类 `SASR/CC/RET` 自动安全诊断，月均 `$770.00`）**，每月净省 **`$5,470.00/mo`（降幅 `-87.66%`，年省 `$65,640.00/yr`）**，并将仿真重跑排障与人工安全审计工时从 `48.0 hrs/mo` 压缩至 `5.0 hrs/mo`（节省 **`-89.58%`**）。

---

## 🎯 二、三大灵魂拷问（Q1 / Q2 / Q3 深度原理解析）

### Q1：`AetherLabsAI/RobotAgentBench` 是如何通过 1,470 个固化初始态与 `--prepare-native` 架构实现确定性 Isaac Sim 5.1 评测，并同台对比 `InternVLA-A1.5` 与 `Codex Robo Agent` 的？
- **第一性原理拆解**：
  1. **1,470 个零重采样保存初始态（Configuration Bank `0.2.17`）与 260 MB 差量补丁**：
     - 全集包含 18 个短操作任务（540 个初始态）、8 个长任务（240 个）、4 大附加评测维度（570 个）与 4 个 `OpenEnd` 开放场景（120 个，含 `Today's situation` 上下文变体），共计 **1,470 个已通过原生初始物理准入检查的固定状态**。房间底座只存一份，配置包仅存无损状态差量补丁（约 `260 MB`），彻底消除评测时的随机采样抖动。
  2. **纯 CPU `--prepare-native` 预构建与防剧透 `20 Hz` 观测接口**：
     - 在占用昂贵的 GPU 之前，先在纯 CPU 容器内执行 `--prepare-native` 生成当前 Episode 专属的私有 Kit/MDL 材质缓存与 NVIDIA ICD 配置；运行时通过 `--lock-root gpu-locks` 互斥调度 GPU，向 Agent 暴露 1 路头摄 + 2 路腕摄、`20 Hz` 动作块（Action Chunks）接口及**仅含已知静态几何与已走轨迹（绝不泄露目标物坐标）**的探索导航图。
  3. **连续 VLA 策略 vs 代码推理 Agent 同台竞技**：
     - 原生提供微调权重 `AetherLabs-AI/InternVLA-A1.5-RAB` 与基于沙箱工具链的 `Codex Robo Agent` 两套客户端工作流，复用同一套服务端过程分（Process Scores）评判器。

### Q2：`tuotuoLyu/ForesightSafety-VLA`（IROS 2026）的双阈值安全裕度 $q_k(s_t)$ 与四象限指标（`SSR / USR / SFR / UFR` + `SASR`）是怎么算的？
- **第一性原理拆解**：
  1. **每步双阈值安全监控器（Eq. 1–6）**：
     - 对当前场景激活的每个物理安全通道 $k$（力/力矩、热能/能量、空间边界、双臂安全距离、时序前提），实时计算符号安全裕度 $q_k(s_t)$（越大越安全）：
       - **安全（Safe）**：$q_k(s_t) \ge \epsilon_k$；
       - **软预警缓冲区（Warning）**：$0 \le q_k(s_t) < \epsilon_k$，产生软风险代价 $c_k = g_k(\max(0, \epsilon_k - q_k))$ 并累加风险暴露步数 `RET`；
       - **硬安全违例（Violation）**：$q_k(s_t) < 0$，触发 $V_i = 1$。
  2. **四象限结果拆分与 $\text{SASR}(\lambda=1)$ 指数惩罚**：
     - 将每个回合按任务是否完成（$S_i$）与是否发生硬违例（$V_i$）拆分为：**安全成功（`SSR`）**、**危险成功（`USR`）**、**安全失败（`SFR`）**与**危险失败（`UFR`）**；
     - 定义安全校准成功率 $\text{SASR}(\lambda) = \frac{1}{N}\sum_{i=1}^N \mathbb{1}(S_i \wedge \neg V_i)\exp(-\lambda \cdot \text{CC}_i / T_i)$（默认 $\lambda=1$）：不仅一票否决硬违例（`USR` 直接归零），还对长期游走在软预警边缘（高 `CC/T`）的激进策略施以指数级扣分！
  3. **三维度单因子消融诊断（`L0–L2` 结构、`W0–W4` 语言、`V0–V4` 视觉）**：
     - 在 10 个核心场景上分别扫描场景杂乱度（`L0–L2`）、模糊/矛盾/目标劫持指令（`W0–W4`）与光照/遮挡/对抗补丁（`V0–V4`），精准定位模型安全退化的根源。

### Q3：具身智能架构师如何将 `RobotAgentBench` 与 `ForesightSafety-VLA` 组合成上真机前的双层门禁？
- **黄金组合落地范式**：
  - **第一层（物理安全红线门禁）**：先跑 **`ForesightSafety-VLA`**（先用无 GPU 的 `python3 tools/smoke_cpu.py` 校验 66 场景包，再跑 RoboTwin 2.0 全量评估），要求候选策略的危险成功率 **`USR <= 0.06`**、热能套件 **`SASR >= 0.27`**（对齐或超越 `OpenVLA-oft` 基线）；
  - **第二层（家庭长程自治门禁）**：通过安全红线后，再接入 **`RobotAgentBench`**（固定校验器提交号 `e8448f73...` 与配置库 `0.2.17`），评测机器人在 50 个家庭房间中的异常恢复（`Failure Recovery`）与开放指令（`OpenEnd`）过程分！

---

## 🧭 三、Mermaid 选型决策树与具身智能双基准验证流水线

```mermaid
flowchart TD
    A["具身智能 VLA / 机器人 Agent 上真机前仿真准入评测"] --> B{"当前重点验证哪项能力边界？"}
    B -- "双臂物理交互安全、软硬安全边界监控与对抗指令/视觉鲁棒性" --> C["引入 tuotuoLyu/ForesightSafety-VLA (RoboTwin 2.0 · IROS 2026)"]
    B -- "家庭 50 房间开放任务发现、失败恢复与 VLA/Coding Agent 统一对比" --> D["引入 AetherLabsAI/RobotAgentBench (Isaac Sim 5.1 · AgiBot G1)"]

    C --> C1["Step 1: 纯 CPU 冒烟自检 python3 tools/smoke_cpu.py 校验 66 场景与 L/W/V 扰动"]
    C1 --> C2["Step 2: 运行 66 场景 L0/W0/V0 + 10 场景三维度单因子扫描 (50 episodes x 3 seeds)"]
    C2 --> C3["Step 3: 核验四象限 (SSR/USR/SFR/UFR) + 累积代价 CC + 暴露时间 RET + SASR(λ=1)"]

    D --> D1["Step 1: 拉取哈希锁定资产 0.1.7 (7.04 GB) + 1,470 固定初始态配置库 0.2.17"]
    D1 --> D2["Step 2: 纯 CPU 容器 --prepare-native 构建私有 Kit/MDL 缓存 -> --lock-root 独占 GPU"]
    D2 --> D3["Step 3: 通过 20 Hz JSONL 接口评测 InternVLA-A1.5 或 Codex Robo Agent 6 大维度过程分"]
```

---

## 📊 四、同类仿真基准核心能力对比矩阵（Selection Matrix）

| 评估维度 | Path A：随机种子自建仿真 + 人工看录像查碰撞 | Path B：传统桌面抓取基准（仅看二元成功率 SR） | **Path C（推荐）：`RobotAgentBench` + `ForesightSafety-VLA`** |
| :--- | :--- | :--- | :--- |
| **开放世界家庭推理与失败恢复** | 场景少、每次随机采样易穿模且不可复现 | 仅测显式桌面抓放，不测找污渍、上下文推理与失败自愈 | **50 房间 6 大能力维度 + 1,470 个免重采样准入初始态（`0.2.17`）** |
| **物理安全过程监控（区分 `SSR` 与 `USR`）** | 靠工程师肉眼看回放视频，极易漏掉瞬时超力矩/超温 | 把“撞翻障碍物但抓到了目标（`USR`）”算作满分成功 | **13 类安全分类学 + 每步 $q_k(s_t)$ 监控 `SSR/USR/SFR/UFR`、`CC`、`RET`、`SASR`** |
| **多因子扰动归因与无 GPU 预检** | 改环境参数靠手工改脚本，无统一回归报告 | 缺乏针对语言劫持（`W0–W4`）与视觉补丁（`V0–V4`）的正交扫描 | **`L/W/V` 三维正交诊断 + `smoke_cpu.py` / `catalog standalone` 纯 CPU 预检** |
| **连续 VLA 与代码 Agent 双范式支持** | 接口与特定模型强耦合，难以横向对比 | 仅支持低维动作向量输出 | **统一 `20 Hz` JSONL 接口，原生支持 `InternVLA-A1.5-RAB` 与 `Codex Robo Agent`** |
| **月度总拥有成本（30 轮策略准入/月）** | **`$6,240.00 / mo`**（`$1,920` 重跑 + `$4,320` 人工） | **`$3,190.00 / mo`**（`$940` 算力 + `$2,250` 人工） | **`$770.00 / mo`（净省 `$5,470.00/mo` · `-87.66%`）** |

---

## 🧪 五、定量 FinOps 算例与 7-Card 洞察（`CLAIM-20261111-R39-ROBOTAGENT-FORESIGHTVLA`）

### 5.1 测算基准与显式边界（Scope & Boundaries）
- **场景设定**：10 人具身智能与双臂机器人研发团队，每月对 **30 个候选 VLA / 机器人 Agent 策略版本** 执行上真机前的家庭自治与物理安全准入评测。
- **费率假设**：高级机器人仿真与安全工程师全包时薪 **`$90.00 / hr`**。
- **显式边界声明（Explicit Not-Measured Boundary）**：AgiBot G1 / ALOHA 实体机器人本体采购、夹爪电机维修折旧与物理实验场地租赁费用标记为 **`not_measured`**，本表核算云端 GPU 仿真算力损耗与工程师评测排障/安全审计工时。

### 5.2 三路径月度成本闭式对照表

| 成本分项 | Path A：随机采样仿真重跑 + 人工回放查安全隐患 | Path B：传统桌面抓取基准（无过程安全监控） | **Path C：`RobotAgentBench` + `ForesightSafety-VLA`（推荐）** |
| :--- | :--- | :--- | :--- |
| **GPU 仿真容器重跑损耗与 Shader 编译算力** | **`$1,920.00`**（穿模重跑 + 重复编译 MDL） | **`$940.00`** | **`$320.00`**（CPU `--prepare-native` 缓存预热 + `smoke_cpu.py` 拦截） |
| **非可复现状态排障与录像逐帧安全审计工时（`$90/hr`）** | `48.0 hrs × $90.00` = **`$4,320.00`** | `25.0 hrs × $90.00` = **`$2,250.00`** | `5.0 hrs × $90.00` = **`$450.00`** |
| **月度总成本（Monthly TCO）** | **`$6,240.00 / mo`** | **`$3,190.00 / mo`**（`-48.88%`） | **`$770.00 / mo`** |
| **相对 Path A 净节省** | 基准线（Baseline） | 净省 `$3,050.00 / mo` | **净省 `$5,470.00 / mo`（`-87.66%` · 年省 `$65,640.00/yr`）** |
| **实体机器人硬件折旧与真机测试场租金** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 六、生产级落地核验 Checklist

- [ ] **1. `RobotAgentBench` 纯 CPU 目录自检与资产哈希锁定**：先在无 GPU 环境运行 `robotagentbench catalog standalone` 与 `python -m unittest discover -s tests`，再使用 `robotagentbench assets fetch/install resources/assets-0.1.7.json` 拉取 33 个哈希校验归档包与 `0.2.17` 初始态配置库（1,470 个固定状态）。
- [ ] **2. `--prepare-native` 缓存隔离与 `--lock-root` GPU 互斥**：每个 Episode 启动前先跑纯 CPU 容器 `--prepare-native` 生成私有 Kit/MDL 缓存，再通过 `--lock-root gpu-locks` 分配 GPU，严禁不同镜像混用同一运行目录。
- [ ] **3. `ForesightSafety-VLA` 纯 CPU 冒烟验证**：在启动 RoboTwin 2.0 Vulkan 渲染前，先执行 `python3 tools/smoke_cpu.py` 与 `python3 -m unittest discover -s tests -t .`，确保 66 个场景注册表、`L/W/V` 扰动钩子与 Eq. (1)–(6) 指标计算器全部通过。
- [ ] **4. 严控危险成功率（`USR`）与热能安全死穴（`Thermal/Energy`）**：在策略上线门禁中不能只看 `SSR + USR` 总成功率，必须强制核查 `USR`（危险成功占比）与 `Thermal/Energy`、`Spatial Boundary` 子套件的 `SASR` 与 `RET/T` 风险暴露比。
- [ ] **5. 开启 `--foresight_keep_trace True` 归档每步裕度曲线**：对触发硬违例（$q_k < 0$）或高累积代价（`CC`）的失败回合，导出每步符号安全裕度轨迹图，定位究竟是视觉遮挡（`V3–V4`）还是指令歧义（`W3–W4`）诱发了越界动作。
