# Academic Paper Polish — English Reference

> The prompts are written in Chinese. This file is the English **reference and methodology summary**.
> For English-language use, translate the corresponding `prompts/*.md` module and apply the same rules.

---

## What this repository is

A set of **10 role-scoped prompts** covering the full academic writing pipeline, plus the methodology distilled from two geoscience writing courses:

| Source | What it contributes |
|---|---|
| Zhang Peng (Researcher, CUG Wuhan), *How to Write a Research-Direction Literature Review*, 2026-10-16, 94 pp. | The **methodological skeleton**: inverted-pyramid introduction, journal-specific Results/Discussion rules, six-step discussion, review 18-step workflow, Elsevier ACCEPTANCE checklist |
| Tian Li (CUG), *Paper Writing Conventions & Techniques* / *Literature Review*, 2025-09-08, 43+35 pp. | The **operational parameters**: citation-density table, figure hard limits, three-stage submission review, 6–8 week schedule, search tooling |

**Not a template. Not fill-in-the-blank. It's role + constraints + output spec for the LLM.**

---

## The 10 modules

| # | Module | Tagline |
|---|---|---|
| 1 | Abstract | Compress the paper into ~300 words |
| 2 | Introduction | Inverted pyramid · gap argument · roadmap |
| 3 | Literature Review | Make sources "converse" rather than enumerate |
| 4 | Methods | Survive peer reproduction |
| 5 | Results | Report *what was found*, not *what it means* |
| 6 | Discussion | Results ↔ literature ↔ theory ↔ limitations |
| 7 | Conclusion | Elevate without introducing new information |
| 8 | De-AI Polish | Whole-manuscript humanization (final step) |
| 9 | Journal Matching & Submission | Pick the journal **before** drafting |
| 10 | Reviewer Response | Answer every point, with line references |

Recommended order: **9 → 2–7 → 10 → 8**

---

## The seven hard rules

### 1. Pick the journal before you write

This determines every structural decision downstream.

| Journal | Results/Discussion | Conclusion section | Envelope |
|---|---|---|---|
| **GCA** | **Must be separated**, independently numbered | Allowed | Rejects pure methods/technical/modelling papers; rejects regional case studies; cover letter **must** name 3 Associate Editors |
| **ES&T** | **Merged** into Results and Discussion | ❌ *"A separate conclusion is not to be used"* | 7,000 words |
| **PPP** | — | — | Articles 5,000–7,000 words / 4–8 figures; single column <85 mm, double <180 mm |
| **Earth-Science Reviews** | — | — | IF > 10 |
| **Biological / Chemical / Nature Reviews** | — | — | IF > 14 / > 50 / 46–123 |

> **Format failure = desk rejection.** Format is the first impression, the baseline of academic literacy, and reviewers are hunting for errors. Format comments usually outnumber content comments.

### 2. Inverted pyramid, and opening must match resolution

| Shape | Term | Reader reaction |
|---|---|---|
| Opening wider than resolution | *overpromising* | Feels cheated |
| **Opening = resolution** | ***on target*** | **Satisfied** |
| Resolution wider than opening | *underpromising* | No story worth following |

### 3. Citation density

| Section | Requirement |
|---|---|
| **Introduction** | Everything except the problem statement and transitional sentences needs citations |
| **Results** | **Essentially none** |
| **Discussion** | **5–8 sentences per paragraph** = topic sentence + **3–4 cited sentences** + **2–3 sentences on your own data** |
| **Abstract / Conclusion** | **No citations at all** |

> Reviewing the literature more thoroughly does **not** reduce originality. Under-citing signals insufficient reading.

### 4. Paragraphs: 5–8 sentences

One- or two-sentence paragraphs are poor structure. Switch paragraphs when the subject changes.

### 5. The six-step discussion

```
① Recap the gap  ② Restate findings (with data/figures)
③ Interpret and compare with others  ④ State limitations
⑤ Implications for future work  ⑥ Conclusion
```

**Step ④ is the one reviewers notice most when it's missing.**

### 6. Conclusions must carry limitations + future directions

