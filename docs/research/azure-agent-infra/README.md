# Azure AI Agent Infrastructure Playbook：从四层全栈架构、六大计算运行时到 AKSClaw 与 E2B on Azure 生产实践 (Bilingual Edition / 中英双语版)

> 🌐 **Language / 语言切换**: **[🇨🇳 中文主页 (README.md)](README.md)** | **[🇬🇧 English Edition (README.en.md)](README.en.md)** | **[📚 305章完整技术长卷归档 (`docs/full-monograph-archive.md`)](docs/full-monograph-archive.md)** | **[📊 7-Card 评测报告 (中文)](test-report.md)** | **[📊 7-Card Report (EN)](test-report.en.md)** | **[🖼️ 7-Card 离线卡片 (`cards.html`)](cards.html)** | **[🖥️ 交互式选型与 10万沙箱计算器 (`selector.html`)](selector.html)**

> **Executive Summary / 核心结论概览**：
> 企业级 AI 应用正从 **“无状态单次 Prompt 问答（Stateless Chat）”** 演进为 **“长周期、有状态、会写代码、会调工具、会操作完整虚拟计算机的自主智能体（Stateful Autonomous Agent）”**。本专题围绕 **“计算与状态解耦（Compute-State Decoupling）”** 与 **“平台级零信任硬边界（Never Trust the Prompt）”** 两大核心公理，系统拆解在 Azure 上构建生产级 AI Agent 的 **四层参考架构（Build · Run · Ground · Control & Govern）**、**六大计算运行时光谱**、**代际实测基准** 与 **现场五步落地法**：
> 1. **六大运行时精准卡位不同隔离边界与恢复延迟 SLO**：从全托管 `Foundry Hosted Agents`（1,400+ MCP 工具）、`Durable Functions`（跨天 HITL 零算力挂起）、`ACA Dynamic Sessions`（Hyper-V 预热池 `~210 ms`）、`ACA Sandboxes Preview`（显式快照 `~320 ms`）、`AKS + Kata Pod VM (AKSClaw)`（多租户独立内核 + 5 道平台安全硬边界）到 `E2B on Azure VMSS Flexible (Standard_D96as_v7)`（10 万+ 并发 Firecracker MicroVM）。
> 2. **第五代 AMD EPYC Turin (`Standard_D96as_v7`) + Azure Boost 代际跃迁**：实测将 E2B Base 沙箱恢复延迟从上代 `D96as_v6`（239 ms）缩短至 **`108 ms`（提速 54.8%）**，Code-Interpreter V1 启动延迟从 `255 ms` 缩短至 **`132 ms`（提速 48.2%）**；在 `85% HugePages` 预留与 `60% CPU` 扩容水位下，仅需 **261 台 `D96as_v7` 客户端节点**（总计 278 台 VM）即可在单个 VMSS Flexible 规模集内稳态承载 **100,000 个并发 512 MiB MicroVM 沙箱**。
> 3. **双层状态底座与零信任治理**：采用 **Azure HorizonDB (Preview)**（PG ACID + JSONB + DiskANN Vector + 15 只读副本，配合 PgBouncer 将 10 万沙箱连接收敛至 1,200 后端连接，`4.8 ms` P99）或 **Azure Cosmos DB** 存储业务检查点与长期记忆，结合 **`UFFD + NBD` 沙箱快照** 冻结进程内存与文件系统现场；通过 **Microsoft Entra Agent ID + Unified AI Gateway (APIM) + 封禁 IMDS (`169.254.169.254`)** 落实 5 道不可绕过的平台安全硬边界。
> 4. **全量可复核工程资产**：配套 **8 幅通过 XML 校验的高清 SVG 架构图谱**、**305 章跨行业物理仿真章节**（完整长卷归档于 [`docs/full-monograph-archive.md`](docs/full-monograph-archive.md)）、**298 套 Bicep/Terraform/YAML 生产级蓝图**（[`blueprints/`](blueprints)）与 **297 个确定性仿真器 / 306 项单元测试**（[`simulator/`](simulator)）。

---

## 1. 交互式工作台与可复核评测套件 (Interactive Workbench & Benchmark Suite)

