# AGENTS.md — Academic Paper Polish

> **本文件是本仓库的跨工具规则单一来源（single source of truth）。**
> Codex · Cursor · Copilot · opencode · Qoder · ZCode · MiniMax Code · Gemini CLI · Aider · Zed 等**原生读取**本文件。
> Claude Code 通过 `CLAUDE.md` 的 `@AGENTS.md` 导入读取（见文末兼容性说明）。

本仓库提供学术论文写作、润色、改稿与投稿的全流程 AI 辅助。**它是一套给 LLM 的规则与 prompt 资产，不是一个软件项目** —— 没有构建步骤，没有测试套件，没有依赖安装。

---

## 仓库结构

```
academic-paper-polish/
├── AGENTS.md                        # ⭐ 跨工具规则单一来源（本文件）
├── CLAUDE.md                        # Claude Code 跳板：@AGENTS.md + Claude 专属说明
├── opencode.json                    # opencode 指令注册（instructions 指向 AGENTS.md + SKILL.md）
├── README.md                        # 人类向说明：安装、方法论、FAQ
├── CHANGELOG.md                     # 版本历史
├── CITATION.cff                     # 学术引用元数据
├── LICENSE                          # MIT
├── skills/
│   └── academic-paper-polish/       # ⭐ 自包含 skill 包（整目录拷贝即可安装）
│       ├── SKILL.md                 # Agent Skills 入口（name 必须 = 目录名）
│       ├── agents/
│       │   └── openai.yaml          # Codex 界面元数据（display_name / default_prompt）
│       ├── prompts/                 # 10 个可独立调用的 prompt 模块（中文）
│       │   ├── 01-abstract.md
│       │   ├── 02-introduction.md
│       │   ├── 03-literature-review.md
│       │   ├── 04-methods.md
│       │   ├── 05-results.md
│       │   ├── 06-discussion.md
│       │   ├── 07-conclusion.md
│       │   ├── 08-deai-polish.md
│       │   ├── 09-journal-submission.md
│       │   └── 10-reviewer-response.md
│       ├── prompts-en/              # 同 10 模块英文版，每文件自包含（单文件复制进任意 LLM 即可用）
│       └── references/              # 按需加载的深度参考（progressive disclosure）
│           ├── checklist.md             # 投稿前自查清单
│           ├── journal-constraints.md   # 期刊结构硬约束
│           ├── figure-specs.md          # 图表硬参数
│           ├── color-system.md          # 配色系统与视觉编码（对照冷暖/色相编码/灰度检验）
│           ├── paleobiology-journal.md  # ★ Paleobiology 全刊规范（图件+文体+数据）
│           ├── multi-journal-style-guides.md  # ★ 9 家期刊官方 Style Guide 汇总
│           ├── literature-search.md     # 检索与素材积累
│           ├── sentence-bank.md         # 句式库
│           ├── 论文写作方法论骨架.md     # 写作方法论（引言/讨论/综述/投稿）
│           └── 格式硬参数与文献检索实操.md  # 格式参数与检索实操
├── scripts/                         # 规范一致性校验脚本
│   ├── check_skill.py               # frontmatter / name / 行数 / 引用存在性
│   ├── check_links.py               # 本地 .md 链接可达性
│   ├── check_encoding.py            # U+FFFD 编码损坏扫描
│   ├── check_markdown.py            # 全量 Markdown 结构体检（围栏/标题/表格/空白）
│   └── check_anchors.py             # README 内部锚点可达性
├── evals/                           # 评测集用例与基线
│   ├── evals.json
│   └── README.md
├── docs/
│   ├── COMPATIBILITY.md             # 各 AI 工具兼容性矩阵
│   └── PROMPTS-EN.md                # 英文版 prompt 入口
├── assets/banner.svg
├── .cursor/rules/                   # Cursor 规则（含 mdc 头）
└── .qoder/rules/                    # Qoder / QCode 规则
```

---

## AI 在本仓库中的工作方式

### 何时加载哪个模块

