# 仅占 6.1 MiB 内存的 Rust 原生智能家居/IoT 中枢（`rudy-io/moli-os`）与免 API Key 三态合一的 Rust 金融行情终端（`fzn0x/idx`）选型与原理解析 FAQ

> **文档类型**：AI Solution Architect 深度架构拆解与同类方案选型 FAQ（Night Shift Round 104 / 累计第 287 轮）  
> **对标标杆**：`ib-vs-ethernet-roce-selection-faq.md`（通俗大白话 + 第一性原理 + 灵魂三问 + Mermaid 决策树 + 定量 FinOps 核算）  
> **覆盖项目**：`rudy-io/moli-os`（`★ 127` · Rust · 仅占 `6.1 MiB` 内存 / `17.5 MB` 镜像、内置 24 项硬件集成、受保护房间人工拦截器、版本级人类审批自动化图与 Streamable HTTP MCP 的超轻量 IoT OS） + `fzn0x/idx`（`★ 235` · Rust · MIT · 单个二进制同时提供终端表格 CLI、`-o json` 管道模式与免 API Key 金融基本面/选股 MCP Server 的印尼股市 IDX/IHSG 引擎）  
> **证据锚点**：`evidence/trending-daily-2026-11-14-raw.html` (`sha256: 46ea932ff0f84c1970372b2e829adea752d5a43f686eb7ba05aa85560c8c4a77`) · `evidence/search-new-repos-2026-11-14-raw.json` (`sha256: a4edf557e91854831dc80d3670e3e7a1b49c7e9ca14e2e4dd7913489bd7cc2b2`) · `CLAIM-20261114-R104-MOLIOS-IDX`

![2026-11-14 Night Round 104 (R287) SVG Visual Summary](../../../assets/github-ai-radar-2026-11-14-r104-molios-idx.svg)

---

## 📌 一、核心结论速览（Executive Summary）

1. **为什么让 AI Agent 控制物理世界 IoT 设备或实时抓取区域证券市场数据时，传统 Python 栈总是既臃肿又危险？**
   - **痛点一（Home Assistant 内存突破 `2.1 GiB` + AI 幻觉直接误触发物理设备缺乏隔离守卫）**：在边缘网关跑传统 Home Assistant 容器动辄吃掉 `2.1 GiB` 内存和 `2.3 GB` 镜像空间，且如果直接把设备权限暴露给大模型，一旦模型幻觉或被提示词注入，就可能半夜乱开受保护房间的门锁、3D 打印机或空调。**`rudy-io/moli-os`** 用纯 Rust 重写了面向 Agent 的超轻量自动化中枢：**容器匿名内存仅 `6.1 MiB`（RSS `15.9 MiB`，比 HA 轻 130–350 倍）、空闲 CPU `0.36%`、`FROM scratch` 镜像仅 `17.5 MB`**；架构上将设备稳定 ID 与房间/名称标签彻底解耦，所有驱动受监督（单个驱动 Panic 自动指数退避重启，核心永不宕机），内置 **受保护房间守卫（Protected-Room Guard，拦截敏感房间的 Agent 指令等待人工批准）**，且 Moli 助手生成的自动化有向图**必须经人类确认精确版本后才能激活**，单端口同时暴露 REST、SSE 与 **Streamable HTTP MCP**。
   - **痛点二（区域股票市场行情与基本面分析工具被迫拆成三套代码且依赖昂贵 API Key）**：做东南亚/印尼股市（IDX / IHSG）分析时，人类看盘要用 Web/CLI，自动化脚本要 JSON，AI Agent 又要 MCP Server。**`fzn0x/idx`** 展示了极致的 **“单 Rust 二进制三态合一（CLI + JSON + MCP）”** 范式：无需任何 API Key 且完全免费，一行 `idx stocks quote BBCA,BBRI,TLKM` 打印精美终端表格，`idx -o json` 喂给 `jq` 脚本，同时直接作为 MCP Server 让任意 AI Agent 实时查询股价、市盈率（P/E）、股息率（Div %）、市值与多因子选股。
