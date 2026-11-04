# Module 5 · Results Polish

> **How to use**: copy the code block below, replace the placeholder, send to any LLM. Self-contained.

```text
Optimise my results section so that the presentation is objective, clear, and compliant
with academic figure and table convention.

- **Objectivity**: remove all subjective, interpretive, or speculative language (for
  example "surprisingly", "unexpectedly", "this seems to suggest"). This section reports
  only what was found. The "why" and the "what it means" belong to the discussion.
- **Logical structure**: check that the presentation order matches the order in which the
  research questions or hypotheses were posed, so readers can follow the logic.
- **Figure and table citation**: ensure every figure and table is explicitly cited in the
  text (e.g. "as shown in Figure 1"). Check that titles are concise and information-dense,
  and that key elements (axes, legends, units, abbreviations) are clear without forcing
  readers back into the body text.
- **Figure-type match**: check that the chart type matches the data type (bar for
  categorical, scatter for continuous relationships, line for trends). If mismatched,
  propose a replacement and explain why.

Process the results section below (figure descriptions may be attached):
[PASTE YOUR RESULTS DRAFT HERE]
```

---

## 🔴 Results vs Discussion: different axes

The same body of results is reorganised along **different axes** in the two sections:

| | Organising logic | Example structure |
|---|---|---|
| **Results** | By **product / measurement** in parallel | 3.1 OH yield · 3.2 H₂O₂ yield · 3.3 Fe²⁺ + SO₄²⁻ · 3.4 XRD/SEM-EDS/XPS · 3.5 Substrate oxidation |
| **Discussion** | By **mechanism**, converging | 4.1 Anoxic oxidation mechanism · 4.2 Oxic oxidation mechanism → 4.2.1 H₂O₂ formation and decomposition / 4.2.2 Relative contribution of each pathway / 4.2.3 Mechanism summary · 4.3 Environmental significance |

### Journal differences (confirm before drafting)

| Journal | Requirement |
|---|---|
| ***GCA*** | Results and Discussion **must be separated**, independently numbered; Results gives data and observations only, **no mechanistic discussion** |
| ***ES&T*** | **Merged** into Results and Discussion; *be complete but concise*; **no separate conclusion section** |

---

## 🔴 Citation density: Results carries almost none

| Error | Why it fails |
|---|---|
| Results saturated with **published (cited) data** | That belongs in the Discussion |
| Mechanistic explanation inside Results ("this indicates…") | That belongs in the Discussion |

> Cite only when **comparing your own data with published data** — and cite only the paper being compared.

---

## 🔴 Figure hard limits (the technical-check gate)

| Item | Requirement |
|---|---|
| Format | TIFF / JPG |
| 🔴 **Resolution** | **300 dpi minimum** |
| 🔴 File size | **<10 MB per figure / <50 MB total** |
| Fonts in figures | Arial, Helvetica, Times New Roman |
| Width (two-column journal) | Single column **<85 mm** / double **<180 mm** |
| Line weights | **0.25 and 0.5 mm combined** |
| Type sizes | **10&6** or **12&8**; 🔴 **never below 4 pt** |
| Caption | 🔴 **Readable on its own — a reader should understand the figure from the caption alone** |
| Table title | **On the table itself** |

### 🔴🔴 The Word scaling rule
> **From figure creation → export → insertion into Word, never scale diagonally or proportionally.**
> It destroys proportions and resolution. Do not drag corners in Word.

### 🔴 Copyright red lines
- **Never paste a published figure directly** (except OA or licensed); **cite the source if modified**
- **Do not use politically disputed maps**

### Composition
- **Golden ratio 0.618** beats the rule of thirds; put subject edges on the thirds lines for balance
- **Symmetry** → rigour, stability, classification; **asymmetry** → change, dynamics, evolution

### Colour
- Avoid relying on colour alone as the discriminator — a significant share of readers have colour-vision deficiency (**red-green is most common**). Add a second discriminator.
- *Paleobiology* additionally bans **red/blue, red/green, blue/green, blue/yellow** pairs.

### Specimen photography (palaeontology-specific)
- 🔴 **Photos must not be altered** beyond tone, contrast, and added labels or outlines
- Illuminate **obliquely from the upper left** unless shot in situ
- 🔴 **A scale bar with a stated numerical value is mandatory**; magnification factors such as ×40 are **not** acceptable because the figure may be resized in print
- Scale bars must be of uniform thickness

## Journal-specific dpi (same photo, different requirements)

| Journal | Photographs | Line art |
|---|---|---|
| *Paleobiology* | **600 dpi** | **1200 dpi** |
| *Acta Palaeontologica Polonica* | **400 dpi** (non-interpolated, uncompressed) | **400 dpi** |
| *PNAS* | **300 dpi** (600–900 if the figure contains text) | **1000–1200 dpi** |
| Elsevier journals | **300 dpi** | **1000 dpi** |
| *Palaeontologia Electronica* | **300 ppi** (150 ppi allowed for first PDF) | **300 ppi** |

> 🔴 **Preparing all specimen photos at 600 dpi at final size satisfies every journal above.**


---

## v2.16.0 - Figure types unique to METHOD-CLASS papers

> Source: `references/ai-ml-paper-patterns.md` 5 (50 papers).

| Figure type | Verbatim caption | Source |
|---|---|---|
| Confusion matrix | "The confusion matrix is generated based on the prediction results of the final classifer on the test dataset." | Duan 2023 |
| ROC curves | "The ROC curves are generated based on the prediction results of the final classifer on the Test set." | Duan 2023 |
| Feature space | "Data features visualized by t-SNE (A), visualize original data features; (B), visualize the last layer of features after training on the original data." | Duan 2023 |
| Network architecture | "Overview of the convolutional neural network used and its procedures in the experiment." | Duan 2023 |
| Error cases | "Some incomplete fossil samples [(A), the part enclosed by the white oval dotted line] and samples with surfaces attached to colloids (B)." | Duan 2023 |

**Fixed confusion-matrix caption convention**: rows = ground truth, columns = prediction, cell = percentage, diagonal = 100 %.

**Table note convention**: bold the best value; footnote markers (a/b) for input size etc.; **put training /
inference time in the same table as the accuracy metrics** - compute cost is reported as a first-class dimension.

---

## v2.16.1 - Actual frequency of method-class figures (pooled, 31 papers)

> Source: `references/ai-ml-paper-patterns.md` sections 9.1 / 9.5.

| Figure / practice | Measured rate | Verbatim |
|---|---|---|
| Confusion matrix | **11/24 = 45.8%** (strict: main-text figure only, 10/24 = 41.7%) - 🔴 **not a "standard"**; nearly half substitute a per-class F1/Precision/Recall table | "The confusion matrix is generated based on the prediction results of the final classifer on the test dataset." |
| Stand-alone hyper-parameter table | **2/21 = 9.5%** | see 9.1 |
| Statistical tests | **5/30 = 16.7%** (a minority; most use "mean +/- SD over 10 runs" instead) | see 9.1 |
| Training / loss curves | **3/22 = 13.6%**, and often pushed into the supplement | "The training and validation iterations are given in Supplements 4.2 figure S1, which confirms that the data is neither overfit, nor underfit." |
| Interpretability figure | Three routes coexist: Grad-CAM / saliency map / **none at all**; not a requirement | "the weighted activation heatmap (Grad-CAM) (Servaraju et al., 2017) ... centered around the thoracic and abdominal walls of the specimens" |

🔴 **Training curves and Grad-CAM are frequently pushed into supplementary material** (shard_02 CH3 / CH4-1).
