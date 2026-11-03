# Module 7 · Conclusion Polish

> **How to use**: copy the code block below, replace the placeholder, send to any LLM. Self-contained.

```text
Rewrite or optimise my conclusion so that it closes the paper forcefully and elevates the
value of the research.

- **Core recap**: restate the core question, key method, and main findings in concise
  language. Avoid simply repeating sentences from the abstract or introduction; use new,
  more general phrasing.
- **Restating the contribution**: re-emphasise, in highly condensed form, the most
  important theoretical contribution and practical significance, so that this is the core
  message readers leave with.
- **No new information**: check whether the conclusion introduces concepts, data, or
  arguments not previously mentioned. A conclusion closes the paper; it does not start a
  new one.
- **Broader vision (optional)**: at the end, a wider perspective may be offered on where
  the field is heading, and where this study sits in that picture and its potential
  long-term influence — giving the ending both closure and inspiration.

Process the conclusion below:
[PASTE YOUR CONCLUSION DRAFT HERE]
```

---

## 🔴 Do / Don't

| ✅ Do | ❌ Don't |
|---|---|
| Summarise your overall findings | Repeat background information from the Introduction |
| Provide a synthesis of key points | Present new arguments or evidence |
| Highlight the important takeaways | Draw conclusions not supported by your data |
| Point out the problems and questions remaining | Be abrupt and leave a reader hanging |
| Indicate future directions | |
| **End with a strong, final sentence** | |

---

## 🔴 Two things the conclusion must carry

1. **Summary and highlight** — the significance of the work at a high level; foreground the innovation
2. **Direction** — not only what you did and found, but:
   - the theoretical and/or practical implication
   - **the limitations**
   - the problems not yet solved
   - where the field should go next

---

## 🔴 Journal difference: the conclusion section may not exist

| Journal | Conclusion section |
|---|---|
| ***ES&T*** | ❌ *"A separate conclusion is not to be used"* — concluding statements fold into Results and Discussion |
| ***GCA*** | Allowed |

**Check the target journal's guide for authors before drafting.**

## Length

One to two paragraphs, briefly presenting the most important conclusions of the paper.

**Model structure** (GCA-style):
- Paragraph 1: what was done + the main finding and its mechanism (e.g. under anoxic conditions ·OH is generated mainly by surface sulfur-defect oxidation of H₂O(ad); under oxic conditions mainly by O₂ reduction, with H₂O₂ the key intermediate…)
- Paragraph 2: implications for the fate of organic contaminants and redox-active elements, especially in flowing environments


---

## v2.16.0 - Conclusions in METHOD-CLASS papers

> Source: `references/ai-ml-paper-patterns.md` 6.3, 7.

### A method-class conclusion must state its boundary of validity

> "The optimal classifer, c6, obtained an AUC value of 0.9 on the test set. This was a good result for the
> classication of a conodont species, especially considering that the model was trained in the low data
> regime, and some conodont images have natural defects (e.g., some parts of the fossil were missing and
> the surface of the fossil was covered by colloid)." - Duan 2023

> "Machine learning models and outputs should be used with caution in studies where quantification of the
> abundance of rare species is a central goal, as the models we show..." - Kahanamoku et al. 2024

**"Not every task suits AI" recurs across this corpus** - a method-class conclusion must answer
**"when should this method NOT be used"**.

### Skeletons are not interchangeable (descriptive vs method-class)

| Component | Descriptive | Method-class |
|---|---|---|
| Geological setting | almost always | **0/50** |
| Repository | required | **0/50** |
| Systematic | core section | **0/50** |
| Standalone Results | usually absent | **46 % present** |
| Standalone Discussion | absent in 65 % | **48 % present** |
| Standalone Conclusion | present | **52 % present** |