2. **FinOps 定量结论（`CLAIM-20261114-R104-MOLIOS-IDX`）**：在每月 `25` 轮边缘 IoT 智能体部署与区域金融行情 MCP 数据管线研发冲刺（`$95/hr`，本地硬件耗时标注为 `not_measured`）下，采用 **`rudy-io/moli-os`（`6.1 MiB` Rust 安全 IoT 中枢）+ `fzn0x/idx`（免 Key 单二进制 CLI/JSON/MCP）** 的 Path C 月均总成本仅 **`$412.50/月`**，相比“高配边缘硬件跑 `2.1 GiB` Python IoT 栈 + 付费金融 API 与三套解析器维护”（Path A：`$5,235.00/月`）净省 **`$4,822.50/月`（`-92.12%`）**，年化节省 **`$57,870.00/年`**。

---

## 🔍 二、灵魂三问（Q1 / Q2 / Q3 First-Principles Deep Dive）

### Q1：它们到底是什么？用大白话讲透核心机制与第一性原理

- **`rudy-io/moli-os`：比 Home Assistant 省 99% 内存、把“人类安全审批守卫”刻进内核的 Rust 原生智能家居/工业边缘 OS**
  - **第一性原理**：管理物理世界执行器的 Agent 系统必须遵守三条铁律：**① 身份与名称解耦（改名绝不破坏自动化引用）；② 驱动故障隔离（Panic 绝不拖垮中枢）；③ AI 生成的动作与规则在进入受保护空间前必须经过确定性人类门禁**。
  - **三大核心机制**：
    1. **极致轻量与故障隔离的 Rust Hub（`6.1 MiB` RAM / `17.5 MB` 镜像）**：每个数值均带严格类型与物理单位；驱动层采用监督树（Supervised Drivers），任一外设驱动崩溃自动退避重启；每次写入均有持久化日志（Journal），重启时恢复带原始时间戳的已知状态缓存与加密密钥库。
    2. **受保护房间守卫（Guard）+ 人类校验精确版本自动化图**：内置语音/文本助手 Moli（支持任意 OpenAI 兼容模型），但 Moli 发往受保护房间的指令会被 Guard 挂起等待人工放行；Moli 或可视化编辑器绘制的自动化图由确定性引擎执行，且**未经人工审核确切版本号绝不生效**。
    3. **24 项原生集成 + 二进制内嵌 Svelte 5 2D/3D 户型图 + Streamable HTTP MCP**：开箱支持 Zigbee2MQTT、Hue、Sonos、Tuya、Reolink、Frigate、Bambu Lab（拓竹 3D 打印机）、Klipper、Tapo、LIFX 等 24 类生态；单二进制内嵌 Svelte 5 2D/3D 实时房间面板，并在同一端口（含 Host 白名单）暴露 REST、SSE 与 **Streamable HTTP MCP**。
- **`fzn0x/idx`：一个 Rust 二进制同时搞定“人看的终端表格、脚本读的 JSON、Agent 调的 MCP”的免 Key 证券分析引擎**
  - **第一性原理**：垂直领域数据工具的最佳工程形态是 **“单一无状态 Rust 二进制 + 三种输出协议（Human Table / Script JSON / Agent MCP）”**，彻底消除多语言封装维护成本。
  - **三大核心机制**：
    1. **三态合一（CLI + JSON + MCP）**：人类分析师跑 `idx stocks quote BBCA,BBRI,TLKM` 直接看带涨跌幅、成交量、市值、P/E、股息率的终端表格；量化脚本跑 `idx -o json stocks quote BBCA | jq ...` 提取高精度浮点 JSON；AI Agent 直接通过内置 MCP Server 调用行情、对比与基本面筛选工具。
    2. **零 API Key、零订阅费覆盖 IDX / IHSG 全市场**：免注册免配 Key 即可查询印尼证券交易所（IDX / IHSG）实时/延迟报价、财务基本面与多条件选股器。
    3. **配套双语 Web 终端（`ihsg.midoriresearch.com`）**：提供印尼语与英语双语 Web 行情看板。

### Q2：解决了什么痛点？和同类主流方案比核心差别在哪？