| 用户意图 | 中文模块 | 英文模块 |
|---|---|---|
| 润色摘要 | `skills/academic-paper-polish/prompts/01-abstract.md` | `skills/academic-paper-polish/prompts-en/01-abstract.md` |
| 润色引言 / 强化论证结构 | `skills/academic-paper-polish/prompts/02-introduction.md` | `skills/academic-paper-polish/prompts-en/02-introduction.md` |
| 组织文献综述 / review paper 结构 | `skills/academic-paper-polish/prompts/03-literature-review.md` | `skills/academic-paper-polish/prompts-en/03-literature-review.md` |
| 审查方法可复现性 | `skills/academic-paper-polish/prompts/04-methods.md` | `skills/academic-paper-polish/prompts-en/04-methods.md` |
| 检查结果与图表规范 | `skills/academic-paper-polish/prompts/05-results.md` | `skills/academic-paper-polish/prompts-en/05-results.md` |
| 深化讨论 / 提炼贡献与局限 | `skills/academic-paper-polish/prompts/06-discussion.md` | `skills/academic-paper-polish/prompts-en/06-discussion.md` |
| 写结论 | `skills/academic-paper-polish/prompts/07-conclusion.md` | `skills/academic-paper-polish/prompts-en/07-conclusion.md` |
| 终稿去 AI 化 | `skills/academic-paper-polish/prompts/08-deai-polish.md` | `skills/academic-paper-polish/prompts-en/08-deai-polish.md` |
| 选期刊 / 投稿 / Cover Letter | `skills/academic-paper-polish/prompts/09-journal-submission.md` | `skills/academic-paper-polish/prompts-en/09-journal-submission.md` |
| 回复审稿意见 | `skills/academic-paper-polish/prompts/10-reviewer-response.md` | `skills/academic-paper-polish/prompts-en/10-reviewer-response.md` |

**加载原则**：先读 `skills/academic-paper-polish/SKILL.md` 建立框架 → 按用户意图只读对应的 `skills/academic-paper-polish/prompts/*.md` → 涉及具体数字时再读 `skills/academic-paper-polish/references/*.md`。

**英文用户**：优先加载 `skills/academic-paper-polish/prompts-en/` 对应模块。它与中文版规则一致，且**自包含** —— 已内置该模块所需的硬规则与期刊数字，不需要额外读 `skills/academic-paper-polish/references/`。

**不要一次把所有文件读进上下文。** 本仓库的核心设计是渐进披露（progressive disclosure）。

### 改稿时的默认行为

1. **先问目标期刊** —— 未确认期刊时，不给结构层面的建议（因为 Results/Discussion 是否分离、有无结论段都取决于期刊）
2. **保留原意** —— 改措辞、改进结构可以；**不改数据、不改结论、不引入未经证实的推测**
3. **逐条处理** —— 用户给多个问题时按顺序处理，不合并
4. **明确改动** —— 输出时说明改了什么、为什么

---

## 🔴 不可违反的内容红线

作为学术写作助手，本仓库的规则**凌驾于"让用户满意"之上**。

| ❌ 禁止 | 原因 |
|---|---|
| 改动数据、单位、图表编号 | 学术不端 |
| 把"结论 A"改成"结论 B" | 改变科学主张 |
| 在润色中引入未经证实的推测并写成事实 | 学术不端 |
| 为降低相似度而删掉关键引用 | "知而不引"，学术不端 |
| 编造不存在的参考文献 | 学术不端 |
| 给出"保证过 AI 检测"之类的承诺 | 无法保证，且目标本身错误 |
| 建议直接复制已发表的图 | 版权违规 |

**遇到用户要求越过上述红线时**：说明风险并拒绝该部分，继续完成其余合法部分。

---

## 学术规范要点（AI 生成内容必须遵守）

### 引文密度（最易出错）

| 章节 | 要求 |
|---|---|
| Introduction | 除**问题句和过渡句**外都要有引用 |
| Results | **几乎没有**引用 |
| Discussion | **每段 5–8 句** = topic sentence + 3–4 句带引用 + 2–3 句自己数据 |
| Abstract / Conclusion | **不应出现**引用 |

