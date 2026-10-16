# AI 工具兼容性矩阵

> **核验时间：2026-10-16。** 各工具随时可能改默认值，尤其开关类。唯一可靠的验证方式是让 AI 复述本文件中的硬规则条数。

---

## 一、结论先行

本仓库采用**双轨适配**：

```
AGENTS.md   ← 跨工具规则单一来源（多数工具原生读取）
CLAUDE.md   ← 仅第一行 @AGENTS.md 导入 + Claude 专属说明
SKILL.md    ← Agent Skills 标准入口（name 必须 = 目录名）
```

这样做的理由：`AGENTS.md` 在 2026 Q2 由 **Agentic AI Foundation（Linux Foundation 下）** 接管，已成为跨厂商事实标准。Claude Code 是唯一需要跳板的工具。

---

## 二、兼容性矩阵

| 工具 | 读 `AGENTS.md` | 读 `CLAUDE.md` | 读 `SKILL.md` | 专属规则文件 | 备注 |
|---|---|---|---|---|---|
| **OpenAI Codex CLI** | ✅ 原生 | ❌ | — | — | 支持嵌套目录与 `AGENTS.override.md`；默认 32 KiB 上限（`project_doc_max_bytes`） |
| **Cursor** | ✅ 原生 | ❌ | — | `.cursor/rules/*.mdc` | 本仓库已放适配层 |
| **GitHub Copilot** | ✅ 原生（2025-08 后） | ❌ | `.github/copilot-instructions.md` | `.github/` | 网页版 Chat 不支持，需手动粘贴 |
| **opencode** | ✅ 原生 | ✅ 回退 | `~/.claude/skills/` | — | 无 `AGENTS.md` 时回退 `CLAUDE.md`；`OPENCODE_DISABLE_CLAUDE_CODE=1` 可关闭 |
| **Qoder / QCode** | ✅ 原生 | ❌ | — | `.qoder/rules/` | 本仓库已放适配层 |
| **ZCode（智谱）** | ✅ 原生 | ❌ | — | — | **不读 CLAUDE.md**（仅 onboarding 时一次性迁移）；不扫子目录、不展开 @import |
| **MiniMax Code（mcode）** | ✅ 原生 | ❌ | 支持 Skills | — | `mcode init .` 可生成/更新 `AGENTS.md` |
| **Trae** | ⚠️ 认但默认关 | ❌ | — | `.trae/rules/` | CLI 默认读；**桌面版需手动开**「设置 → 规则 → 将 AGENTS.md 包含在上下文中」 |
| **Claude Code** | ⚠️ 有条件 | ✅ 原生 | ✅ `~/.claude/skills/` | `.claude/rules/` | **需 v2.1.277+ 且无 `CLAUDE.local.md` 阻挡**；本仓库用 `@AGENTS.md` 导入兜底 |
| **Gemini CLI** | ❌ | ❌ | — | `GEMINI.md` | 需配 `context.fileName: AGENTS.md`，或用 `GEMINI.md` 跳板 |
| **Aider** | ❌ | ❌ | — | `.aider.conf.yml` | 需写 `read: AGENTS.md` |
| **Windsurf / Roo / Cline** | ✅ 原生 | ❌ | — | `.windsurf/` `.roo/` `.clinerules/` | — |
| **VS Code / Zed / Warp** | ✅ 原生 | ❌ | ✅ VS Code 支持 Skills | `.rules/` | VS Code 走 Customization Marketplace |
| **WorkBuddy** | ✅ 原生 | ❌ | ✅ `~/.workbuddy/skills/` | — | Skill 目录 `~/.workbuddy/skills/<name>/` |

---

## 三、安装路径

### 作为 Skill（推荐：获得完整的 10 模块 + 渐进披露）

**Claude Code**
```bash
git clone https://github.com/syxscott/academic-paper-polish.git \
  ~/.claude/skills/academic-paper-polish
```

**WorkBuddy**
```bash
git clone https://github.com/syxscott/academic-paper-polish.git \
  ~/.workbuddy/skills/academic-paper-polish
```

**opencode / ZCode / MiniMax Code / VS Code**
```bash
# 这些工具兼容 Agent Skills 目录结构
git clone https://github.com/syxscott/academic-paper-polish.git \
  ~/.config/opencode/skills/academic-paper-polish     # opencode
# ~/.zcode/skills/                                    # ZCode
# ~/.code/skills/                                     # MiniMax Code
```

