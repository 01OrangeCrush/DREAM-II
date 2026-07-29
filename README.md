# DREAM II: Prompt Fidelity and AI-Resilient Assessment Evaluation

DREAM II is a pilot study of whether a frozen large language model (LLM) can apply a published AI-resilient assignment-design rubric consistently when evaluating cybersecurity assignment prompts. Four faculty evaluators and a corrected, prompt-faithful LLM independently scored ten public prompts.

The repository's central methodological lesson is simple: **a polished LLM evaluation can use the wrong rubric without announcing the substitution**. Prompt fidelity must be verified before reliability statistics or validity claims are interpreted.

> **Project status:** Manuscript under anonymous review for ACM SIGCITE 2026. This public repository is reserved for the replication package and does not reveal the anonymous submission URL. Human-participant data collection must not begin until the required Penn State IRB determination or approval is in place.

## What to inspect first

Readers can understand the main contribution in about five minutes:

1. Open the [pre-fidelity drift example](prompts/DREAM_II_PreFidelity_Drift_Example.md). Read the one-sentence prompt, then compare the requested rubric dimensions with the five plausible but unrequested criteria returned by the model.
2. Open the [final frozen evaluator prompt](prompts/DREAM_II_LLM_Scoring_Script_Combined.md). Visually locate the embedded rubric, the substitution prohibition, the exact preflight dimension check, the anchor-linked rationale requirement, and the midpoint re-check.
3. Use the [Prompt Fidelity Inspection Guide](docs/PROMPT_FIDELITY_INSPECTION_GUIDE.md) to compare the two artifacts side by side.

### The drift at a glance

| Published rubric required | Early model returned |
|---|---|
| Authenticity | Real-World Relevance |
| Process Transparency | Complexity & Critical Thinking |
| Ethical GenAI Use | Open-Endedness / Student Agency |
| Interactive Verification | Authentic Evaluation Criteria |
| Evaluative Judgment | AI / Academic Integrity Vulnerability |

The drifted response still had five labels, integer scores, rationales, a total out of 15, and a redesign recommendation. Its form looked correct; its construct was not. **Inspect labels and anchors before numbers.**

## Research focus

The project evaluates the operational consistency of the rubric and the fidelity of the LLM evaluation process. It does not evaluate faculty performance, students, student work, grades, educational records, or protected health information.

The five published dimensions are:

1. Authenticity
2. Process Transparency
3. Ethical GenAI Use
4. Interactive Verification
5. Evaluative Judgment

Each dimension is scored from 1 (not addressed) to 3 (fully addressed). A total below 10 of 15 is flagged for revision.

## Why the final prompt is different

The early prompt referred informally to a rubric in an attached PowerPoint and asked the model to evaluate an assignment. It did not prove that the model had recovered the intended instrument. The repaired prompt therefore:

- embeds the complete rubric and its anchor language;
- prohibits renaming, supplementing, substituting, or reconstructing another framework;
- requires the model to enumerate the five dimensions exactly before any scoring;
- binds every rationale to assignment evidence and the relevant anchor;
- repeats the fidelity check halfway through the run; and
- stops scoring when verification fails.

These are broadly useful GenAI controls whenever a task depends on a rubric, policy, schema, taxonomy, or checklist.

## Reproducibility workflow

1. Freeze the model, platform, evaluator prompt, artifact order, and session settings.
2. Run and verify the five-dimension preflight check.
3. Submit artifacts one at a time in the seeded order documented in the evaluator script.
4. Repeat the fidelity check at the midpoint.
5. Preserve any failed output as a fidelity-failure artifact; do not relabel or score it after the fact.
6. Collect faculty scores using coded reviewer tabs (Reviewer A-D); names must not appear in analytic files.
7. Validate spreadsheet ranges, threshold coding, and scoring completeness before analysis.
8. Compute descriptive statistics, percent agreement, Gwet's AC1, and weighted Cohen's kappa as specified in the analysis plan.
9. Report results only in aggregate; do not rank or identify individual evaluators.

## Repository map

- `prompts/DREAM_II_PreFidelity_Drift_Example.md` - documented criterion-substitution failure and why it looked trustworthy.
- `prompts/DREAM_II_LLM_Scoring_Script_Combined.md` - frozen final evaluator with initial and midpoint fidelity checks.
- `docs/PROMPT_FIDELITY_INSPECTION_GUIDE.md` - side-by-side reader inspection path and pass/fail rule.
- `docs/METHODS.md` - study design, scoring protocol, and planned analyses.
- `docs/REPRODUCIBILITY.md` - run metadata and integrity checklist.
- `docs/ETHICS_AND_PRIVACY.md` - participant and repository safeguards.
- `docs/DATA_DICTIONARY.md` - public metadata and scoring fields.
- `data/artifact_catalog.csv` - source links, licenses, and seeded artifact order.
- `templates/DREAM_II_Rubric_Scoring_Workbook_Coded.xlsx` - blank coded faculty-scoring workbook.

## Data availability and boundaries

This repository may contain public-source artifact metadata and links, blank or coded templates, frozen prompts, analysis scripts, fidelity-failure examples, and de-identified or aggregate results approved for release.

Do **not** upload evaluator identities or linkage files, identifiable scoring workbooks, IRB correspondence, identifiable consent records, restricted copyrighted artifacts, confidential Penn State records, or credentials. Any temporary reviewer linkage must be stored separately on an approved Penn State system and destroyed according to the approved protocol.

The pre-study source packet included assignment text with varying rights. The repository therefore distills the documented drift episode without republishing that assignment packet. Required scholarly and third-party attribution is retained.

## Licensing

Except where otherwise noted, original documentation, research instruments, prompts, metadata, and released datasets are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Third-party materials are excluded and retain their respective terms. See `LICENSE`, `LICENSE_NOTES.md`, and `data/artifact_catalog.csv`.

## Citation

Citation metadata are provided in `CITATION.cff`. Update conference status, DOI, pages, release version, and archival identifiers after acceptance.

## Authors and contact

Jennifer McCauley; Edward J. Glantz; Mahdi Nasereddin; Michael R. Bartolacci  
College of Information Sciences and Technology  
The Pennsylvania State University  
Contact: Edward J. Glantz, PhD - ejg8@psu.edu

## Disclaimer

This repository is a research artifact. Its presence does not indicate IRB approval, publication acceptance, endorsement by Penn State, or validation for high-stakes educational decisions. The LLM workflow supports disclosed faculty review and triage; it is not a replacement for faculty judgment.
