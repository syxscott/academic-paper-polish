# Academic Paper Polish — English

> **This is the English entry point.** The 10 ready-to-use prompt modules live in
> [`prompts-en/`](../prompts-en/) — one file per module, each **self-contained**.

---

## How to use (no installation required)

1. Open the module you need in [`prompts-en/`](../prompts-en/)
2. Copy the code block
3. Replace the bracketed placeholder with your draft
4. Send it to any LLM — ChatGPT, Claude, Gemini, Copilot, or a local model

Each file contains its own prompt **plus** the hard rules and numbers it depends on, so you never need to read another file first. This matters because a prompt copied into a generic chatbot has no access to the rest of this repository.

---

## The 10 modules

| # | Module | File | One-line purpose |
|---|---|---|---|
| 1 | 📝 Abstract | [`01-abstract.md`](../prompts-en/01-abstract.md) | Compress the paper into its journal's word limit |
| 2 | 🔭 Introduction | [`02-introduction.md`](../prompts-en/02-introduction.md) | Inverted pyramid · gap argument · roadmap |
| 3 | 📚 Literature Review | [`03-literature-review.md`](../prompts-en/03-literature-review.md) | Make sources converse rather than accumulate |
| 4 | 🧪 Methods | [`04-methods.md`](../prompts-en/04-methods.md) | Survive peer reproduction |
| 5 | 📊 Results | [`05-results.md`](../prompts-en/05-results.md) | Report *what was found*, not *what it means* |
| 6 | 💡 Discussion | [`06-discussion.md`](../prompts-en/06-discussion.md) | Results ↔ literature ↔ theory ↔ limitations |
| 7 | 🎯 Conclusion | [`07-conclusion.md`](../prompts-en/07-conclusion.md) | Elevate without introducing new information |
| 8 | 🤖 De-AI Polish | [`08-deai-polish.md`](../prompts-en/08-deai-polish.md) | Final whole-manuscript humanisation pass |
| 9 | 🎯 Journal Matching & Submission | [`09-journal-submission.md`](../prompts-en/09-journal-submission.md) | Pick the journal **before** drafting |
| 10 | 💬 Reviewer Response | [`10-reviewer-response.md`](../prompts-en/10-reviewer-response.md) | Answer every point, with line references |

**Recommended order**: `9 → 2–7 → 10 → 8`

> ⚠️ Module 8 must come last, and it must never alter data, units, figure numbers, or conclusions.

---

## What this repository is

A set of **10 role-scoped prompts** covering the full academic writing pipeline, plus the methodology distilled from two geoscience writing courses and nine official journal style guides.

**Not a template. Not fill-in-the-blank. It's role + constraints + output spec for the LLM.**

| Source | Contribution |
|---|---|
| Zhang Peng (Researcher, China University of Geosciences, Wuhan), *How to Write a Research-Direction Literature Review*, 2026-10-16, 94 pp. | Methodological skeleton: inverted-pyramid introduction, journal-specific Results/Discussion rules, six-step discussion, review 18-step workflow, Elsevier ACCEPTANCE checklist |
| Tian Li (CUG), *Paper Writing Conventions & Techniques* / *Literature Review*, 2025-09-08, 43+35 pp. | Operational parameters: citation-density table, figure hard limits, three-stage submission review, 6–8 week schedule, search tooling |
| Nine official journal style guides | Journal-by-journal hard constraints (see [`references/multi-journal-style-guides.md`](../references/multi-journal-style-guides.md)) |

---

## The eight hard rules

### 1. Pick the journal before you write

This determines every structural decision downstream.

| Journal | Results/Discussion | Conclusion section |
|---|---|---|
| ***GCA*** | 🔴 **Must be separated**, independently numbered | Allowed |
| ***ES&T*** | 🔴 **Merged** into Results and Discussion | ❌ *"A separate conclusion is not to be used"* |
| ***Paleobiology*** | — | 🔴 Requires a separate **Non-technical Summary** |

> 🔴 **Format failure = desk rejection**, before the manuscript reaches an editor or reviewers.

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
| **Abstract / Conclusion** | **No citations at all** (PNAS exception: an abstract citation must be given in full inside the abstract *and* in the text) |

