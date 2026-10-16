---
name: academic-paper-polish
description: 学术论文写作、润色、改稿与投稿的全流程助手。10 个模块覆盖摘要、引言、文献综述、研究方法、结果、讨论、结论、期刊匹配与投稿、审稿意见回复、去 AI 化终稿润色。融合中国地质大学张鹏研究员《研究方向文献综述与论文写作》与田力《论文写作规范与技巧》《文献综述》两份课件的方法论：期刊结构硬约束（GCA/ES&T/PPP 的 Results-Discussion 分离vs合并、有无独立结论段）、引言倒金字塔与 opening-resolution 对齐、引文密度表、讨论六步框架、结论局限句式、综述 18 步、图表硬参数（300dpi/<10MB/<180mm/禁对角线缩放）、送审三段流程、参考文献五误区、审稿回复四要素。触发词：写论文、论文写作、论文润色、SCI、投稿、返修、审稿意见、文献综述怎么写、review paper、cover letter、期刊要求、GCA、ES&T、PPP、Earth-Science Reviews、制图规范、图件要求、Highlights、行号、论文自查、降低AI率、去AI化、论文结构、文献检索、关键词怎么选。
license: MIT
metadata:
  author: syxscott
  version: "2.0.0"
  source_courses:
    - "张鹏 研究员（中国地质大学武汉）《如何开展研究方向文献综述：论文写作》2026-10-16, 94页"
    - "田力（中国地质大学）《论文写作规范与技巧》《文献综述》2025-09-08, 43+35页"
---

# 学术论文写作与润色全流程

覆盖从选题到返修的完整链路。**不是模板，不是填空，是给 LLM 的角色定义 + 约束 + 输出规范。**

## 何时使用

- 「帮我润色一下论文摘要 / 引言 / 讨论」
- 「我要投 X 期刊，需要注意什么」
- 「审稿意见怎么回复」
- 「文献综述怎么组织结构」
- 「这张图合规吗 / 参考文献怎么排序」
- 「怎么降低 AI 率」

不适用：纯文献检索（用检索工具）、数据统计分析、英文写作（先英化再用）。

---

## 🔴 铁律 0：先定期刊，再动笔

**这一步决定后面所有结构决策。** 不是流程形式。

| 期刊 | Results/Discussion | 结论段 | 收录边界 |
|---|---|---|---|
| **GCA** | 🔴 **必须分离**，各自独立编号 | 允许 | ❌ 不收纯方法学/技术/模型论文；❌ 不收 regional case studies；Cover Letter 必推荐 3 位副主编 |
| **ES&T** | 🔴 **合并**为 R&D | ❌ *"A separate conclusion is not to be used"* | Research Article 限 **7,000 词** |
| **PPP** | — | — | Articles **5000–7000 词 / 4–8 图**；图单栏 **<85 mm** / 双栏 **<180 mm** |
| **Paleobiology**<br>★化石/古生物方向，规则最细 | — | — | 送审图 **<40 兆像素**；终稿 **线条 1200 / 半调 600 / 组合 800 dpi**；单栏 9 cm / 双栏 18 cm / 最大高 24 cm；🔴 **须提供 Non-technical Summary + Abstract 各 ≤300 词**；全稿 **12 号 TNR + 双倍行距 + 连续行号**；**Ga/Ma/ka = 年代，Gyr/Myr/kyr = 跨度** |
| **Earth-Science Reviews** | — | — | **IF > 10** |
| **Biological Reviews / Chemical Reviews / Nature Reviews** | — | — | **IF > 14 / > 50 / 46–123** |

> 🔴 **格式不过关，直接拒稿 —— 走不到学术编辑和审稿人那一步。**
> 原因：① 第一印象 ② 基本学术素养 ③ 评审是挑错过程 ④ 格式意见往往比内容意见多

详见 `references/journal-constraints.md`。

---

## 模块索引

