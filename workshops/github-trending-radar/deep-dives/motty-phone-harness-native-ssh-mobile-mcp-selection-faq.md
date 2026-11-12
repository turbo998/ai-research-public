# 零 WebView 原生 Go 运维工作台（`t8y2/motty` 终端脱敏与 `mcp-serve`）与云端真机 iPhone/Android 桥接（`phone-harness/mcp`）选型 FAQ

> **文档定位**：本文是 **2026-11-11 夜班多轮深潜 Round 25（累计第 70 篇独立选型专题）**，严格对标 `ib-vs-ethernet-roce-selection-faq.md` 的「通俗大白话 + 第一性原理 + 可核算定量算例」标杆文风，为全栈 SRE 运维与移动端自动化测试架构师拆解今日两款打通“远程服务器运维”与“真机 iOS/Android 操控”的 MCP 基础设施标杆：
> 1. **`t8y2/motty`（`945★`，Go 1.26+ 基于原生 GPU 框架 `Viva` 构建，零 WebView）**：将 PTY 终端、带原子校验与独立 `sudo` 提权开关的 SFTP、SSH 隧道内嵌 VNC/RDP 远程桌面、系统资源监控以及**自带密钥脱敏的 AI 助手与双模 MCP（窗口化 HTTP MCP + 无头 `motty mcp-serve` Stdio）**整合进单一原生窗口；
> 2. **`phone-harness/mcp`（`785★`，Python，MIT，遵循 `mobile-mcp` 标准）**：无需本地 Mac、无需配置 Xcode 或 `adb`，通过单一 Streamable HTTP URL（`https://mcp.phone-harness.com/mcp`）或本地 Stdio，将**云端真实物理 iPhone（`$80/月` 包月不限分钟）与按量计费 Android 模拟器（`5 美分/分钟`）**作为 14 个标准 MCP 工具挂载给 Claude、Cursor、Codex、Devin、Copilot 与 OpenClaw。
>
> **English Companion**: [motty-phone-harness-native-ssh-mobile-mcp-selection-faq.en.md](motty-phone-harness-native-ssh-mobile-mcp-selection-faq.en.md) · **架构总结图**: [`assets/github-ai-radar-2026-11-11-r25-motty-phoneharness.svg`](../../../assets/github-ai-radar-2026-11-11-r25-motty-phoneharness.svg)

![Motty & Phone-Harness MCP Architecture](../../../assets/github-ai-radar-2026-11-11-r25-motty-phoneharness.svg)

---

## 📌 一、核心结论速览（Executive Summary）

1. **先用大白话讲透这两个项目到底解决了什么痛点？**
   - **远程服务器运维“切 4 个软件、Electron 吃内存、Agent 读终端日志把私钥和数据库密码全发给大模型”的痛点（`t8y2/motty` 解决的问题）**：平时查线上故障，工程师得同时开终端、SFTP 传文件工具、VNC/RDP 远程桌面客户端；如果让外部 Coding Agent 直接跑 `ssh` 命令，不仅跳板机（Jump Host）和一次性验证码（TOTP）很难配，终端里打印出的环境变量赋值、URL 内嵌密码、API Token 还会原封不动上传给云端大模型造成严重凭据泄漏！`Motty` 基于 Go 1.26+ 与原生 `Viva` 图形框架（彻底抛弃臃肿的 Electron WebView），把终端、原子级暂存 SFTP（支持不提权终端而单独开启远程文件 `sudo sftp-server`）、自动跟随 SSH 标签页生命周期的端口转发与内嵌 VNC/RDP 装进一个窗口。更关键的是：**它在把终端文本发给 AI 前会自动正则抹除私钥、赋值语句与 URL 密码**，并提供无头 **`motty mcp-serve`**，只向 Agent 暴露你显式勾选授权的 SSH 主机！
   - **移动端 App 自动化验证“没 Mac 跑不了 iOS、USB 线天天掉线、商业真机云按席位天价收费”的痛点（`phone-harness/mcp` 解决的问题）**：想让 Coding Agent 写完 React Native / Flutter / iOS 代码后自己上真机点一点看有没有崩，传统做法要买 Mac mini、配 WebDriverAgent、插着 USB 线维护 `adb`，或者买年费几万美元的企业级真机云。`phone-harness/mcp` 把**云端独占真机 iPhone（`$80/月` 包月或 `$64/月` 年付，带 eSIM 仅 `$100/月`）**和**按分钟计费的云端 Android 模拟器（启动免费，`$0.05/分钟`，调 `phone_stop_device` 即刻停表）**封装成 14 个遵循 `mobile-mcp` 标准的工具，配好一个 URL 登录 OAuth 即可在 Claude Code、Codex、Cursor、Devin、GitHub Copilot 中直接看屏、提取无障碍树/OCR 中心点坐标并点击滑动！
