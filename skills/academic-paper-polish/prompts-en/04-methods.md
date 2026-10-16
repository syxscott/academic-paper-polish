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