| # | 模块 | 一句话定位 | 文件 |
|---|---|---|---|
| 1 | 📝 摘要 | 把整篇压缩进 300 词 | `prompts/01-abstract.md` |
| 2 | 🔭 引言 | 倒金字塔 · 缺口 · 路线图 | `prompts/02-introduction.md` |
| 3 | 📚 文献综述 | 让文献"对话"而非罗列 | `prompts/03-literature-review.md` |
| 4 | 🧪 研究方法 | 经得起同行复现 | `prompts/04-methods.md` |
| 5 | 📊 结果 | 只讲"发现了什么" | `prompts/05-results.md` |
| 6 | 💡 讨论 | 结果 ↔ 文献 ↔ 理论 ↔ 局限 | `prompts/06-discussion.md` |
| 7 | 🎯 结论 | 升华但不引入新信息 | `prompts/07-conclusion.md` |
| 8 | 🤖 去 AI 化 | 终稿通篇润色 | `prompts/08-deai-polish.md` |
| 9 | 🎯 期刊匹配与投稿 | 先定期刊再动笔 | `prompts/09-journal-submission.md` |
| 10 | 💬 审稿意见回复 | 逐条答复的四要素 | `prompts/10-reviewer-response.md` |

**推荐顺序**：`① 期刊匹配(9) → ② 写/润色正文(2-7) → ③ 返修回复(10) → ④ 终稿去 AI 化(8)`

### 快速调用

```
读取 prompts/02-introduction.md，按其中的规则帮我润色引言：【粘贴初稿】
```

---

## 🔴 八条硬规则（跨模块通用）
### 1. 引言 = 倒金字塔，且 opening 必须与 resolution 对齐

| 图形 | 英文 | 后果 |
|---|---|---|
| 开口 > 收口 | *overpromising* | 读者觉得被欺骗 |
| **开口 = 收口** | ***on target*** | ✅ 认可 |
| 收口 > 开口 | *underpromising* | 读者看不到值得关注的 story |

### 2. 引文密度（最易自查的一张表）

| 章节 | 引文要求 |
|---|---|
| **Introduction** | 除**问题句和过渡句**外都要有引用 |
| **Results** | **几乎没有**引用 |
| **Discussion** | **每段 5–8 句** = topic sentence + **3–4 句带引用** + **2–3 句自己数据** |
| **Abstract / Conclusion** | **不应出现**引用 |

> ⚠️ 以为多引他人工作会降低原创性，**实际效果常常相反**。不充分引用 → 审稿人**至少会认为你阅读文献不够**。

### 3. 段落：5–8 句最合理

**1–2 句话的段落是非常差的结构。** 换了对象主体就分段 —— 一段集中讲清一个问题。

### 4. 讨论必须走完六步（含"局限性"）

```
① 引言空白 → ② 重述发现(用数据/图) → ③ 解释并与他人比较
→ ④ 表明局限性 → ⑤ 对以后研究的启示 → ⑥ 结论
```

### 5. 结论要含"局限性 + 未来方向"

```
Despite its advantages, the [方法名] also has some limitations.
First, [限制1]. Second, [限制2].
Further research should focus on [方向].
```

### 6. 措辞分寸

| ❌ 避免 | ✅ 改用 |
|---|---|
| *for the first time* | 直接陈述与前人工作的差异 |
| "首次提出 / 首次发现 / 国际先进水平" | 只陈述客观增量 |
| *The deficiency of Wang's approach is…* | *However, the mechanism has not been fully understood.* |

### 7. 参考文献五误区

**知而不引 · 断章取义 · 引而不确 · 来源不实 · 盲目自引**

综述约 **100 篇**是质量标志；优先近 5 年（最好 1–3 年）、优先一次文献。

### 8. 🔴 地质年代：Ga/Ma/ka ≠ Gyr/Myr/kyr

地学论文最常见的形式错误，两个方向都要查：

| | 表示什么 | 例 |
|---|---|---|
| **Ga / Ma / ka** | 🔴 **年代（dates）** | 距今十亿 / 百万 / 千年 |
| **Gyr / Myr / kyr** | 🔴 **时间跨度（duration）** | — |

