<div align="center">

<img src="assets/banner.svg" alt="Academic Paper Polish Banner" width="900" />

<br/>

### *让 AI 像资深同行评审一样打磨你的论文*

<br/>

<img src="https://img.shields.io/badge/📜_MIT_License-22c55e?style=social&logo=opensourceinitiative" alt="MIT" />
<img src="https://img.shields.io/badge/🧩_10_Modules-8b5cf6?style=social&logo=bookstack" alt="Modules" />
<img src="https://img.shields.io/badge/📚_10_References-0ea5e9?style=social&logo=readthedocs" alt="References" />
<img src="https://img.shields.io/badge/🌐_中文-ef4444?style=social&logo=googletranslate" alt="中文" />
<img src="https://img.shields.io/badge/🪄_12_AI_Tools-3b82f6?style=social&logo=anthropic" alt="AI Tools" />
<img src="https://img.shields.io/badge/🏷️_v2.4.1-fbbf24?style=social&logo=github" alt="v2.4.1" />

<br/>

<img src="https://img.shields.io/github/stars/syxscott/academic-paper-polish?style=social&logo=github&color=22c55e" alt="Stars" />
<img src="https://img.shields.io/github/forks/syxscott/academic-paper-polish?style=social&logo=github&color=8b5cf6" alt="Forks" />
<img src="https://img.shields.io/github/watchers/syxscott/academic-paper-polish?style=social&logo=github&color=3b82f6" alt="Watchers" />
<img src="https://img.shields.io/github/issues/syxscott/academic-paper-polish?style=social&logo=github&color=ef4444" alt="Issues" />

<br/><br/>

