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

## Suggested release artifacts

- frozen evaluator script;
- artifact catalog and source links;
- blank coded scoring workbook;
- analysis code;
- aggregate/de-identified results;
- figure-generation code;
- manuscript citation and version information.