### 结构

- 引言 = **倒金字塔**；opening（提出的问题）必须与 resolution（答案）对齐
- 段落 **5–8 句**最合理；1–2 句段落很差
- 讨论 **六步框架**，含"表明局限性"
- 结论含 **总结 + 亮点 + 局限性 + 未来方向**
- 综述 **18 步**：prepare(1-4) → structure(5-7) → draft(8-13) → revise(14-18)
  - 其中 **主体(11) → 结论(12) → 引言(13) → 摘要(14)**，顺序反直觉但正确

### 期刊差异（必须先确认目标期刊）

- **GCA**：Results 与 Discussion **必须分离**；不收纯方法学论文、不收 regional case studies
- **ES&T**：Results 与 Discussion **合并**；**禁用独立结论段**；限 7000 词
- **ES&T 编辑红线**：摘要语法错误 **>6 处 → 不读正文**
- ***Paleobiology***（古生物 / 化石形态学，规则最细，见 `skills/academic-paper-polish/references/paleobiology-journal.md`）：
  - 送审图须 **<40 兆像素** 才能进 PDF proof；终稿 **线条 1200 / 半调 600 / 组合 800 dpi**
  - 单栏 **9 cm** / 双栏 **18 cm** / 最大高 **24 cm**；线宽 ≥**0.3 pt**；字号 ≥**8 pt**
  - 🔴 **标本照片必须带比例尺，不可用 ×40 等放大倍数代替**（终版可能缩放）
  - 🔴 **须提供 Non-technical Summary + Abstract，各自 ≤300 词**
  - 全稿 **12 号 Times New Roman + 双倍行距**；**US Letter**；四边 1 英寸；**不用两端对齐**；**不在右边界断词**
  - 🔴 **从标题页开始编连续行号**
  - **Ga/Ma/ka = 年代；Gyr/Myr/kyr = 跨度**（混用是审稿常扣分项）
  - 🔴 **图不得嵌入正文**，作为独立文件提交；**不用图注排位（no figure call outs）**
  - 数据与代码遵循 **FAIR**；Dryad/Zenodo 由期刊全额付费；**DOI 必须最终 DOI**
  - 🔴 **Supplementary Material 的文献不计入主 Literature Cited**

### 措辞

- ❌ *for the first time* / "首次提出" / "国际先进水平"
- ❌ 直接点名批评前人（*The deficiency of Wang's approach is…*）
- ✅ *However, the mechanism has not been fully understood.*

---

## 维护约定

- **`skills/academic-paper-polish/SKILL.md` 的 `name` 必须等于其父目录名**（`academic-paper-polish`），否则违反 Agent Skills 规范，会**静默加载失败**
- **SKILL.md 正文控制在 500 行以内**，详细内容下沉到 `skills/academic-paper-polish/prompts/` 和 `skills/academic-paper-polish/references/`
- **改动后跑一遍全部校验**（与 CI 同一套，缺一不可）：
  ```bash
  python3 scripts/check_skill.py --strict   # Agent Skills 规范
  python3 scripts/check_links.py            # 本地链接
  python3 scripts/check_encoding.py         # U+FFFD
  python3 scripts/check_markdown.py         # ★ 全量 md 结构体检（含表格列数）
  python3 scripts/check_anchors.py README.md # 内部锚点
  ```
- **修改 prompt 时同步更新** `README.md` 的模块表与 `docs/PROMPTS-EN.md`（如有对应条目）
- **引用规则或数字时标注出处**（来自哪份资料、哪一条），便于核验
- 保持**中文为主、关键术语中英并列**的现状；英文版单独放 `docs/`

### 内容来源（修改时可回查）

| 来源 | 提供什么 |
|---|---|
| 写作方法论骨架 | 引言倒金字塔、Results/Discussion 期刊差异、讨论六步、综述 18 步、ACCEPTANCE 十点 |
| 格式硬参数与文献检索 | 引文密度表、图表硬参数、送审三段流程、6–8 周时间预算、检索工具 |