> Reviewing the literature more thoroughly does **not** reduce originality. Under-citing signals insufficient reading.

### 4. Paragraphs: 5–8 sentences

One- or two-sentence paragraphs are poor structure. Switch paragraphs when the subject changes.

### 5. The six-step discussion

```
① Recap the gap → ② Restate findings (with data/figures) → ③ Interpret and compare
→ ④ State limitations → ⑤ Implications for future work → ⑥ Conclusion
```

Step ④ is the one reviewers notice most when it is missing.

### 6. Conclusions must carry limitations + future directions

```
Despite its advantages, the [method] also has some limitations.
First, … Second, …
Further research should focus on …
```

### 7. Five citation mistakes

**Citing without citing · Quoting out of context · Inaccurate citation · Unreliable sources · Blind self-citation**

For review papers, ~**100 references** is the quality benchmark. Favour the last 5 years (ideally 1–3) and primary literature.

### 8. Geologic time: Ga/Ma/ka ≠ Gyr/Myr/kyr

| | Means |
|---|---|
| **Ga / Ma / ka** | 🔴 **Dates** (billions / millions / thousands of years ago) |
| **Gyr / Myr / kyr** | 🔴 **Duration** |

**upper/middle/lower** → rock or time-stratigraphic units; **early/late** → time units; capitalise Early/Middle/Late only for formally recognised ICS time units. Boundaries use `/`, ranges use `–`. *"Middle Cretaceous"* is non-standard.

---

## Figure hard limits

| Item | Requirement |
|---|---|
| Format | TIFF / JPG |
| 🔴 **Resolution** | **300 dpi minimum** |
| 🔴 File size | **<10 MB per figure / <50 MB total** |
| Fonts in figures | Arial, Helvetica, Times New Roman |
| Width (two-column journal) | Single column **<85 mm** / double **<180 mm** |
| Line weights | **0.25 and 0.5 mm combined** |
| Type sizes | **10&6** or **12&8**; 🔴 never below 4 pt |
| Caption | 🔴 Readable on its own |
| Table title | On the table itself |

**🔴🔴 The Word rule**: from figure creation → export → insertion into Word, **never scale diagonally or proportionally**.

**🔴 Copyright**: never paste a published figure directly (except OA or licensed); cite the source if modified; do not use politically disputed maps.

### Specimen photography (palaeontology)

- 🔴 **Photos must not be altered** beyond tone, contrast, and added labels or outlines
- Illuminate obliquely from the **upper left** unless shot in situ
- 🔴 **A scale bar with a stated numerical value is mandatory**; magnification factors such as ×40 are **not** acceptable
- 🔴 **AI tools must not create or modify images representing original observational or experimental data** (Elsevier / *Palaeoworld*)

### dpi by journal — the same photo, different requirements

| Journal | Photographs | Line art |
|---|---|---|
| *Paleobiology* | **600 dpi** | **1200 dpi** |
| *Acta Palaeontologica Polonica* | **400 dpi** | **400 dpi** |
| *PNAS* | **300 dpi** (600–900 with text) | **1000–1200 dpi** |
| Elsevier journals | **300 dpi** | **1000 dpi** |
| *Palaeontologia Electronica* | **300 ppi** | **300 ppi** |

> 🔴 **Preparing all specimen photos at 600 dpi at final size satisfies every journal above.**

---

## Submission review pipeline

| Work type | Pipeline |
|---|---|
| SCI paper | Technical check (format) → **Editorial screening (journal fit)** → Peer review |
| Thesis | Supervisor → **External examination** → Internal examination |

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

---

## Tool compatibility

See [`docs/COMPATIBILITY.md`](COMPATIBILITY.md) for the full matrix. Short version:

- **`AGENTS.md`** is the cross-vendor single source of truth (Codex, Cursor, Copilot, opencode, Qoder, ZCode, MiniMax Code, Windsurf, VS Code, WorkBuddy read it natively).
- **`CLAUDE.md`** is a one-line `@AGENTS.md` shim for Claude Code.
- **`SKILL.md`** follows the Agent Skills spec; its `name` **must equal the directory name** or loading fails silently.

English-language contributors: the `prompts-en/` modules are the translation surface. When you update a Chinese module in `prompts/`, mirror the change here. Pull requests welcome.
