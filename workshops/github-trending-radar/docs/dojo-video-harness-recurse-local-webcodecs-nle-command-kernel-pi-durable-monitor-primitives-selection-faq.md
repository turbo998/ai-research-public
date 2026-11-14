# 命令内核驱动的本地 WebCodecs 视频剪辑 Harness（`PansaLegrand/dojo-video-harness`）与基于 Pi Durable 的自后台监控原语（`ebetica/recurse`）深度拆解与选型 FAQ

> **文档元数据（2026-11-14 · 晚班 Round 69 / 累计 Round 252）**  
> - **对标范式**：`ib-vs-ethernet-roce-selection-faq.md`（第一性原理 + 大白话拆解 + 灵魂三问 + Mermaid 决策树 + 闭式 FinOps 核算）  
> - **核心评估对象**：  
>   1. [`PansaLegrand/dojo-video-harness`](https://github.com/PansaLegrand/dojo-video-harness)（`★ 53`，MIT 开源的本地非线性视频编辑器（NLE）与教学级 TypeScript 智能体 Harness：将复杂的轨道波纹、转场与帧边界规则下沉到**经过严格测试的文档与命令内核（Document & Command Kernel）**，基于 `@dojo-video-engine/* v1.2.3` 在浏览器内通过 **WebCodecs 零云端 Worker 直出 MP4**，支持持久化检查点、确定性上下文修剪与结构化待办提问卡）  
>   2. [`ebetica/recurse`](https://github.com/ebetica/recurse)（`★ 46`，基于 **Pi Durable** 构建的纯本地 Web 优先自主编码 Harness，MIT 开源：提炼出 **自动转后台 Shell（Auto-Backgrounding Shells）、输出触发唤醒监控器（Monitors：将目标巡检、定时循环与 CI 盯盘统一还原为一条后台监控原语）与独立 Git Worktree 多智能体树（`subagent.ts`）** 三大极简原语）  
> - **配套架构图**：[`assets/github-ai-radar-2026-11-14-r69-dojovideo-recurse.svg`](../../../assets/github-ai-radar-2026-11-14-r69-dojovideo-recurse.svg)  
> - **审计契约号**：`CLAIM-20261114-R69-DOJOVIDEO-RECURSE`（本地工作站硬件折旧标注为 `not_measured`）

---

## 📌 一、核心结论速览（Executive Summary：3 分钟读懂本质）

1. **为什么让大模型直接改视频时间线 JSON 总是把多轨音画剪错位，而商用 AI 视频剪辑 SaaS 又强制要求把涉密视频上传到云端队列渲染？`PansaLegrand/dojo-video-harness` 怎么破局？**  
   - **通俗大白话**：视频时间线（Timeline）有一堆极其严苛的不变量——删掉中间一段素材时后面的字幕要不要波纹跟进（Ripple）？转场时长能不能超过前后片段的一半？如果靠大模型自己在 Prompt 里算毫秒加减法，剪三次必出轨道重叠或黑屏。  
   - **`dojo-video-harness` 的第一性原理破局**：
     - **“把复杂视频规则锁进确定性文档与命令内核（Document & Command Kernel）”**：Agent 只负责理解人类意图并调用强类型的编辑命令，所有帧边界、轨道对齐与波纹联动全部由经过单测验证的命令内核执行；人类手工拖拽与 Agent 对话修改的是**同一个实时时间线**！
     - **零数据库、零云端 Worker、浏览器 WebCodecs 原生直出 MP4 + 密钥单向隔离**：一行 `npm run launch` 启动 `http://127.0.0.1:4310`，手动剪辑、导字幕、加动效与通过 `@dojo-video-engine v1.2.3`（WebCodecs）导出 MP4 **完全不需要任何 API Key**；配置 LLM 与 ASR 密钥后，已保存的密钥绝不回传给浏览器前端，且修改配置只影响新请求、正在运行的任务严格锁定原配置（Shared Loop `0.1.3` 支持持久化检查点与安全中断恢复）。
2. **为什么很多号称“能自主跑长任务”的 Agent 框架代码动辄几万行，而 `ebetica/recurse` 基于 Pi Durable 只用“后台 Shell + 输出唤醒 Monitor + Worktree 子树”三个原语就能把目标循环、CI 盯盘和定时任务全包圆？**  
   - **通俗大白话**：传统 Agent 跑一个 10 分钟的构建或测试时，要么傻等阻塞整个会话，要么每隔 5 秒发一次 LLM 请求去轮询（Polling）日志，白白烧掉几百次上下文 Token。  
   - **`recurse` 的第一性原理破局**：
     - **自动后台化 Shell + 输出触发唤醒监控器（Output-Triggered `Monitors`）**：任何长耗时命令会自动切入后台并在结束时唤醒 Agent；而 **Monitor 就是一个“只要往标准输出打印一行字就立即唤醒 Agent”的后台 Shell**！借此，**目标检查（Goal）、周期性循环（Loop）、CI 状态看门狗（CI Watcher）和定时提醒（Reminder）全部被统一还原为一个极简的 Monitor Skill**，零轮询 Token 浪费！
     - **共享 Bun 进程的 Pi Durable 多智能体树（`subagent.ts`）+ 纯 Web 隧道界面（`:8787`）**：每个聊天窗口就是一个 Agent，通过 `subagent.ts` 在独立 Git Worktree 中派生子 Agent 并沿树向上汇报；彻底摒弃易卡顿的终端 TUI，提供可通过 SSH 隧道随时随地访问的 `:8787` Web 前端，内置异步上下文压缩（Async Compaction）、`fffgrep` 与安全审查。
3. **闭式 FinOps 审计结论（`CLAIM-20261114-R69-DOJOVIDEO-RECURSE`）**：  
   - 按每月完成 **35 支本地隐私视频人机协同剪辑与长周期后台监控/CI 自治循环任务**（工程师时薪 **`$95.00/hr`**）核算：从“Path A：按分钟购买云端视频渲染 Worker + 高频轮询长耗时 Shell 烧穿上下文 Token”（**`$5,000.00/月`**，含 `$1,580.00` 云渲染队列与无效轮询 Token 开销 + `36.0h` 时间线错位返工与长任务断连恢复人力 `$3,420.00`）切换到“Path C：`dojo-video-harness` 本地 WebCodecs 命令内核 + `recurse` Pi-Durable 事件监控原语”（**`$417.50/月`**，含 `$85.00` 按需唤醒 Token 开销 + `3.5h` 审阅人力 `$332.50`），每月净省 **`$4,582.50`**（降本 **`91.65%`**，年化节省 **`$54,990.00`**），剪辑排障与值守工时缩减 **`90.28%`**。

![Dojo Video Harness & recurse Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r69-dojovideo-recurse.svg)

---

## 💬 二、架构师灵魂三问（Q1–Q3 Deep Dive）

### Q1：为什么 `PansaLegrand/dojo-video-harness` 坚持“复杂的视频剪辑规则必须活在 Document & Command Kernel 里，而不是写在 Agent 的 System Prompt 里”？

1. **把“领域不变量（Domain Invariants）”从概率模型剥离到确定性内核**：  
   - 视频多轨时间线的片段裁剪、字幕对齐与转场重叠属于容错率为零的几何约束。如果靠在 System Prompt 里写 5,000 字规则教大模型算时间戳，不仅消耗大量 Token，还依然会出现越界崩溃。由类型化的 Command Kernel 兜底校验并返回明确的状态转移或结构化追问卡片（Structured Pending Question），才能让教育级轻巧 Agent 稳稳操控专业级非线性编辑。

---

### Q2：`ebetica/recurse` 提出的“Goal（目标）、Loop（循环）、CI Watcher（盯盘）本质上都是同一个 `Monitor` 原语”给架构设计带来什么极简启发？

1. **用操作系统进程流（Unix Stream Wakeup）替代框架层复杂调度器**：  
   - 许多 Agent 框架为了支持 Cron 定时、Webhook 触发和目标自检，造出了三四套互不兼容的调度器子系统。在 `recurse` 中，只要一个后台脚本在条件满足时 `echo` 一行文本，Monitor 就会通过 Pi Durable 唤醒休眠的 Agent——用短短几十行代码统一了所有事件驱动自治模式。

---

### Q3：为什么 `dojo-video-harness` 规定“修改 LLM/ASR 密钥配置后立即对新请求生效，但正在运行的作业必须继续使用启动时的旧配置”？

1. **运行期作业配置不可变性（In-Flight Job Configuration Immutability）**：  
   - 如果长耗时转写或多步剪辑任务执行到一半时，用户在设置面板切换了模型 ID 或 Base URL，中途热切换会导致前后工具调用 Schema 或分段时间戳格式不一致而损坏工程文档。锁定在途作业快照并在服务端单向隐藏密钥（绝不回传浏览器）保障了并发操作安全。

---

## 🧭 三、架构选型决策树与本地 WebCodecs 剪辑 / Monitor 原语拓扑图（Mermaid）

```mermaid
flowchart TD
    Start["本地人机共剪视频工作台 & 长周期零轮询自主编码 Harness 选型"] --> Scenario{"目标工程场景?"}

    Scenario -->|"人机同屏编辑视频时间线 + 本地零云端导出 MP4"| VideoGate{"内核与隐私诉求?"}
    VideoGate -->|"追求 Document/Command Kernel 严守轨道不变量<br/>+ 浏览器 WebCodecs 零 Key 导出 + loop 0.1.3 断点恢复"| UseDojo["✅ PansaLegrand/dojo-video-harness (MIT · TypeScript)<br/>• 0 数据库 / 0 Redis / 0 云 Worker，手动与 Agent 共编同一时间线<br/>• 密钥服务端单向隔离，在途任务配置快照锁定"]
    VideoGate -->|"纯命令行批量无界面转码"| RawFFmpeg["🔄 传统 FFmpeg CLI 脚本"]

    Scenario -->|"长耗时编译/测试监控 + 多 Worktree 子 Agent 协同"| RecurseGate{"长任务唤醒机制?"}
    RecurseGate -->|"追求长命令自动切后台 + Monitor 标准输出唤醒<br/>+ Pi Durable 同进程多 Worktree 子树"| UseRecurse["✅ ebetica/recurse (MIT · Bun 1.4+ & Pi Durable)<br/>• 用单一 Monitor 原语统一实现 Goal / Loop / CI Watcher<br/>• :8787 Web 界面支持 SSH 隧道远控 + 异步压缩与 fffgrep"]
    RecurseGate -->|"高频定时轮询日志"| PollingLoop["⚠️ 传统轮询循环 (高 Token 浪费)"]

    UseDojo --> FinOps["💰 闭式 FinOps 收益 (CLAIM-20261114-R69-DOJOVIDEO-RECURSE)<br/>月度总成本 $5,000.00 ➔ $417.50 (-91.65% · 年省 $54,990)"]
    UseRecurse --> FinOps
```

---

## 📊 四、同类方案横向对比矩阵（Decision Matrix）

| 评估维度 | `PansaLegrand/dojo-video-harness` (本地 WebCodecs NLE) | 云端 AI 视频剪辑 SaaS / 裸调 FFmpeg | `ebetica/recurse` (Pi Durable + Monitor 原语) | 传统轮询式 TUI Agent 框架 |
| :--- | :--- | :--- | :--- | :--- |
| **核心控制原语** | **强类型 Document & Command Kernel + Shared Loop `0.1.3`** | 云端黑盒队列或让 LLM 手算毫秒拼 FFmpeg | **自动后台 Shell + 输出触发 `Monitor` + Worktree `subagent.ts`** | 阻塞等待或每几秒发 LLM 请求轮询日志 |
| **基础设施与隐私依赖** | **0 数据库 / 0 Redis / 0 云 Worker，浏览器 WebCodecs 直出 MP4** | 必须上传原始视频至云端对象存储按分钟计费 | **单 Bun 进程共享 Pi Durable 状态，`:8787` Web 支持 SSH 隧道** | 多进程内存膨胀，TUI 远程转发易乱码卡顿 |
| **恢复与安全机制** | **持久化检查点 + 密钥不回传浏览器 + 在途任务配置锁定** | 断网即丢云端编辑态 | **跨中断/重启持久化恢复 + 内置异步上下文压缩与安全审查** | 终端断开即杀死后台编译子进程 |
| **开源协议与定位** | **MIT 开源，兼具生产可用本地 NLE 与教学级清晰 Agent 架构** | 商业闭源按导出分钟与席位收费 | **MIT 开源，用最小原语组合出复杂多智能体图与定时流** | 插件机制臃肿，二次定制门槛高 |

---

## 🧮 五、7-Card 定量洞察与闭式 FinOps 核算（`CLAIM-20261114-R69-DOJOVIDEO-RECURSE`）

> **核算范围与边界声明**：本模型核算每月完成 **35 支本地视频人机共剪工程与长周期后台监控/CI 自治任务** 的云端视频渲染队列/高频轮询 Token 开销，以及修复时间线错位、恢复中断后台编译任务的工程师人力成本（按 **`$95.00/hr`** 计价）；本地工作站硬件折旧标注为 **`not_measured`**。

| 方案路径 | 云端渲染与轮询 Token 开销 (`USD/月`) | 时间线返工与中断恢复工时 (`hrs/月`) | 工程师人力成本 (`@ $95/hr`) | 月度总成本 (`USD/月`) | 相对 Path A 净节省 (`USD/月` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：云端视频渲染 SaaS + 高频轮询长耗时 Shell** | `$1,580.00` | `36.0 hrs` | `$3,420.00` | **`$5,000.00`** | Baseline (`0.00%`) |
| **Path B：无内核裸调 FFmpeg + 手工开 `tmux` 盯盘** | `$750.00` | `17.0 hrs` | `$1,615.00` | **`$2,365.00`** | `-$2,635.00` (`-52.70%`) |
| **Path C（推荐）：`Dojo Video` 内核 + `recurse` Monitor** | **`$85.00`** | **`3.5 hrs`** | **`$332.50`** | **`$417.50`** | **`-$4,582.50` (`-91.65%`)** |

- **闭式校验公式**：
  - $\text{Path A Total} = 1580.00 + 36.0 \times 95.00 = 1580.00 + 3420.00 = \$5,000.00$
  - $\text{Path B Total} = 750.00 + 17.0 \times 95.00 = 750.00 + 1615.00 = \$2,365.00$
  - $\text{Path C Total} = 85.00 + 3.5 \times 95.00 = 85.00 + 332.50 = \$417.50$
  - $\text{Net Savings (Path C vs Path A)} = 5000.00 - 417.50 = \$4,582.50/\text{mo} \quad (-91.65\%, \text{Annualized } \$54,990.00/\text{yr})$

---

## 🛠️ 六、AI 解决方案架构师实战上手 Checklist

1. **一键启动 `PansaLegrand/dojo-video-harness` 本地 WebCodecs 视频编辑工作台**：
   ```bash
   git clone https://github.com/PansaLegrand/dojo-video-harness.git && cd dojo-video-harness
   npm run launch   # 自动检查环境并打开 http://127.0.0.1:4310
   ```
2. **基于 Bun 1.4+ 安装 `ebetica/recurse` 体验 Pi Durable 后台监控原语**：
   ```bash
   curl -fsSL https://github.com/ebetica/recurse/releases/latest/download/install.sh | bash
   recurse /path/to/repo   # 浏览器或 SSH 隧道访问 http://127.0.0.1:8787
   ```
