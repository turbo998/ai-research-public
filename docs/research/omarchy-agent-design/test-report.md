# Omarchy Agent 设计机制契约评测报告（7 页 4:5 视觉卡片版）

**来源性质：** `measured (offline static contract verifier · upstream_runtime=not_run)`，基于固定上游 commit [`9480d1b6a98156314dbabe6bfef08f39f8b9cd07`](https://github.com/omacom/omarchy/tree/9480d1b6a98156314dbabe6bfef08f39f8b9cd07)（规范仓库 `omacom/omarchy`，请求别名 `basecamp/omarchy`）的确定性静态契约与证据完整性核验，未执行上游 bash 脚本、安装器、桌面会话或真实 Agent 二进制。

结构化数据与可离线预览工件：
- [7 页 4:5 视觉评测卡片 HTML（CSP 锁定自包含）](test-report-cards.html)
- [完整卡片与证据绑定 JSON](evidence/test-report.json)
- [12 项机制契约评测明细 CSV](evidence/test-scenarios.csv)
- [6 项模式扰动与逆序鲁棒性 CSV](evidence/test-robustness.csv)
- [批量契约核验耗时对比 CSV](evidence/test-batch-latency.csv)
- [174 条源码/文档/测试断言索引 CSV](evidence/assertion-index.csv) 与 [源码 Blob 台账](evidence.json)

---

## Card 1（`1 / 7` · `HANDS-ON · AGENTIC OS HARNESS BENCHMARK`）：总览与契约工作台

**核心发现标题：** **14 harnesses unified, soft boundaries exposed**（统一封装 14 个异构 Agent CLI，但默认无人值守参数与软隔离边界暴露）。

本评测针对 `omacom/omarchy@9480d1b6a98156314dbabe6bfef08f39f8b9cd07`（根树 `f1ef20f439289dc3cd1c968eb475a9750d64bc61`，共 2,663 个树条目）的 6 个机制专题（`E1`–`E6`）、87 个引用源文件（本地缓存核验 272 个 Git blob，共 1.22 MB）、7 份官方对比文档（`W1`–`W7`）及 174 条可追溯断言执行静态契约评测。

报告采用三档验证置信度与动作门控（Action Gating）：
- `Act automatically` / `Auto`（自动采信）：100% 由固定 commit 字节直接证实的确定性代码/IPC 契约（对应 `source_fact`，占总断言 `122 / 174 = 70.1%`）；
- `Confirm`（需结合上下文复核）：仓库文档声明、官方平台文档对比或存在模式切换/缓存边界漂移的机制（对应 `documentation_claim`，占总断言 `33 / 174 = 19.0%`）；
- `Send to a human` / `Human`（转交人工/待运行验证）：静态测试契约（`test_contract`，`19 / 174 = 10.9%`，`not_run`）以及涉及 OS 容器沙箱缺失、第三方 CLI 真实加载行为的运行期边界。

| 工作台决策字段 | 题型 | 核心评测问题 | 评测输出 | 置信度 / 比例 | 动作分档 | 分布明细 |
|---|---|---|---|---:|---|---|
| `e1_argv_contract` | `choice` | 14 个可启动 harness 在无 prompt / 有 prompt 共 28 条分支中是否全部保持单参数 argv 边界？ | `28 / 28 branches (100.0%)` | `1.000`（100.0%） | `Act automatically` | `direct_exec_argv` 78.6%（11/14）, `subcommand_run_or_code` 14.3%（2/14）, `gateway_tui_openclaw` 7.1%（1/14） |
| `e4_provider_alignment` | `choice` | 可启动 harness（14）、多账户 provider（3）与默认用量收集器（4）是否一一同构？ | `Non-isomorphic (3 / 14 = 21.4%)` | `0.786`（78.6%） | `Confirm` | `launch_only_harness` 78.6%（11/14）, `account_and_usage_provider` 21.4%（3/14）, `usage_only_fireworks` 25.0%（1/4 usage） |
| `e6_isolation_model` | `score` | E6 梳理的 16 项安全与隔离机制中，硬性代码/OS 边界与软性提示词/目录约定占比几何？ | `5 / 16 hard boundaries (31.3%)` | `0.313`（31.3%） | `Send to a human` | `soft_convention_or_flag` 68.8%（11/16）, `hard_code_or_ipc_boundary` 31.3%（5/16）, `os_container_sandbox_in_launcher` 0.0%（0/14） |

---

## Card 2（`2 / 7` · `SCENARIO: E1–E6 STATIC CONTRACT DEEP DIVE`）：单样本深度拆解

**核心发现标题：** **174 assertions. 87 blobs. 7 doc-vs-code drifts caught.**

针对固定基线 `omacom/omarchy@9480d1b6a98156314dbabe6bfef08f39f8b9cd07` 的全量断言库，从**证据层级构成**、**崩溃转 Agent 人工门控**与**多账户自动切换缓存边界**三个维度做深度拆解：

| 决策字段 | 题型 | 深度拆解问题 | 核验结果 | 置信度 / 概率 | 动作分档 | 分布明细 |
|---|---|---|---|---:|---|---|
| `evidence_composition` | `choice` | 174 条断言在三类证据状态（源码事实 / 文档声明 / 未运行测试契约）中的精确占比？ | `source_fact 122 / 174 (70.1%)` | `0.701`（70.1%） | `Act automatically` | `source_fact · static_read` 70.1%（122）, `documentation_claim · doc/official` 19.0%（33）, `test_contract · not_run` 10.9%（19） |
| `e3_crash_pipeline_gates` | `noul` | `omarchy-crash-watch` 是否强制执行全部 5 道前置过滤门禁且必须由用户点击通知才启动 Agent？ | `Yes (5 / 5 gates · 100.0%)` | `P(true) = 1.0` | `Act automatically` | `enforced_static_gates` 100.0%（5/5：`_UID`、`disabled`、`ignore`、`mute`、`seen_key`）, `silent_background_agent_exec` 0.0%（0/5） |
| `e4_autoswitch_vs_stale` | `score` | `omarchy-agent-account-autoswitch` 在满足 `mode=auto`、`>=95%` 触发与排除 `Waiting for auth` 时，是否排除 `stale=true` 缓存账户？ | `4 / 5 rules (80.0% · stale=true not excluded)` | `0.800`（80.0%） | `Confirm` | `mode_95pct_auth_tiebreak` 80.0%（4/5 已验证）, `stale_cache_still_eligible_gap` 20.0%（1/5 未过滤 `stale=true`） |

**拆解结论：**
1. 原始研究计划附件（`PLAN.md:121`）仅列出 13 个 harness，漏掉了走专用 `openclaw-gateway.service` + `openclaw tui` 生命周期的 `openclaw`（`bin/omarchy-agent:85-93`）；附件 `README.md:5` 声称已在 Azure VM 完成验证，但附件 `evidence/` 与 `findings/` 仅含空 `.gitkeep`。
2. 上游 `shell/plugins/agents/README.md:3-8` 声称桌面插件“strictly a display layer”，但 `Panel.qml:278-447,770-777` 实际派发账户切换（`use`）、模式切换（`manual`/`auto`）、重新登录终端与 `usage-update --limits-only` 4 类写/控制动作。

---

## Card 3（`3 / 7` · `WHAT I TESTED`）：6 专题 12 项契约评测全矩阵

下表汇总 6 个机制专题（`E1`–`E6`）共 12 项正式契约检验。带有 `✕`（方向/预期不成立）的条目代表**静态核验捕获的文档偏差、附件假设错误或软隔离风险边界**：

| 专题场景 | 契约检验问题 | 核验结果（报告百分比） | 预期是否成立 | 动作分档 | 源码证据锚点 |
|---|---|---|---:|---|---|
| `E1 Launcher` | 附件 harness 列表（13 个）是否覆盖 `bin/omarchy-agent` 全部可启动分支（14 个）？ | `13/14 matched (missed openclaw gateway)` (93%) `✕` | 否 | `Confirm` | `bin/omarchy-agent:57-132` (`E1-10`–`E1-28`) |
| `E1 Launcher` | 14 个 harness × 2 种模式（28 条路径）是否全部保持单参数 prompt argv 边界？ | `28/28 preserve argv boundary` (100%) | 是 | `Auto` | `bin/omarchy-agent:57-146` (`E1-10`–`E1-25`) |
| `E1 Launcher` | 无 prompt 模式下启用自动/跳过权限 flag 的 12 个 harness 在有 prompt 模式下是否保持一致？ | `11/12 retained (crush drops --yolo on run)` (92%) `✕` | 否 | `Confirm` | `bin/omarchy-agent:65-67` (`E1-12`) |
| `E2 Skills` | `omarchy-provision-user` 是否幂等链接全部 6 个全局技能根目录及已有 Hermes profiles？ | `6/6 roots + Hermes profiles/*/skills` (100%) | 是 | `Auto` | `bin/omarchy-provision-user:84-104` (`E2-01`–`E2-03`) |
| `E2 Skills` | 6 个全局技能软链接根目录是否覆盖全部 14 个可启动 harness 的配置命名空间？ | `6/14 linked (8 harnesses have no symlink root)` (43%) `✕` | 否 | `Human` | `bin/omarchy-provision-user:88-94` (`E2-01`, `E2-19`) |
| `E3 Crash` | 崩溃守护进程是否完整执行 5 道前置过滤且必须点击通知才启动诊断 Agent？ | `5/5 gates + user click required` (100%) | 是 | `Auto` | `bin/omarchy-crash-watch:48-159` (`E3-03`–`E3-12`) |
| `E4 Accounts` | 可启动 harness（14）、账户管理（3）与默认用量收集（4）三套集合是否同构？ | `3/14 account-managed (+Fireworks usage-only)` (21%) `✕` | 否 | `Confirm` | `bin/omarchy-agent-account-state:69-85`, `usage-update:15` (`E4-01`, `E4-34`) |
| `E4 Accounts` | 自动切换是否严格执行 `mode=auto`、`>=95%` 触发、排除 `Waiting for auth` 与 5h→周→编号排序？ | `4/4 source & test contracts verified` (100%) | 是 | `Auto` | `bin/omarchy-agent-account-autoswitch:5-225` (`E4-20`–`E4-29`) |
| `E4 Accounts` | 自动切换在候选排序时是否过滤 `stale=true` 的过期缓存文件？ | `0/1 filtered (stale=true still eligible)` (0%) `✕` | 否 | `Confirm` | `bin/omarchy-agent-account-autoswitch:49-85` (`E4-25`) |
| `E4 Desktop UI` | `shell/plugins/agents/README.md` 所称 QML 插件“strictly a display layer”是否成立？ | `2/6 read-only (4 write/exec actions in Panel.qml)` (33%) `✕` | 否 | `Confirm` | `shell/plugins/agents/Panel.qml:278-447,770-777` (`E4-77`, `E4-81`–`E4-83`) |
| `E5 Repo Native` | `test/all`（11 个无头 shell 测试集）是否与图形 VM 验收测试（`test/acceptance`）严格分离？ | `11/11 headless isolated from VM acceptance` (100%) | 是 | `Auto` | `test/all:1-13`, `docs/testing.md:7-53` (`E5-06`, `E5-07`) |
| `E6 Safety` | E6 盘点的 16 项安全与隔离控制中，硬性代码/IPC 边界是否占主导？ | `5/16 hard boundaries (0/14 OS sandbox in launcher)` (31%) `✕` | 否 | `Human` | `findings/06-safety-model.md` (`E6-01`, `E6-02`) |

---

## Card 4（`4 / 7` · `UNDER THE HOOD`）：从 Journald 崩溃事件到参数安全启动的协议链路

Card 4 展示了 Omarchy 最具代表性的跨层协议设计：如何将不受信任的操作系统崩溃日志转化为带账户隔离与人工确认门控的 Agent 诊断会话，同时避免将崩溃字段交由外层 shell `eval` 解析。

**输入端（`systemd-coredump` JSON 事件 + NUL 分隔 `execArgv`）：**

```json
{
  "SYSLOG_IDENTIFIER": "systemd-coredump",
  "_UID": "1000",
  "COREDUMP_EXE": "/usr/bin/waybar",
  "COREDUMP_UNIT": "waybar.service",
  "COREDUMP_SIGNAL": "11",
  "COREDUMP_SIGNAL_NAME": "SIGSEGV",
  "COREDUMP_TIMESTAMP": "1787843905000000"
}
```

` ↓ 用户点击 "Investigate with AI" -> omarchy-agent-crash 组装模板 & omarchy-launch-agent 绑定账户 HOME `

**输出端（结构化诊断 Prompt 模板 + 确定性 `exec` 边界）：**

```xml
<crash_investigation_prompt>
Application: /usr/bin/waybar (waybar.service) · Signal: 11 (SIGSEGV)
Step 1: coredumpctl info 1787843905000000 + journalctl --since/@timestamp
Step 2: Identify root cause (config vs package update vs upstream bug)
Step 3: Propose fix and ask for confirmation before modifying files
</crash_investigation_prompt>
# omarchy-agent-account-exec claude -> exports OMARCHY_AGENT_CLAUDE_HOME & CLAUDE_CONFIG_DIR
# exec $1 "$@" -> claude --dangerously-skip-permissions "<prompt>" -> <answer>
```

**协议边界要点：**
- **硬边界（CLI 入口之前）**：`omarchy-crash-watch` 通过 `omarchy-notification-send --exec` 将 `omarchy-agent-crash` 及其 6 个参数打包为 NUL 分隔数组写入状态文件；用户点击通知后由 `notification-daemon` 直接按 `execArgv` 数组拉起进程，再由 `omarchy-agent` 使用 `exec $1 "$@"` 将整段 prompt 作为单个参数传入 CLI。
- **软边界（CLI 启动之后）**：一旦进入目标 CLI，默认启动器对 12/14 个无 prompt 分支（11/14 个有 prompt 分支）传入了 `--dangerously-skip-permissions`、`--yolo` 或 `--allow-all` 等权限豁免参数，此时“修改文件前先询问用户”仅依赖 prompt 文本与 `SKILL.md` 软约束。

---

## Card 5（`5 / 7` · `ROBUSTNESS CHECK`）：模式扰动、显式覆盖与窗口敏感度检验

对 6 组关键架构不变量进行基线状态（`ORIGINAL`）与扰动/逆向状态（`REVERSED`）的配对一致性比对：

| 评测维度 | 配对比较定义（Original vs Reversed / Perturbed） | 基线比例 % | 扰动比例 % | 变化（百分点） | 主结论是否保持 |
|---|---|---:|---:|---:|---|
| `E1 · Prompt Argv Token Integrity (14 Harnesses)` | 无 prompt 启动（14/14）vs 含空格/引号的 `omarchy-agent-prompt` 启动（14/14） | `100.0` | `100.0` | `0.0` | 是 |
| `E1 · Unattended / Bypass Flag Retention (14 Harnesses)` | 无 prompt 启用自动/豁免 flag（12/14）vs 有 prompt 模式（11/14；`crush` 丢弃 `--yolo`） | `85.7` | `78.6` | `-7.1` | 是 |
| `E2 · Global Skill Symlink Roots (6 Namespaces)` | `omarchy-provision-user`（6/6 根目录）vs 初版迁移 `1786719479.sh`（5/6，早于 Hermes 迁移） | `100.0` | `83.3` | `-16.7` | 是 |
| `E4 · Explicit Provider Home Override Precedence (3 Providers)` | 新会话自动 pin（3/3）vs 外部显式指定 `CLAUDE_CONFIG_DIR` / `CODEX_HOME` / `GROK_HOME`（3/3） | `100.0` | `100.0` | `0.0` | 是 |
| `E4 · Collector Stale-Window Retention on Transient Failure (4 Providers)` | 正常模式本地状态/缓存复用（3/4）vs 网络失败时保留旧配额窗口（2/4：Claude 与 Grok） | `75.0` | `50.0` | `-25.0` | 是 |
| `E5 · Git Trailer Attribution Denominator (200-Commit Window)` | 最新 100 条提交含 Agent trailer（10/100）vs 第 101–200 条提交（11/100） | `10.0` | `11.0` | `+1.0` | 是 |

---

## Card 6（`6 / 7` · `LATENCY`）：批量静态契约核验耗时实测与源码轮询周期阶梯

### 1. 本地静态契约核验器：批量共享加载 vs 逐条子进程调用（7 次运行中位数，实测 `measured`）

由于单次契约核验需读取并计算 87 个引用源文件的 Git blob SHA-1 与行号表，在本地 Windows ARM64（CPython 3.12.10）上对 `1 / 3 / 6 / 12` 组契约检验问题各运行 7 次取中位数，**单进程批量共享内存索引（Batched）相比逐条启动子进程核验（One by one）在 12 题规模下提速 13.5 倍（`137 ms` vs `1,848 ms`）**：

| 契约检验问题组数 | 批量核验中位数 ms（Batched） | 逐条核验实测中位数 ms（One by one） | 批量相对耗时比 | 重复运行次数 |
|---:|---:|---:|---:|---:|
| `1` | `159` | `173` | `0.92x` | `7` |
| `3` | `155` | `423` | `0.37x` | `7` |
| `6` | `239` | `1566` | `0.15x` | `7` |
| `12` | `137` | `1848` | `0.07x`（13.5x faster） | `7` |

### 2. 上游源码定义的运行期缓存与轮询周期阶梯（`source_fact`，未运行真实轮询）

| 计时器 / 缓存窗口名称 | 源码配置毫秒数（秒） | 触发条件与设计作用 | 源码位置 |
|---|---:|---|---|
| Claude 用量探测缓存窗口 | `15,000 ms`（`15 s`） | 15 秒内复用正常配额探测结果，避免重复调用 `/api/oauth/usage` | `bin/omarchy-agent-usage-claude:372-377` (`E4-37`) |
| 本地会话日志扫描缓存窗口 | `20,000 ms`（`20 s`） | 20 秒内且最新日志文件 mtime 未变时跳过 `~/.claude/projects` / `~/.codex` 全量扫描 | `bin/omarchy-agent-usage-claude:636-652`, `usage-codex:495-511` (`E4-44`, `E4-48`) |
| 桌面面板 `retryAdvised` 快速重试 | `30,000 ms`（`30 s`） | 任一已配置 provider 返回 `retryAdvised=true` 时，定时器缩短至 30 秒重试 | `shell/plugins/agents/Main.qml:43-50,247` (`E4-78`) |
| Grok 速率限制探测缓存窗口 | `60,000 ms`（`60 s`） | 60 秒内复用 `grok.com/rest/rate-limits` 的 `DEFAULT` / `FAST` / `EXPERT` / `HEAVY` 窗口数据 | `bin/omarchy-agent-usage-grok:153-168` (`E4-55`) |
| 临近上限（`>=80%`）快速轮询 | `180,000 ms`（`180 s`） | 任一主窗口使用率达到 80% 时，后台刷新间隔从 15 分钟缩短为 3 分钟 | `shell/plugins/agents/Main.qml:46,247` (`E4-78`) |
| 默认后台轮询 / `limits-only` 缓存 | `900,000 ms`（`900 s`） | 正常状态下每 15 分钟刷新一次；Claude `--limits-only` 模式缓存上限同为 900 秒 | `shell/plugins/agents/Main.qml:45,247`, `usage-claude:618-634` (`E4-43`, `E4-78`) |

---

## Card 7（`7 / 7` · `MY TAKE`）：适用场景、禁用边界与工程复用意涵

### ✅ 适用场景（Good fit）
1. **单用户开发者桌面多 CLI 统一入口**：通过 `omarchy-agent` + `omarchy-launch-agent` 将 14 个异构 Agent CLI 统一到单一桌面快捷键、工作目录（`~/Work`）与终端 `app-id` 下。
2. **单一真源（SSOT）技能软链接分发**：以 `default/agents/skills/` 为唯一真源，通过登录/迁移幂等软链接同步到 `.agents`、`.claude`、`.codex`、`.pi/agent`、`.gemini/config` 与 `.hermes`（含多 profile）。
3. **Human-in-the-loop 系统崩溃辅助诊断**：通过 `systemd-coredump` 过滤、去重、静音与桌面通知点击门控，在人工确认后才将结构化诊断模板送入 Agent。
4. **本地多订阅配额池化与会话级环境固定**：通过 95% 阈值自动切换与 `OMARCHY_AGENT_<PROVIDER>_HOME` 环境变量锁，使新会话自动避开耗尽账户且不干扰运行中会话。
5. **无头契约测试与图形 VM 验收分层**：将毫秒级无头 shell 单元测试（`test/all`）与需要完整桌面会话的 `test/acceptance` 显式分离。

### ⛔ 不适用场景（Not for）
1. **多租户或零信任强隔离环境**：`omarchy-agent` 不提供容器、namespace 或 VM 级强沙箱，不能替代企业级执行沙箱。
2. **将目录切换或提示词约定当作安全边界**：`cd ~/Work`、`--yolo` / `--allow-all` 默认参数以及 `SKILL.md` 中的“修改前请确认”均属于软约束，不能替代确定性策略引擎。
3. **将本地估算或非公开 Web 接口当作权威财务账单**：本地 transcript 扫描与 OAuth/cookie 速率接口仅供桌面状态指示，不具备财务对账精度与 SLA 保证。
4. **假设所有可启动 CLI 均自动加载软链接技能**：14 个可启动 harness 中有 8 个在 `omarchy-provision-user` 中无专用技能软链接目录，软链接存在不等于运行时已生效。
