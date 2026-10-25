# 7-Card 4:5 评测与验证报告：E2B 沙箱集群在 Nomad 单非 Leader Server 故障下的韧性评测

> **语言 / Language**: **中文 (当前)** | [English (`test-report.en.md`)](test-report.en.md)  
> **配套可视卡片与数据**: [7-Card 4:5 HTML 卡片组 (`test-report-cards.html`)](test-report-cards.html) · [密封评测数据 (`report.json`)](report.json) · [溯源账本 (`evidence.json`)](evidence.json) · [深度学习笔记 (`README.zh-CN.md`)](README.zh-CN.md)

---

## Card 1 (`1 / 7` · `HANDS-ON · CLOUD ARCHITECTURE & AI SANDBOX INFRASTRUCTURE RESILIENCE`) — 概览与实验工作台

### 核心发现标题
**单台非 Leader Nomad Server 停机导致 35% 健康 E2B Orchestrator 被误杀替换 — 配置 `disconnect (50s)` 与 `heartbeat_grace (50s)` 实现 100% 存量与容量保持**

### 实验工作台摘要（3 Nomad Servers · 20 Sandbox Hosts）
- **被测拓扑**：3 台 Nomad Server（1 Leader + 2 Followers，维持 2/3 Raft 多数派）+ 20 台 Nomad Client 沙箱宿主机（运行 `20` 个 `Orchestrator`、`20` 个 `session-proxy`、`3` 个 `client-proxy` 及上层 `API`）。
- **核心评测指标面板**：
  - `Baseline: 7/20 Orch & 2/3 Proxy Replaced`（基线无 `disconnect`、默认 `heartbeat_grace = 10s`，11 分钟观测窗口）
  - `disconnect=50s: 10/10 Sandboxes · 23/23 Streams`（开启三组件 `disconnect` 后存量沙箱与 HTTP NDJSON 长流 100% 保活）
  - `Short Requests: 12,581 / 12,581 (0 Errors)`（高频短请求零错误）
  - `heartbeat_grace=50s: 20/20 Ready (2 Rounds)`（调大 Server `heartbeat_grace` 后连续 2 轮测试 20/20 节点保持 `ready`）

---

## Card 2 (`2 / 7` · `SCENARIO: SINGLE NON-LEADER NOMAD SERVER FAILURE`) — 单例故障深度剖析

### 量化发现标题
**为什么心跳在 $t \approx 21\text{s}$ 恢复后，旧任务反而在 $t \approx 39\text{s}$ 开始 `Killing`、长流在 $t \approx 44\text{s}$ 关闭？两个 `50s` 窗口如何分别解开死结？**

> **日志实测引文**：在云平台确认非 Leader Server 停止后约 `21s`，Client 日志记录已成功向健康 Server 发送心跳；但在约 `39s` 时原任务开始执行 `Killing`，约 `44s` 时原应用 HTTP NDJSON 长流被关闭。

| 决策项 / 子维度 | 题型标签 | 核心结论 | 置信度 | 动作门控 | 关键分布指标 |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **`baseline_paradox_root_cause`** | `choice` | `yamux` Keepalive（`30s` 间隔 + `10s` Pong = `10–40s`）在与 Leader 计时器（`10–20s TTL + 10s grace = 20–30s`）的竞态中落败；Client 重连后拉取到已签发的 `stop` 计划 | `100%` | `Send to a human` | `client-proxy` 替换 `66.7%` (2/3) · `Orchestrator` 替换 `35.0%` (7/20) · `session-proxy` 替换 `35.0%` (7/20) |
| **`solution_1_disconnect_validation`** | `score` | 配置 `lost_after = "50s"`, `replace = false`, `reconcile = "keep_original"` 后，Allocation 进入 `unknown` 仅持续 `1.7s–31.6s` 即恢复为 `running` | `100%` | `Act automatically` | 沙箱状态保留 `100%` (10/10) · NDJSON 长流保持 `100%` (23/23) · 最大 `unknown` 占窗口比 `63.2%` (31.6s/50s) |
| **`solution_2_grace_vs_capacity`** | `score` | 配置 `server { heartbeat_grace = "50s" }` 后，Leader 容忍窗口扩展至 `60s–70s`，连续 2 轮测试 `20/20` Client 全程保持 `ready` | `98%` | `Act automatically` | 存活节点保持 `ready` `100%` (20/20) · E2B API 节点池容量 `100%` (20/20) · `yamux` 最大切换占预算比 `61.5%` (40s/65s) |

