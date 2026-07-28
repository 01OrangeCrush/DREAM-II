# DREAM II: Prompt Fidelity and AI-Resilient Assessment Evaluation

DREAM II is a pilot study examining whether a frozen large language model (LLM) can apply a published AI-resilient assignment-design rubric consistently when evaluating cybersecurity assignment prompts. The study compares coded faculty-evaluator scores with scores produced by a frozen LLM evaluator.

> **Project status:** Protocol and materials development. Human-participant data collection must not begin until the required institutional review determination or approval is in place.

## Research focus

The project evaluates the **operational consistency of the rubric** and the **fidelity of the LLM evaluation process**. It does not evaluate faculty performance, students, student work, grades, educational records, or protected health information.

The analytic unit is the publicly available cybersecurity assignment prompt. Four faculty evaluators independently score approximately ten prompts using five dimensions:

1. Authenticity
2. Process Transparency
3. Ethical GenAI Use
4. Interactive Verification
5. Evaluative Judgment

Each dimension is scored from 1 (not addressed) to 3 (fully addressed). A total below 10 of 15 is flagged for revision.

## Reproducibility workflow

1. Freeze the model, platform, evaluator prompt, artifact order, and session settings.
2. Confirm the required five-dimension fidelity check before scoring.
3. Submit artifacts one at a time in the randomized order documented in the evaluator script.
4. Repeat the fidelity check at the midpoint.
5. Collect faculty scores using coded reviewer tabs (Reviewer A-D); names must not appear in analytic files.
6. Validate spreadsheet ranges and scoring completeness before analysis.
7. Compute descriptive statistics, percent agreement, Gwet's AC1, and weighted Cohen's kappa as specified in the analysis plan.
8. Report results only in aggregate; do not rank or identify individual evaluators.

## Data availability

This repository should contain only public-source artifact metadata and links, blank or coded scoring templates, frozen prompts and analysis scripts, and de-identified or aggregate results approved for release.

Do **not** upload evaluator identities or linkage files, identifiable scoring workbooks, institutional-review correspondence, identifiable consent records, restricted copyrighted artifacts, confidential institutional records, or credentials.

Any temporary reviewer linkage should be stored separately on an approved institutional system and destroyed according to the approved protocol.

## Licensing

Except where otherwise noted, the original documentation, research instruments, prompts, metadata, and released datasets in this repository are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Third-party materials are excluded and remain subject to their respective copyright and license terms. See `LICENSE`, `LICENSE_NOTES.md`, and `data/artifact_catalog.csv`.

Many evaluated assignment prompts are linked from external repositories and carry licenses that may restrict redistribution. This repository stores metadata and source links rather than reproducing restricted full text where possible.

## Citation

Citation metadata are provided in `CITATION.cff`. Author identities are withheld during anonymous review and should be restored when anonymity is no longer required. Update publication metadata when the paper is accepted or archived.

## Disclaimer

This repository is a research artifact. Its presence does not indicate institutional-review approval, publication acceptance, institutional endorsement, or validation for high-stakes educational decisions.
