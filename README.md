<div align="center">

<img src="assets/banner.svg" alt="Academic Paper Polish Banner" width="900" />

<br/>

### *让 AI 像资深同行评审一样打磨你的论文*

<br/>

<img src="https://img.shields.io/badge/📜_MIT_License-22c55e?style=social&logo=opensourceinitiative" alt="MIT" />
<img src="https://img.shields.io/badge/🧩_10_Modules-8b5cf6?style=social&logo=bookstack" alt="Modules" />
<img src="https://img.shields.io/badge/🌐_中文-ef4444?style=social&logo=googletranslate" alt="中文" />
<img src="https://img.shields.io/badge/🪄_11_AI_Tools-3b82f6?style=social&logo=anthropic" alt="AI Tools" />
<img src="https://img.shields.io/badge/🏷️_v2.0.0-fbbf24?style=social&logo=github" alt="v2.0.0" />

<br/>

<img src="https://img.shields.io/github/stars/syxscott/academic-paper-polish?style=social&logo=github&color=22c55e" alt="Stars" />
<img src="https://img.shields.io/github/forks/syxscott/academic-paper-polish?style=social&logo=github&color=8b5cf6" alt="Forks" />
<img src="https://img.shields.io/github/watchers/syxscott/academic-paper-polish?style=social&logo=github&color=3b82f6" alt="Watchers" />
<img src="https://img.shields.io/github/issues/syxscott/academic-paper-polish?style=social&logo=github&color=ef4444" alt="Issues" />

<br/><br/>

