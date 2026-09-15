<div align="center">

# ✨ 学术论文润色指令合集 ✨
### Academic Paper Polish Prompts

**让 AI 真正读懂学术写作的 8 个 prompt 模块**

[![MIT License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Modules](https://img.shields.io/badge/Modules-8-8b5cf6?style=for-the-badge)](#-八模块速览-modules)
[![Lang](https://img.shields.io/badge/Lang-中文-ef4444?style=for-the-badge)](#-english-summary)
[![Claude Skill](https://img.shields.io/badge/Claude_Code-Skill_Ready-3b82f6?style=for-the-badge)](#-skill-安装-install-as-skill)
[![Release](https://img.shields.io/badge/Release-v1.0.0-000000?style=for-the-badge)](https://github.com/syxscott/academic-paper-polish/releases/tag/v1.0.0)

<br/>

> **从初稿到终稿，让 AI 像资深同行评审一样打磨你的论文**
>
> *From draft to final — let AI polish your paper like a seasoned reviewer.*

[🚀 快速开始](#-快速开始-quick-start) ·
[🧩 模块详情](#-八模块速览-modules) ·
[📦 Skill 安装](#-skill-安装-install-as-skill) ·
[🌍 English](#-english-summary)

</div>

---

## 🎯 一句话总结 TL;DR

> **8 个 prompt 模块 × 1 条指令 = 从初稿到终稿的全流程学术润色**
>
> *8 modules × 1 prompt each = full-pipeline academic polishing.*

不是模板，不是填空，是给 LLM 的 **精准角色定义 + 输入约束 + 输出规范**。
*Not a template. Not a fill-in-the-blank. It's role + constraints + output spec for the LLM.*

---

## ✨ 为什么选这个 Skill? Why?

<table>
<tr>
<td align="center">🎓<br/><b>学术规范</b><br/>Academic-grade</td>
<td align="center">⚡<br/><b>即拿即用</b><br/>Plug & play</td>
<td align="center">🌐<br/><b>跨平台</b><br/>Cross-platform</td>
<td align="center">🔓<br/><b>完全开源</b><br/>MIT licensed</td>
</tr>
<tr>
<td>严格遵循 IMRaD 写作逻辑<br/><i>Strict IMRaD compliance</i></td>
<td>每个模块独立可调用<br/><i>Each module is independently usable</i></td>
<td>Claude Code / Cursor / Trae / 任意 LLM<br/><i>Works everywhere</i></td>
<td>可商用、可二次开发<br/><i>Commercial & derivative-friendly</i></td>
</tr>
</table>

---

## 🧩 八模块速览 Modules

> 推荐顺序：`摘要 → 引言 → 文献综述 → 研究方法 → 结果 → 讨论 → 结论 → 降低 AI 率`

| # | 模块 Module | 一句话定位 Tagline |
|---|---|---|
| 1 | 📝 **摘要润色** Abstract | 把整篇论文压缩进 200 字 |
| 2 | 🔭 **引言润色** Introduction | 倒金字塔 · 缺口 · 问题 · 路线图 |
| 3 | 📚 **文献综述润色** Lit Review | 让文献"对话"而非罗列 |
| 4 | 🧪 **研究方法润色** Methods | 经得起同行复现的细节度 |
| 5 | 📊 **结果润色** Results | 只讲"发现了什么"，不解释"为什么" |
| 6 | 💡 **讨论润色** Discussion | 结果 ↔ 文献 ↔ 理论 ↔ 实践 |
| 7 | 🎯 **结论润色** Conclusion | 升华，但不引入新信息 |
| 8 | 🤖 **降低 AI 率** De-AI Polish | 终稿通篇去 AI 化润色 |

---

## 🚀 快速开始 Quick Start

### 方式一 · 直接当 Prompt 用

复制任意模块 → 替换 `【此处粘贴你的 XXX 初稿】` → 发给任意 LLM。

```text
请根据我提供的论文摘要初稿进行优化与重构 ...

请处理以下摘要内容：
【把这里替换成你的摘要初稿】
```

### 方式二 · 作为 Skill 加载

<table>
<tr>
<th>🤖 Claude Code</th>
<th>💠 Cursor</th>
</tr>
<tr>
<td>

```bash
git clone https://github.com/syxscott/academic-paper-polish.git \
  ~/.claude/skills/paper-polish-prompts
```

</td>
<td>

把 `SKILL.md` 复制到 `~/.cursor/rules/`，顶部补 mdc 头：

```yaml
---
description: 论文润色指令合集
globs: *
alwaysApply: false
---
```

</td>
</tr>
<tr>
<th>🌊 Trae / Cline / Continue</th>
<th>🤖 任意 LLM API</th>
</tr>
<tr>
<td>将 <code>SKILL.md</code> 整文件作为 system prompt 或规则文件载入</td>
<td>复制模块正文 + 替换占位符，直接调 API</td>
</tr>
</table>

---

## 🗺️ 写作流程 Workflow

```
   📝 摘要        🔭 引言        📚 文献综述      🧪 研究方法
     │             │              │              │
     └─────────────┴──────────────┴──────────────┘
                                     │
                                     ▼
   🎯 结论  ◀── 💡 讨论  ◀── 📊 结果  ◀─────────┘
     │
     ▼
   🤖 降低 AI 率（终稿）
```

> ⚠️ 模块 8「降低 AI 率」必须在前 7 章全部定稿后再使用。
>
> *Module 8 must be the last step, after chapters 1-7 are finalized.*

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

## ⭐ 如果这个 Skill 对你有帮助，欢迎 Star！

[![Star History Chart](https://img.shields.io/github/stars/syxscott/academic-paper-polish?style=social)](https://github.com/syxscott/academic-paper-polish)

**MIT Licensed** · Made with ❤️ for Chinese academic writers

[⬆ 回到顶部](#-学术论文润色指令合集-)

</div>