2. **闭式 FinOps 核算结论（`CLAIM-20261111-R25-MOTTY-PHONEHARNESS`）**：
   - 在 **全栈 SRE 与移动质量团队维护 60 台远程 Linux/Windows 主机 + 每月执行 6,000 分钟（100 小时）移动端真机/模拟器回归与 1,500 次远程排障** 基准下（高级 SRE/QA 工程师全包时薪 `$85.00/hr`；生产环境业务云服务器账单与 Apple 开发者年费：`not_measured`）：
   - 从 **Path A（传统商业真机云高价套餐 + 裸跑未脱敏 SSH 脚本与多软件切换，`$5,900.00/月`）** 升级至 **Path C（`t8y2/motty` 原生窗口 + 预脱敏 `motty mcp-serve` + `phone-harness/mcp` 2 台包月云真机 iPhone 与按需 Android，`$990.00/月`）**，每月净省 **`$4,910.00/月`（降幅 `-83.22%`，年化节省 `$58,920.00/年`）**，工程师维护真机插线、轮换泄露密钥与跨工具搬运的工时从 `44.0 小时/月` 降至 `6.0 小时/月`（**节省 `86.36%`**）。

---

## 🎯 二、三大灵魂拷问（Q1 / Q2 / Q3 Deep-Dive）

### Q1：`t8y2/motty` 的「终端文本预脱敏 + 双模 MCP（窗口 HTTP vs. 无头 `motty mcp-serve`）+ 独立 SFTP Sudo」在工程细节上是如何设计的？
- **第一性原理拆解**：
  1. **发往大模型前的确定性凭据抹除（Pre-LLM Secret Redaction）与固定上下文预算**：
     - 在 `Ask`（只读问答）或 `Agent`（带风险分级与审批门的命令执行，且自动隐藏 Motty 自身的捕获 Wrapper 与标记，不污染终端显示与本地历史）模式下，所有终端缓冲区文本在离开本机前都会经过脱敏过滤：自动抹除私钥文件块、敏感变量赋值（`KEY=...`）、URL 内嵌凭据（`https://user:pass@host`）及主流 Token 格式；超长会话仅在固定 Token 预算内截取最新轮次。
  2. **按主机显式白名单隔离的双模 MCP（`motty mcp-serve`）**：
     - 窗口内 HTTP MCP 默认关闭，开启后仅监听本地 Loopback 且强制校验 Bearer Token，`list_sessions` 仅列出当前已打开的终端标签页；
     - 无头模式 `motty mcp-serve` 通过 Stdio 启动（无需监听端口），`list_hosts` 与 `list_sessions` **严格剔除未显式向 Agent 开放的受保护生产机**，只返回已授权主机的稳定 ID。
  3. **原子级暂存 SFTP 与非提权终端的独立 `sudo sftp-server`**：
     - SFTP 替换远端文件时先上传临时文件、校验断点续传前缀并计算编辑前后哈希，全部同步成功后才执行原子重命名（失败时原文件 100% 完好）；修改 `root` 属主配置文件时，只需打开文件面板旁的 `sudo` 开关（仅将文件传输切换至特权 `sftp-server`，绝不将交互式 Shell 终端提升为 root，且密码仅驻留当前连接内存）。

### Q2：`phone-harness/mcp` 是如何解决多模态 Agent 在手机屏幕上“点不准坐标”和“云真机计费失控”两大痛点的？
- **第一性原理拆解**：
  1. **带坐标空间映射头的截图与原生无障碍树/OCR 双轨定位**：
     - 大模型直接看原始高分屏截图算 `(x, y)` 极易因为图片缩放比例不一致而点偏。`phone_take_screenshot` 默认将长边限制在 `max_size: 1024`，并在图片前附带**精确的图像像素到点击坐标空间的转换说明文本**；
     - 更进一步，`phone_list_elements_on_screen` 在 Android 上直接拉取系统 **Accessibility Tree（无障碍节点树）**，在真机 iPhone 上运行**文本识别并直接算出每个可见文案的可点击中心点坐标（Tap-Ready Centers）**，让 Agent 百发百中！
  2. **透明可预期计费模型与会话寿命控制**：
     - `phone_start_device` 的 `minutes` 参数（默认 30 分钟）代表超时自动关机保护时长而非最小计费单位：云端 Android 模拟器启动免费、按实际运行分钟数收取 **`$0.05/分钟`**，任务跑完立即调用 `phone_stop_device` 即可秒级停表；而高频测试的 iOS 场景直接采用 **`$80/月`（年付 `$64/月`）固定包月真机 iPhone**，彻底杜绝按分钟计费爆表风险。

