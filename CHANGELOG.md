# Changelog

本文件记录本仓库（agent skill：学术论文写作、润色、改稿与投稿）的主要变更。

## [2.3.2] — 2026-10-17

### 新增
- **`opencode.json`** —— 对齐同类仓库做法，把 `AGENTS.md` 与 `skills/academic-paper-polish/SKILL.md`
  注册进 `instructions`。此前 README 只教用户「自己写一个」，仓库本身并没有该文件，
  是当初借鉴清单里唯一漏落地的一项。

### 文档
- README「方式四」改为「仓库已自带 opencode.json」，并说明已有配置时如何合并
- `docs/COMPATIBILITY.md` opencode 行的「专属规则文件」列补上 `opencode.json`
- `AGENTS.md` 仓库结构树补 `opencode.json`

### 核查结论（未改动）
逐条复核借鉴清单 6 项，全部已落地；另核实两项曾被我误判为「差距」的：
- **description 437 字符不算冗余** —— 官方 Agent Skills 规范明确鼓励 description
  包含具体关键词以帮助 agent 识别任务，本 skill 含 160 字符触发词，符合推荐做法。
- **`check_skill.py` 已完整覆盖 name 全部约束** —— 实测 7 个样本（含 `-pdf`、`pdf-`、
  `pdf--processing`、`PDF-Processing` 等官方明令非法者）全部正确拒绝。

## [2.3.1] — 2026-10-17

### 🔴 修复
- **README 整段内容丢失**：先前用脚本重建「仓库结构」代码块时，正则跨度过大，
  把从树开头到下一个围栏之间的内容一并替换掉，导致
  「🧩 十模块」模块表尾与整个「🔴 八条硬规则」章节（1️⃣–5️⃣）被误删，
  并使围栏数变成奇数（21）→「讨论六步」代码块被提前闭合、后续内容渲染错乱。
  已从损坏前的提交取回原文并更新其中路径，现围栏 22 个全部配对。
  ⚠️ 该损坏曾随 `bcb542d` 推送到 GitHub。

### 新增
- `scripts/check_markdown.py` —— Markdown 结构体检：围栏配对、`<details>` 配对、
  标题层级跳级、表格列数一致性（均跳过代码块内部，避免把 `# shell 注释` 当标题）。
- `scripts/check_anchors.py` —— 校验 README 内部锚点是否指向真实标题
  （按 GitHub slug 规则生成锚点集合）。
- CI 增跑上述两项，README 结构问题今后不会再漏到 main。

### 修复
- **README 顶部导航锚点全部失效**：GitHub 对 emoji 是删除后留下其后的空格转为的连字符，
  正确锚点形如 `#快速开始-quick-start`（无前导连字符），
  原写作 `#-快速开始-quick-start` 双连字符 → 六个链接全部点不动。已按实测规则改正。
- 补全顶部导航遗漏的两节（`🔴 八条硬规则`、`📐 技术检查卡口`）；
  移除不存在的 `#-安装-install`（无对应标题）。

### 内容校正（与仓库实际状态对齐）
- 版本号徽章 `v2.0.0` → `v2.3.0`（原与 SKILL.md 的 version 不一致）
- 「6 份深度参考」→ **9 份**（实际 references 为 9 个文件）
- 「11 个 AI 工具」→ **10 个**（兼容性表实际 10 条；Codex/Cursor/Copilot/opencode/
  Qoder/ZCode/MiniMax Code/Gemini CLI/Aider/Claude Code），徽章同步改为 `10_AI_Tools`
- 正文与 FAQ 中的「v2.0」表述改为「v2.x」，避免每次升版都要改

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
