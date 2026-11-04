# Module 6 · Discussion Polish

> **How to use**: copy the code block below, replace the placeholder, send to any LLM. Self-contained.

```text
Perform a deep optimisation of my discussion section. Help me bring my results into
dialogue with the existing literature and excavate their theoretical and practical meaning.

- **Interpreting results**: check whether the interpretation of the core results is deep
  enough. Help me move beyond restating the results ("as shown in Figure X, Y rose") and
  explain the underlying mechanism or cause.
- **Dialogue with the literature**: identify places where my results can be directly
  compared with, or connected to, important papers mentioned in the introduction or
  literature review. State explicitly the extent to which my findings support, challenge,
  or extend prior work.
- **Theoretical contribution**: based on the findings, help me distil one to three clear,
  specific theoretical contributions. For example: does it propose a new conceptual
  framework? Does it validate or correct an existing theory? Does it reveal a new causal
  relationship?
- **Practical implications**: think through and propose specific, actionable implications
  of the findings for the relevant field (industry, policy, clinical practice, etc.).
- **Limitations and future research**: check whether the stated limitations are honest,
  specific, and constructive. Ensure the future research directions that follow from them
  are well-targeted rather than generic.

Process the discussion below:
[PASTE YOUR DISCUSSION DRAFT HERE]
```

---

## 🔴 The six-step discussion (all six are mandatory)

```
① Recap the gap        → restate the scientific question and purpose
② Restate findings     → 🔴 with data and figures, not prose restatement
③ Interpret            → meaning; comparison with others; similarities, differences, causes
④ State limitations    → 🔴 their potential effect on the results
⑤ Implications         → how to explore further
⑥ Conclusion           → revisit the question and the result
```

**Step ④ is the one reviewers notice most when it is missing.**

---

## 🔴 Citation density: 5–8 sentences per paragraph

```
topic sentence                    ← 1 sentence
sentences carrying citations      ← 3–4 sentences  ← your results in dialogue with others
sentences carrying your own data  ← 2–3 sentences  ← your own evidence
```

| Error | Why it fails |
|---|---|
| A whole paragraph with **no citations at all** | That is a restatement of Results, or a conclusion drawn without comparison |
| A whole paragraph with **no data of your own**, all references | That is a review, not a discussion |
| Paragraphs of 1–2 sentences | Structure is too fragmented |

---

## Limitations + future directions (ready to use)

```
Despite its advantages, the [method] also has some limitations.
First, [limitation 1: constrained by the instrument / probe / method itself].
Second, [limitation 2: which prevents some application, e.g. field measurement].
Further research should focus on [identifying a suitable X] and [developing a device
that supports Y].
```

**Worked example** (redox-capacity measurement of Fe/Mn minerals):
1. First — measurable only at −0.4 V vs SHE for EAC and 0.7 V vs SHE for EDC, constrained by the lack of suitable chemical probes
2. Second — under oxidising conditions the chemical probes themselves vary too much → unsuitable for **field measurement**
3. Further research should focus on — identifying suitable chemical probes + developing a device supporting reliable field measurement

---

## Verbs by function

| Function | Verbs |
|---|---|
| Stating a claim or your view | suggest, report, present, expect, describe |
| Supporting an argument | support, provide, indicate, identify, find, demonstrate, confirm, clarify |
| Recommending | suggest, recommend, propose, necessity, necessary, expect |

---

## Environmental / geological significance (common final subsection in geoscience)

After the introduction, methods, and results-and-discussion, readers know *what you did* and *what problem you solved* — but are left wanting: **so what?**

This subsection answers it, commonly appearing as an independent section such as 4.3 Environmental significance or 4.3 Geological implications.


---

## v2.16.0 - Discussion in METHOD-CLASS papers

> Source: `references/ai-ml-paper-patterns.md` 6.2, 4.5 (50 papers).

### Three observed shapes

| Shape | Practice | Source |
|---|---|---|
| 1. Separate Discussion + dedicated "Threats to validity" section | "5.2 Threats to validity and areas for future work", numbered limits | Duan 2023 |
| 2. Separate Strengths + Limitations, closing the paper | no Discussion heading; paper ends with Strengths then Limitations | Foxon 2021 |
| 3. Discussion folded into the end of each results subsection | each subsection: experiment -> explanation -> comparison with literature -> meaning for the field | Bueno 2017 |

### Attribute errors to the fossils, not to the model

> "Segmentation faults, including omissions, misidentifications and incomplete segmentations, were rarely
> seen and mostly occurred in poor-preserved fossils." - Huang et al. 2024

Limits in method-class papers are about **the data and the objects**: specimen breakage, damaged texture,
class imbalance, life-cycle morphological variation, viewing angle - not about the model being weak.

---

## v2.16.1 - Seven sentence patterns for stating limitations (measured)

> Source: `references/ai-ml-paper-patterns.md` section 9.6 (8 shards, 31 papers).

| # | Pattern | Verbatim |
|---|---|---|
| 1 | "It is worth noting that…" | "It is worth noting that…" |
| 2 | Single-sentence naming | "The limitation of the proposed method is the lack of…" |
| 3 | **Caution pattern** (also says when NOT to use it) | "Machine learning models and outputs should be used with caution in studies where…" |
| 4 | Conditional | "If the initial metaweb is too narrow…" |
| 5 | Concession + dedicated numbered subsection | "4.1 Future Research" |
| 6 | **"Because X could not be done, Y was not adopted"** | scattered in the data-processing subsection |
| 7 | **Method-trade-off pattern** (advantage first, limitation second, per subsection) | "the major advantage…" → "the major limitation…" |

Two attribution patterns worth stealing:

- **Parallel attribution for domain shift** (no assertion): "The still remaining small shift might represent either a slight residual methodological drift, or genuine biological signal…"
- Admit out-of-domain, then attribute it to the training data: "As the CNN training… and accuracy are independent from the camera itself"

🔴 All seven still point at **the data and the objects**; only #3 and #7 add "when not to rely on this method".
