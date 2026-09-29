# Released data

`ratings_deidentified.csv` contains the corrected dimension-level ratings for 10 artifacts, four coded faculty raters, and the frozen LLM evaluator. Faculty codes are arbitrary public identifiers; no linkage to author names is included.

`artifact_catalog.csv` records the seeded scoring order, stable artifact IDs, source links, and source-reported licenses. Assignment files are not redistributed.

`correction_log.csv` documents the one post-scoring correction confirmed with the rater.

`llm_scoring_output.md` preserves the frozen analytic scoring-session text. `fidelity_verification.md` isolates the preflight and midpoint checks. `drift_episode.md` preserves the pre-analytic failure that motivated the prompt-fidelity gate.
