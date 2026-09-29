# Reproducibility Checklist

Record the following for every LLM run:

- platform and access environment;
- model name and platform-reported version;
- date and time of run;
- temperature or determinism setting, when exposed;
- retention setting, when exposed;
- evaluator-script commit hash;
- artifact-catalog commit hash;
- randomized run order;
- initial fidelity-check result;
- midpoint fidelity-check result;
- any interruption, refusal, truncation, drift, or manual correction.

## Integrity rules

- Do not modify the evaluator prompt during an analytic run.
- Do not resubmit an artifact merely to obtain a preferred score.
- Preserve raw model outputs before cleaning or tabulation.
- Document exclusions and reruns with reasons.
- Keep calibration artifacts separate from the analytic sample.
- Verify that threshold coding uses `total < 10` for REVISE and `total >= 10` for KEEP.

## Released artifacts

- frozen evaluator prompt;
- artifact catalog and source links;
- blank coded scoring workbook;
- corrected de-identified ratings and correction log;
- raw frozen-session text and fidelity checks;
- pre-analytic drift transcript;
- executable analysis code and generated outputs;
- manuscript source, PDF, citation, and version information.

## Verification

From the repository root, run `python analysis/reproduce.py`. The four-dimension point estimates should round to faculty AC1 0.287, faculty quadratic weighted kappa 0.408, LLM-faculty AC1 0.216, and LLM-faculty quadratic weighted kappa 0.474.
