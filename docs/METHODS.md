# Methods Overview

## Design

DREAM II uses a repeated-measures comparison in which the same set of publicly available cybersecurity assignment prompts is independently evaluated by four coded faculty evaluators and one frozen LLM evaluator.

## Unit of analysis

The assignment prompt or assignment directions distributed to students are the unit of analysis. Faculty evaluators are not ranked, graded, or assessed for competence.

## Rubric

Each artifact is scored on five dimensions using a three-point scale:

- 1 = not addressed
- 2 = partially addressed
- 3 = fully addressed

Dimensions:

1. Authenticity
2. Process Transparency
3. Ethical GenAI Use
4. Interactive Verification
5. Evaluative Judgment

The total score ranges from 5 to 15. A total below 10 is flagged for revision; 10 or above is retained.

## Faculty evaluation

Each faculty evaluator receives an assigned coded worksheet (Reviewer A-D), the rubric, evaluator instructions, and source links. Evaluators score independently and provide a concise rationale for each dimension. Names and initials are not entered into analytic workbooks.

## LLM evaluation

The LLM is run using the frozen evaluator script in `prompts/`. The script requires an initial fidelity check, fixed output structure, one artifact per turn, and a midpoint fidelity re-check. Model, platform, date, session settings, and any platform-reported version information should be recorded in the research log.

## Planned analyses

- Descriptive statistics by artifact and rubric dimension
- Exact and adjacent-category percent agreement
- Gwet's AC1 for chance-corrected agreement
- Weighted Cohen's kappa for pairwise ordinal comparisons, where appropriate
- Qualitative examination of score rationales and fidelity failures

Because this is a small pilot, estimates should be reported with appropriate caution. The study does not support conclusions about population-level faculty performance.

## Reporting

Only aggregate or coded results are reported. Individual evaluators are not named, ranked, or characterized as more or less accurate.