### Q3：架构师在跨端研发与运维闭环中如何组合部署 `t8y2/motty` 与 `phone-harness/mcp`？
- **组合实战流**：
  - Coding Agent（如 Claude Code 或 Codex）同时挂载本地 `motty mcp-serve`（连接预授权的测试/预发后端服务器）与远程 `https://mcp.phone-harness.com/mcp`（连接云端真机 iPhone 与 Android 模拟器）：
  - Agent 在真机 iPhone 上通过 `phone_launch_app` 与 `phone_click_on_screen_at_coordinates` 触发业务请求 → 同时通过 `motty mcp-serve` 实时读取后端预发服务器的脱敏日志与资源监控 → 定位问题后修复代码并重跑真机端到端验证！

---

## 🧭 三、Mermaid 选型决策树与端云一体运维+真机测试架构

```mermaid
flowchart TD
    A["AI Agent 远程服务器运维与移动真机 (iOS/Android) 闭环验证需求"] --> B{"当前操作目标属于哪一层基础设施?"}
    B -- "远程 Linux/Windows 服务器 (SSH / SFTP / 端口转发 / 内网 VNC&RDP)" --> C["采用 t8y2/motty (Go 1.26+ 原生 Viva 窗口 + motty mcp-serve)"]
    B -- "移动客户端真机/模拟器交互 (iOS 物理真机 / Android 模拟器)" --> D["采用 phone-harness/mcp (Streamable HTTP / Stdio 14 工具)"]

    C --> C1["AES-256-GCM 凭据保险箱 (系统密钥链保护 + HLC .mottybak 同步)"]
    C1 --> C2["motty mcp-serve (Stdio): 仅暴露显式授权给 Agent 的 SSH 主机"]
    C2 --> C3["终端文本预脱敏 (抹除私钥/赋值/URL密码) + Ask/Agent 风险审批门禁"]
    C3 --> C4["原子级暂存 SFTP (独立 sudo sftp-server 开关) + SSH 隧道内嵌 VNC/RDP"]

    D --> D1["OAuth (phone:drive) 或 PHONE_HARNESS_API_KEY 接入 15+ 主流 Agent"]
    D1 --> D2["phone_start_device: 启动包月真机 iPhone ($80/mo) 或按需 Android ($0.05/min)"]
    D2 --> D3["phone_list_elements_on_screen (A11y/OCR 中心点) + phone_take_screenshot 坐标校准"]
    D3 --> D4["执行点击/长按/滑动/输入验证 -> 完结立即调用 phone_stop_device 停止计费"]
```

---

## 📊 四、同类方案核心能力对比矩阵（Comparison Matrix）

| 评估维度 | Path A：商业真机云 SaaS + 裸跑 SSH 脚本 | Path B：自建 Mac+USB 手机架 + Electron SSH 客户端 | **Path C（推荐标杆）：`t8y2/motty` + `phone-harness/mcp`** |
| :--- | :--- | :--- | :--- |
| **SSH/SFTP/桌面客户端资源占用** | 需同时开 3～4 个软件，上下文割裂 | Electron WebView 终端常驻消耗数百 MB 内存 | **Go 1.26+ 原生 `Viva` GPU 渲染，零 WebView，单窗口全集成** |
| **终端凭据防泄漏与主机授权** | 原始 `ssh` 输出直接进 LLM，极易泄露 Token 与密码 | 无针对 Agent 的按主机白名单与自动脱敏网关 | **发往模型前自动正则脱敏 + `motty mcp-serve` 严格隐蔽未授权主机** |
| **真机 iOS 与 Android 接入成本** | 企业并发席位动辄 `$1,500+/月`，合同绑定繁琐 | 需专人维护 Mac mini、Xcode 签名与经常断连的 USB 线 | **零配置 URL 直连：iPhone `$80/月` 包月，Android `$0.05/分钟` 随开随停** |
| **移动端屏幕点击坐标准确率** | 仅靠原始截图盲猜像素，缩放后点击频频偏移 | 需自己写 Appium / WDA 坐标换算脚本 | **`phone_list_elements_on_screen` 直出可点击中心点 + 截图坐标转换头** |
| **月度总拥有成本（60 主机+100h 测试）** | **`$5,900.00 / 月`**（设备/Token `$2,160` + 人工 `$3,740`） | **`$3,130.00 / 月`**（机房/Token `$920` + 人工 `$2,210`） | **`$990.00 / 月`（净省 `$4,910.00/月`，降幅 `-83.22%`）** |

