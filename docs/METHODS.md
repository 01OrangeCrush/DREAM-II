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

Each faculty evaluator used an assigned worksheet, the rubric, evaluator instructions, and source links. Evaluators scored independently and supplied a concise rationale for each dimension. The public ratings file replaces source worksheet identities with `Faculty_A` through `Faculty_D` and omits the name-to-code linkage.

## LLM evaluation

The LLM was run using the frozen evaluator script in `prompts/`. The script required an initial fidelity check, fixed output structure, one artifact at a time, and a midpoint fidelity re-check. Penn State AI Studio identified the hosted model as OpenAI GPT-5.4 on July 14, 2026. Temperature 0 and zero retention were requested but could not be independently verified.

## Analyses

- Gwet AC1 for chance-corrected pairwise agreement
- Quadratic weighted Cohen kappa for ordinal pairwise agreement
- 1,000 assignment-level bootstrap resamples with seed 2026
- Simple agreement at the published KEEP/REVISE threshold
- Separate four-dimension estimates excluding the provenance-floored Ethical GenAI Use dimension and five-dimension estimates for comparability

Because this is a small exploratory pilot, the estimates demonstrate and initially test the workflow but do not establish robustness, transferability, stable subgroup effects, or population-level faculty performance.

## Reporting

Only aggregate or coded results are reported. Individual evaluators are not named, ranked, or characterized as more or less accurate.
