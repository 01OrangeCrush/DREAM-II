# Analysis

`reproduce.py` reads the released de-identified ratings and reproduces the paper's four- and five-dimension faculty-faculty and LLM-faculty agreement estimates. It implements unweighted two-rater Gwet AC1, quadratic weighted Cohen kappa, 1,000 assignment-level bootstrap resamples with seed 2026, and threshold agreement.

Run from the repository root with Python 3.10 or later:

```text
python analysis/reproduce.py
```

The script uses only the Python standard library and writes `analysis/outputs/summary.json` and `analysis/outputs/pairwise_agreement.csv`.