---

## Card 3 (`3 / 7` · `WHAT I TESTED`) — 9 项全量评测矩阵（Scorecard）

| SCENARIO | QUESTION / TASK | MODEL / SYSTEM ANSWER | PROB / SCORE | PASS | ACTION |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Baseline · Default Control Plane (`grace=10s`)** | `Orchestrator` 任务组（20 台 Client，停 1 台非 Leader Server，11m 观测） | `13/20` 保留 \| **`7/20` (`35.0%`) 被替换**（宿主机本身完全健康） | `65%` | ✕ | `Human` |
| **Baseline · Default Control Plane (`grace=10s`)** | `session-proxy` 任务组（20 台 Client，停 1 台非 Leader Server，11m 观测） | `13/20` 保留 \| **`7/20` (`35.0%`) 在 $t \approx 21\text{s}$ 重连后被替换** | `65%` | ✕ | `Human` |
| **Baseline · Default Control Plane (`grace=10s`)** | `client-proxy` 共享入口（3 个实例，停 1 台非 Leader Server，11m 观测） | `1/3` 保留 \| **`2/3` (`66.7%`) 被替换**，导致活跃流在 $t \approx 44\text{s}$ 断开 | `33%` | ✕ | `Human` |
| **Solution 1 · `disconnect` (`lost_after=50s`, `replace=false`)** | `Orchestrator` + `session-proxy` + `client-proxy` 全链路实例保留率（`unknown` `1.7–31.6s`） | **`43/43` (`100%`) Allocation 完整保留**；重连时 `0` 次任务重启 | `100%` | ✓ | `Auto` |
| **Solution 1 · `disconnect` (`lost_after=50s`, `replace=false`)** | 存量运行中 Firecracker 沙箱状态（进程 PID、内存页与本地文件） | **`10/10` (`100%`) 沙箱在故障后多轮独立复检中完好无损** | `100%` | ✓ | `Auto` |
| **Solution 1 · `disconnect` (`lost_after=50s`, `replace=false`)** | 外部活跃业务流量（`23` 条 HTTP NDJSON 长流 + `12,581` 次短请求） | **`23/23` (`100%`) NDJSON 长流不断连 \| `12,581/12,581` 短请求 `0` 错误** | `100%` | ✓ | `Auto` |
| **Solution 1 · Creation Capacity Blast Radius** | E2B API 新建沙箱节点池（过滤 `Status == "ready"` / `ClientStatus == "running"`） | **`13/20` (`65.0%`) 可用节点**；7 台 `disconnected` 节点被暂时剔除（单机负载 `+53.8%`） | `65%` | ✕ | `Confirm` |
| **Solution 2 · Server `heartbeat_grace = 50s`** | 连续 2 轮单 Server 强停测试中 20 台存活 Client 的状态稳定性（`60–70s` 预算） | **`20/20` (`100%`) Client 全程保持 `ready`**（`0` 台失联、`0` 次替换） | `100%` | ✓ | `Auto` |
| **Solution 2 · Real Host Crash Trade-Off** | 当物理沙箱宿主机**真实宕机**时 Nomad 心跳层的故障感知延迟 | 从 `20–30s` 延后至 **`60–70s`（增加 `+40s`）**；需配合上层 gRPC 健康探测快速熔断 | `57%` | ✕ | `Confirm` |

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`) — 源码调用链与协议配置核验

### 上游源码锚点（`hashicorp/nomad@bf24b0dd` · `hashicorp/yamux@v0.1.2` · `e2b-dev/runtime@afaaeaef`）

```json
{
  "nomad_heartbeat_and_reconciler_contract": {
    "client_heartbeat_rpc": "client/client.go#L2236: c.RPC('Node.UpdateStatus', {NodeID, Status: 'ready'}) -> resp.HeartbeatTTL",
    "client_failover_wait": "client/rpc.go#L83 + yamux@v0.1.2/session.go#L327: 30s Keepalive + 10s Pong -> 10-40s silent drop wait",
    "leader_timer_formula": "nomad/heartbeat.go#L93: resetHeartbeatTimerLocked(id, ttl + HeartbeatGrace)",
    "leader_expiry_branch": "nomad/heartbeat.go#L137: Status = Down; if canDisconnect && hasPendingReconnects -> Disconnected",
    "disconnect_expiry": "nomad/structs/alloc.go#L756: lastUnknown.Add(tg.GetDisconnectLostAfter())",
    "reconciler_guard": "scheduler/reconciler/filters.go#L527: if isDisconnecting && !alloc.ReplaceOnDisconnect() { return }",
    "reconnect_kill_trigger": "client/allocrunner/alloc_runner.go#L1078: if !ar.Alloc().TerminalStatus() && update.TerminalStatus() -> killTasks()"
  }
}
```

`↓ 调优后的 Nomad HCL 配置与 E2B API 节点池过滤逻辑交互`

```hcl
# 1. Nomad Server 配置（将判定失联前的切换预算从 20-30s 扩展至 60-70s）
server {
  heartbeat_grace = "50s"
}