> ⚠️ **目录名必须是 `academic-paper-polish`**，与 `SKILL.md` 的 `name` 字段一致。
> 不一致 → **静默加载失败**（不报错，只是不生效）。这是 Agent Skills 规范要求。

### 作为项目规则（仓库级）

```bash
git clone https://github.com/syxscott/academic-paper-polish.git
```
在工作目录使用本仓库的文件，`AGENTS.md` 会作为项目规则生效。

### 直接当 Prompt 用（零安装）

复制 `skills/academic-paper-polish/prompts/*.md` 中任意模块的内容 → 替换 `【此处粘贴你的 XXX 初稿】` → 发给任意 LLM。

---

## 四、Claude Code 的版本差异（重要）

Claude Code 读 `AGENTS.md` 的行为**随版本变化**：

| 版本 | 行为 |
|---|---|
| < v2.1.277 | ❌ 只读 `CLAUDE.md`，**不读 `AGENTS.md`** |
| ≥ v2.1.277 | ⚠️ **默认仅当没有 `CLAUDE.md` 或 `CLAUDE.local.md` 时**才直接读 `AGENTS.md` |
| ≥ v2.1.277 + `/config` 设为 `claude-md-and-agents-md` | ✅ 两者都读 |

**本仓库的应对**：`CLAUDE.md` 第一行写 `@AGENTS.md`。即使在所有版本上都能工作（官方文档明确支持 `@` 导入语法，导入最多 4 跳）。

### Claude Code 规则未加载的排查

1. 确认版本 ≥ v2.1.277
2. 检查同目录及上级目录是否有 `CLAUDE.local.md` —— **它的存在会阻止 `AGENTS.md` 直接加载**
3. `/config` → *Project instructions* → 设为 `claude-md-and-agents-md`
4. 会话内确认：`/memory` 或 `/context` 查看已加载的文件
5. 老版本可执行：`claude --print-instructions`（Codex 也有同名开关）

---

## 五、Codex 的 32 KiB 限制

Codex 累积加载 `AGENTS.md` 超过 **32 KiB** 会截断，且**离当前目录近的文件最后加载、最易被截掉**。

本仓库 `AGENTS.md` 约 5 KB，远低于限制。但如果你把它复制进大型 monorepo：

- 保持根目录 `AGENTS.md` 精简（<3 KB）
- 详细内容放 `docs/`，在 `AGENTS.md` 中引用
- 必要时在子目录加 `AGENTS.override.md`

---

## 5.5 英文用户（English users）

本仓库同时提供**中文与英文**两套 prompt，规则完全一致：

| 目录 | 语言 | 说明 |
|---|---|---|
| `skills/academic-paper-polish/prompts/` | 中文 | 10 个模块 |
| `skills/academic-paper-polish/prompts-en/` | English | 同 10 个模块，**每文件自包含** |

**英文版为何自包含**：prompt 被复制进通用 LLM（ChatGPT / Gemini / 本地模型）后，那个 LLM **拿不到本仓库的其他文件**。所以每个英文模块都内嵌了它依赖的硬规则与期刊数字，单文件即可完整工作。

**入口**：[`docs/PROMPTS-EN.md`](PROMPTS-EN.md)

**给 AI 工具的指令示例**：
```
Read skills/academic-paper-polish/prompts-en/02-introduction.md and polish my introduction per its rules: [paste draft]
```

---

## 六、验证你的环境是否正确加载

**通用方法**（唯一可靠的方式）：

```
请列出你已加载的项目规则文件，并复述其中「🔴 不可违反的内容红线」一节有几个禁止项。
```

正确加载时，AI 应能说出 **7 个禁止项**（改数据/改结论/引入未证实推测/为降重删引用/编造文献/保证过检测/复制已发表图）。

若 AI 说没读到规则，按上表对应工具排查。

---

## 七、维护本矩阵

修改工具适配层时，同步更新本文件与 `AGENTS.md` 的兼容性表格。

**判断依据优先级**：工具官方文档 > 社区实测 > 本文件。
若发现本表有过时条目，欢迎提 PR —— 请注明**核验日期与工具版本**。