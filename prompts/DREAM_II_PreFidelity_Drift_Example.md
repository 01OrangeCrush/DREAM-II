# Pre-Fidelity Rubric Drift Example

> **Purpose:** This is a documented failure example, not a scoring instrument. It shows why a plausible LLM response must not be treated as rubric-compliant until the criterion set is verified.

## What the early prompt said

The initial test supplied a presentation containing the rubric and then used this instruction:

> The above PowerPoint contains our framework to evaluate assignments. Evaluate the following assignment using the rubric discussed in the PowerPoint.

The instruction did not embed the rubric, require the model to enumerate the five dimensions, prohibit criterion substitution, or define a stop condition when the rubric could not be recovered exactly.

## Intended published dimensions

1. Authenticity
2. Process Transparency
3. Ethical GenAI Use
4. Interactive Verification
5. Evaluative Judgment

## What the model returned

The response looked complete: it contained five labeled criteria, 1-to-3 scores, rationales, a total out of 15, a vulnerability diagnosis, and a redesign recommendation. However, it silently used this different framework:

1. Real-World Relevance
2. Complexity & Critical Thinking
3. Open-Endedness / Student Agency
4. Authentic Evaluation Criteria
5. AI / Academic Integrity Vulnerability

| Requested dimension | Returned criterion |
|---|---|
| Authenticity | Real-World Relevance |
| Process Transparency | Complexity & Critical Thinking |
| Ethical GenAI Use | Open-Endedness / Student Agency |
| Interactive Verification | Authentic Evaluation Criteria |
| Evaluative Judgment | AI / Academic Integrity Vulnerability |

The substitution was wholesale, not a harmless paraphrase. A total such as 11/15 was arithmetically valid but measured a different construct.

## Why the failure was easy to miss

- The output shape matched expectations.
- The prose was fluent and domain-relevant.
- The scores and total were internally consistent.
- Several substituted concepts sounded compatible with authentic assessment.
- No preflight check forced the model to prove that it had recovered the published instrument.

This is the central lesson: **format compliance is not prompt fidelity**. Inspect criterion labels and anchors before inspecting scores.

## The repair

The frozen evaluator in [DREAM_II_LLM_Scoring_Script_Combined.md](DREAM_II_LLM_Scoring_Script_Combined.md) adds four linked safeguards:

1. embeds the complete rubric and anchor language;
2. explicitly prohibits substitution or reconstruction of another framework;
3. requires rationales tied to the supplied anchor language; and
4. verifies the exact five-dimension set before scoring and again at midpoint.

If either verification fails, scoring must stop. See the [Prompt Fidelity Inspection Guide](../docs/PROMPT_FIDELITY_INSPECTION_GUIDE.md) for a reader-oriented comparison.

## Provenance note

This example is distilled from the pre-study test files supplied with the project: the presentation containing the rubric, the one-sentence prompt above, and the resulting model evaluation. Assignment text from the test packet is not reproduced here because source rights vary. Required scholarly and third-party attribution is preserved elsewhere in the repository.