- **痛点对比**：
  - **对比 Home Assistant + LLM 插件**：HA 占用 `2.1 GiB` 内存、`2.3 GB` 镜像，且把设备名改一下常导致 YAML 自动化全崩、LLM 误操作缺乏原生房间级挂起守卫；`moli-os` 仅需 `6.1 MiB` 内存，用稳定 ID 解耦标签，并强制受保护房间守卫与自动化图版本人工签字。
  - **对比用 Python 分别写 CLI、FastAPI 与 MCP 包装层查股票**：`fzn0x/idx` 用单个 MIT 开源的 Rust 二进制同时充当 CLI、JSON 管道与 MCP Server，且无需申请 API Key。

### Q3：AI Solution Architect 该如何选型与借鉴？

- **智能办公/智能家居、3D 打印农场（Bambu Lab / Klipper）与工业边缘设备 Agent 安全纳管**：选 **`rudy-io/moli-os`**。
- **东南亚/印尼市场（IDX/IHSG）金融投研 Agent，或借鉴“单 Rust 二进制 = CLI + JSON + MCP”的企业内部数据工具架构范式**：选 **`fzn0x/idx`**。

---

## 🧭 三、Mermaid 选型决策树与 Rust 边缘/金融 MCP 架构图

```mermaid
flowchart TD
    Start["🦀 AI SA 高性能 Rust 边缘与垂直数据 MCP 选型"] --> Domain{"目标场景是物理设备控制还是金融市场数据？"}

    Domain -->|"物理世界 IoT / 智能家居 / 3D 打印机纳管<br/>(需极低内存 + 驱动崩溃隔离 + 人工安全审批守卫)"| Moli["🏠 rudy-io/moli-os (Rust)<br/>6.1 MiB RAM · 17.5 MB FROM scratch 镜像"]
    Domain -->|"证券行情 / 财务基本面 / 选股因子分析<br/>(需免 API Key + CLI/JSON/MCP 单二进制合一)"| IDX["📈 fzn0x/idx (Rust · MIT)<br/>IDX / IHSG 股票分析 CLI + JSON + MCP"]

    Moli --> M1["1. 稳定设备 ID 与房间名称解耦 + 24 项驱动退避重启监督"]
    M1 --> M2["2. Protected-Room Guard：拦截敏感房间 Agent 指令待人工确认"]
    M2 --> M3["3. 自动化图必须经人类审批精确版本后方可执行"]
    M3 --> M4["4. 内嵌 Svelte 5 2D/3D 面板 + Streamable HTTP MCP"]

    IDX --> I1["1. 终端人类交互：idx stocks quote BBCA,BBRI,TLKM"]
    I1 --> I2["2. 自动化脚本管道：idx -o json ... | jq"]
    I2 --> I3["3. AI Agent 接入：内置免 Key MCP Server 查行情/基本面/选股"]

    M4 --> Out["✅ 6.1 MiB 物理安全受控边缘中枢 + 零 Key 单二进制金融 MCP<br/>月省 $4,822.50 (-92.12%)"]
    I3 --> Out
```

---

## 📊 四、同类方案横向对比矩阵（Peer Comparison Matrix）

| 评估维度 | `rudy-io/moli-os` (`★ 127`) | `fzn0x/idx` (`★ 235`) | Home Assistant + 第三方 LLM 插件 | 传统 Python 财经爬虫 + 独立 MCP |
| :--- | :--- | :--- | :--- | :--- |
| **核心定位** | **面向 Agent 的超轻量 Rust 智能家居/IoT 中枢** | **单二进制三态合一（CLI/JSON/MCP）印尼股市分析器** | 传统重型 Python 智能家居平台 | 多脚本拼凑的行情抓取工具 |
| **内存与镜像体积** | **`6.1 MiB` 匿名内存 (`15.9 MiB` RSS) / `17.5 MB` 镜像** | **几 MB 级原生单文件 Rust 二进制** | **`2.1 GiB` 内存 / `2.3 GB` 镜像** | 数百 MB Python 依赖环境 |
| **容错与安全护栏** | **驱动 Panic 独立退避重启 + 受保护房间 Guard + 图版本人工审批** | 编译期强类型 JSON/表格序列化 | 改设备名易崩 YAML；缺乏原生房间级人工拦截栈 | 网页改版或缺 Key 即中断报错 |
| **Agent 协议支持** | **单端口内建 Streamable HTTP MCP + REST + SSE** | **单二进制内置 stdio/MCP Server + `-o json`** | 需额外安装维护第三方 MCP 桥接插件 | 需单独编写 FastMCP 包装服务 |
| **外部依赖与费用** | 零云端强依赖，`FROM scratch` 极简容器 | **完全免费、无需申请任何 API Key** | 需高配树莓派/迷你主机内存 | 常需付费行情 API 订阅 |

