<div align="center">

<!-- 1. 主标题（social 风格，圆角轻盈） -->
<a href="https://github.com/syxscott/academic-paper-polish">
  <img src="https://img.shields.io/badge/✨_学术论文润色指令合集-Academic_Paper_Polish-8b5cf6?style=social&logo=openai&logoColor=white" alt="Title" />
</a>

<br/>

### *让 AI 像资深同行评审一样打磨你的论文*

<br/>

<!-- 2. 8 模块彩虹进度条（social 风格，每个纯色块，无黑色） -->
<a href="#modules-overview"><img src="https://img.shields.io/badge/📝_摘要-8b5cf6?style=social" alt="摘要" /></a>
<a href="#modules-overview"><img src="https://img.shields.io/badge/🔭_引言-ec4899?style=social" alt="引言" /></a>
<a href="#modules-overview"><img src="https://img.shields.io/badge/📚_综述-f59e0b?style=social" alt="综述" /></a>
<a href="#modules-overview"><img src="https://img.shields.io/badge/🧪_方法-22c55e?style=social" alt="方法" /></a>
<br/>
<a href="#modules-overview"><img src="https://img.shields.io/badge/📊_结果-06b6d4?style=social" alt="结果" /></a>
<a href="#modules-overview"><img src="https://img.shields.io/badge/💡_讨论-3b82f6?style=social" alt="讨论" /></a>
<a href="#modules-overview"><img src="https://img.shields.io/badge/🎯_结论-6366f1?style=social" alt="结论" /></a>
<a href="#modules-overview"><img src="https://img.shields.io/badge/🤖_去_AI-ef4444?style=social" alt="去 AI" /></a>

<br/>

<!-- 3. 一句话定位 -->
**🎯 8 个 prompt 模块 × 1 条指令 = 从初稿到终稿的全流程学术润色**

<br/>

<!-- 4. 元信息徽章（social 风格，彩色圆角） -->
<img src="https://img.shields.io/badge/📜_MIT_License-22c55e?style=social&logo=opensourceinitiative" alt="MIT" />
<img src="https://img.shields.io/badge/🧩_8_Modules-8b5cf6?style=social&logo=bookstack" alt="Modules" />
<img src="https://img.shields.io/badge/🌐_中文-ef4444?style=social&logo=googletranslate" alt="中文" />
<img src="https://img.shields.io/badge/🤖_Claude_Code-3b82f6?style=social&logo=anthropic" alt="Claude" />
<img src="https://img.shields.io/badge/🏷️_v1.0.0-fbbf24?style=social&logo=github" alt="v1.0.0" />

<br/>

<!-- 5. 实时仓库统计（social 风格） -->
<img src="https://img.shields.io/github/stars/syxscott/academic-paper-polish?style=social&logo=github&color=22c55e" alt="Stars" />
<img src="https://img.shields.io/github/forks/syxscott/academic-paper-polish?style=social&logo=github&color=8b5cf6" alt="Forks" />
<img src="https://img.shields.io/github/watchers/syxscott/academic-paper-polish?style=social&logo=github&color=3b82f6" alt="Watchers" />
<img src="https://img.shields.io/github/issues/syxscott/academic-paper-polish?style=social&logo=github&color=ef4444" alt="Issues" />

<br/><br/>

