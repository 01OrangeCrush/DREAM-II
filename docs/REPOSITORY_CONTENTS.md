# Recommended Repository Contents

## Reader path

The repository should make the prompt-fidelity lesson visible before presenting agreement statistics:

1. `README.md` - the drift-at-a-glance comparison and five-minute inspection path.
2. `prompts/DREAM_II_PreFidelity_Drift_Example.md` - the informal external-rubric prompt, the substituted criteria, and the failure analysis.
3. `prompts/DREAM_II_LLM_Scoring_Script_Combined.md` - the frozen corrected evaluator with the embedded rubric and runtime checks.
4. `docs/PROMPT_FIDELITY_INSPECTION_GUIDE.md` - a side-by-side visual inspection checklist and explicit pass/fail rule.

## Include now

- `README.md`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `LICENSE` and `LICENSE_NOTES.md`
- `CHANGELOG.md`
- documented pre-fidelity drift example
- frozen prompt-faithful LLM evaluator script
- prompt-fidelity visual inspection guide
- coded blank scoring workbook
- methods overview
- data dictionary
- reproducibility checklist
- ethics and privacy guidance
- artifact metadata catalog
- placeholder directories for analysis, figures, and releasable data

## Preserve as evidence, not analytic data

When a fidelity check fails, preserve the raw output, model/platform label, date, input prompt, referenced instrument, and failure classification. Do not silently rename substituted criteria or reuse the scores. A public example may be distilled when the original packet contains third-party material that cannot be redistributed.

## Add after IRB approval and data collection

- versioned analysis scripts
- a de-identified long-format scoring file
- aggregate agreement tables
- figure source files and accessible captions
- session-level LLM metadata without credentials or private account information
- a release-specific README describing deviations from the preregistered or approved plan

## Add after manuscript acceptance

- accepted manuscript citation
- DOI and conference metadata
- camera-ready manuscript, subject to ACM and publisher rights
- archival release tag and checksum manifest
- final figure files
- frozen fidelity-check transcripts and permitted raw model outputs

## Do not include publicly

- HRP-591 or HRP-594 forms containing personal contact details unless intentionally redacted and approved for release
- reviewer name/code mapping
- completed identifiable evaluator files
- restricted source-artifact copies
- private peer-review correspondence
- pre-study assignment packets when redistribution rights are unclear
