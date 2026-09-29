# DREAM II Prompt Fidelity Replication Package

This repository accompanies the SIGCITE 2026 paper **Prompt Fidelity in LLM-Assisted Assessment: Rubric Drift and Operational Validation of an AI-Resilient Cybersecurity Assessment Rubric** by Jennifer McCauley, Edward J. Glantz, Mahdi Nasereddin, and Michael R. Bartolacci.

The study tested whether four cybersecurity faculty and a frozen hosted LLM evaluator could apply a published five-dimension assignment-design rubric consistently. The main methodological result is that prompt fidelity must be checked before agreement or validity claims are interpreted.

## Headline results

Over the four dimensions with score variation:

- faculty-faculty mean Gwet AC1: 0.287;
- faculty-faculty mean quadratic weighted kappa: 0.408;
- LLM-faculty mean Gwet AC1: 0.216;
- LLM-faculty mean quadratic weighted kappa: 0.474.

Including the provenance-floored Ethical GenAI Use dimension raises the respective values to 0.451, 0.485, 0.388, and 0.573. Run `python analysis/reproduce.py` to regenerate the released estimates.

## Repository contents

```text
analysis/                         Agreement analysis and generated results
data/                             Catalog, coded ratings, transcripts, and correction log
docs/                             Methods, data, privacy, model, and release documentation
paper/                            Camera-ready source and PDF
prompts/                          Frozen evaluator prompt without third-party assignment text
templates/                        Coded blank scoring workbook
```

## Reproduce the analysis

Python 3.10 or later is sufficient; no third-party package is required.

```text
python analysis/reproduce.py
```

Expected output:

```text
Four-dimension faculty means: 0.287 0.408
Four-dimension LLM-faculty means: 0.216 0.474
```

## Data and licensing

The analytic unit is a publicly available assignment prompt. This repository releases metadata and source links rather than third-party assignment files. It contains no student records or student work. Faculty ratings are coded as `Faculty_A` through `Faculty_D`; the repository does not contain a name-to-code linkage.

Original repository documentation, prompts, metadata, and released data are licensed CC BY 4.0 except where noted. Linked assignment materials retain their original rights and licenses. See `LICENSE`, `LICENSE_NOTES.md`, and `data/artifact_catalog.csv`.

## Citation and publication metadata

Use `CITATION.cff` for the current citation. The conference DOI, ISBN, venue dates, location, and final page range have not yet been supplied. `docs/PUBLICATION_METADATA_TODO.md` records every location that must be updated when those details arrive.

`CHECKSUMS.sha256` records release-file hashes for integrity checking.

## Contact

Edward J. Glantz, PhD  
College of Information Sciences and Technology  
The Pennsylvania State University  
ejg8@psu.edu

## Scope

These materials support reproducibility and methodological inspection. They do not validate the rubric for high-stakes or autonomous educational decisions.