# 2. Nomad Job 任务组配置（必须同时覆盖 orchestrator、session-proxy、client-proxy）
group "orchestrator" {
  disconnect {
    lost_after = "50s"           # 从 Allocation 进入 unknown (tU≈25s) 起算，至 tU+50s≈75s+ 到期
    replace    = false           # 节点失联期间禁止立即创建替换 Allocation
    reconcile  = "keep_original" # 窗口内重连成功后保留原节点上的运行中实例
  }
}
```

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`) — 策略扰动与工程权衡对比表

| QUESTION / DIMENSION | SELECTED COMPARISON | ORIGINAL (%) | TUNED (%) | CHANGE (PTS) | HELD / IMPROVED |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **`Orchestrator` 实例保留率** | Baseline (无 `disconnect`) $\rightarrow$ Solution 1 (`disconnect 50s`) | `65.0%` | `100.0%` | **`+35.0`** | ✓ |
| **`session-proxy` 实例保留率** | Baseline (无 `disconnect`) $\rightarrow$ Solution 1 (`disconnect 50s`) | `65.0%` | `100.0%` | **`+35.0`** | ✓ |
| **`client-proxy` 入口实例保留率** | Baseline (无 `disconnect`) $\rightarrow$ Solution 1 (`disconnect 50s`) | `33.3%` | `100.0%` | **`+66.7`** | ✓ |
| **新建沙箱可用节点池容量比例** | Solution 1 (`grace=10s`) $\rightarrow$ Solution 2 (`grace=50s`) | `65.0%` | `100.0%` | **`+35.0`** | ✓ |
| **真实宿主机宕机的心跳层感知及时率** | Default (`grace=10s`, $\le 30\text{s}$) $\rightarrow$ Extended (`grace=50s`, $\le 70\text{s}$) | `100.0%` | `42.9%` | **`-57.1`** | ✕ (Trade-off) |

---

## Card 6 (`6 / 7` · `LATENCY`) — 关键控制面时间窗口下界/前值 vs 上界/后值对比（ms）

