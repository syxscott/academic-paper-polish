# Changelog

本文件记录本仓库（agent skill：学术论文写作、润色、改稿与投稿）的主要变更。

## [2.3.0] — 2026-10-17

### 修复
- 🔴 **修正安装说明在嵌套布局下失效**：README「方式二」原为把整个仓库 clone 成
  `~/.claude/skills/academic-paper-polish`，重构后 SKILL.md 已下沉到
  `skills/academic-paper-polish/`，照旧安装会多套一层目录，**客户端发现不了入口、静默不生效**。
  现改为整目录拷贝 `cp -R /tmp/app/skills/academic-paper-polish <skills 目录>/`，
  并列出 Claude Code / WorkBuddy / Codex / opencode / Cursor 五个目标路径 + 一行安装验证命令。

### 改动
- `AGENTS.md` 仓库结构树重建（补 `scripts/`、`evals/`、`agents/`、两个中文 references 文件，修正缩进）
- `README.md` 仓库结构树重建，与 `AGENTS.md` 对齐
- `SKILL.md` metadata：`version` 2.0.0 → 2.3.0；字段 `source_courses` → `source_material`，
  去掉"课件"表述，与「这是 agent skill、不是课件总结」的定位一致
- `scripts/check_links.py` 消除假阳性：扫描链接前先剥离围栏代码块与行内代码
  （其中的链接语法是示例文本，不是真实链接 —— 首版 CI 就因此把文档里的
  `[x](y)` 示例误判成断链而失败）；另跳过含通配符的路径模式；
  `CHANGELOG.md` 中的行内代码路径不再按当前链接校验（变更日志按设计要记录
  "改动前"的旧路径与已删除文件），但其中的真实链接仍然校验

## [2.2.0] — 2026-10-17

### 改动
- **目录布局对齐 Agent Skills 官方规范**：`SKILL.md`、`references/`、`prompts/`、`prompts-en/` 全部移入
  `skills/academic-paper-polish/`，使 skill 自包含、支持整目录拷贝安装。
- **新增 Codex 接口声明**：`skills/academic-paper-polish/agents/openai.yaml`
  （`interface.display_name` / `short_description` / `default_prompt`）。
- **新增可执行校验脚本** `scripts/`：
  - `check_skill.py` —— 校验 frontmatter（`name` 与目录名一致、长度与字符集）、
    description 长度、正文行数上限、`references/*.md` 引用存在性。
  - `check_links.py` —— 校验根级 Markdown 本地链接可解析。
  - `check_encoding.py` —— 拦截 U+FFFD 编码损坏。
- **新增 CI**：`.github/workflows/spec-consistency.yml`，push / PR 时自动跑上述三脚本。
- **新增学术引用文件** `CITATION.cff`。
- **新增评测集** `evals/`（`evals.json` + `README.md`）。

### 内容补录（此前遗漏的图内文字）
- 学位论文写作整节：高校写作规范结构、**GB/T 7714-2015** 引用标准、CNKI 学位论文范例检索、
  **硕士同行评议评分表（A1–A5 + 规范性 20 分）**。
- Review 版式四页完整范例（Nature 栏目横幅 → 图注竖线格式 → References → back-matter 结构）。
- PPP 图表硬参数细化：**dpi 三档（照片 300 / 线条图 1000 / 混合图 500）**、面板标签规范、
  **Palaeo-3 不允许 Plates**、地图禁止政治争议边界、Graphical Abstract 最小 531×1328 px。
- 行号连续编号规则、Introduction/Discussion 禁四级标题、研究点位坐标规则。
- 时间单位精确规则：**Ma/ka/Ga vs Myr/kyr/Gyr**、>2500 Ma 用 m.y.、**cal. B.P.** 近 5 万年强制校准。
- 引用格式细节（a/b/c 区分、同姓同年加首字母）、文献三层排序算法。
- 检索实操：中英双语关键词、**「作者+主题词+期刊+年份」混合检索串**、被引次数二次查询（滚雪球）。
- 素材库方法：批注式参考库（英文原文 + 中文逐段批注）、辨证阅读笔记模板。
- **TREE 综述提案真实要求**：300–600 词 point-by-point + 10–20 篇近 2–4 年关键文献 + 与近 3 年已有综述的差异化说明。

### 规范清理
- 删除纯出处索引文件 `references/course-sources.md`
- 剥离全部幻灯片页码引用与提取过程标注，改为中性技能表述

## [2.1.0] — 2026-10-16

### 新增
- `prompts-en/`：10 个英文 prompt 模块，**每文件自包含**（单文件复制进任意 LLM 即可用，不依赖仓库其他文件）
- `docs/PROMPTS-EN.md` 重写为英文入口

### 改动
- `SKILL.md`、`AGENTS.md`、`README.md`、`COMPATIBILITY.md` 模块表改为**中英双列**

## [2.0.0] — 2026-10-16

### 新增
- 跨平台兼容层：`AGENTS.md`（单一事实源）、`CLAUDE.md`（`@AGENTS.md` shim）、
  `.cursor/rules/*.mdc`、`.qoder/rules/*.md`、`docs/COMPATIBILITY.md`
- `references/multi-journal-style-guides.md`：9 份官方 style guide 汇总
- `references/journal-constraints.md` 新增地质年代硬规则

### 修复
- 🔴 **修正 `SKILL.md` 的 `name` 与目录名不一致**（原 `paper-polish-prompts` ≠ 目录
  `academic-paper-polish`）——该不一致会导致技能**静默加载失败**

## [1.0.0] — 初始版本

- 10 个中文 prompt 模块 + 8 个 references 文件