```
Despite its advantages, the [method] also has some limitations.
First, … Second, …
Further research should focus on …
```

### 7. Five citation mistakes

**Citing without citing · Quoting out of context · Inaccurate citation · Unreliable sources · Blind self-citation**

For review papers, ~**100 references** is the quality benchmark. Favour the last 5 years (ideally 1–3) and primary literature.

---

## Figure hard limits

| Item | Requirement |
|---|---|
| Format | TIFF / JPG |
| Resolution | **300 dpi minimum** |
| File size | **<10 MB per figure / <50 MB total** |
| Fonts in figures | Arial, Helvetica, Times New Roman |
| Width (two-column journal) | Single column **<85 mm** / Double **<180 mm** |
| Line weights | **0.25 and 0.5 mm combined** |
| Type sizes | **10&6** or **12&8**; **never below 4 pt** |
| Caption | Must be **self-sufficient** |
| Table title | **On the table itself** |

**Never scale figures diagonally when inserting into Word** — it distorts proportions and resolution.

**Copyright:** never copy a published figure directly (except OA or licensed); cite the source if modified; **do not use politically disputed maps**.

---

## Wording discipline

| ❌ Avoid | ✅ Prefer |
|---|---|
| *for the first time* | State the concrete difference from prior work |
| "first proposed / first discovered / internationally advanced" | State only the objective increment |
| *The deficiency of Wang's approach is…* | *However, the mechanism has not been fully understood.* |

Every novel paper can call itself "the first". "First" should be reserved for **genuinely important advances**.

---

## Submission review pipeline

| Work type | Pipeline |
|---|---|
| **SCI paper** | Technical check (format) → **Editorial screening (journal fit)** → Peer review |
| **Thesis** | Supervisor → **External examination** → Internal examination |

**Format failure means desk rejection before stage two.**

### Elsevier's "ACCEPTANCE" checklist

By Nigel John Cook (EiC, *Ore Geology Reviews*):

**A**ttention to details · **C**heck and double check · **C**onsider the reviews · **E**nglish must be as good as possible · **P**resentation is important · **T**ake your time with revision · **A**cknowledge those who helped · **N**ew, original and previously unpublished · **C**ritically evaluate your own manuscript · **E**thical rules obeyed

---

## Reviewer response — four elements

```
→ Thanks for this concern. As suggested, we supplemented the experiments…
→ To address the reviewer's concern, the original statement "…" was revised
  to "…" (Lines 193–195).
→ In addition, the Fig. R1 was copied as Fig. S5 in the revised supporting information.
```

**Thanks → action taken → which line changed to what → supporting-material numbering**

Six disciplines: answer every point · run the requested experiments where possible · explain honestly what you can't do and why · **cite the papers reviewers recommend** · **do not fight reviewers** · thank them.

---

## Schedule

One journal article (4–8 figures + 5,000–7,000 words) ≈ **6–8 weeks**
```
1–2 figures per week + 2–3 sentences per day (~15 words each)
= 1 figure every 3 days, 3 sentences a day = 2 months per paper
```

Imitating published sentences as practice is fine, but **5+ consecutive identical characters = plagiarism**; uncited imitation carries the same risk.

---

## Hard limits on AI assistance

An AI writing assistant must never: alter data, units, or figure numbers · change one conclusion into another · present unverified speculation as fact · delete key citations to reduce similarity · fabricate references · promise AI-detection passage · suggest copying published figures.

**Polish must not change the science.** Wording and structure may change; data and scientific claims may not.

The goal is not "passing detection" — it is reading like a person while keeping information density high.

---

## Tool compatibility

See [`COMPATIBILITY.md`](COMPATIBILITY.md) for the full matrix. Short version:

- **`AGENTS.md`** is the cross-vendor single source of truth (Codex, Cursor, Copilot, opencode, Qoder, ZCode, MiniMax Code, Windsurf, VS Code, Zed, WorkBuddy read it natively).
- **`CLAUDE.md`** is a one-line `@AGENTS.md` shim for Claude Code.
- **`SKILL.md`** follows the Agent Skills spec; its `name` **must equal the directory name** or loading fails silently.