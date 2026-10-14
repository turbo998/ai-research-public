# E1 · 全 harness 启动矩阵

**源码推导，不是运行日志。** 由固定版本 `bin/omarchy-agent:57–132` 的全部 14 个 case 生成；`P` 表示一个非空 prompt 参数，不是可执行 shell 字符串。下面写法为 argv 的易读表示，未建议执行。

| Harness | 无 prompt 的 argv | 有 prompt 的 argv | 分支证据 |
|---|---|---|---|
| opencode | `opencode --auto` | `opencode --auto --prompt P` | E1-M01 · [57–60](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L57-L60) |
| agy | `agy --dangerously-skip-permissions` | `agy --dangerously-skip-permissions --prompt-interactive P` | E1-M02 · [61–64](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L61-L64) |
| copilot | `copilot --allow-all` | `copilot --allow-all --interactive P` | E1-M03 · [65–68](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L65-L68) |
| crush | `crush --yolo` | `crush run P` | E1-M04 · [69–76](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L69-L76) |
| claude | `claude --permission-mode auto` | `claude --permission-mode auto -- P` | E1-M05 · [77–80](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L77-L80) |
| grok | `grok --permission-mode bypassPermissions` | `grok --permission-mode bypassPermissions -- P` | E1-M06 · [81–84](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L81-L84) |
| openclaw | `omarchy-launch-openclaw --tui` | `omarchy-launch-openclaw --tui --message P` | E1-M07 · [85–93](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L85-L93) |
| codex | `codex --approve-for-me` | `codex --approve-for-me -- P` | E1-M08 · [94–97](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L94-L97) |
| cursor-agent | `cursor-agent --yolo --trust` | `cursor-agent --yolo --trust agent -- P` | E1-M09 · [98–105](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L98-L105) |
| hermes | `hermes --yolo` | `env -u HERMES_SESSION_SOURCE hermes chat --yolo --tui --query=P` | E1-M10 · [106–112](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L106-L112) |
| muse | `muse --approval-mode never` | `muse --approval-mode never -- P` | E1-M11 · [113–117](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L113-L117) |
| omp | `omp --auto-approve` | `omp --auto-approve -- P` | E1-M12 · [118–121](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L118-L121) |
| ori | `ori code` | `ori code --interactive --prompt P` | E1-M13 · [122–128](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L122-L128) |
| pi | `pi` | `pi P` | E1-M14 · [129–132](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L129-L132) |

## 环境及执行外壳

| 范围 | argv/env 规则 | 证据 |
|---|---|---|
| Claude | `CLAUDE_CONFIG_DIR`；pin `OMARCHY_AGENT_CLAUDE_HOME` | E1-11 |
| Codex | `CODEX_HOME`；pin `OMARCHY_AGENT_CODEX_HOME` | E1-11 |
| Grok | `GROK_HOME`；pin `OMARCHY_AGENT_GROK_HOME` | E1-11 |
| 上述三者重选时 | 前置 `env -u HOME_VAR PIN=selected_home`；home 非空再添加 `HOME_VAR=selected_home` | [139–160](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L139-L160) |
| 上述三者显式 override | 不覆盖与父 pin 不同的非空 home；不额外添加新 pin | E1-11 |
| Hermes prompted | 清除 `HERMES_SESSION_SOURCE`，query 是一个含 `=` 的参数 | E1-M10 |
| 其余 harness | 本 launcher 不加 provider-specific home/pin；不代表其本身没有身份配置 | E1-11 |
| 所有 harness | inline 直接 exec；否则统一 `org.omarchy.agent` app-id | [162–168](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L162-L168) |
| HOME 启动 | Work 已存在时才改变目录 | [34–38](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L34-L38) |

`HOME_VAR` 是 provider 配置目录变量，不是改进程的 `$HOME`。账户 dispatch 的 session pin 见[E4 状态契约](e4-state-contracts.md)。

## 安装与 lifecycle 分类

默认选择中 pi/opencode/claude/codex/grok/copilot/crush/cursor-agent 的默认 mise package 名与命令名相同；agy 使用 `antigravity-cli`，omp 使用 `github:can1357/oh-my-pi`，ori 使用 `github:OpenRouterLabs/ori-releases`，muse 使用显式 HTTP launcher backend。Cursor/Muse 等用户已有可执行安装保留规则由 selector 和 provision 分别处理。Hermes/OpenClaw 调专用 installer，不能写成 mise package。证据：`E1-04`、`E1-07`。

OpenClaw 的最后 argv 是 `openclaw tui [--message P]`，但它之前还有配置、onboarding、gateway service 恢复及 readiness 验证；见[E1 lifecycle 图](../findings/01-launcher.md)。`--check` 会探测 runtime，**不是本研究允许执行的纯文件检查**。

## 错误与证据边界

意外参数、prompt 缺值、默认未设置、缺少 binary、不支持默认、安装失败、gateway 无响应分别保留错误分支，不用另一 agent 静默兜底。测试中的 argv 断言是未运行测试契约。以上 flag 只确认传参，不声称各 harness 的 auto/yolo 权限、sandbox 或 skill 发现等价；尤其 Muse 注释称保留 sandbox，尚无匹配安装版本的验证。