| 序号 (`#`) | 对比阶段说明 | 下界 / 调优前耗时 (`ms`) | 上界 / 调优后窗口 (`ms`) | 架构含义 |
| :---: | :--- | :---: | :---: | :--- |
| **`#1`** | Nomad 动态心跳周期 `TTL`（典型值 `15s`） vs 默认 Leader 超时预算（`TTL + 10s grace = 25s`） | `15,000 ms` | `25,000 ms` | 默认仅给 `10,000 ms` 额外宽限期 |
| **`#2`** | `yamux` 静默断连最快感知（`10s` Pong 超时） vs 最慢感知（`30s` Ping + `10s` Pong = `40s`） | `10,000 ms` | `40,000 ms` | 慢半区（`25,000–40,000 ms`）必然突破 `#1` 的默认预算 |
| **`#3`** | 实测日志中心跳恢复时刻（$t \approx 21\text{s}$） vs 本地任务开始 `Killing` 时刻（$t \approx 39\text{s}$） | `21,000 ms` | `39,000 ms` | 重连恢复心跳后 `18,000 ms` 拉取并执行控制面 `stop` 计划 |
| **`#4`** | 方案一实测最大 `unknown` 持续时长（`31.6s`） vs 配置的 `lost_after` 容忍上限（`50.0s`） | `31,600 ms` | `50,000 ms` | 留有 `18,400 ms`（`36.8%`）安全余量，实现 `0` 替换 |
| **`#5`** | 默认 Leader 典型预算（`25s`） vs 方案二 `heartbeat_grace = 50s` 典型预算（`65s`） | `25,000 ms` | `65,000 ms` | `65,000 ms` 完整包络 `#2` 的 `40,000 ms` `yamux` 切换上限 |
| **`#6`** | 真实宿主机宕机时默认心跳最大发现时间（`30s`） vs `grace = 50s` 最大发现时间（`70s`） | `30,000 ms` | `70,000 ms` | 调大 `grace` 带来 `+40,000 ms` 心跳盲区，需上层 gRPC 快检补偿 |

---

## Card 7 (`7 / 7` · `MY TAKE`) — 适用场景、反模式警示与生产就绪建议

### ✅ 推荐实践（Good Fit）
- **组合防御（Defense-in-Depth）**：将适度调大的 Server `heartbeat_grace` 与任务组级 `disconnect { lost_after = "50s", replace = false, reconcile = "keep_original" }` 结合使用。
- **全链路覆盖**：确保 `Orchestrator`、`session-proxy` 和 `client-proxy` 全部配置 `disconnect`，防止“沙箱还活着但代理被杀导致流断开”。
- **双层健康检查解耦**：由 E2B API 的主动 gRPC 健康探测与创建失败熔断负责秒级隔离**真实死机**的宿主机，让 Nomad 心跳层专注容忍控制面 transient 抖动。
- **容量冗余规划**：若采用较短 `heartbeat_grace` + `disconnect`，需预留 $\ge 35\%$ 的新建沙箱容量余量以吸收单 Server 故障期间的节点池收缩。

### ⛔ 严禁踩坑（Not For）
- 切勿在默认无 `disconnect` 配置下运行有状态 Firecracker `Orchestrator`（单台非 Leader Server 停机即可造成 `35%` 沙箱宿主机任务被杀）。
- 切勿只给 `Orchestrator` 配置 `disconnect` 而遗漏 `session-proxy` 与 `client-proxy`（基线中 `client-proxy` 替换率高达 `66.7%`）。
- 切勿混淆 `lost_after = "50s"`（从进入 `unknown` 的 $t_U \approx 25\text{s}$ 起算）与 `heartbeat_grace = "50s"`（在进入 `disconnected` 之前生效）。
- 切勿在缺乏上层业务健康检查的情况下盲目将 `heartbeat_grace` 设得过大，否则真实宕机宿主机将在 `60s–70s` 内继续接收新建沙箱请求。

### 溯源声明（Provenance）
- **数据属性**：`anonymized_reported` + `static_source_verified`（`independently_reproduced = false`；基于公开故障注入实测报告与上游源码逐行核验，配套 `6/6` 确定性单元测试通过）。
- **验证锚点**：`hashicorp/nomad@bf24b0dd97430d3b364b68b1f7375e85e585778f` · `hashicorp/yamux@v0.1.2` · `e2b-dev/runtime@afaaeaef96aae86f65ce60bf38fe083e7638a28e` · `hashicorp/nomad#17974`。