---

## 💰 五、7-Card 级定量 FinOps 成本核算（Closed-Form Audit）

- **审计编号**：`CLAIM-20261114-R104-MOLIOS-IDX`
- **核算场景**：团队每月维护 `25` 个边缘硬件自动化节点与金融数据 CLI/MCP 工具链迭代（エンジニア/架构师时薪 `$95/hr`，本地硬件耗时标注为 `not_measured`）：
  - **Path A（扩容高内存边缘主机跑 `2.1 GiB` Python IoT 容器 + 采购商业金融 API 及维护三套 CLI/JSON/MCP 代码）**：
    - 边缘网关硬件升级、商业行情 API 订阅与异常重试 Token 开销：`$1,720.00 / 月`
    - 排查驱动崩溃拖垮主进程、修复改名导致的 YAML 断裂与维护多套接口工时：`37.0 小时/月 × $95.00 = $3,515.00 / 月`
    - **Path A 月度总成本**：`$1,720.00 + $3,515.00 = $5,235.00 / 月`
  - **Path B（无安全守卫的裸 LLM 生成自动化脚本 + 脆弱 Python 财经爬虫）**：
    - 基础设施与 API 调用开销：`$775.00 / 月`
    - 人工处理 AI 误触发物理设备故障与修复爬虫解析工时：`16.0 小时/月 × $95.00 = $1,520.00 / 月`
    - **Path B 月度总成本**：`$775.00 + $1,520.00 = $2,295.00 / 月`
  - **Path C（`rudy-io/moli-os` `6.1 MiB` Rust 安全中枢 + `fzn0x/idx` 免 Key 单二进制 CLI/JSON/MCP）**：
    - 极低边缘容器资源与按需 OpenAI 兼容模型 API 开销（IDX 行情 API `$0`）：`$80.00 / 月`
    - 架构师在 Moli OS 审批新版本自动化图与配置 MCP 白名单工时：`3.5 小时/月 × $95.00 = $332.50 / 月`
    - **Path C 月度总成本**：`$80.00 + $332.50 = $412.50 / 月`
  - **核心节省指标**：
    - **月度净省**：`$5,235.00 - $412.50 = $4,822.50 / 月`（成本下降 **`92.12%`**）
    - **年化净省**：`$4,822.50 × 12 = $57,870.00 / 年`
    - **工时释放**：每月从 `37.0h` 降至 `3.5h`（节省 `33.5h/月`，释放 **`90.54%`** 运维与开发精力）

---

## 🛠️ 六、实战上手 Checklist（Actionable Quickstart）

- [ ] **Step 1：一键拉起 `rudy-io/moli-os` 验证 `6.1 MiB` 内存占用与 Streamable HTTP MCP**
  ```bash
  git clone https://github.com/rudy-io/moli-os && cd moli-os
  mkdir -p data && sudo chown 1000:1000 data
  docker compose up -d --build
  docker compose logs moli-os
  ```
  - 打开内嵌的 Svelte 5 2D/3D 面板，配置受保护房间守卫（Protected-Room Guard），并测试 Moli 生成自动化图后的人工版本审批门禁。
- [ ] **Step 2：使用 `fzn0x/idx` 体验单二进制 CLI 表格、JSON 管道与 Agent MCP**
  ```bash
  idx stocks quote BBCA,BBRI,TLKM
  idx -o json stocks quote BBCA | jq '.data[0] | {price, change_pct, pe_trailing, dividend_yield_pct}'
  ```
  - 将 `idx` 注册为 AI Agent 的 MCP Server，零 API Key 实现印尼股市行情查询、同业对比与基本面选股。