[🚀 快速开始](#-快速开始-quick-start) ·
[🧩 十模块](#-十模块-modules) ·
[📦 安装](#-安装-install) ·
[🪄 兼容性](#-ai-工具兼容性) ·
[🗺️ 流程图](#-写作流程-workflow) ·
[❓ FAQ](#-faq) ·
[🌍 English](docs/PROMPTS-EN.md)

</div>

<br/>

---

## 🎯 TL;DR

> **不是模板，不是填空，是给 LLM 的精准角色定义 + 输入约束 + 输出规范。**

v2.0 把原来的 8 个润色 prompt 扩展到 **10 个模块 + 6 份深度参考**，并新增 **11 个 AI 工具的跨平台适配层**。

**v2.0 新增**

| 新增 | 说明 |
|---|---|
| 🎯 **模块 9 · 期刊匹配与投稿** | 🔴 **先定期刊再动笔** —— GCA 与 ES&T 的结构要求完全相反 |
| 💬 **模块 10 · 审稿意见回复** | 四要素范式 + 六条纪律 |
| 📐 **图表硬参数** | 300 dpi / <10 MB / <180 mm / 禁对角线缩放 |
| 📊 **引文密度表** | Intro / Results / Discussion 各有不同的引用要求 |
| 🔤 **句式库** | 可直接套用的英文句式 |
| 🪄 **跨平台适配** | AGENTS.md + CLAUDE.md 双轨，覆盖 11 个工具 |

**内容来源**：融合中国地质大学张鹏研究员《研究方向文献综述与论文写作》（94 页）与田力《论文写作规范与技巧》《文献综述》（78 页）两份课件 —— 从"怎么写"到"怎么投"全链路。

---

## 📂 仓库结构 Repo Layout

```
academic-paper-polish/
├── AGENTS.md              # ⭐ 跨工具规则单一来源（Codex/Cursor/opencode/ZCode…）
├── CLAUDE.md              # Claude Code 跳板：@AGENTS.md
├── SKILL.md               # ⭐ Agent Skills 入口
├── README.md              # 📖 你正在读的文件
├── prompts/               # 10 个可独立调用的 prompt 模块
├── prompts-en/            # 同 10 模块英文版，每文件自包含
│   ├── 01-abstract.md              📝 摘要
│   ├── 02-introduction.md🔭 引言
│   ├── 03-literature-review.md     📚 文献综述
│   ├── 04-methods.md               🧪 研究方法
│   ├── 05-results.md               📊 结果
│   ├── 06-discussion.md            💡 讨论
│   ├── 07-conclusion.md            🎯 结论
│   ├── 08-deai-polish.md           🤖 降低 AI 率
│   ├── 09-journal-submission.md    🎯 期刊匹配与投稿  ★新
│   └── 10-reviewer-response.md     💬 审稿意见回复    ★新
├── references/            # 按需加载的深度参考
│   ├── checklist.md            投稿前自查清单（A–J 十组）
│   ├── journal-constraints.md  期刊结构硬约束
│   ├── figure-specs.md         图表硬参数
│   ├── paleobiology-journal.md ★ Paleobiology 全刊规范
│   ├── multi-journal-style-guides.md ★ 9 份官方 style guide 汇总
│   ├── literature-search.md    检索与素材积累
│   ├── sentence-bank.md        句式库
│   └── course-sources.md       课件逐页索引
├── docs/
│   ├── COMPATIBILITY.md    🪄 11 工具兼容性矩阵
│   └── PROMPTS-EN.md       🌍 英文版参考
├── assets/banner.svg
├── .cursor/rules/          Cursor 适配层
├── .qoder/rules/           Qoder 适配层
└── LICENSE                 MIT
```

---

## 🧩 十模块 Modules

> 推荐顺序：`🎯 期刊匹配(9) → ✍️ 写/润色正文(2-7) → 💬 返修回复(10) → 🤖 终稿去 AI 化(8)`

| # | 模块 Module | 一句话定位 Tagline | 中文 | English |
|---|---|---|---|---|
| 1 | 📝 **摘要** Abstract | 把整篇论文压缩进 300 词 | `prompts/01-abstract.md` | `prompts-en/01-abstract.md` |
| 2 | 🔭 **引言** Introduction | 倒金字塔 · 缺口 · 问题 · 路线图 | `prompts/02-introduction.md` | `prompts-en/02-introduction.md` |
| 3 | 📚 **文献综述** Lit Review | 让文献"对话"而非罗列 | `prompts/03-literature-review.md` | `prompts-en/03-literature-review.md` |
| 4 | 🧪 **研究方法** Methods | 经得起同行复现的细节度 | `prompts/04-methods.md` | `prompts-en/04-methods.md` |
| 5 | 📊 **结果** Results | 只讲"发现了什么"，不解释"为什么" | `prompts/05-results.md` | `prompts-en/05-results.md` |
| 6 | 💡 **讨论** Discussion | 结果 ↔ 文献 ↔ 理论 ↔ 实践 | `prompts/06-discussion.md` | `prompts-en/06-discussion.md` |
| 7 | 🎯 **结论** Conclusion | 升华，但不引入新信息 | `prompts/07-conclusion.md` | `prompts-en/07-conclusion.md` |
| 8 | 🤖 **降低 AI 率** De-AI Polish | 终稿通篇去 AI 化润色 | `prompts/08-deai-polish.md` | `prompts-en/08-deai-polish.md` |
| 9 | 🎯 **期刊匹配与投稿** ★新 | 🔴 先定期刊，再动笔 | `prompts/09-journal-submission.md` | `prompts-en/09-journal-submission.md` |
| 10 | 💬 **审稿意见回复** ★新 | 逐条答复的四要素 | `prompts/10-reviewer-response.md` | `prompts-en/10-reviewer-response.md` |

> 🌍 **English users**: read the `prompts-en/` module directly. Each file is **self-contained** — copy one file into any LLM (ChatGPT, Claude, Gemini) and it works, no need to read `references/` first. English entry point: [`docs/PROMPTS-EN.md`](docs/PROMPTS-EN.md).


---

## 🔴 八条硬规则

### 1️⃣ 先定期刊，再动笔

**这不是流程形式，它决定后面所有结构决策。**

| 期刊 | Results/Discussion | 结论段 |
|---|---|---|
| **GCA** | 🔴 **必须分离**，各自独立编号 | 允许 |
| **ES&T** | 🔴 **合并**为 Results and Discussion | ❌ *"A separate conclusion is not to be used"* |
| ***Paleobiology*** | — | 🔴 **须另加 Non-technical Summary**；送审图 **<40 MP**，终稿按图型 **1200/800/600 dpi** |
| **Acta Palaeontologica Polonica** | — | 图件参数最精确：单栏 **89 mm** / 双栏 **183 mm** / 最大长 **237 mm**；**Calibri 8 pt**；线宽 **0.2 mm**；照片 **400 dpi**；🔴 **ZooBank 强制注册** |
| **Palaeontologia Electronica** | — | 🔴 **无页限、无版面费**；图宽 **175 mm / 84 mm**，**300 ppi**，**RGB 不用 CMYK**；🔴 文件名 **ISO 9660**（≤8 字符，仅小写/数字/`_`/`.`） |
| **PalZ** | — | Systematic Palaeontology：分类单元名**粗体**，authority **加逗号**（与 Paleobiology/APP 系相反），同义名列表**隔行缩进** |

> 🔴 **格式不过关 → 直接拒稿，走不到学术编辑和审稿人那一步。**
> 原因：① 第一印象 ② 基本学术素养 ③ 评审是挑错过程 ④ **格式意见往往比内容意见多**

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
| **Ga / Ma / ka** | 🔴 **年代（dates）** |
| **Gyr / Myr / kyr** | 🔴 **时间跨度（duration）** |

**upper/middle/lower** → 岩石地层单位；**early/late** → 时间单位；仅正式 ICS 时间单元大写。
界线用 **/**，范围用 **–**。⚠️ *"Middle Cretaceous"* 不规范。

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
> ⚠️ 上表是**通用 / 地球化学方向**参数。**投 *Paleobiology* 时不同**：线条 **1200 dpi** / 半调 **600** / 组合 **800**；单栏 **9 cm**、双栏 **18 cm**、最大高 **24 cm**；线宽 ≥**0.3 pt**、字号 ≥**8 pt**；🔴 **标本照片必须带比例尺，不可用 ×40 代替**。详见 [references/paleobiology-journal.md](references/paleobiology-journal.md)。
>
> 🔴 **严禁直接复制已发表的图**（除 OA / 已获许可）；修改后必须标注文献来源；**不使用有政治分歧的地图**。

---

## 🚀 快速开始 Quick Start

<details open>
<summary><b>📋 方式一 · 直接当 Prompt 用（零安装，最快）</b></summary>

复制 `prompts/*.md` 中任意模块 → 替换 `【此处粘贴你的 XXX 初稿】` → 发给任意 LLM。

```text
请根据我提供的论文摘要初稿进行优化与重构...

请处理以下摘要内容：
【把这里替换成你的摘要初稿】
```

</details>

<details open>
<summary><b>📦 方式二 · 作为 Skill 安装（推荐）</b></summary>

获得完整 10 模块 + 渐进披露（只加载你需要的部分）。

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
git clone https://github.com/syxscott/academic-paper-polish.git \
  ~/.config/opencode/skills/academic-paper-polish
```

> ⚠️ **目录名必须是 `academic-paper-polish`** —— 与 `SKILL.md` 的 `name` 字段一致。
> 不一致会**静默加载失败**（不报错，只是不生效）。

重启客户端，自动发现。

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

```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["AGENTS.md", "SKILL.md"]
}
```

</details>

<details open>
<summary><b>🌍 方式五 · 英文直接用（零安装，零翻译）</b></summary>

打开 [`prompts-en/`](prompts-en/) 对应模块 → 复制代码块 → 替换占位符 → 发给任意 LLM。

每个英文文件**自包含**（已内嵌硬规则与期刊数字），不需要先读本仓库其他文件。

</details>

<details>
<summary><b>🐍 方式六 · 任意 LLM API</b></summary>

```python
import openai

skill = open("SKILL.md", encoding="utf-8").read()
module = open("prompts/01-abstract.md", encoding="utf-8").read()

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
| **GitHub Copilot** | ✅ 原生（2025-08 后） | 零配置 |
| **opencode** | ✅ 原生 | 零配置 |
| **Qoder / QCode** | ✅ 原生 + `.qoder/rules/` | 零配置（已放适配层） |
| **ZCode（智谱）** | ✅ 原生 | 零配置 |
| **MiniMax Code（mcode）** | ✅ 原生 | 零配置 |
| **Claude Code** | ✅ `CLAUDE.md` → `@AGENTS.md` | 已配好（见下） |
| **WorkBuddy** | ✅ `~/.workbuddy/skills/` | 零配置 |
| **Trae** | ⚠️ 桌面版需手动开启 | 设置 → 规则 |
| **Gemini CLI** | ❌ 不原生读 | 配 `context.fileName: AGENTS.md` |
| **Aider** | ❌ 不原生读 | `.aider.conf.yml` 写 `read: AGENTS.md` |

**设计原理**：`AGENTS.md` 是**跨工具规则单一来源**（2026 Q2 起由 Linux Foundation 下的 Agentic AI Foundation 接管，成为跨厂商事实标准）。Claude Code 通过 `CLAUDE.md` 的一行 `@AGENTS.md` 导入共享同一份规则 —— **改一处，所有工具同步生效**。

**Claude Code 用户注意**：若发现规则未加载，检查同目录是否有 `CLAUDE.local.md`（它的存在会阻止 `AGENTS.md` 直接加载），或在 `/config` 把 *Project instructions* 设为 `claude-md-and-agents-md`。

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

通用学术写作（CS / 社科 / 人文 / 医学 / **地学**）。地学、地质、环境、古生物方向**规则最完整** —— 期刊硬约束（GCA / ES&T / PPP / Earth-Science Reviews）、图表参数、地层术语规范都来自地学写作课并已通用化。

非地学学科把"样品/仪器"换成"数据/工具"即可。

</details>

<details>
<summary><b>🤔 2. v2.0 和 v1.0 的区别？</b></summary>

| | v1.0.0 | v2.0.0 |
|---|---|---|
| 模块 | 8 | **10**（+期刊匹配与投稿、审稿意见回复） |
| 参考资料 | 无 | **6 份**（期刊约束 / 图表参数 / 检索 / 句式库 / 自查清单 / 课件索引） |
| 平台支持 | 主要 Claude Code / Cursor | **11 个工具**，AGENTS.md 双轨 |
| 硬规则 | 部分 | **八条**，全部标注出处 |
| 内容来源 | 通用 IMRaD | 融合 **172 页**地学写作课件 |

**⚠️ v1.0 有一个 bug 已修复**：`SKILL.md` 的 `name` 是 `paper-polish-prompts`，但仓库目录名是 `academic-paper-polish`。Agent Skills 规范要求两者一致，**不一致会静默加载失败**。v2.0 已修正。

</details>

<details>
<summary><b>🤔 3. 会"过度润色"丢失原意吗？</b></summary>

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
<summary><b>🤔 4. 模块必须按顺序用吗？</b></summary>

不强求。但推荐：`9（定期刊）→ 2–7（正文）→ 10（返修）→ 8（终稿去 AI 化）`。

**模块 8 必须最后用** —— 通篇润色，不分章节。

</details>

<details>
<summary><b>🤔 5. 英文论文能用吗？</b></summary>

可以。prompt 是中文写的，所以：
- 给中文初稿 → 直接用
- 给英文初稿 → 把对应 `prompts/*.md` 英化（结构一致），或用本 Skill 把中文 prompt 翻成英文 prompt 再用

英文**方法论参考**见 [docs/PROMPTS-EN.md](docs/PROMPTS-EN.md)。英文 prompt 完整版欢迎 PR。

</details>

<details>
<summary><b>🤔 6. 内容可靠吗？</b></summary>

**所有硬性数字都有出处**，并在 `references/course-sources.md` 中逐页索引：

| 来源 | 页数 | 提供 |
|---|---|---|
| 张鹏 研究员（中国地质大学武汉）《如何开展研究方向文献综述：论文写作》2026-10-16 | 94 | 方法论骨架、期刊结构差异、ACCEPTANCE 十点 |
| 田力（中国地质大学）《论文写作规范与技巧》《文献综述》2025-09-08 | 78 | 引文密度表、图表硬参数、送审流程、时间预算 |

规则部分逐条标注了来源与页码，便于核验。

</details>

<details>
<summary><b>🤔 7. 怎么验证我的环境正确加载了？</b></summary>

对 AI 说：

```
请列出你已加载的项目规则文件，并复述其中「🔴 不可违反的内容红线」一节有几个禁止项。
```

正确加载时会说出 **7 个禁止项**。详见 [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md) 第六节。

</details>

---

## 🌍 English

See **[docs/PROMPTS-EN.md](docs/PROMPTS-EN.md)** for the English methodology reference covering all 10 modules, the seven hard rules, figure specifications, and submission workflow.

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