[🚀 快速开始](#-快速开始-quick-start) ·
[🧩 八模块](#modules-overview) ·
[📦 Skill 安装](#-skill-安装-install-as-skill) ·
[🗺️ 流程图](#-写作流程-workflow) ·
[❓ FAQ](#-faq) ·
[🌍 English](#-english-summary)

</div>

<br/>

---

## 🎯 TL;DR

> **不是模板，不是填空，是给 LLM 的精准角色定义 + 输入约束 + 输出规范。**
>
> *Not a template. Not a fill-in-the-blank. It's role + constraints + output spec for the LLM.*

<details>
<summary><b>👀 一句话技术总结</b></summary>

8 个 prompt 模块覆盖论文写作全流程。每个模块包含：

- **角色定义**：「你是一位资深学术编辑」「你是一位评审专家」
- **输入约束**：明确哪些要素必须覆盖（背景、方法、发现、意义…）
- **输出规范**：语言风格、字数、客观性要求、避免的措辞
- **可替换占位符**：`【此处粘贴你的 XXX 初稿】`

把这套机制喂给 Claude / GPT / Gemini 等任意 LLM，立刻获得专业级润色。

</details>

---

## ✨ 为什么选这个 Skill? Why?

<table>
<tr>
<td align="center" width="25%">🎓<br/><b>学术规范</b><br/><i>Academic-grade</i></td>
<td align="center" width="25%">⚡<br/><b>即拿即用</b><br/><i>Plug & play</i></td>
<td align="center" width="25%">🌐<br/><b>跨平台</b><br/><i>Cross-platform</i></td>
<td align="center" width="25%">🔓<br/><b>完全开源</b><br/><i>MIT licensed</i></td>
</tr>
<tr>
<td align="center">严格遵循 IMRaD 写作逻辑<br/><sub>Strict IMRaD compliance</sub></td>
<td align="center">每个模块独立可调用<br/><sub>Each module is independently usable</sub></td>
<td align="center">Claude Code / Cursor / Trae / 任意 LLM<br/><sub>Works everywhere</sub></td>
<td align="center">可商用、可二次开发<br/><sub>Commercial & derivative-friendly</sub></td>
</tr>
</table>

---

## 🧩 Modules Overview

> 推荐顺序：`摘要 → 引言 → 文献综述 → 研究方法 → 结果 → 讨论 → 结论 → 降低 AI 率`

| # | 模块 Module | 一句话定位 Tagline | 核心评审维度 |
|---|---|---|---|
| 1 | 📝 **摘要润色** Abstract | 把整篇论文压缩进 200 字 | 背景 · 方法 · 发现 · 意义 |
| 2 | 🔭 **引言润色** Introduction | 倒金字塔 · 缺口 · 问题 · 路线图 | 倒三角结构 · 缺口论证 · 问题 |
| 3 | 📚 **文献综述润色** Lit Review | 让文献"对话"而非罗列 | 主题整合 · 批判分析 · 对话 |
| 4 | 🧪 **研究方法润色** Methods | 经得起同行复现的细节度 | 设计 · 数据 · 模型 · 指标 |
| 5 | 📊 **结果润色** Results | 只讲"发现了什么"，不解释"为什么" | 客观性 · 逻辑 · 图表规范 |
| 6 | 💡 **讨论润色** Discussion | 结果 ↔ 文献 ↔ 理论 ↔ 实践 | 解读 · 对话 · 贡献 · 局限 |
| 7 | 🎯 **结论润色** Conclusion | 升华，但不引入新信息 | 回顾 · 重申 · 不越界 |
| 8 | 🤖 **降低 AI 率** De-AI Polish | 终稿通篇去 AI 化润色 | 自然节奏 · 弱化绝对化 |

<details>
<summary><b>📝 点击展开 · 模块 1 详情 · 摘要润色</b></summary>

**核心目标**：精炼概括研究的核心贡献

**评审维度**：
- 研究背景：宏观背景 + 具体问题 + 研究缺口
- 研究方法：核心方法 / 关键技术 / 理论框架
- 核心发现：精确数据 + 定性结论
- 意义与影响：理论贡献 + 实践价值
- 语言风格：正式、客观、无口语

**占位符**：`【此处粘贴你的摘要初稿】`

</details>

<details>
<summary><b>🔭 点击展开 · 模块 2 详情 · 引言润色</b></summary>

**核心目标**：快速建立研究动机（不展开系统综述）

**评审维度**：
- 倒三角写作范式
- 文献缺口论证
- 研究问题与假设
- 论文结构概述

**占位符**：`【此处粘贴你的引言初稿】`

</details>

<details>
<summary><b>📚 点击展开 · 模块 3 详情 · 文献综述润色</b></summary>

**核心目标**：构建批判性、综合性的分析框架

**评审维度**：
- 主题式整合（而非按作者罗列）
- 批判性分析（指出矛盾、局限、缺陷）
- 建立文献间对话关系
- 凝练研究缺口

**占位符**：`【此处粘贴你的文献综述初稿】`

</details>

<details>
<summary><b>🧪 点击展开 · 模块 4 详情 · 研究方法润色</b></summary>

**核心目标**：严谨性、清晰度、可复现性

**评审维度**：
- 研究设计 + 适用性依据
- 数据采集/处理（来源、样本、纳入排除、时间、缺失值）
- 模型/算法描述（数学表达、假设、实现细节）
- 评估指标（相关性、定义、公式）

**占位符**：`【此处粘贴你的研究方法初稿】`

</details>

<details>
<summary><b>📊 点击展开 · 模块 5 详情 · 结果润色</b></summary>

**核心目标**：客观、清晰、符合学术图表规范

**评审维度**：
- 客观性陈述（剔除主观/推测语言）
- 逻辑结构（与研究问题一致）
- 图表引用与说明
- 图表类型与数据匹配性

**占位符**：`【此处粘贴你的结果初稿】`

</details>

<details>
<summary><b>💡 点击展开 · 模块 6 详情 · 讨论润色</b></summary>

**核心目标**：将结果与现有文献对话 + 挖掘理论与实践意义

**评审维度**：
- 结果解读（超越简单复述）
- 与文献对话
- 理论贡献（1-3 个清晰、具体）
- 实践启示（具体、可操作）
- 局限性与未来研究

**占位符**：`【此处粘贴你的讨论初稿】`

</details>

<details>
<summary><b>🎯 点击展开 · 模块 7 详情 · 结论润色</b></summary>

**核心目标**：强有力总结全文 + 升华研究价值

**评审维度**：
- 核心回顾（用新语言，不重复摘要）
- 贡献重申（高度凝练）
- 避免引入新信息
- 宏大愿景（可选）

**占位符**：`【此处粘贴你的结论初稿】`

</details>

<details>
<summary><b>🤖 点击展开 · 模块 8 详情 · 降低 AI 率（终篇通篇）</b></summary>

**核心目标**：去 AI 化通篇润色，仅在前 7 章定稿后使用

**评审维度**：
- 自然节奏（资深学者笔调）
- 连接词替换（避免"首先/其次/最后"等机械连接）
- 语态与句式（主动语态、长短交错）
- 审慎的个人化表达（不改变核心结论）
- 结构调整（打破总分总模板）
- 适度冗余（口语化插入语、限定词）
- 避免绝对化（替换 AI 高频词）
- 具体化表达（具体动词、可设问）

**占位符**：`【此处粘贴你的完整初稿】`

</details>

---

## 🚀 快速开始 Quick Start

<details open>
<summary><b>📋 方式一 · 直接当 Prompt 用（最快）</b></summary>

复制任意模块 → 替换 `【此处粘贴你的 XXX 初稿】` → 发给任意 LLM。

```text
请根据我提供的论文摘要初稿进行优化与重构 ...

请处理以下摘要内容：
【把这里替换成你的摘要初稿】
```

</details>

<details>
<summary><b>🤖 方式二 · Claude Code Skill</b></summary>

```bash
git clone https://github.com/syxscott/academic-paper-polish.git \
  ~/.claude/skills/paper-polish-prompts
```

重启 Claude Code，自动发现。

</details>

<details>
<summary><b>💠 方式三 · Cursor Rule</b></summary>

1. 复制 `SKILL.md` 内容
2. 顶部补 mdc 头：

   ```yaml
   ---
   description: 论文润色指令合集
   globs: *
   alwaysApply: false
   ---
   ```

3. 保存到 `~/.cursor/rules/paper-polish-prompts.mdc`

</details>

<details>
<summary><b>🌊 方式四 · Trae / Cline / Continue / 其他通用 Agent</b></summary>

将 `SKILL.md` 整文件作为 system prompt 或规则文件载入即可。

</details>

<details>
<summary><b>🤖 方式五 · 任意 LLM API</b></summary>

```python
import openai

prompt = open("SKILL.md").read()
# 取模块 1 的部分，加上你的初稿
user_input = prompt + "\n\n以下是我的初稿：\n" + your_abstract

openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "system", "content": prompt},
              {"role": "user", "content": user_input}]
)
```

</details>

---

## 🗺️ 写作流程 Workflow

```mermaid
flowchart LR
    A[📝 摘要] --> B[🔭 引言]
    B --> C[📚 文献综述]
    C --> D[🧪 研究方法]
    D --> E[📊 结果]
    E --> F[💡 讨论]
    F --> G[🎯 结论]
    G --> H{{🤖 降低 AI 率}}
    H --> I[✨ 终稿]
    style H fill:#8b5cf6,color:#fff
    style I fill:#22c55e,color:#fff
```

> ⚠️ **模块 8「降低 AI 率」必须在前 7 章全部定稿后再使用。**
>
> *Module 8 (De-AI Polish) must be the last step, after chapters 1-7 are finalized.*

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
<summary><b>🤔 1. 这个 Skill 适合什么学科？</b></summary>

通用学术写作。CS / 社科 / 人文 / 医学都能用。模块四「研究方法」对 CS 类更友好（提到超参数、训练测试划分）；其他学科把"超参数"换成"研究工具 / 材料 / 访谈提纲"即可。

</details>

<details>
<summary><b>🤔 2. 和 ChatGPT 默认润色有什么不同？</b></summary>

ChatGPT 默认润色没有明确的角色 / 约束 / 输出规范。本 Skill 给 LLM：
- **角色定义**：「你是一位资深学术编辑」
- **输入约束**：明确评审维度（5-7 个 checklist）
- **输出规范**：禁用词清单、语言风格、字数范围

直接复制 prompt 给 ChatGPT 也能用，体验比"帮我润色一下"高一个数量级。

</details>

<details>
<summary><b>🤔 3. 八个模块必须按顺序用吗？</b></summary>

不强求顺序。但推荐按论文写作顺序：摘要 → 引言 → 综述 → 方法 → 结果 → 讨论 → 结论 → 降低 AI 率。

模块 8「降低 AI 率」**必须最后用**——通篇润色，不分章节。

</details>

<details>
<summary><b>🤔 4. 英文论文能用吗？</b></summary>

可以。prompt 是中文写的，所以：
- 给中文初稿：直接用
- 给英文初稿：把 prompt 主体英化（结构一致），或者先用本 Skill 把中文 prompt 翻成英文 prompt 再用

后续可加 `prompts-en/SKILL.md` 英文版（欢迎 PR）。

</details>

<details>
<summary><b>🤔 5. 模块之间会冲突吗？比如"客观陈述"和"降低 AI 率"的口语化？</b></summary>

模块 1-7 是**学术规范**（客观、严谨），模块 8 是**终篇润色**（自然、人味）。两者不冲突——
前 7 章先保证学术规范，终稿再用模块 8 调整"人味"。

</details>

<details>
<summary><b>🤔 6. 是否会"过度润色"丢失原意？</b></summary>

不会。每个 prompt 都强调"不改变核心结论、不引入未经证实的推测"。模块 8 明确要求"在适当位置可加入审慎的个人判断或反思性表述……但不得改变核心结论或引入未经证实的推测"。

建议每章润色后人工 review 一遍再进入下一章。

</details>

---

## 🌍 English Summary

A curated set of **8 academic writing polish prompts** that walk you through the full pipeline:

`Abstract → Introduction → Literature Review → Methods → Results → Discussion → Conclusion → De-AI Polish`

Each module gives the LLM a clear **role**, strict **input constraints**, and a defined **output format** — not a template, not a fill-in-the-blank.

- **Format**: Anthropic / Claude Code Skill (`SKILL.md` + YAML frontmatter)
- **Platforms**: Claude Code · Cursor · Trae · Cline · any LLM API
- **License**: MIT
- **Version**: [v1.0.0](https://github.com/syxscott/academic-paper-polish/releases/tag/v1.0.0)
- **Author**: [@syxscott](https://github.com/syxscott)

Pull requests and translations (e.g. `prompts-en/`) are welcome.

---

## 📂 项目结构 Repo Layout

```
academic-paper-polish/
├── SKILL.md       # ⭐ 主体（frontmatter + 8 模块）
├── README.md      # 📖 本文件
├── LICENSE        # 🔓 MIT
└── .gitignore     # 🚫 标准忽略
```

---

<div align="center">

## ⭐ Star History

<a href="https://github.com/syxscott/academic-paper-polish">
  <img src="https://api.star-history.com/svg?repos=syxscott/academic-paper-polish&type=Date&theme=dark" alt="Star History Chart" />
</a>

<br/><br/>

Made with ❤️ for Chinese academic writers

**MIT Licensed** · [⬆ 回到顶部](#-学术论文润色指令合集-)

</div>