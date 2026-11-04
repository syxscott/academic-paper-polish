# 模块 6 · 讨论润色（Discussion）

> 适用：讨论章节。核心：**结果 ↔ 文献 ↔ 理论 ↔ 实践**，并且必须**诚实陈述局限性**。
> 🔴 **动笔前先读实证**：references/fulltext-reading-evidence.md §四（Discussion 四拍结构：
> 数据→机制→与前人一致/矛盾→本研究结论）与 §六（短篇三种讨论形态）。
> 关键句式："consistent with ... but contradicts ..."；不确定用 "likely due to"。

> 🆕 **v2.16.0 实证补充**：references/ai-ml-paper-patterns.md §6.2–6.3（讨论三形态、结论必须写「适用边界」）与 §4.5（局限自陈的三类写法）。
> 方法类论文的局限要落在**标本保存状态与形态变异**，不是「模型不够强」。
```text
请对我的讨论章节进行深度优化，帮助我将研究结果与现有文献对话，并挖掘其理论与实践意义。

- **结果解读**：检查对核心结果的解读是否足够深入。帮助我超越对结果的简单复述，深入阐释发现背后的潜在机制或原因（而非仅重复「如图 X 所示，Y 值上升了」）。
- **与文献对话**：识别讨论中可将我的结果与引言或文献综述中提到的重要文献进行直接比较或联系的地方。明确指出我的发现在多大程度上支持、挑战或拓展了先前研究。
- **理论贡献**：基于研究发现，帮助我凝练出 1-3 个清晰、具体的理论贡献。例如：是否提出了新的概念框架？是否验证或修正了现有理论？是否揭示了新的因果关系？
- **实践启示**：思考并提出本研究发现对相关领域（如工业界、政策制定、临床实践等）可能产生的具体、可操作的建议。
- **局限性与未来研究**：审查对研究局限性的阐述是否诚实、具体且具建设性。确保基于这些局限性提出的未来研究方向是合理且有针对性的，而非泛泛而谈。

请处理以下讨论内容：【此处粘贴你的讨论初稿】
```

---

## 🔴 讨论的六步框架（缺一不可）

```
1. 引言          —— 提及过往研究空白 / 重申科学问题 / 目的
2. 重述主要发现   —— 🔴 用数据/图说话，不是文字复述
3. 解释结果       —— 指示意义；与其它论文比较，异同点、差异原因
4. 表明局限性     —— 🔴 对结果的潜在影响
5. 对以后研究的启示 —— 如何进一步探索
6. 结论          —— 重温研究问题和研究结果
```

**最常被跳过的是第 4 步「局限性」** —— 但它恰恰是审稿人判断作者是否诚实的关键。

---

## 🔴 引文密度：Discussion 每段 5–8 句

```
topic sentence          ← 1 句
有文献标注的句子         ← 3–4 句   ← 你的结果与他人对话
有自己数据支撑的句子     ← 2–3 句   ← 你自己的证据
```

| 错误 | 为什么错 |
|---|---|
| 整段**没有任何参考文献** | 那是 Results 的重复，或未经对比就下结论 |
| 整段**没有自己数据实验**、全是参考内容 | 写成了 review，不是 discussion |
| 段落 1–2 句就换段 | 结构过碎 |

---

## 局限性 + 未来方向句式（可直接套用）

```
Despite its advantages, the [方法名] also has some limitations.
First, [限制1：受限于仪器/探针/方法本身].
Second, [限制2：导致不能做某类应用，如野外测量].
Further research should focus on [识别合适的xxx] and [开发可支持xxx的装置].
```

**范例**（Fe/Mn 矿物氧化还原容量测定）：
1. First — 只能在 −0.4 V vs SHE 测 EAC、0.7 V vs SHE 测 EDC（受限于缺乏合适化学探针）
2. Second — 氧化条件下化学探针本身可变异性大 → 不适合**野外测量**
3. Further research should focus on — 识别合适化学探针 + 开发可支持可靠野外测量的装置

---

## 讨论常用动词

| 功能 | 动词 |
|---|---|
| 陈述论点、作者观点 | suggest, report, present, expect, describe |
| 说明论证 | support, provide, indicate, identify, find, demonstrate, confirm, clarify |
| 推荐和建议 | suggest, recommend, propose, necessity, necessary, expect |

---

## 环境 / 地学意义（地学论文常见末节）

前言 + 方法 + 结果讨论写完后，读者知道"做了什么、解决了什么问题"，但**意犹未尽 —— 知道了这些有什么用？**

这一节回答它，常作为 Discussion 的独立小节（如 4.3 Environmental significance / 4.3 Geological implications）。

> 无独立 Discussion 时读 §8.11.11：讨论可装进 METHODS / 嵌在引言 / 嵌在 Results / 由类群块 Comparison 承担。

---

## v2.16.1 - 局限自陈的七种句式（实测，可直接套用）

> Source: `references/ai-ml-paper-patterns.md` §9.6（8 个分片 31 篇）。

| # | 句式 | 逐字原文 |
|---|---|---|
| 1 | "It is worth noting that…" | "It is worth noting that…" |
| 2 | 单句点名 | "The limitation of the proposed method is the lack of…" |
| 3 | **警示句式**（顺带说"何时不该用"） | "Machine learning models and outputs should be used with caution in studies where…" |
| 4 | 条件句式 | "If the initial metaweb is too narrow…" |
| 5 | 先扬后抑 + 专设编号小节 | "4.1 Future Research" |
| 6 | **「因为做不到 X 所以不采用 Y」** | 散落在数据处理小节 |
| 7 | **方法论权衡句式**（每小节先优势后局限） | "the major advantage…" → "the major limitation…" |

另有两种**归因句式**：

- 域偏移的**并列归因**（不下断言）："The still remaining small shift might represent either a slight residual methodological drift, or genuine biological signal…"
- 承认域外后把责任归给训练数据："As the CNN training… and accuracy are independent from the camera itself"

🔴 七种句式指向的仍是**数据 / 对象本身**；只有第 3、7 种会顺带说到"何时不该依赖本方法"。