---

## 🔴 修改仓库结构时的注意事项

- **不要删除 `AGENTS.md`** —— 它是多数工具的唯一规则入口
- **不要把 `CLAUDE.md` 做成内容副本** —— 它应只有 `@AGENTS.md` 一行 + Claude 专属说明，否则会产生双份维护
- **新增 prompt 模块时**，同步更新六处：`skills/academic-paper-polish/SKILL.md` 模块索引（中英双列） · `README.md` 模块表 · `AGENTS.md` 加载表 · `docs/PROMPTS-EN.md` · 对应的 `skills/academic-paper-polish/prompts-en/` 英文文件 · `evals/evals.json` 补一条用例
- **中英双语维护原则**：`skills/academic-paper-polish/prompts/` 与 `skills/academic-paper-polish/prompts-en/` 是**同一套规则的两种语言**，改一边必须同步另一边。英文版必须**自包含**（内嵌硬规则），因为单文件会被复制进通用 LLM，拿不到仓库其他文件
- **写中文长文档后**，用脚本扫一遍编码替换字符（`re.finditer('\ufffd')`），中文标点与全角字符容易在此环节损坏
- 🔴 **用脚本批量替换 Markdown 代码块时，正则绝不能带 `re.S` 跨越大段内容**。
  本仓库曾因此把「十模块」表尾与整个「八条硬规则」章节误删、并使围栏数变奇数
  （代码块提前闭合、整页渲染错乱），且损坏随 push 进了 main。
  **规避**：① 替换前后用 `grep -c '^```'` 比对围栏数，奇数即结构损坏；
  ② 用 `(?ms)^```\n<锚点开头>.*?^```$` 这类**首尾都锚定**的模式，不要只锚开头；
  ③ 改完立刻 `git diff` 核对行数与章节序列；
  ④ 跑 `python3 scripts/check_markdown.py` —— 它对**全部** md 文件做结构体检。
- 🔴 **`check_markdown.py` 的表格检查必须保留「表头门控」**：
  即 `lines[i].startswith("|")` **且** 次行为分隔行（`^\|[\s\-:|]+\|$`）。
  早期版本缺门控且因缩进错误整段不可达；把逻辑单独抽出实测时，
  在 31 个真表格上产生 **210 行假阳性**，把真问题淹没。
  **仅删除 `continue` 是错的** —— 必须同时加门控。
  同理，管道符计数须忽略行内代码与 `\|` 转义。

---

## 各工具读取本仓库规则的方式

| 工具 | 读取的文件 | 备注 |
|---|---|---|
| **Codex CLI** | `AGENTS.md` | 原生；支持嵌套与 `AGENTS.override.md`；默认上限 32 KiB |
| **Cursor** | `AGENTS.md` + `.cursor/rules/*.mdc` | 原生 |
| **GitHub Copilot** | `AGENTS.md` | 2025-08 后版本原生 |
| **opencode** | `AGENTS.md` | 原生；无则回退 `CLAUDE.md` |
| **Qoder / QCode** | `AGENTS.md` + `.qoder/rules/` | 原生 |
| **ZCode（智谱）** | `AGENTS.md` | 原生；**不读 CLAUDE.md** |
| **MiniMax Code（mcode）** | `AGENTS.md` | 原生；`mcode init .` 可生成 |
| **Gemini CLI** | 不原生读 | 需配 `context.fileName` |
| **Aider** | 不原生读 | 需在 `.aider.conf.yml` 写 `read: AGENTS.md` |
| **Claude Code** | `CLAUDE.md` → 导入 `AGENTS.md` | 见下 |

**给使用 Claude Code 的用户**：`CLAUDE.md` 的第一行是 `@AGENTS.md`，会导入本文件。若 Claude Code **没有**加载到本文件的规则，检查是否存在同目录的 `CLAUDE.local.md`（它会阻止 `AGENTS.md` 直接加载），或在 `/config` 把 *Project instructions* 设为 `claude-md-and-agents-md`。

完整矩阵与安装路径见 `docs/COMPATIBILITY.md`。