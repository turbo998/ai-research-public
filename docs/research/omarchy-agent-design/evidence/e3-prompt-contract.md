# E3 · Prompt 与数据边界契约

**这里只描述源码模板；没有真实运行 prompt、journal 日志或崩溃输入。** 不复制完整上游提示词。

## 字段映射

| 模板位置 | 来源 | 缺省/校验 | 限度 |
|---|---|---|---|
| process | watcher 归一化后的 name，或手工第二参数 | 手工省略为 unknown | 不是原始 comm 的逐字保留 |
| PID | `COREDUMP_PID` / 手工第一参数 | 必填、数字正则；不是存活校验 | 不证明这个 PID 的 core 仍存在 |
| binary | `COREDUMP_EXE` / 第三参数 | 手工省略 unknown；watcher 缺失是 `-` | 不自动校验 executable 内容 |
| signal | `COREDUMP_SIGNAL_NAME` / 第四参数 | 同上 | 来源文本，不是重新诊断信号原因 |
| time | `coredumpctl list PID --no-pager --no-legend` 的末行前四个空格分段 | 失败/空值 unknown | 不用 journal JSON 自带 timestamp；轮转会失去时间 |
| skill path | `$OMARCHY_PATH/default/agents/skills/diagnose-crash/SKILL.md` | runtime env 前提 | 主 skill 引用 reporting 按需深入 |

证据：[agent-crash:14–52](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-crash#L14-L52)，`E3-12`。

## 模板语义

模板先表达「要知道本机一个进程为什么崩溃」，再给 process/PID/binary/signal/time 事实块，最后要求使用 diagnose-crash；若 harness 没有 skill 机制则直接读 skill files。不存在内嵌 core 数据，也没有启动前自动修复命令；用户输入、core 或日志在之后如何被模型读取/发送，由实际 harness 决定。

`cat` heredoc 的变量展开不会把变量值再次当 shell 程序执行；launcher 用数组传递结果，保留其为单个 prompt 值。**模型仍可能把其中的文本当指令，shell-safe 不等于 prompt-injection-safe。**证据：`E3-12`、`E1-M01`–`E1-M14`。

## 边界逐层说明

| 层 | 源码合约 | 不保证什么 |
|---|---|---|
| journal JSON → watcher | 数字 PID、默认已选、`_UID == UID`、basename/unknown、regex/mute/dedupe | systemd 真实事件一定符合 fixture |
| watcher → notification | name/exe/signal 为 discrete argv；typed headline/body | 同用户通知发送者可信、用户一定看到 |
| notification → exec | JSON string array，program 非空且不以 `-` 开头；常量 shell positional exec | 白名单命令、sandbox 或意图判断 |
| agent-crash → launcher | 数字 PID + 一个 prompt 参数 | core 未轮转、prompt 已去敏 |
| launcher → harness | 适配 argv，含 skill path | skill 实际被发现/调用，模型只读 |

相关精确引用：[watch:47–109](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-crash-watch#L47-L109)、[sender:118–201](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-notification-send#L118-L201)、[parse:153–177](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/shell/plugins/notifications/NotificationLogic.js#L153-L177)、[click:394–410](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/shell/plugins/notifications/Service.qml#L394-L410)、[exec helper:61–68](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/shell/Commons/Util.qml#L61-L68)。

## 可选后置验证

需要独立 Linux fake HOME 与 stub；对 option-like、空字段、空白/控制字符/引号字段分别核对完整 argv，再核对 notification click 和 prompt 字节，不用空格拼接的日志替代边界验证。真实 journal 与桌面验证另行授权，不生成真实 core，也不把附件的「VM 已验证」当结果。
