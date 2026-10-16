@AGENTS.md

# CLAUDE.md

> 第一行的 `@AGENTS.md` 会把 [AGENTS.md](AGENTS.md) 导入进来 —— 那是本仓库规则的**单一来源**。
> **不要在本文件重复写规则**，否则会出现双份维护、两处内容漂移。

## Claude Code 专属说明

### 使用方式

本仓库提供两种用法，按场景选：

| 场景 | 做法 |
|---|---|
| **作为 Skill**（推荐） | 克隆到 `~/.claude/skills/academic-paper-polish/`，Claude Code 自动发现 |
| **作为项目规则** | 在论文写作项目里克隆本仓库，`AGENTS.md` 会作为项目规则生效 |

Skill 方式：
```bash
git clone https://github.com/syxscott/academic-paper-polish.git \
  ~/.claude/skills/academic-paper-polish
```

⚠️ **目录名必须是 `academic-paper-polish`** —— 与 `SKILL.md` 的 `name` 字段一致。这是 Agent Skills 规范要求，不一致会**静默加载失败**（不报错，只是不生效）。

### 渐进披露

`SKILL.md` 只放框架与八条硬规则。**不要一次读完全部 `skills/academic-paper-polish/prompts/` 和 `skills/academic-paper-polish/references/`** —— 先读 `SKILL.md`，按用户意图只读需要的模块。

### Claude Code 特有能力

| 能力 | 用法 |
|---|---|
| **子代理并行审稿** | 把 `skills/academic-paper-polish/prompts/02` `skills/academic-paper-polish/prompts/05` `skills/academic-paper-polish/prompts/06` 分给 3 个 subagent 并行审，各自独立上下文互不污染 |
| **`/config` 加载双文件** | *Project instructions* → `claude-md-and-agents-md`，可同时读 `CLAUDE.md` 与 `AGENTS.md` |
| **Skills 更新后需重启** | `SKILL.md` 改动后需重启会话才会重新加载 |
| **`$CLAUDE_SKILL_DIR`** | 在 `scripts/` 中用此变量写可移植路径 |

### 常见问题

| 现象 | 原因 | 解决 |
|---|---|---|
| Skill 不被发现 | 目录名 ≠ SKILL.md 的 `name` | 重命名为 `academic-paper-polish` |
| 规则未加载 | 同目录存在 `CLAUDE.local.md`，阻止 `AGENTS.md` 直接加载 | `/config` 设为 `claude-md-and-agents-md` |
| 规则未加载 | Claude Code < v2.1.277 | 保留 `CLAUDE.md` 的 `@AGENTS.md` 导入（本仓库已配好） |
| 看不到具体模块 | 直接读 SKILL.md 会只看到框架 | 明确读 `skills/academic-paper-polish/prompts/01-abstract.md` 等具体文件 |

---

**完整规则见 [AGENTS.md](AGENTS.md)。**