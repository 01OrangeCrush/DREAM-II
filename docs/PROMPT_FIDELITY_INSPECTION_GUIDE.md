# Prompt Fidelity Inspection Guide

The most important artifact in this repository is not a score table. It is the visible contrast between a fluent rubric-drift failure and the controls added to the final evaluator prompt.

## Five-minute visual inspection

Open these files side by side:

- [Pre-Fidelity Rubric Drift Example](../prompts/DREAM_II_PreFidelity_Drift_Example.md)
- [Frozen Prompt-Faithful LLM Evaluator](../prompts/DREAM_II_LLM_Scoring_Script_Combined.md)

Then inspect in this order.

### 1. Compare criterion labels before scores

In the drift example, compare the requested and returned five-item lists. None of the returned criteria belongs to the published instrument, even though the response contains reasonable-looking scores, rationales, and a total.

**Visual cue:** Ignore the numbers first. Read the five bold or labeled criterion names. If the names do not match, every downstream statistic is about the wrong instrument.

### 2. Find the rubric lock in the final prompt

At the start of the frozen evaluator, locate the instruction that requires the five dimensions in their exact order and tells the model to stop before scoring.

A passing preflight list is:

1. Authenticity
2. Process Transparency
3. Ethical GenAI Use
4. Interactive Verification
5. Evaluative Judgment

**Visual cue:** The verification appears before any artifact. A score produced before this check is not an analytic score.

### 3. Inspect the embedded anchors

Confirm that the final prompt includes the complete definition and 1-to-3 scale for every dimension. It must not merely point to an attachment, slide deck, paper, or prior chat turn.

**Visual cue:** Each criterion has its own anchor language in the same frozen file used for scoring.

### 4. Find the substitution prohibition

Locate the instruction not to substitute, supplement, rename, or reconstruct another framework. This is what the early prompt lacked.

**Visual cue:** A model should report uncertainty or stop rather than fill a missing rubric with a coherent alternative.

### 5. Check evidence binding

For every score, the output format requires a rationale tied to the assignment and the supplied anchor language.

**Visual cue:** A generic rationale that could fit any criterion is not enough. The rationale should reveal which anchor controlled the score.

### 6. Locate the midpoint gate

The evaluator repeats the dimension verification between Artifact E and Artifact F.

**Visual cue:** Fidelity is treated as a runtime property, not a one-time setup assumption.

## Pass/fail rule

A run passes the fidelity gate only when the model:

- names all five dimensions exactly and in order;
- uses only the embedded definitions and anchors;
- produces anchor-linked rationales in the required structure; and
- passes both the initial and midpoint checks.

If any condition fails, stop scoring, preserve the output as a fidelity-failure artifact, and restart only under the documented protocol. Do not repair labels after the fact or compute agreement statistics on the drifted scores.

## General lesson for GenAI work

A response can be coherent, helpful, and wrong at the task-definition level. For any GenAI workflow that depends on a rubric, schema, policy, taxonomy, or checklist:

1. embed the governing instrument;
2. ask the model to restate the operative structure;
3. verify it before production work;
4. re-check during long runs; and
5. preserve failures as evidence rather than silently correcting them.

This pattern applies beyond assessment scoring to document review, coding standards, compliance checks, extraction schemas, and any workflow where a substituted framework can produce plausible but invalid output.
