# E2 · Skill 源、目标与阅读层次

## 部署清单

固定树与全部文件阅读对应 `E2-02`–`E2-13`；下面列出完整同目录参考文件，不虚构 `references/` 子目录。

| 目录 | 主文件 | 同目录参考文件 |
|---|---|---|
| `default/agents/skills/omarchy/` | `SKILL.md` | `hyprland.md`、`plugins.md`、`theming.md`、`hooks.md`、`capture.md`、`contributing.md` |
| `default/agents/skills/omarchy-app/` | `SKILL.md` | `templates.md` |
| `default/agents/skills/diagnose-crash/` | `SKILL.md` | `reporting.md` |

源目录身份与各 blob 长度/hash 见[source index](source-index.md)及[evidence.json](../evidence.json)。

## 六个根目标及 profiles

每个目标 `<skill-name>` 都链接到 `$OMARCHY_PATH/default/agents/skills/<skill-name>`，不是复制正文。

| 目标目录 | 源码保证 | 尚不保证 |
|---|---|---|
| `~/.agents/skills` | 为三个源目录建立 link | 所有 harness 发现它 |
| `~/.claude/skills` | 同上 | 实际安装版本加载它；自定义配置 home 的行为 |
| `~/.codex/skills` | 同上 | 实际安装版本 discovery、session reload |
| `~/.pi/agent/skills` | 同上 | Pi/OMP 的全部版本都兼容 |
| `~/.gemini/config/skills` | 同上 | agy 与旧 Gemini 语义完全相同 |
| `~/.hermes/skills` | 同上 | 任意 profile 自动继承默认 skill |
| `~/.hermes/profiles/*/skills` | 仅已有 profile，先确认目录存在，再建立 link | 不存在的 profile 被创建，未来 profile 自动接入 |

证据：[provision-user:84–104](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-provision-user#L84-L104)，`E2-01`。

## 更新路径

| 迁移 | 作用与限度 | 证据 |
|---|---|---|
| `1786098807.sh` | relink omarchy 到 .agents/.claude/.codex/.pi 四处 | E2-14 |
| `1786539345.sh` | diagnose-crash 同四处，另启用 watcher；TTY 有 wants-symlink fallback | E2-15 |
| `1786719479.sh` | Gemini 默认名迁到 agy；全部 skills 链接到 .gemini/config | E2-16 |
| `1787843905.sh` | 默认 Hermes 与已有 profiles；source 不存在则退出 | E2-17 |
| `1790702606.sh` | omarchy-app 六处与已有 profiles；保留非 link 的用户同名 skill | E2-18 |

Hermes migration test 检查默认目录和已有 profile 的幂等，source 缺失时不得创建 `.hermes`。它不是 harness discovery test。证据：[test:7–75](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/hermes-skills-migration-test.sh#L7-L75)，`T2-01`。

## 开发 guides 不是部署 skills

`AGENTS.md` 让源码贡献者按任务阅读 `agents/skills/{command-metadata,install-scripts,shell-dev,icon-font,acceptance-tests,visual-verification,migrations}.md`。这些普通 Markdown guides 没有被上述 provision loop 分发；它们的存在也不说明每份都有 harness frontmatter discovery。

`AGENTS` 把任务程序放在 agents/skills、架构 reference 放 docs、发布的 end-user 文档放 manual。`CLAUDE.md` 是 Git mode `100644` 的一行 `@AGENTS.md` 普通文件，**不是 symlink**。证据：`E5-01`、`E5-02`。

## 停止/确认边界与观察口

omarchy：用户修改与源码贡献分开，reset 前确认，禁止用户任务编辑 packaged tree。omarchy-app：任务不明先澄清，数据 originals 不改、丢弃前确认，完成需 build/test/可见效果。diagnose-crash：诊断只读、mute 需用户要求；reporting 的三个门槛是 verified Omarchy bug、用户看过并同意 exact title/body、现有 gh 已可用，不代用户安装/认证。证据：`E2-02`–`E2-05`、`E2-13`。

可选验证应分别记录 **link target → harness startup discovery → 实际 skill invocation → 行为约束是否遵守**。当前 Claude SDK 官方页面的初始化 skills 清单只是一个版本相关观察口，并有 user-invocable 条件；其白名单不限制文件仍可被 Read/Bash 读取。不能把一个目录检查或清单检查代替全链路。证据：`W3`；本轮无运行记录。