| 资产类别 | 本地/仓库内直达入口 | 在线交互预览 (GitHub Pages) | 核心能力说明 |
|---|---|---|---|
| **1. 全景交互手册 (`index.html`)** | [`index.html`](index.html) | [打开在线全景手册 ↗](https://turbo998.github.io/Azure-Infra-Lab/workshops/azure-agent-infra/index.html) | 四层架构交互式图谱切换、六大运行时矩阵与五步落地法中英双语导览 |
| **2. 实时双轨仿真台 (`demo.html`)** | [`demo.html`](demo.html) | [启动 AKSClaw × E2B 仿真 ↗](https://turbo998.github.io/Azure-Infra-Lab/workshops/azure-agent-infra/demo.html) | 单步/自动回放 AKSClaw 五道硬边界拦截与 E2B `UFFD+NBD` 108ms 恢复全链路 |
| **3. 选型决策器 & 10万沙箱计算器 (`selector.html`)** | [`selector.html`](selector.html) | [打开选型与容量计算器 ↗](https://turbo998.github.io/Azure-Infra-Lab/workshops/azure-agent-infra/selector.html) | 双阶段决策树、10万并发 VMSS 节点/TCO 测算、HorizonDB 连接池计算器及分域仿真台 |
| **4. 7-Card 4:5 基准报告 (`cards.html`)** | [`cards.html`](cards.html) · [中文报告](test-report.md) · [EN Report](test-report.en.md) | [查看 7-Card 视觉评测卡 ↗](https://turbo998.github.io/Azure-Infra-Lab/workshops/azure-agent-infra/cards.html) | 严格锁定 CSP（`default-src 'none'; style-src 'unsafe-inline'`），绑定 [`report.json`](report.json) |
| **5. 305章完整技术长卷与仿真源码** | [`docs/full-monograph-archive.md`](docs/full-monograph-archive.md) · [`simulator/agent_infra_sizer.py`](simulator/agent_infra_sizer.py) | [Step 04 Workshop Runbook](workshop-runbook.md) | 305 章完整推导、298 套 IaC 蓝图、297 个物理仿真函数与 306 项单元测试 |

---

## 2. 八大高清矢量架构与工作流图谱 (8-SVG Visual Architecture Atlas)

本专题所有架构与工作流图均提供自包含 SVG 矢量源文件（同时位于 [`assets/svg/`](assets/svg) 与 [`assets/`](assets)，100% 通过 `xml.etree.ElementTree` 语法校验）：

### 图 1：Azure AI Agent Infra 四层全栈参考架构全景图 (`Build · Run · Ground · Control & Govern`)

![Azure AI Agent Infra 四层全栈参考架构全景图](assets/svg/01-azure-agent-infra-4layer-panorama.svg)

> **图解说明**：自上而下串联 **L1 Build（MAF / GitHub Copilot SDK / LangGraph / OpenClaw / MCP & A2A）**、**L2 Run（六级计算运行时光谱）**、**L3 Ground（Foundry 11,000+ 模型、Foundry IQ / AI Search、HorizonDB Preview、Cosmos DB 与 `UFFD/NBD` 沙箱快照）** 以及 **L4 Control & Govern（Entra Agent ID 双重归属、Unified AI Gateway APIM 零密钥与配额熔断、Defender & Purview）**。

---

### 图 2：Azure 六大 Agent Runtime 责任边界、隔离机制与恢复延迟矩阵

![Azure 六大 Agent Runtime 责任边界、隔离机制与恢复延迟矩阵](assets/svg/02-runtime-spectrum-6tier-matrix.svg)

| 对比维度 | 1. Foundry Hosted Agents | 2. Durable Functions | 3. ACA Dynamic Sessions | 4. ACA Sandboxes (Preview) | 5. AKS + Kata (`AKSClaw`) | 6. E2B on Azure VMSS (`D96as_v7`) |
|---|---|---|---|---|---|---|
| **核心适用负载** | 标准 To-B 企业 API 与 MCP 助手 | 跨天人工审批挂起与 Saga 事务编排 | 亚秒级不可信代码片段执行 | 有状态 Coding/Browser 工作区（支持 `pause/resume`） | 多租户企业 Agent 平台与 SRE 常驻舰队 | 10万+ 并发云端虚拟电脑（`Manus × E2B` 模式） |
| **底层隔离边界** | 平台托管多租户服务容器 | Serverless Worker 进程隔离 | **Hyper-V 硬件虚拟化微边界** | **Hyper-V 沙箱 + 持久化快照卷** | **Kata Containers 独立 Guest Kernel (`kata-mshv-vm-isolation`)** | **KVM + Firecracker MicroVM + 独立 NetNS (`UFFD + NBD`)** |
| **冷启动 / 恢复延迟** | 托管预热池（`~400 ms`） | 事件驱动重放（`~150–500 ms`） | **`~210 ms`**（预热会话池分配） | **`~320 ms`**（快照显式恢复） | `~850 ms`（Kata Pod VM 启动） | **`108 ms` Base / `132 ms` Code-Interpreter V1** |
| **状态持久化机制** | Foundry Threads + Cosmos DB / AI Search | Durable Task 确定性重放日志 | 临时沙箱（空闲销毁，结果外置落库） | 显式内存/磁盘快照 + `HorizonDB` | 实例独占 RWO PVC + 共享 ROX 技能库 + `HorizonDB` | `UFFD` 缺页流式恢复 + `NBD` 块差分快照 + Blob |
| **运维复杂度** | `1 / 10`（全托管零集群运维） | `3 / 10`（Serverless PaaS） | `2 / 10`（托管会话池） | `4 / 10`（Preview 沙箱 PaaS） | `7 / 10`（托管 K8s + 平台工程团队） | `9 / 10`（自管 VMSS + Nomad/Consul + 内核 `UFFD`） |

---

### 图 3：AI Agent Infra 双阶段架构选型决策树与数据底座配对图

![AI Agent Infra 双阶段架构选型决策树与数据底座配对图](assets/svg/03-scenario-decision-tree-and-routing.svg)

> **图解说明**：
> - **第一阶段（业务形态与研发能力门禁）**：区分 **To-B 企业内部/客户服务场景** 与 **To-C 数字原生 AI 产品**；若客户需要超越全托管服务的底层基础设施控制权，但**缺乏自有研发/平台工程团队**，严禁直接退回推荐 Foundry Hosted Agents，必须触发 **CSU / Partner 交付门禁（Hold for CSU / Partner）**。
> - **第二阶段（隔离级别、恢复延迟与状态配对）**：根据是否执行不可信代码、是否需要跨会话保留进程/DOM 现场、并发规模（千级 vs 10万级）精准路由至对应运行时，并配对 **Azure HorizonDB (Preview)**、**Azure Cosmos DB** 与 **Blob 快照卷**。

---

### 图 4：AKSClaw 多租户 Kubernetes Agent 平台参考架构（6 大支柱与 5 道平台硬边界）

![AKSClaw 多租户 Kubernetes Agent 平台参考架构](assets/svg/04-aksclaw-multi-tenant-k8s-architecture.svg)

> **图解说明**：在 AKS 上运行 OpenClaw / Hermes / 自研 SRE Agent 舰队时，通过 **6 大支柱** 与 **5 道不可绕过的平台层安全硬边界** 实现多租户零信任隔离：
> 1. **Runtime Sandbox**：`runtimeClassName: kata-vm-isolation`（Hyper-V / Cloud Hypervisor 独立 Guest Kernel），防容器逃逸；
> 2. **IMDS Block**：Calico/Cilium `NetworkPolicy` 强制拦截 `169.254.169.254/32`，彻底阻断窃取宿主机 Kubelet 凭据；
> 3. **Egress Allowlist**：默认拒绝出网，仅放行 Unified AI Gateway 与受控 MCP / Git 端点；
> 4. **Keyless Pod & Credential Injection Proxy**：容器环境变量零 API Key，由边车/网关代理注入短时最小权限凭证；
> 5. **Entra Agent ID + Unified AI Gateway (APIM)**：强制记录 `Blueprint + Human Sponsor` 双重审计归属，实施用户/团队/实例三级 RPM·TPM·预算硬熔断。

---

### 图 5：E2B on Azure VMSS 生产级参考架构图（Manus × E2B 10万+ 并发云端沙箱底座）

![E2B on Azure VMSS 生产级参考架构图](assets/svg/05-e2b-on-azure-vmss-reference-architecture.svg)

> **图解说明**：采用 **Application Gateway WAF v2（公私双前端 IP，`*.e2b.<domain>` 通配符证书）→ Azure API Management（按动态沙箱 `Host` 独立 `rate-limit-by-key` 限流并透传 WebSocket）→ Internal ALB → VMSS Flexible Client Pool (`Standard_D96as_v7`)** 双跳入口架构，在单个 Azure VMSS Flexible 规模集（**261 台客户端节点 + 17 台控制面/构建节点 = 278 台 VM**）内稳定支撑 **100,000 个并发 512 MiB Firecracker MicroVM**。

---

### 图 6：Firecracker MicroVM 沙箱内部机理 (`UFFD + NBD`) 与 Azure v6/v7 实测启动延迟对比

![Firecracker MicroVM 沙箱内部机理与 Azure v6/v7 实测启动延迟对比](assets/svg/06-e2b-microvm-internals-and-vm-benchmark.svg)

| Azure VM SKU | 处理器代际与硬件卸载 | 规格 (`vCPU / RAM`) | Base Sandbox 恢复延迟 (`ms`) | Code-Interpreter V1 启动 (`ms`) | Linux 按需单价 (`USD/hr`) | 架构师选型结论 |
|---|---|---|---:|---:|---:|---|
| **`Standard_D96as_v7`** | **第五代 AMD EPYC Turin (最高 4.5 GHz) + Azure Boost** | `96 vCPU / 384 GiB` | **`108 ms`** | **`132 ms`** | `$4.608/hr` | **生产首选标杆（比 v6 Genoa 提速 `54.8%`，单价持平）** |
| `Standard_D96s_v6` | 第五代 Intel Xeon Emerald Rapids | `96 vCPU / 384 GiB` | `116 ms` | `159 ms` | `$4.838/hr` | 次选 Intel 替代方案（CI-v1 慢 `20.5%`，成本高 `5.0%`） |
| `Standard_D96as_v6` | 第四代 AMD EPYC Genoa | `96 vCPU / 384 GiB` | `239 ms` | `255 ms` | `$4.608/hr` | 上代基线（建议立即升级至 v7 Turin） |

---

### 图 7：多智能体协同工作流 (`MAF × Copilot SDK × Durable`) 与状态持久化选型矩阵

![多智能体协同工作流与状态持久化选型矩阵](assets/svg/07-multi-agent-workflow-and-state-checkpoint.svg)

> **图解说明**：展示 **LangGraph / MAF 分诊智能体 → GitHub Copilot SDK 编码/排障智能体（在 ACA Sandbox / AKS Kata 沙箱内安全执行 Shell 与 MCP 工具）→ Foundry 合规审计智能体 + Durable Functions 人工审批挂起** 的端到端闭环，并对比 **Azure HorizonDB (Preview)**、**Azure Cosmos DB** 与 **Sandbox Snapshot (`UFFD + NBD`)** 的协同分工。

---

### 图 8：Azure Agent Infra Playbook 六大高优场景、四维资质筛查与五步落地工作流

![Azure Agent Infra Playbook 六大高优场景、四维资质筛查与五步落地工作流](assets/svg/08-field-playbook-5step-execution-flow.svg)

> **图解说明**：定义从 **Step 01 Initial Screening**（四大技术底座 14 个 Azure 服务家族持续性核验 + `$10,000` 模型消费信号门禁）、**Step 02 Discovery**、**Step 03 Define**、**Step 04 Validate（半天/全天动手 Workshop，详见 [`workshop-runbook.md`](workshop-runbook.md)）** 到 **Step 05 Implement** 的标准化交付漏斗。

---

## 3. 305 章全栈架构与跨行业物理模型分类速查表 (Thematic Chapter Index)

> 📚 **完整 2.68 MB 技术长卷（含全部 305 章数学推导、架构拓扑与代码清单）已归档至 [`docs/full-monograph-archive.md`](docs/full-monograph-archive.md)**，解决了单文件超 GitHub 512 KB 网页渲染上限的问题。每一章均绑定 [`simulator/agent_infra_sizer.py`](simulator/agent_infra_sizer.py) 中的确定性物理仿真函数与 [`blueprints/`](blueprints) 下的生产级 IaC 蓝图：

| 专题分域 (Domain Cluster) | 章节范围 | 核心架构主题与代表性蓝图 (`blueprints/`) | 代表性量化指标与实测结论 |
|---|---|---|---|
| **I. 核心参考架构、六级运行时与 10万沙箱集群底座** | **Ch 01 – Ch 08** | 四层架构全景、6 大运行时对比、E2B on VMSS `D96as_v7` 容量规划、AKSClaw 5 道硬边界、`UFFD+NBD` 页错误物理拆解、`HorizonDB + PgBouncer` 连接池复用（[`e2b-vmss-d96as-v7.bicep`](blueprints/e2b-vmss-d96as-v7.bicep)、[`aksclaw-kata-fleet.yaml`](blueprints/aksclaw-kata-fleet.yaml)、[`e2b-apim-per-host-policy.xml`](blueprints/e2b-apim-per-host-policy.xml)） | `D96as_v7` **`108 ms` Base / `132 ms` CI-v1**；10万并发 = **261 台客户端节点**；PgBouncer `100K -> 1,200` 连接，P99 **`4.8 ms`** |
| **II. 多活容灾、FinOps、机密计算与云原生供应链安全** | **Ch 09 – Ch 22** | 跨区双活容灾 (`RTO 18.4s`)、Spot 驱逐优雅排空 (`61.4%` 降本)、`AMD SEV-SNP` 机密沙箱、Ratify/Cosign MCP 供应链准入、GPU `MIG/MPS/KAITO` 异构调度、`OTel + Cilium Tetragon eBPF`、Durable Saga 垃圾回收、CUA 浏览器 WebRTC 池、`virtiofs DAX` 加速、Swarm 防死锁、主权云 `DKE` 密码学擦除、Argo Rollouts 金丝雀、APIM KV-Cache 亲和路由、`HorizonDB DiskANN + GraphRAG` 分层记忆 | Spot 30s 抢占存活率 **`99.4%`**；`virtiofs DAX` 环境就绪 **`190 ms` (`-99.3%`)**；APIM Prefix-Cache 命中率 **`87.4%`**（TTFT 降低 `58.6%`） |
| **III. 多模态语音、自主研发 CI/CD、Lakehouse 与前沿计算沙箱** | **Ch 23 – Ch 36** | WebRTC 实时音视频沙箱 (`168 ms` 端到端)、BuildKit/Bazel 自主编程沙箱、Fabric OneLake + DuckDB Arrow 零拷贝、跨云 OIDC 联邦清洁室、具身智能 `ROS 2 / Isaac Lab / CBF` 安全护栏、在线强化学习 `RFT/GRPO` 16K 分支树快照、后量子密码 `ML-KEM-768 / ML-DSA-65`、GreenOps 碳感知调度、`Azure Hyperlight + SpinKube WASI` 亚毫秒微沙箱 (`0.85 ms`)、Chaos Studio 拜占庭容错、Managed Lustre + InfiniBand 科学计算、Agentic Commerce `AP2/x402` 支付熔断 | `Hyperlight Wasm` 冷启动 **`0.85 ms`**（单机密度 `48,000`）；`RFT/GRPO` Tree-CoW 分支派生 **`68.0 ms`**；`Lustre` 吞吐 **`160 Gbps`** |
| **IV. 金融核心交易、医疗生命科学、电信电网与交通物流沙箱** | **Ch 37 – Ch 65** | 算法交易 FPGA 超低延迟风控、核心银行 Basel III 结算、临床基因组学 `GATK/ Parabricks`、手术机器人 `IEC 62304` 闭环、5G/6G O-RAN RIC 实时切片、电网 `IEC 61850` 广域相量控制、自动驾驶 `ISO 26262 ASIL-D` 仿真、航空空管 `DO-178C`、海事自主航行与铁路 `EN 50129 SIL-4` 信号控制 | 硬件/平台级安全联锁触发延迟 **`< 0.5 ms`**；跨租户数据与凭据泄露率 **`0.0%`** |
| **V. 清洁能源、核能聚变、大科学装置与空天深海极端工程** | **Ch 66 – Ch 130** | 绿氢电解槽与合成氨、托卡马克磁约束聚变等离子体防淬灭、同步辐射光源束流控制、深空望远镜自适应光学、海底观测网与地热 EGS、小型模块化核反应堆 (`SMR Class 1E`)、盾构机 (`TBM`)、LNG 低温储运、柔性直流海底电缆 (`HVDC`)、直接空气捕集 (`DAC`)、储能电站 (`UL 9540A`)、EUV 光刻机 (`SEMI S2`)、超导量子纠错 (`QEC`)、低轨巨型星座 (`OISL`)、深海采矿与高超音速热防护 | 全面集成 **PINN（物理信息神经网络）+ MPC（模型预测控制）+ `IEC 61511 SIL-3 / Class 1E` 硬件安全联锁**，边缘闭环延迟 **`0.17–0.35 ms`** |
| **VI. 半导体先进制程、航空材料、高端化工与重工业制造** | **Ch 131 – Ch 195** | 第三代半导体 `SiC/GaN` 晶体生长、极低温高深宽比等离子体刻蚀 (`3D NAND HAR`)、晶圆混合键合 `CMP`、单晶高温合金定向凝固、超高真空分子束外延 (`UHV-MBE`)、空芯光纤拉丝、多晶硅西门子法、氯碱电解、碳纤维原丝氧化炭化、盐湖提锂 (`DLE`)、全钒液流电池、超临界水氧化销毁 `PFAS`、大型高炉/转炉/闪速炉冶金与浮法玻璃 | 关键工艺良率提升 **`+42% ~ +53%`**，危险气体/热失控/爆炸越界事故率 **`0.0%`（SIL-3 硬件回路兜底）** |
| **VII. 战略关键金属、稀土全系列、锕系核燃料与同位素工程** | **Ch 196 – Ch 305** | 电子级稀有气体（`Ne/Kr/Xe`）、难熔金属（`W/Mo/Ta/Nb/Re`）、稀散金属（`Ge/Ga/In/Tl/Te/Se`）、核级锆铪分离、铂族贵金属（`Pt/Ir/Ru/Rh/Pd/Os`）、17 种稀土元素全系列分离与磁光晶体（`La–Lu, Sc, Y`）、锕系核燃料循环（`U/Th HALEU TRISO`、`Pu-238/Am-241` 深空同位素热源、`Cm/Bk/Cf-252` 中子源）、医用回旋加速器同位素（`Mo-99/Tc-99m/Ac-225`）及半导体高纯电子特气全谱系 | 覆盖完整元素周期表工业工程场景，**306 / 306 项自动化单元测试 100% 通过**（运行 `python -m unittest discover -s simulator` 即可本地复核） |

---

## 4. 快速本地验证命令 (Local Verification)

```bash
# 1. 运行 306 项确定性架构选型、容量测算、SVG XML 语法与相对链接完整性测试
python -m unittest discover -s docs/research/azure-agent-infra/simulator -p "test_*.py" -v

# 2. 运行端到端实时仿真自检脚本并校验仿真轨迹
python docs/research/azure-agent-infra/demo/run_live_demo.py --self-test
```

---

## 5. 相关导航

- **完整 305 章技术长卷归档**：[`docs/full-monograph-archive.md`](docs/full-monograph-archive.md)
- **English Overview Playbook**：[`README.en.md`](README.en.md)
- **7-Card 4:5 基准评测报告**：[中文 Markdown (`test-report.md`)](test-report.md) · [English Markdown (`test-report.en.md`)](test-report.en.md) · [CSP 锁定 HTML 卡片 (`cards.html`)](cards.html) · [密封数据 (`report.json`)](report.json)
- **现场交付手册與合规审计**：[Step 04 Workshop Runbook (`workshop-runbook.md`)](workshop-runbook.md) · [证据账本 (`evidence.json`)](evidence.json) · [合规复核 (`review.md`)](review.md)
- [返回研究总索引 (`../index.md`)](../index.md) · [返回仓库主页 (`../../../README.md`)](../../../README.md)