- **upper / middle / lower** → 岩石或时间地层单位；**early / late** → 时间单位
- **仅正式 ICS 时间单元**才大写 Early / Middle / Late
- 界线用 **/**，时间范围用 **–**（en-dash）
- 规范依据：**ICS 年代表**（stratigraphy.org/chart）与 **ICS Guide**（stratigraphy.org/guide）
- ⚠️ *"Middle Cretaceous"* 不规范 → 用 *Upper/Lower Cretaceous*，或作形容词时 *mid-Cretaceous*

---

## 🔴 技术检查卡口（这层不过直接拒稿）

### 图表硬参数

| 项 | 要求 |
|---|---|
| 格式 | TIFF / JPG |
| 🔴 **分辨率** | **300 dpi 至少** |
| 🔴 单图 / 总文件 | **<10 MB / <50 MB** |
| 图中字体 | Arial、Helvetica、Times New Roman |
| 图宽度（双栏刊） | 单栏 **<85 mm** / 双栏 **<180 mm** |
| 线条粗细 | **0.25 与 0.5 mm 组合** |
| 字号 | **10&6** 或 **12&8** 组合；🔴 严禁 <4 号 |
| 图注 | 🔴 **只看图注就能把图看明白** |
| 表名 | **写在表上** |

**🔴🔴 Word 铁律**：**从制图 → 导出 → 插入 Word，全程严禁拉对角线或等比例缩放！**

**🔴 版权红线**：严禁直接复制已发表的图（除 OA/获许可）；改后必标来源；**不使用有政治分歧的地图**。

> ⚠️ 上表是**通用 / 地球化学方向**的参数。**若投 *Paleobiology*（古生物 / 化石形态学），参数不同**：
> 线条图 **1200 dpi** / 半调图 **600** / 组合图 **800**；单栏 **9 cm**、双栏 **18 cm**、最大高 **24 cm**；
> 线条 ≥**0.3 pt**、字号 ≥**8 pt**；🔴 **标本照片必须带比例尺，不可用 ×40 等放大倍数代替**；
> 🔴 送审图须 **<40 兆像素** 才能进 PDF proof。
> 详见 `references/paleobiology-journal.md`。

### 排版

**12 号字 + 双倍行距 + 连续行号 + 页码**

*Paleobiology* 另要求：**US Letter 纸张、四边 1 英寸、不用两端对齐、不在右边界断词**。

详见 `references/figure-specs.md` 与 `references/paleobiology-journal.md`。

---

## 送审流程

| 体裁 | 流程 |
|---|---|
| SCI 论文 | 技术检查（格式）→ **学术编辑（期刊符合度）** → 审稿人 |
| 学位论文 | 组内导师 → **校外评审** → 校内评审 |

---

## 时间预算

一篇期刊文章（4–8 图 + 5000–7000 词）≈ **6–8 周**
```
每周 1–2 个图 + 每天 2–3 句（约 15 词/句）
= 每 3 天一个图，每天 3 句话 = 两个月一篇
```

⚠️ 仿写句子练手可以，但**连续 5 个字相同 = 抄袭；不标注引用 = 抄袭嫌疑**。

---

## 🔴 去 AI 化的红线

| ❌ 不能做 | 原因 |
|---|---|
| 改动数据、单位、图表编号 | 学术不端 |
| 把"结论 A"改成"结论 B" | 改变科学主张 |
| 加未经证实的推测并写成事实 | 学术不端 |
| 为降重而删关键引用 | 知而不引 |

**目标不是"过检测"，是"读起来像人写的、且信息密度高"。**
部分期刊要求声明 AI 使用情况，按目标期刊要求处理。

---

## 参考文件

| 文件 | 内容 |
|---|---|
| `references/checklist.md` | 投稿前自查清单（A–J 十组，可打印） |
| `references/journal-constraints.md` | 期刊结构硬约束 + 体裁篇幅 + 引文密度 + 送审流程 |
| `references/figure-specs.md` | 图表硬参数 + 构图 + 版权红线 + 版式范例 |
| `references/paleobiology-journal.md` | ★ *Paleobiology* 全刊规范（图件 + 文体 + 数据可用性） |
| `references/literature-search.md` | 检索工具 + 关键词尺度 + 素材库积累 + review proposal |
| `references/sentence-bank.md` | 句式库（引出不足 / 讨论动词 / 局限句式 / 回复审稿人） |
| `references/course-sources.md` | 两份课件出处与逐页索引（含所有文献范例出处） |
| `docs/COMPATIBILITY.md` | 各 AI 工具兼容性矩阵与安装路径 |
| `docs/PROMPTS-EN.md` | 英文版 prompt（English version of the 10 modules） |