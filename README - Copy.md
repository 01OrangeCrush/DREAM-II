# DREAM II: Prompt Fidelity and AI-Resilient Assessment Evaluation

DREAM II is a pilot study examining whether a frozen large language model (LLM) can apply a published AI-resilient assignment-design rubric consistently when evaluating cybersecurity assignment prompts. The study compares coded faculty-evaluator scores with scores produced by a frozen LLM evaluator.

> **Project status:** Protocol and materials development. Human-participant data collection must not begin until the required Penn State IRB determination or approval is in place.

## Research focus

The project evaluates the **operational consistency of the rubric** and the **fidelity of the LLM evaluation process**. It does not evaluate faculty performance, students, student work, grades, educational records, or protected health information.

The analytic unit is the publicly available cybersecurity assignment prompt. Four faculty evaluators independently score approximately ten prompts using five dimensions:

1. Authenticity
2. Process Transparency
3. Ethical GenAI Use
4. Interactive Verification
5. Evaluative Judgment

Each dimension is scored from 1 (not addressed) to 3 (fully addressed). A total below 10 of 15 is flagged for revision.

## Repository structure

```text
DREAM-II/
├── README.md
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE_NOTES.md
├── CHANGELOG.md
├── docs/
│   ├── METHODS.md
│   ├── DATA_DICTIONARY.md
│   ├── REPRODUCIBILITY.md
│   ├── ETHICS_AND_PRIVACY.md
│   └── REPOSITORY_CONTENTS.md
├── prompts/
│   └── DREAM_II_LLM_Scoring_Script_Combined.md
├── templates/
│   └── DREAM_II_Rubric_Scoring_Workbook_Coded.xlsx
├── data/
│   ├── artifact_catalog.csv
│   └── README.md
├── analysis/
│   └── README.md
└── figures/
    └── README.md
```

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

This repository should contain only:

- public-source artifact metadata and links;
- blank or coded scoring templates;
- frozen prompts and analysis scripts;
- de-identified or aggregate results approved for release.

Do **not** upload:

- evaluator names or the reviewer-code linkage file;
- completed identifiable scoring workbooks;
- IRB correspondence or signed/identifiable consent records;
- copyrighted source artifacts that cannot be redistributed;
- confidential Penn State records or credentials.

The linkage between reviewer names and letters, if temporarily required for study administration, should be stored separately on an approved Penn State system and destroyed according to the approved protocol.

## Source-artifact licensing

Many evaluated assignment prompts are linked from external repositories and carry licenses that may restrict redistribution. This repository therefore stores metadata and source links rather than reproducing restricted full text. See `LICENSE_NOTES.md` and `data/artifact_catalog.csv`.

## Citation

Citation metadata are provided in `CITATION.cff`. Update the manuscript title, author order, conference details, DOI, and release version when the paper is accepted or archived.

## Contact

Edward J. Glantz, PhD  
College of Information Sciences and Technology  
The Pennsylvania State University  
Email: ejg8@psu.edu

## Disclaimer

This repository is a research artifact. Its presence does not indicate IRB approval, publication acceptance, endorsement by Penn State, or validation for high-stakes educational decisions.
