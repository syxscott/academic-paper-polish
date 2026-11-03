# Module 4 · Methods Polish

> **How to use**: copy the code block below, replace the placeholder, send to any LLM. Self-contained.

```text
Review and optimise the methods section I provide, ensuring it is rigorous, clear, and
reproducible.

- **Research design**: check that the study type (experiment, survey, case study,
  meta-analysis, etc.) is stated explicitly, along with the justification for its
  suitability — why this design can effectively answer the research question.
- **Data collection / processing**: check that each of the following is stated:
  (1) data source (database name / collection platform / experimental environment);
  (2) sample size and inclusion/exclusion criteria; (3) time range of collection;
  (4) missing-value handling and the reason for it. Flag any omission and require it to
  be supplied.
- **Model / algorithm description**: for the core model or algorithm, check that the
  mathematical notation is correct, key assumptions are listed explicitly, and
  implementation details (hyperparameters, train/test split, hardware and software) are
  sufficient for others to reproduce.
- **Evaluation metrics**: check that the chosen metrics are tightly relevant to the
  research objective and that their definitions and formulae are clear and correct. If a
  better alternative exists, propose it and explain why.

Process the methods section below:
[PASTE YOUR METHODS DRAFT HERE]
```

---

## Earth-science / experimental-science additions

### Four-part pattern
1. Objective description of the **regional geological setting, climatic background, environmental parameters**
2. **Sampling method and sample count**
3. **Experimental method, instrument conditions, software versions**
4. 🔴 **Key point: after reading, a reader should know how to conduct and how to reproduce the work**

### Self-check (any omission is a fail)
- [ ] Study/experimental design + justification (why this design answers the question)
- [ ] Sampling localities / depths / coordinates / dates
- [ ] Sample count and preservation conditions
- [ ] Instrument model + operating conditions (temperature, pressure, pH, concentration, calibration)
- [ ] Data-processing software and version
- [ ] Missing-value / outlier handling and justification

### Common errors
- ❌ No citations and no standard protocol (home-grown? not accepted?)
- ❌ Insufficient detail — **others cannot reproduce it**

---

## Citation density

**The methods section also needs citations** — to the **standard protocols and established methods**, not to your results.

| Situation | Cite? |
|---|---|
| Adopting a standard method | ✅ Cite the original method or standard |
| Your own modified method | ✅ Cite the original and state the modification |
| Routine operations (cleaning, drying) | May omit, but state the parameters |
| **Your experimental results** | ❌ No (that belongs to Results) |

---

## Data and code availability (required by most journals)

- Data availability: repository DOI / attachment / available on request
- Code availability: GitHub URL + DOI (e.g. Zenodo)
- 🔴 If unavailable, you must state why — silence is not an option

**Journal-specific requirements**

| Journal | Requirement |
|---|---|
| *PNAS* | 🔴 Data sharing plan submitted **at submission**; the main text must stand alone without the SI |
| *Earth-Science Reviews* | Option C: deposit in a repository + cite and link, **or** explain why sharing is impossible |
| *Paleobiology* | FAIR principles; Dryad/Zenodo **fully paid by the journal**; **the DOI must be the final DOI**, never the private peer-review link |
| *Acta Palaeontologica Polonica* | Joint Data Archiving Policy: Dryad / MorphoBank / GenBank; embargo up to one year permitted |
| *Palaeontologia Electronica* | Single file ≤50 MB, total ≤200 MB |

> 🔴 **References inside Supplementary Material must not appear in the main Literature Cited.**


---

## v2.16.0 - Evidence-based additions for METHOD-CLASS (AI / data-driven) papers

> Source: `references/ai-ml-paper-patterns.md` 4 (50 fossil+AI papers read verbatim).
> **These are observed practices, not prescriptions.**

### The six mandatory dataset items

| Item | Observed wording (verbatim) | Source |
|---|---|---|
| Source and query | taxon name + download date: "taxon/taxa name 'Ammonoidea'", "10 November, 2020" | Foxon 2021 |
| Initial N -> cleaning rule -> final N | "Outlying cases or samples that contain very few coccoliths ... have been removed from the analyses." | Boeckel & Baumann 2004 |
| Per-class sample size | tabulated per class with a percentage column | Duan 2023 |
| Annotation | "manually cropped and labeled by an expert diatomist" | Bueno et al. 2017 |
| Split ratio | "a 10-fold cross-validation has been applied" / "~85% / ~15%" | Bueno 2017 / Duan 2023 |
| Class imbalance | "The conodont dataset collected in this study has two problems: the dataset is small and imbalanced." + weighted loss "Weighti = 1 - ni/N" | Duan 2023 |

### Data magnitudes in this field (state them, or the work looks implausible)

613 images / 9 conodont species - 781 specimens / 11 ammonite species - 24,000 images / 80 diatom taxa -
34,640 images / 35 planktic foraminifera species.

### Environment versions (most often omitted, most often asked for)

> "All models were trained using an NVIDIA GeForce RTX 2070 graphics card, and the operating system
> version was Windows 10 Professional. Python version 3.7.0 was used, along with PyTorch version 1.10.0
> and CUDA version 10.2." - Duan 2023

### Always report a naive baseline

> "the simplest baselines ... are given by using transfer learning via ImageNet-initialised off-the-shelf
> CNN architectures" - Karaderi 2022; the ammonite study writes the majority-class baseline explicitly:
> **148/781 = 0.190** - Foxon 2021