[🎯 TL;DR](#tldr) ·
[📂 仓库结构](#仓库结构-repo-layout) ·
[🧩 十模块](#十模块-modules) ·
[🔴 八条硬规则](#八条硬规则) ·
[🎨 配色系统](#配色系统-new) ·
[📐 检查卡口](#技术检查卡口) ·
[🚀 快速开始](#快速开始-quick-start) ·
[🪄 兼容性](#ai-工具兼容性) ·
[🗺️ 流程图](#写作流程-workflow) ·
[❓ FAQ](#faq)

</div>

<br/>

---

## 🎯 TL;DR

> **不是模板，不是填空，是给 LLM 的精准角色定义 + 输入约束 + 输出规范。**

**10 个模块 + 10 份深度参考 + 12 个 AI 工具适配 + 6 个 CI 校验脚本。**
覆盖从选题到返修的完整链路 —— 从「怎么写」到「怎么投」。

| | v1.0 | **v2.4** |
|---|---|---|
| 模块 | 8 | **10**（+ 期刊匹配与投稿、审稿意见回复） |
| 深度参考 | 无 | **10 份**（期刊约束 / 图表参数 / **配色系统** / 检索 / 句式库 / 自查清单 / 多刊 style guide / Paleobiology 全刊规范 / 写作方法论 / 格式与检索实操） |
| AI 工具 | 主要 Claude Code / Cursor | **12 个**，`AGENTS.md` 单轨 + `CLAUDE.md` 跳板 |
| CI 校验 | 无 | **6 个脚本**，含全量 Markdown 结构体检 |
| 硬规则 | 部分 | **八条**，全部标注出处 |

**内容定位**：地学 SCI 论文与学位论文的写作、改稿、投稿与返修方法库。
**地学 / 地质 / 环境 / 古生物方向规则最完整** —— 期刊硬约束、图件参数、地层术语规范、
配色决策逻辑均来自地学写作课并已通用化。非地学学科替换名词即可用。

---

## 📂 仓库结构 Repo Layout

```
academic-paper-polish/
├── AGENTS.md                        # ⭐ 跨工具规则单一来源（Codex/Cursor/opencode/ZCode…）
├── CLAUDE.md                        # Claude Code 跳板：@AGENTS.md
├── opencode.json                    # opencode 指令注册
├── README.md                        # 📖 你正在读的文件
├── CHANGELOG.md                     # 版本变更
├── CITATION.cff                     # 学术引用元数据
├── LICENSE                          # MIT
├── skills/
│   └── academic-paper-polish/       # ⭐ 自包含 skill 包（整目录拷贝即可安装）
│       ├── SKILL.md                 # Agent Skills 入口（name 必须 = 目录名）
│       ├── agents/
│       │   └── openai.yaml          # Codex 接口声明
│       ├── prompts/                 # 10 个可独立调用的 prompt 模块（中文）
│       │   ├── 01-abstract.md       # 📝 摘要
│       │   ├── 02-introduction.md   # 🔭 引言
│       │   ├── 03-literature-review.md  # 📚 文献综述
│       │   ├── 04-methods.md        # 🧪 研究方法
│       │   ├── 05-results.md        # 📊 结果
│       │   ├── 06-discussion.md     # 💡 讨论
│       │   ├── 07-conclusion.md     # 🎯 结论
│       │   ├── 08-deai-polish.md    # 🤖 降低 AI 率
│       │   ├── 09-journal-submission.md  # 🎯 期刊匹配与投稿
│       │   └── 10-reviewer-response.md    # 💬 审稿意见回复
│       ├── prompts-en/              # 同 10 模块英文版，每文件自包含
│       └── references/              # 按需加载的深度参考（10 份）
│           ├── checklist.md              # 投稿前自查清单（A–J 十组）
│           ├── journal-constraints.md    # 期刊结构硬约束
│           ├── figure-specs.md           # 图表硬参数 + 构图
│           ├── color-system.md           # 🎨 配色系统与视觉编码
│           ├── paleobiology-journal.md   # ★ Paleobiology 全刊规范
│           ├── multi-journal-style-guides.md  # ★ 9 家期刊官方 Style Guide
│           ├── literature-search.md      # 检索与素材积累
│           ├── sentence-bank.md          # 句式库
│           ├── 论文写作方法论骨架.md       # 写作方法论（引言/讨论/综述/投稿）
│           └── 格式硬参数与文献检索实操.md  # 格式参数与检索实操
├── scripts/                         # 规范一致性校验脚本（CI 全跑）
│   ├── check_skill.py               # frontmatter / name / 行数 / 引用存在性
│   ├── check_links.py               # 本地 Markdown 链接可达性
│   ├── check_encoding.py            # U+FFFD 编码损坏扫描
│   ├── check_markdown.py            # 围栏配对 / 标题层级（根级 6 文件）
│   ├── check_anchors.py             # README 内部锚点可达性
│   └── check_md_full.py             # ★ 全量 Markdown 结构体检（全部 39 文件）
├── evals/                           # 评测集用例与基线
│   ├── evals.json
│   └── README.md
├── docs/
│   ├── COMPATIBILITY.md             # 各 AI 工具兼容性矩阵
│   └── PROMPTS-EN.md                # 英文版 prompt 入口
├── assets/banner.svg
├── .github/workflows/
│   └── spec-consistency.yml         # push / PR 自动跑全部 6 个脚本
├── .cursor/rules/                   # Cursor 规则（含 mdc 头）
└── .qoder/rules/                    # Qoder / QCode 规则
```

---

## 🧩 十模块 Modules

> 推荐顺序：`🎯 期刊匹配(9) → ✍️ 写/润色正文(2–7) → 💬 返修回复(10) → 🤖 终稿去 AI 化(8)`

| # | 模块 Module | 一句话定位 Tagline | 中文 | English |
|---|---|---|---|---|
| 1 | 📝 **摘要** Abstract | 把整篇论文压缩进 300 词 | [`prompts/01-abstract.md`](skills/academic-paper-polish/prompts/01-abstract.md) | [`prompts-en/01`](skills/academic-paper-polish/prompts-en/01-abstract.md) |
| 2 | 🔭 **引言** Introduction | 倒金字塔 · 缺口 · 问题 · 路线图 | [`prompts/02-introduction.md`](skills/academic-paper-polish/prompts/02-introduction.md) | [`prompts-en/02`](skills/academic-paper-polish/prompts-en/02-introduction.md) |
| 3 | 📚 **文献综述** Lit Review | 让文献"对话"而非罗列 | [`prompts/03-literature-review.md`](skills/academic-paper-polish/prompts/03-literature-review.md) | [`prompts-en/03`](skills/academic-paper-polish/prompts-en/03-literature-review.md) |
| 4 | 🧪 **研究方法** Methods | 经得起同行复现的细节度 | [`prompts/04-methods.md`](skills/academic-paper-polish/prompts/04-methods.md) | [`prompts-en/04`](skills/academic-paper-polish/prompts-en/04-methods.md) |
| 5 | 📊 **结果** Results | 只讲"发现了什么"，不解释"为什么" | [`prompts/05-results.md`](skills/academic-paper-polish/prompts/05-results.md) | [`prompts-en/05`](skills/academic-paper-polish/prompts-en/05-results.md) |
| 6 | 💡 **讨论** Discussion | 结果 ↔ 文献 ↔ 理论 ↔ 实践 | [`prompts/06-discussion.md`](skills/academic-paper-polish/prompts/06-discussion.md) | [`prompts-en/06`](skills/academic-paper-polish/prompts-en/06-discussion.md) |
| 7 | 🎯 **结论** Conclusion | 升华，但不引入新信息 | [`prompts/07-conclusion.md`](skills/academic-paper-polish/prompts/07-conclusion.md) | [`prompts-en/07`](skills/academic-paper-polish/prompts-en/07-conclusion.md) |
| 8 | 🤖 **降低 AI 率** De-AI Polish | 终稿通篇去 AI 化润色 | [`prompts/08-deai-polish.md`](skills/academic-paper-polish/prompts/08-deai-polish.md) | [`prompts-en/08`](skills/academic-paper-polish/prompts-en/08-deai-polish.md) |
| 9 | 🎯 **期刊匹配与投稿** | 🔴 先定期刊，再动笔 | [`prompts/09-journal-submission.md`](skills/academic-paper-polish/prompts/09-journal-submission.md) | [`prompts-en/09`](skills/academic-paper-polish/prompts-en/09-journal-submission.md) |
| 10 | 💬 **审稿意见回复** | 逐条答复的四要素 | [`prompts/10-reviewer-response.md`](skills/academic-paper-polish/prompts/10-reviewer-response.md) | [`prompts-en/10`](skills/academic-paper-polish/prompts-en/10-reviewer-response.md) |

> 🌍 **English users**: read the `skills/academic-paper-polish/prompts-en/` module directly.
> Each file is **self-contained** — copy one file into any LLM (ChatGPT, Claude, Gemini) and it works,
> no need to read `references/` first. English entry point: [`docs/PROMPTS-EN.md`](docs/PROMPTS-EN.md).

---

## 🔴 八条硬规则

### 1️⃣ 先定期刊，再动笔

**这不是流程形式，它决定后面所有结构决策。**

| 期刊 | Results/Discussion | 结论段 / 关键约束 |
|---|---|---|
| **GCA** | 🔴 **必须分离**，各自独立编号 | 允许；❌ 不收纯方法学论文、不收 regional case studies |
| **ES&T** | 🔴 **合并**为 Results and Discussion | ❌ *"A separate conclusion is not to be used"*；限 **7,000 词** |
| **PPP** | — | Articles **5000–7000 词 / 4–8 图**；图单栏 **<85 mm** / 双栏 **<180 mm** |
| ***Paleobiology*** | — | 🔴 须另加 **Non-technical Summary ≤300 词**；送审图 **<40 MP**；终稿 **1200/800/600 dpi** |
| **APP** | — | 单栏 **89 mm** / 双栏 **183 mm** / 最大长 **237 mm**；**Calibri 8 pt**；🔴 **ZooBank 强制注册** |
| **Palaeontologia Electronica** | — | 🔴 **无页限、无版面费**；**300 ppi，RGB 不用 CMYK**；🔴 文件名 **ISO 9660**（≤8 字符） |

> 🔴 **格式不过关 → 直接拒稿，走不到学术编辑和审稿人那一步。**
> 原因：① 第一印象 ② 基本学术素养 ③ 评审是挑错过程 ④ **格式意见往往比内容意见多**

📖 完整 9 家期刊对照见 [`skills/academic-paper-polish/references/multi-journal-style-guides.md`](skills/academic-paper-polish/references/multi-journal-style-guides.md)

### 2️⃣ 引言 = 倒金字塔，opening 必须与 resolution 对齐

| 图形 | 英文 | 后果 |
|---|---|---|
| 开口 > 收口 | *overpromising* | 读者觉得被欺骗 |
| **开口 = 收口** | ***on target*** | ✅ **读者认可** |
| 收口 > 开口 | *underpromising* | 读者看不到值得关注的 story |

### 3️⃣ 引文密度（最易自查）

| 章节 | 要求 |
|---|---|
| **Introduction** | 除**问题句和过渡句**外都要有引用 |
| **Results** | **几乎没有**引用 |
| **Discussion** | **每段 5–8 句** = topic sentence + **3–4 句带引用** + **2–3 句自己数据** |
| **Abstract / Conclusion** | **不应出现**引用 |

### 4️⃣ 段落 5–8 句最合理

**1–2 句话的段落是非常差的结构。** 换了对象主体就分段。

### 5️⃣ 讨论必须走完六步（含"局限性"）

```
① 引言空白 → ② 重述发现(用数据/图) → ③ 解释并比较
→ ④ 表明局限性 → ⑤ 未来启示 → ⑥ 结论
```

**第 ④ 步最常被跳过，但它恰恰是审稿人判断作者是否诚实的关键。**

### 6️⃣ 结论要含"局限性 + 未来方向"

```
Despite its advantages, the [方法名] also has some limitations.
First, [限制1]. Second, [限制2].
Further research should focus on [方向].
```

### 7️⃣ 参考文献五误区

**知而不引 · 断章取义 · 引而不确 · 来源不实 · 盲目自引**

综述约 **100 篇**是质量标志；优先近 5 年（最好 1–3 年）、优先一次文献。

### 8️⃣ 地质年代：Ga/Ma/ka ≠ Gyr/Myr/kyr

| | 表示什么 |
|---|---|
| **Ga / Ma / ka** | 🔴 **年代（dates）** —— 距今十亿 / 百万 / 千年 |
| **Gyr / Myr / kyr** | 🔴 **时间跨度（duration）** |

**upper/middle/lower** → 岩石地层单位；**early/late** → 时间单元；仅正式 ICS 时间单元大写。
界线用 **/**，范围用 **–**（en-dash）。⚠️ *"Middle Cretaceous"* 不规范。

---

## 🎨 配色系统 NEW

> 图表硬参数（dpi / 尺寸 / 字号）见 [`figure-specs.md`](skills/academic-paper-polish/references/figure-specs.md)；
> **配色怎么组织**见 [`color-system.md`](skills/academic-paper-polish/references/color-system.md)。

**核心认知：配色是语义系统，不是审美选择。**
判据 —— 拿掉图例，只看颜色，能否在 3 秒内判断「哪个是对照、哪个是处理」？做不到就是配色失败。

| 规则 | 要点 |
|---|---|
| 🔴 **色相全图可追溯** | 同一组在**所有面板**必须是同一色相 —— 不能 A 图蓝=对照、B 图蓝=处理。（冷色=对照是常见约定，非铁律） |
| 🔴 **一通道一变量** | 颜色/形状/大小/位置各承载一个变量 —— 轴用了什么，颜色就避开它 |
| 🔴 **阴性组用空心** | 空心 ○ = 阴性对照或无显著差异，不必另配第三种颜色 |
| 🔴 **一色一义** | 同一颜色只能承载一个含义；柱状图的颜色深浅**不能**重复表达数值大小 |
| 🔴 **色相编码主变量，明度编码次变量** | 如「属 = 色相，种 = 明度」，读者一眼看出层次 |
| 🔴 **基因型用色温编码版面** | 左右分屏用**冷蓝 / 暖红**极浅底色，省去反复对照图例 |
| 🔴 **连续数据用感知均匀色阶** | 禁 jet 彩虹色阶与红绿渐变；发散色阶**必须以 0 为中心** |
| 🔴 **红绿并置必配第二重线索** | 形状（●/▲/■）、线型（实线/虚线）或直接标注 |
| **显著性星号保持中性色** | 🔴 染色后会被误读为属于某个组别 |
| **荧光通道色是全球约定** | 绿=目标蛋白 / 蓝=DAPI / 洋红=线粒体，色标文字写在图下方 |

**地学场景特别注意**：地层柱状图颜色只编码**时代**，岩性用**花纹** —— 两者混用印刷后极易糊成一团。
完整规则与 **12 条交稿前检查清单**见 [`color-system.md`](skills/academic-paper-polish/references/color-system.md)。

---

## 📐 技术检查卡口

| 项 | 要求 |
|---|---|
| 图表格式 | TIFF / JPG |
| **分辨率** | 🔴 **300 dpi 至少** |
| **文件大小** | 🔴 单图 **<10 MB** / 总 **<50 MB** |
| 图中字体 | Arial、Helvetica、Times New Roman |
| 图宽度（双栏刊） | 单栏 **<85 mm** / 双栏 **<180 mm** |
| 线条粗细 | **0.25 与 0.5 mm 组合** |
| 字号 | **10&6** 或 **12&8**；🔴 严禁 <4 号 |
| 图注 | 🔴 **只看图注就能把图看明白** |
| 表名 | **写在表上** |
| 排版 | **12 号字 + 双倍行距 + 连续行号 + 页码** |

> 🔴🔴 **从制图 → 导出 → 插入 Word，全程严禁拉对角线或等比例缩放！**
>
> ⚠️ 上表是**通用 / 地球化学方向**参数。**投 *Paleobiology* 时不同**：线条 **1200 dpi** / 半调 **600** / 组合 **800**；单栏 **9 cm**、双栏 **18 cm**、最大高 **24 cm**；线宽 ≥**0.3 pt**、字号 ≥**8 pt**；🔴 **标本照片必须带比例尺，不可用 ×40 代替**。详见 [`paleobiology-journal.md`](skills/academic-paper-polish/references/paleobiology-journal.md)。
>
> 🔴 **严禁直接复制已发表的图**（除 OA / 已获许可）；修改后必须标注文献来源；**不使用有政治分歧的地图**。

---

## 🚀 快速开始 Quick Start

<details open>
<summary><b>📋 方式一 · 直接当 Prompt 用（零安装，最快）</b></summary>

复制 `skills/academic-paper-polish/prompts/*.md` 中任意模块 → 替换 `【此处粘贴你的 XXX 初稿】` → 发给任意 LLM。

```text
请根据我提供的论文摘要初稿进行优化与重构...

请处理以下摘要内容：
【把这里替换成你的摘要初稿】
```

</details>

<details open>
<summary><b>📦 方式二 · 作为 Skill 安装（推荐）</b></summary>

获得完整 10 模块 + 渐进披露（只加载你需要的部分）。

Skill 包位于仓库的 `skills/academic-paper-polish/`，**只需把这一个目录拷进你的客户端 skills 目录**：

```bash
# 1) 取到仓库（任意临时位置）
git clone --depth 1 https://github.com/syxscott/academic-paper-polish.git /tmp/app

# 2) 整目录拷贝 —— 按你的客户端选一行
cp -R /tmp/app/skills/academic-paper-polish ~/.claude/skills/            # Claude Code
cp -R /tmp/app/skills/academic-paper-polish ~/.workbuddy/skills/        # WorkBuddy
cp -R /tmp/app/skills/academic-paper-polish "$CODEX_HOME/skills/"       # Codex CLI（默认 ~/.codex/skills/）
cp -R /tmp/app/skills/academic-paper-polish ~/.config/opencode/skills/  # opencode / ZCode / MiniMax Code
cp -R /tmp/app/skills/academic-paper-polish ~/.cursor/skills/           # Cursor
```

> ⚠️ **两个必须满足的条件，否则会静默加载失败**（不报错，只是不生效）：
> 1. 目标**目录名必须是 `academic-paper-polish`** —— 与 `SKILL.md` 的 `name` 字段一致；
> 2. **拷贝 `skills/` 里面的那一层**，不是仓库根目录。直接把仓库 clone 成 `~/.claude/skills/academic-paper-polish` 会多套一层目录，客户端发现不了 SKILL.md。

验证安装：

```bash
ls "$HOME/.claude/skills/academic-paper-polish/SKILL.md"
```

然后重启客户端，自动发现。

</details>

<details>
<summary><b>📖 方式三 · 作为项目规则使用</b></summary>

克隆到你的论文写作项目，`AGENTS.md` 会作为项目规则生效：

```bash
git clone https://github.com/syxscott/academic-paper-polish.git
```

</details>

<details>
<summary><b>🔗 方式四 · 接入 opencode.json（多文件指令）</b></summary>

本仓库已自带 [`opencode.json`](opencode.json)，克隆后 opencode 会自动读取：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["AGENTS.md", "skills/academic-paper-polish/SKILL.md"]
}
```

若你已有自己的 `opencode.json`，把上面两项追加进 `instructions` 数组即可。

</details>

<details open>
<summary><b>🌍 方式五 · 英文直接用（零安装，零翻译）</b></summary>

打开 [`skills/academic-paper-polish/prompts-en/`](skills/academic-paper-polish/prompts-en/) 对应模块 → 复制代码块 → 替换占位符 → 发给任意 LLM。

每个英文文件**自包含**（已内嵌硬规则与期刊数字），不需要先读本仓库其他文件。

</details>

<details>
<summary><b>🐍 方式六 · 任意 LLM API</b></summary>

```python
import openai

skill = open("skills/academic-paper-polish/SKILL.md", encoding="utf-8").read()
module = open("skills/academic-paper-polish/prompts/01-abstract.md", encoding="utf-8").read()

openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": skill},
        {"role": "user", "content": module + "\n\n以下是我的摘要初稿：\n" + your_abstract},
    ],
)
```

</details>

---

## 🪄 AI 工具兼容性

| 工具 | 读取方式 | 配置 |
|---|---|---|
| **OpenAI Codex CLI** | ✅ 原生读 `AGENTS.md` | 零配置 |
| **Cursor** | ✅ 原生 + `.cursor/rules/*.mdc` | 零配置（已放适配层） |
| **GitHub Copilot** | ✅ 原生（2025-08 后） | 网页版 Chat 需手动粘贴 |
| **opencode** | ✅ 原生 + `opencode.json` | 零配置（已自带） |
| **Qoder / QCode** | ✅ 原生 + `.qoder/rules/` | 零配置（已放适配层） |
| **ZCode（智谱）** | ✅ 原生 | 零配置 |
| **MiniMax Code（mcode）** | ✅ 原生 + Skills | 零配置 |
| **Claude Code** | ✅ `CLAUDE.md` → `@AGENTS.md` | 需 v2.1.277+ |
| **WorkBuddy** | ✅ `~/.workbuddy/skills/` | 零配置 |
| **Windsurf / Roo / Cline** | ✅ 原生 | 零配置 |
| **VS Code / Zed / Warp** | ✅ 原生（VS Code 支持 Skills） | 零配置 |
| **Trae** | ⚠️ 认但默认关 | 设置 → 规则 → 手动开启 |
| **Gemini CLI** | ❌ 不原生读 | 配 `context.fileName: AGENTS.md` |
| **Aider** | ❌ 不原生读 | `.aider.conf.yml` 写 `read: AGENTS.md` |

**设计原理**：`AGENTS.md` 是**跨工具规则单一来源**（2026 Q2 起由 Linux Foundation 下的
Agentic AI Foundation 接管，成为跨厂商事实标准）。Claude Code 通过 `CLAUDE.md` 的
一行 `@AGENTS.md` 导入共享同一份规则 —— **改一处，所有工具同步生效**。

**Claude Code 用户注意**：若发现规则未加载，检查同目录是否有 `CLAUDE.local.md`
（它的存在会阻止 `AGENTS.md` 直接加载），或在 `/config` 把 *Project instructions* 设为 `claude-md-and-agents-md`。

完整矩阵与排查指南见 **[docs/COMPATIBILITY.md](docs/COMPATIBILITY.md)**。

---

## 🗺️ 写作流程 Workflow

```mermaid
flowchart LR
    A[🎯 模块9<br/>定期刊] --> B[🔭 引言]
    B --> C[📚 文献综述]
    C --> D[🧪 研究方法]
    D --> E[📊 结果]
    E --> F[💡 讨论]
    F --> G[🎯 结论]
    G --> H[📝 摘要]
    H --> I[💬 模块10<br/>返修回复]
    I --> J{{🤖 模块8<br/>去 AI 化}}
    J --> K[✨ 终稿]
    style A fill:#f59e0b,color:#fff
    style J fill:#8b5cf6,color:#fff
    style K fill:#22c55e,color:#fff
```

> ⚠️ **注意摘要与引言的位置** —— 严格遵循「综述 18 步」时，**主体 → 结论 → 引言 → 摘要**才是自然顺序（引言和摘要在结构定稿后才写得出来）。
>
> ⚠️ **模块 8「降低 AI 率」必须最后用**，且**不得改动数据、单位、图表编号与结论**。

---

## 💎 Before vs After

<table>
<tr>
<th width="50%">📉 原稿 Draft (AI-flavored)</th>
<th width="50%">📈 润色后 Polished</th>
</tr>
<tr>
<td>

"首先，本文通过实验验证了该方法的有效性。其次，实验结果表明该方法具有较好的性能。最后，综上所述，本文提出的方法在多个数据集上达到了 state-of-the-art。"

</td>
<td>

"本文的核心假设在三个公开基准上得到了验证。在数据规模较小的子集（CIFAR-100, n=5k）上，该方法较 baseline 提升 4.7 个百分点 —— 这一结果略超我们最初的预期，可能与更强的数据增强策略有关。"

</td>
</tr>
</table>

---

## ❓ FAQ

<details>
<summary><b>🤔 1. 适合什么学科？</b></summary>

通用学术写作（CS / 社科 / 人文 / 医学 / **地学**）。地学、地质、环境、古生物方向**规则最完整** ——
期刊硬约束（GCA / ES&T / PPP / Earth-Science Reviews）、图件参数、地层术语规范、
配色决策逻辑都来自地学写作课并已通用化。

非地学学科把"样品/仪器"换成"数据/工具"即可。

</details>

<details>
<summary><b>🤔 2. 会"过度润色"丢失原意吗？</b></summary>

不会，而且**这是本仓库的红线**：

| ❌ 禁止 | 原因 |
|---|---|
| 改动数据、单位、图表编号 | 学术不端 |
| 把"结论 A"改成"结论 B" | 改变科学主张 |
| 引入未经证实的推测并写成事实 | 学术不端 |
| 为降重而删关键引用 | 知而不引，学术不端 |
| 编造不存在的参考文献 | 学术不端 |

**措辞与结构可改，数据与科学主张不可改。**

</details>

<details>
<summary><b>🤔 3. 模块必须按顺序用吗？</b></summary>

不强求。但推荐：`9（定期刊）→ 2–7（正文）→ 10（返修）→ 8（终稿去 AI 化）`。

**模块 8 必须最后用** —— 通篇润色，不分章节。

</details>

<details>
<summary><b>🤔 4. 英文论文能用吗？</b></summary>

可以。`prompts-en/` 是**与中文版规则完全一致**的英文版，每文件自包含：

- 给英文初稿 → 直接用 `prompts-en/` 对应模块
- 给中文初稿 → 直接用 `prompts/` 对应模块

英文入口见 [docs/PROMPTS-EN.md](docs/PROMPTS-EN.md)。

</details>

<details>
<summary><b>🤔 5. 内容可靠吗？</b></summary>

**所有硬性数字都来自期刊官方 Guide for Authors 或已发表文献**：

| 来源 | 提供什么 |
|---|---|
| 写作方法论骨架 | 章节写法、期刊结构差异、ACCEPTANCE 十点、综述 18 步 |
| 格式硬参数与文献检索 | 引文密度表、图表硬参数、送审流程、时间预算 |
| 9 份期刊官方 Style Guide | ESR / Nature / PNAS / CVPR / Palaeoworld / Paleobiology / APP / PE / PalZ 原文数字 |
| Cell / Cell Metabolism / Cancer Cell 顶刊 Figure | 配色组织逻辑（符号矩阵、气泡三通道、色标方向、空心编码、灰度检验） |

规则部分逐条标注了来源，便于核验。

</details>

<details>
<summary><b>🤔 6. v1.0 有什么已修复的 bug？</b></summary>

`SKILL.md` 的 `name` 原为 `paper-polish-prompts`，与仓库目录名 `academic-paper-polish` 不一致 ——
Agent Skills 规范要求两者一致，**不一致会静默加载失败**（不报错，只是不生效）。v2.0 已修正。

</details>

<details>
<summary><b>🤔 7. 怎么验证我的环境正确加载了？</b></summary>

对 AI 说：

```
请列出你已加载的项目规则文件，并复述其中「🔴 不可违反的内容红线」一节有几个禁止项。
```

正确加载时会说出 **7 个禁止项**。详见 [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md) 第六节。

</details>

<details>
<summary><b>🤔 8. 贡献代码前要跑什么？</b></summary>

改动后跑一遍全部 6 个校验脚本（与 CI 同一套，缺一不可）：

```bash
python3 scripts/check_skill.py --strict    # Agent Skills 规范
python3 scripts/check_links.py             # 本地链接
python3 scripts/check_encoding.py          # U+FFFD
python3 scripts/check_markdown.py          # 根级 6 文件结构
python3 scripts/check_anchors.py README.md # 内部锚点
python3 scripts/check_md_full.py           # ★ 全部 39 个 md 结构体检
```

`check_md_full.py` 是 v2.4 新增 —— 原 `check_markdown.py` 只检查 6 个根级文件，
**33 个 references/prompts 文件从未被结构检查过**。

</details>

---

## 🌍 English

See **[docs/PROMPTS-EN.md](docs/PROMPTS-EN.md)** for the English methodology reference
covering all 10 modules, the hard rules, figure specifications, and submission workflow.

---

<div align="center">

## ⭐ Star History

<a href="https://github.com/syxscott/academic-paper-polish">
  <img src="https://api.star-history.com/svg?repos=syxscott/academic-paper-polish&type=Date&theme=dark" alt="Star History Chart" />
</a>

<br/><br/>

Made with ❤️ for Chinese academic writers

**MIT Licensed**

</div>
