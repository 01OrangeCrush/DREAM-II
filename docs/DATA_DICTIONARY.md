# Data Dictionary

## Artifact catalog

| Field | Description |
|---|---|
| `artifact_id` | Stable study identifier, such as P03 |
| `run_order` | Randomized LLM scoring position |
| `artifact_letter` | Letter used in the frozen evaluator session |
| `title` | Short artifact title |
| `level` | Intended instructional level |
| `type` | Assignment or activity type |
| `license` | Source-reported license or rights status |
| `source_url` | Public source location |
| `source_file_hint` | File or folder name used to locate the prompt |

## Scoring data

| Field | Description | Allowed values |
|---|---|---|
| `reviewer_code` | Coded evaluator identifier | A, B, C, D, or LLM |
| `artifact_id` | Artifact identifier | P03-P13 as cataloged |
| `authenticity` | Rubric score | 1, 2, 3 |
| `process_transparency` | Rubric score | 1, 2, 3 |
| `ethical_genai_use` | Rubric score | 1, 2, 3 |
| `interactive_verification` | Rubric score | 1, 2, 3 |
| `evaluative_judgment` | Rubric score | 1, 2, 3 |
| `total` | Sum of five dimension scores | 5-15 |
| `decision` | Rubric threshold result | REVISE if total <10; KEEP otherwise |
| `rationale_*` | Brief evidence supporting each score | Text |

## Prohibited fields in public analytic data

Do not include evaluator names, initials, email addresses, employment identifiers, IP addresses, or a reviewer-code linkage key.
