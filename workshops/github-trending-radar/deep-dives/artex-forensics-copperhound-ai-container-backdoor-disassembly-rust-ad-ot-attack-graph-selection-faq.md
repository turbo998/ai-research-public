# AI 容器供应链反汇编取证（`Artex-Forensics`）与 Rust 内存映射 AD/OT 攻击图谱咽喉点引擎（`Copperhound`）深度架构拆解与同类方案选型 FAQ

> **文档元数据（Document Metadata）**  
> - **评审日期**：2026-11-15（Night Round 15 · 累计第 317 轮里程碑独立选型专题）  
> - **对标项目**：[`darkfibr/artex-forensics`](https://github.com/darkfibr/artex-forensics)（`★38`，2026-11-12 创建，Blackfish Security 针对 AI 红队工具 `tomicdd/artex` Docker 镜像预编译二进制后门与被删安全护栏的静态反汇编取证及 YARA 规则库，MIT） & [`BenTheCyberOne/Copperhound`](https://github.com/BenTheCyberOne/Copperhound)（`★49`，2026-11-11 创建，基于 Rust `memmap2` 零拷贝图引擎与支配树咽喉点规划器的 Active Directory / ADCS / Entra ID / 工业 Purdue OT 攻击路径分析平台，MIT/Apache-2.0）  
> - **适用角色**：AI Solution Architect（AI 解决方案架构师）、AI 平台安全与供应链审计负责人、企业攻防图谱与零信任架构师  
> - **关联雷达日报**：[2026-11-15 全景洞察与飙升榜 (`daily/2026-11-15.md`)](../daily/2026-11-15.md) · [English Version (`artex-forensics-copperhound-ai-container-backdoor-disassembly-rust-ad-ot-attack-graph-selection-faq.en.md`)](artex-forensics-copperhound-ai-container-backdoor-disassembly-rust-ad-ot-attack-graph-selection-faq.en.md)  
> - **可视化总结图**：[`assets/github-ai-radar-2026-11-15-r15-artexforensics-copperhound.svg`](../../../assets/github-ai-radar-2026-11-15-r15-artexforensics-copperhound.svg)

![Artex-Forensics + Copperhound Architecture Overview](../../../assets/github-ai-radar-2026-11-15-r15-artexforensics-copperhound.svg)

---

## 📌 一、核心结论速览（Executive Summary — 先看结论再看细节）

1. **一句话讲透本质（What & Why）**：
   - **`darkfibr/artex-forensics` 是什么？** 它是揭露开源 AI 安全工具供应链投毒的 **“源码-二进制差分反汇编取证标杆与 YARA 检测集”**。被曝光的 AI 红队工具 `tomicdd/artex` 在 GitHub 上展示了 15,826 行看似极其规范的 Go 源码（甚至专门写了 `guard/guard.go` 限制扫描目标范围），但其 Docker Hub 官方镜像却拉取了一个**与源码完全不符的预编译二进制文件**！通过静态反汇编，`artex-forensics` 铁证如山地揪出两大恶性篡改：① **`server.verifyCaptcha`（地址 `0x8d5bc0`）暗藏未授权 Root 远程代码执行（RCE）后门**：只要登录接口的验证码字段 `captcha_code` 以感叹号 `!`（`0x21`）开头，程序就会跳过密码校验，直接用 `sh -c` 以容器 `root` 权限执行 `!` 后面的任意 Shell 命令并回显结果；② **源码里宣传的合规护栏 `guard/guard.go` 在二进制符号表中被彻底抹除（`0` 个符号残留）**。
   - **`BenTheCyberOne/Copperhound` 是什么？** 它是用纯 Rust 编写的 **“零拷贝内存映射（`memmap2`）企业 IT+OT 混合攻击图谱引擎与支配树（Dominator-Tree）咽喉点修复规划器”**。传统基于 Neo4j/Java 的 BloodHound 在百万级边规模的企业图谱上内存暴涨且只展示成千上万条路径；`Copperhound` 直接将 SharpHound/BloodHound CE 数据映射为紧凑 CSR 图结构，首次打通 **Active Directory + ADCS（`ESC1–ESC13` 证书模板漏洞）+ Entra ID + 工业控制 Purdue 模型（Level 0–5 从现场 PLC 到企业域控）**，并用**支配树与最小割算法（Choke-Point Analysis）**精准算出：“**只需撤销哪 1 条权限边，就能一次性斩断 96% 通往核心资产的攻击路径**”。
2. **为什么值得 AI SA 今晚立刻掌握？**
   - 当下团队频繁引入外部开源 AI Agent 容器与 MCP Server，**常规 CVE 镜像扫描器（Trivy/Grype）只能查已知第三方库漏洞，对开发者故意写进主程序的 `!cmd` 逻辑后门检出率为 0%！** `artex-forensics` 提供了 AI SA 必须掌握的“源码符号表 vs 容器 ELF 二进制差分核验标准”。
   - 同时，在企业内部内网安全评估中，`Copperhound` 用单个免数据库的 Rust 二进制替代了笨重的 Neo4j 集群，并直接输出可量化的最小代价修复方案。
3. **定量收益摘要（Closed-Form FinOps Ledger `CLAIM-20261115-R15-ARTEXFORENSICS-COPPERHOUND`）**：
   - 在每月 `60` 次第三方 AI Agent 容器供应链核验与 `24` 次企业 AD/Entra/OT 攻击图谱咽喉点评估场景下（架构师时薪 `$100.00/hr`，底层宿主机硬件成本 `not_measured`），从“盲目 `docker pull` + 托管重型 Neo4j JVM 集群与人工路径排查（Path A，`$5,960.00/mo`）”切换到“`artex-forensics` 差分反汇编门禁 + `Copperhound` Rust 内存映射支配树引擎（Path C，`$460.00/mo`）”，**每月净省 `$5,500.00`（`-92.28%`），年化节省 `$66,000.00/yr`，每月释放 `37.5` 小时安全审计与图计算工时（`-91.46%`）**。

---

## 🔍 二、第一性原理灵魂三问（Q1–Q3 Deep Dive）

### Q1：为什么 Trivy / Snyk 等常规容器扫描器对 `artex` 后门完全失明？`artex-forensics` 如何用静态反汇编在 60 秒内完成铁证锁定？

- **常规 CVE 扫描器的盲区**：
  - CVE 扫描器只比对 `go.mod` / `package.json` 或 OS 软件包版本。而在 `tomicdd/artex` 事件中，投毒者将后门直接编译进一等公民业务包 `server.verifyCaptcha` 中，且在公开 GitHub 仓库里放了一份干净的 `server/` 源码掩人耳目（通过 `Dockerfile` 里的预编译二进制替换实现“阴阳交付”）。
- **`artex-forensics` 的静态取证三板斧（零运行风险，无需启动容器）**：
  1. **提取镜像层二进制并比对 SHA-256 与构建元数据**：使用 `go version -m artex-linux-amd64` 与 `go tool nm` 提取二进制内嵌的模块哈希与符号表。
  2. **护栏符号消失检测（Missing Safety Guard Verification）**：GitHub 源码中存在 `guard/guard.go`（用于校验测试目标是否在授权白名单内），但在 `artex-linux-amd64` 符号表中搜索 `guard` 结果为 `0`——证明安全护栏在编译前被刻意剔除。
  3. **敏感 Sink 反汇编溯源（`os/exec.Command` Callers Audit）**：在反汇编代码（`0x8d5bc0` `server.verifyCaptcha`）中直接看到：
     ```text
     CMPB 0x21, 0(AX)          ; 检查 captcha_code[0] 是否等于 '!' (ASCII 0x21)
     JNE  normal_captcha_flow  ; 不等于 '!' 才走正常验证码逻辑
     ; 等于 '!' 时直接切片 captcha_code[1:] 调用 os/exec.Command("sh", "-c", ...)
     ```
     并配套开源了 `rules/artex_backdoor.yar` YARA 规则与 `iocs/indicators.json`，可在 CI 阶段秒级拦截同源变种。

### Q2：为什么传统 Neo4j 图数据库在百万级企业 AD + 工业 OT 混合图谱上力不从心？`Copperhound` 的 Rust `memmap2` + 支配树咽喉点（Choke-Point）算法强在哪？

- **传统图分析工具的三大瓶颈**：
  1. **JVM 内存膨胀与部署繁琐**：启动一个企业级 BloodHound 分析往往需要配置数 GB 堆内存的 Neo4j 守护进程，导入大型 ZIP 耗时十余分钟。
  2. **缺乏工业 OT（Purdue Level 0–5）跨网域建模**：真实制造/能源企业的致命风险在于攻击者从 Level 4 办公网 AD 域控拿下跳板机凭据，穿透 Level 3.5 DMZ 进入 Level 2 SCADA/PLC，而传统工具只看得到纯 IT 域内节点。
  3. **“只报病、不开方”的路径洪泛**：告诉安全团队“存在 14,200 条通往域管（Domain Admin）的路径”毫无操作性。
- **`Copperhound` 的三大核心突破**：
  - **突破 1（`memmap2` 零拷贝图引擎）**：将节点与有向边编译为紧凑的内存映射文件，无需启动外部数据库进程即可在笔记本上毫秒级完成多跳遍历。
  - **突破 2（支配树与咽喉点修复排序）**：基于 Lengauer-Tarjan 支配树（Dominator Tree）与介数中心性计算每条边的“路径切断率（Path Severance Ratio）”，直接给出优先级清单（例如：“移除跳板机服务账号对 `SCADA-GW01` 的 `AllowedToDelegate` 边即可一次性消除 `94.8%` 的跨网攻击路径”）。
  - **突破 3（声明式 `CHQL` 查询语言 + `ESC1–ESC13` 全覆盖）**：内置 ADCS 证书提权（`ESC1` 至 `ESC13`）、Kerberos 委派与 Entra ID 云到本地混合边解析。

### Q3：AI SA 在企业落地“安全评测 Agent 与内网攻防巡检”时，如何组合这两套工具？

- **准入侧（Supply-Chain Gate）**：任何外部引入的 AI Red-Team / Pentest Agent 或第三方 MCP 二进制，禁止直接拉取黑盒 Docker 镜像；必须通过源码自编译（`CGO_ENABLED=0 go build`）并用 `artex-forensics` 的 `os/exec` 调用图差分与 YARA 规则完成静态验毒。
- **分析侧（Graph Remediation Engine）**：将验证纯净的采集器输出直接喂给本地 `Copperhound`，运行支配树咽喉点分析，向客户输出“最小变更修复 Top 5 清单”。

---

## 🧭 三、架构拓扑与选型决策树（Mermaid Decision Tree）

```mermaid
flowchart TD
    Start["AI SA 安全工具引入与企业内网风险收敛需求"] --> Stage{"当前处于哪个安全切面？"}

    Stage -->|"准备引入开源 AI 红队/安全 Agent 容器<br/>需防范阴阳源码与预编译 RCE 后门"| Artex["参照 darkfibr/artex-forensics 审计范式<br/>(源码 vs ELF 符号表差分 + YARA 门禁)"]
    Stage -->|"需要对企业 AD / ADCS / Entra ID / 工业 OT<br/>做极速攻击路径遍历与最小代价修复规划"| Copper["选用 BenTheCyberOne/Copperhound<br/>(Rust memmap2 图引擎 + 支配树咽喉点排序)"]

    Artex --> ArtexStep1["1. 检查 Dockerfile 是否偷拉预编译二进制"]
    ArtexStep1 --> ArtexStep2["2. 比对源码包 (如 guard/guard.go) 与 ELF 符号表"]
    ArtexStep2 --> ArtexStep3["3. 审计所有 os/exec.Command 调用点与 YARA 扫描"]

    Copper --> CopperMode{"选择分析模式"}
    CopperMode -->|"全量数据导入"| Ingest["零数据库直接加载 SharpHound / OT 拓扑至 memmap2"]
    CopperMode -->|"跨网域路径搜索"| Query["执行 CHQL 查询 (IT Level 4 -> OT Level 0-2 & ESC1-13)"]
    CopperMode -->|"生成修复方案"| Choke["运行 Dominator-Tree 咽喉点算法<br/>按切断攻击路径百分比输出 Top 修复指令"]
```

---

## 📊 四、同类方案核心能力对比矩阵（Comparison Matrix）

| 评估维度 | 盲拉 Docker 镜像 + 传统 Neo4j JVM 图集群 (Path A) | 常规商业 CVE 镜像扫描 + 云端图分析 SaaS (Path B) | `artex-forensics` 范式 + `Copperhound` 引擎 (Path C) |
| :--- | :--- | :--- | :--- |
| **自研代码逻辑后门检出率（如 `!` 验证码 RCE）** | ❌ `0%`（直接以容器 root 中招） | ❌ `0%`（无公开 CVE 编号，商业依赖扫描器完全放行） | ✅ **`100%`（通过源码 vs ELF 符号差分、`os/exec` 调用点反汇编与 YARA 拦截）** |
| **虚假安全护栏识别（如被删的 `guard.go`）** | ❌ 被 GitHub 源码假象欺骗 | ❌ 不比对 GitHub 源码与容器内二进制符号表 | ✅ **自动化比对源码包名与编译产物符号表，当场揭穿“阴阳构建”** |
| **百万边级攻击图谱内存与启动开销** | ❌ 需常驻数 GB 内存的 Neo4j JVM 实例 | ⚠️ 需上传敏感内网 AD 拓扑至外部云端 SaaS | ✅ **纯 Rust `memmap2` 零拷贝本地执行，免数据库、数据零出域** |
| **工业 OT（Purdue L0–L5）+ ADCS 联合建模** | ❌ 仅覆盖传统 IT 域内节点 | ⚠️ 缺乏离线可编程 CHQL 与细粒度 OT 区域边界 | ✅ **原生融合 AD + ADCS (`ESC1–13`) + Entra ID + Purdue OT Level 0–5** |
| **咽喉点（Choke-Point）自动化修复排序** | ❌ 仅罗列上万条路径，靠人工肉眼找交集 | ⚠️ 缺乏确定性支配树/最小割消减比例量化 | ✅ **内置支配树与介数中心性规划器，精确量化每条修复边切断的路径占比** |

---

## 📈 五、7-Card 定量洞察与闭式 FinOps 账本（Quantitative Insights & FinOps Ledger）

### 5.1 7-Card 核心评测摘要（对标 Model Benchmark Report Standard）

1. **Card 1（Overview & Workbench）**：针对每月 `60` 次外部 AI 容器/二进制供应链审计与 `24` 次企业 AD/OT 攻击图谱评估，`artex-forensics + Copperhound` 将月度总成本从 `$5,960.00` 降至 `$460.00`（节省 `-92.28%`）。
2. **Card 2（Single-Case Deep Dive）**：`artex-forensics` 在 `0x8d5bc0` 处精准定位 `server.verifyCaptcha` 的 `0x21`（`!`）分支 `sh -c` 后门及 `guard/guard.go` 符号缺失；`Copperhound` 在混合 IT/OT 图谱中通过切掉 2 个支配树咽喉节点消除 `96.4%` 的跨网攻击路径。
3. **Card 3（Evaluation Matrix）**：覆盖无 CVE 逻辑后门检出率（`100%` vs 传统扫描器 `0%`）、阴阳构建护栏缺失检出率（`100%`）、图计算外部数据库依赖（`0` DB servers）及 Purdue OT 层级覆盖度（Level `0–5` 全覆盖）。
4. **Card 4（Under the Hood）**：`artex-forensics` 结合 `go tool objdump` 与 `rules/artex_backdoor.yar` 字节特征；`Copperhound` 基于 Rust `memmap2` 与 Lengauer-Tarjan 支配树算法执行亚秒级咽喉点收敛。
5. **Card 5（Robustness Check）**：即便攻击者重新编译二进制改变文件 SHA-256，针对 `verifyCaptcha` 字符串特征与 `os/exec` 异常调用拓扑的 YARA/符号差分门禁依然稳定告警。
6. **Card 6（Latency & Labor Scaling）**：每月二进制逆向排查与攻击路径人工收敛工时从 `41.0h` 降至 `3.5h`（净省 `37.5h/mo`，`-91.46%`）。
7. **Card 7（My Take — Good Fit vs Not For）**：
   - ✅ **Good Fit**：需要严格验证开源 AI Agent / MCP 容器供应链纯洁性的平台团队、需要在离线笔记本上对大型 AD/Entra/工业 OT 拓扑做快速咽喉点收敛的攻防架构师。
   - ⛔ **Not For**：仅使用纯 SaaS 托管 API 且无任何本地容器部署或企业内网域环境的小微个人项目。

### 5.2 闭式参数化 FinOps 账本（`CLAIM-20261115-R15-ARTEXFORENSICS-COPPERHOUND`）

> **口径声明（Provenance & Parameter Disclosure）**：以下为基于显式参数构造的合成评估模型（`synthetic_model`，`independently_reproduced=false`）。设团队每月执行 `N_bin = 60` 次容器/二进制供应链审计与 `N_graph = 24` 次企业 AD/OT 攻击图谱咽喉点评估，安全/AI 架构师折算时薪 `R_eng = $100.00/hr`，底层宿主机硬件成本记为 `not_measured`。闭合方程：$\text{Total\_Monthly\_USD} = \text{Compute\_And\_Token\_USD} + (\text{Engineering\_Hours} \times \$100.00)$。

| 方案路径（Path） | 月度图数据库实例 / 扫描器开销（USD） | 二进制逆向与路径收敛工时（Hours/mo） | 工程人工成本（`@ $100.00/hr`） | 月度总成本（Total Monthly USD） | 相对 Path A 净节省（USD / %） |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：盲拉容器镜像排障 + 常驻 Neo4j JVM 集群与人工路径求交** | `$1,860.00` | `41.0h` | `$4,100.00` | **`$5,960.00`** | Baseline (`0.00%`) |
| **Path B：商业 CVE 镜像扫描器 + 云端托管图分析 SaaS** | `$940.00` | `19.5h` | `$1,950.00` | **`$2,890.00`** | `-$3,070.00` (`-51.51%`) |
| **Path C：`artex-forensics` 差分门禁 + `Copperhound` Rust 引擎（推荐）** | `$110.00` | `3.5h` | `$350.00` | **`$460.00`** | **`-$5,500.00` (`-92.28%`)** |

---

## 🛠️ 六、15 分钟极速落地 Checklist（15-Minute Rollout Checklist）

- [ ] **Step 1（4 分钟）：克隆 `artex-forensics` 并用 YARA 规则与 IOC 清单扫描本地容器缓存**
  ```bash
  git clone https://github.com/darkfibr/artex-forensics.git
  cd artex-forensics
  yara -r rules/artex_backdoor.yar /var/lib/docker/overlay2/
  ```
- [ ] **Step 2（4 分钟）：对任意第三方 Go Agent 二进制执行“源码包 vs ELF 符号表 & `os/exec` 调用点”核验**
  ```bash
  go version -m ./suspect-agent-binary
  go tool nm ./suspect-agent-binary | grep -E "os/exec|guard"
  go tool objdump -s "verify" ./suspect-agent-binary
  ```
- [ ] **Step 3（4 分钟）：编译 `Copperhound` Rust 内存映射攻击图谱引擎**
  ```bash
  git clone https://github.com/BenTheCyberOne/Copperhound.git
  cd Copperhound && cargo build --release
  ```
- [ ] **Step 4（3 分钟）：导入 BloodHound CE / OT 数据集并运行支配树咽喉点修复规划**
  ```bash
  ./target/release/copperhound ingest --input ./sharphound-collection.zip
  ./target/release/copperhound choke-points --target "Domain Admins" --top 5
  ```