---

## 🧪 五、闭式定量 FinOps 算例与 7-Card 评测洞察（`CLAIM-20261111-R25-MOTTY-PHONEHARNESS`）

### 5.1 基准假设与边界声明
- **评测负载**：全栈 SRE 与移动 QA 团队管理 **60 台远程服务器**，每月执行 **1,500 次远程排障操作** 与 **6,000 分钟（100 小时：其中 2 台常驻 iPhone + 4,000 分钟 Android 弹性并发）移动端自动化测试**。
- **单价基准**：高级 SRE/QA 工程师全包时薪 **`$85.00 / hr`**；`phone-harness` 云真机 iPhone **`$80.00 / 台 / 月`**，云 Android 模拟器 **`$0.05 / 分钟`**。
- **显式边界声明（Scope Boundary）**：被管理的生产业务云服务器本身账单及 Apple Developer 账号年费标记为 **`not_measured`**。

### 5.2 三路径闭式成本核算表

| 成本构成项 | Path A：传统商业真机云套餐 + 裸跑未脱敏 SSH | Path B：自建 USB 手机机架 + Electron 终端 | **Path C：`t8y2/motty` + `phone-harness/mcp`（推荐）** |
| :--- | :--- | :--- | :--- |
| **移动真机/模拟器与终端 LLM 费用** | `$1,650.00 + $510.00` = **`$2,160.00`** | **`$920.00`** | `2×$80 + 4,000×$0.05 + $120` = **`$480.00`** |
| **机架维护、密钥轮换与排障工时（`$85/hr`）** | `44.0 hrs × $85.00` = **`$3,740.00`** | `26.0 hrs × $85.00` = **`$2,210.00`** | `6.0 hrs × $85.00` = **`$510.00`** |
| **月度总成本（Monthly Total）** | **`$5,900.00 / 月`** | **`$3,130.00 / 月`**（`-46.95%`） | **`$990.00 / 月`** |
| **相对 Path A 净节省（Savings）** | 基准线（Baseline） | 节省 `$2,770.00 / 月` | **净省 `$4,910.00 / 月`（`-83.22%` · 年省 `$58,920.00`）** |
| **生产服务器账单与 Apple 开发者年费** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 六、生产级落地核验 Checklist（SA Actionable Verification）

- [ ] **1. `Motty` 主机指纹校验与 AES-256-GCM 保险箱启用**：通过 `brew install --cask t8y2/tap/motty` 或 `scoop install t8y2/motty` 安装，确认首次连接强制核对 `known_hosts` 指纹，且密码与 TOTP 种子存入绑定系统密钥链的 AES-256-GCM Vault。
- [ ] **2. `motty mcp-serve` 最小权限主机白名单核验**：仅将测试/预发或只读诊断主机显式勾选开放给 Agent，运行 `list_hosts` 确认未授权核心生产机被彻底隐蔽，并在窗口 HTTP MCP 模式下默认保持 `observe` 或 `ask` 审批门禁。
- [ ] **3. SFTP 原子替换与非持久 `sudo` 检查**：验证远端大文件修改走暂存哈希校验后原子重命名流程，并在完成 root 配置文件编辑后及时关闭文件面板旁的 `sudo` 开关。
- [ ] **4. `phone-harness/mcp` OAuth / Bearer 环境变量接入**：在 Claude Code 或 Codex 中通过 `claude mcp add --transport http phone-harness https://mcp.phone-harness.com/mcp`（或配置 `bearer_token_env_var = "PHONE_HARNESS_API_KEY"`）接入，切勿将 `pck_...` 密钥硬编码进版本库。
- [ ] **5. `phone_list_elements_on_screen` 优先与 `phone_stop_device` 停表门禁**：编写自动化测试 Prompt 时优先调用 `phone_list_elements_on_screen` 获取精准可点击中心坐标，并在 CI `finally` 块中强制调用 `phone_stop_device` 终止云端 Android 按分钟计费。
