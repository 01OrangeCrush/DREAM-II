#!/usr/bin/env python3
"""Reproduce the agreement estimates reported in the DREAM II paper.

Uses only the Python standard library. Run from the repository root:
    python analysis/reproduce.py
"""

from __future__ import annotations

import csv
import itertools
import json
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "ratings_deidentified.csv"
OUT = ROOT / "analysis" / "outputs"
DIMS = ["authenticity", "process_transparency", "ethical_genai_use", "interactive_verification", "evaluative_judgment"]
PRIMARY_DIMS = [d for d in DIMS if d != "ethical_genai_use"]


def mean(values):
    return sum(values) / len(values)


def ac1(a, b, categories=(1, 2, 3)):
    """Unweighted two-rater Gwet AC1."""
    observed = mean([x == y for x, y in zip(a, b)])
    pooled = [((a.count(k) + b.count(k)) / (2 * len(a))) for k in categories]
    chance = sum(p * (1 - p) for p in pooled) / (len(categories) - 1)
    return (observed - chance) / (1 - chance)


def quadratic_weighted_kappa(a, b, categories=(1, 2, 3)):
    """Cohen kappa with quadratic weights."""
    n = len(a)
    q = len(categories)
    observed = [[0.0] * q for _ in range(q)]
    for x, y in zip(a, b):
        observed[x - 1][y - 1] += 1 / n
    pa = [a.count(k) / n for k in categories]
    pb = [b.count(k) / n for k in categories]
    numerator = denominator = 0.0
    for i in range(q):
        for j in range(q):
            weight = ((i - j) / (q - 1)) ** 2
            numerator += weight * observed[i][j]
            denominator += weight * pa[i] * pb[j]
    return math.nan if denominator == 0 else 1 - numerator / denominator


def percentile(values, p):
    values = sorted(values)
    index = (len(values) - 1) * p
    lo, hi = math.floor(index), math.ceil(index)
    if lo == hi:
        return values[lo]
    return values[lo] + (values[hi] - values[lo]) * (index - lo)


def load():
    ratings = {}
    with DATA.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ratings[(row["artifact_id"], row["rater"])] = {d: int(row[d]) for d in DIMS}
    artifacts = sorted({a for a, _ in ratings})
    raters = sorted({r for _, r in ratings})
    return ratings, artifacts, raters


def vectors(ratings, artifact_order, rater, dimensions):
    return [ratings[(artifact, rater)][dimension] for artifact in artifact_order for dimension in dimensions]


def pair_results(ratings, artifacts, pairs, dimensions):
    results = []
    for left, right in pairs:
        a = vectors(ratings, artifacts, left, dimensions)
        b = vectors(ratings, artifacts, right, dimensions)
        results.append({"left": left, "right": right, "ac1": ac1(a, b), "qwk": quadratic_weighted_kappa(a, b)})
    return results


def bootstrap_ci(ratings, artifacts, left, right, dimensions, seed=2026, resamples=1000):
    rng = random.Random(seed)
    estimates = []
    for _ in range(resamples):
        sample = [rng.choice(artifacts) for _ in artifacts]
        a = vectors(ratings, sample, left, dimensions)
        b = vectors(ratings, sample, right, dimensions)
        estimates.append(ac1(a, b))
    return [percentile(estimates, 0.025), percentile(estimates, 0.975)]


def threshold_results(ratings, artifacts, faculty):
    decisions = {}
    for rater in [*faculty, "LLM"]:
        decisions[rater] = [sum(ratings[(artifact, rater)][d] for d in DIMS) >= 10 for artifact in artifacts]
    rows = []
    for left, right in itertools.chain(itertools.combinations(faculty, 2), (("LLM", r) for r in faculty)):
        agreement = mean([x == y for x, y in zip(decisions[left], decisions[right])])
        rows.append({"left": left, "right": right, "simple_agreement": agreement})
    return rows


def main():
    ratings, artifacts, raters = load()
    faculty = [r for r in raters if r.startswith("Faculty_")]
    faculty_pairs = list(itertools.combinations(faculty, 2))
    llm_pairs = [("LLM", r) for r in faculty]
    output = {"method": {"bootstrap_resamples": 1000, "bootstrap_seed": 2026}, "bases": {}, "threshold": {}}
    flat_rows = []
    for label, dimensions in (("four_dimension", PRIMARY_DIMS), ("five_dimension", DIMS)):
        faculty_results = pair_results(ratings, artifacts, faculty_pairs, dimensions)
        llm_results = pair_results(ratings, artifacts, llm_pairs, dimensions)
        for row in faculty_results + llm_results:
            row["ac1_bootstrap_95_ci"] = bootstrap_ci(ratings, artifacts, row["left"], row["right"], dimensions)
            flat_rows.append({"basis": label, **row})
        output["bases"][label] = {
            "dimensions": dimensions,
            "faculty_pair_mean_ac1": mean([r["ac1"] for r in faculty_results]),
            "faculty_pair_mean_qwk": mean([r["qwk"] for r in faculty_results]),
            "llm_faculty_mean_ac1": mean([r["ac1"] for r in llm_results]),
            "llm_faculty_mean_qwk": mean([r["qwk"] for r in llm_results]),
            "faculty_pairs": faculty_results,
            "llm_faculty_pairs": llm_results,
        }
    thresholds = threshold_results(ratings, artifacts, faculty)
    faculty_thresholds = [r["simple_agreement"] for r in thresholds if not (r["left"] == "LLM" or r["right"] == "LLM")]
    llm_thresholds = [r["simple_agreement"] for r in thresholds if r["left"] == "LLM" or r["right"] == "LLM"]
    output["threshold"] = {
        "rule": "total < 10 = REVISE; total >= 10 = KEEP",
        "faculty_simple_agreement_range": [min(faculty_thresholds), max(faculty_thresholds)],
        "llm_faculty_simple_agreement_range": [min(llm_thresholds), max(llm_thresholds)],
        "pairs": thresholds,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "summary.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    with (OUT / "pairwise_agreement.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["basis", "left", "right", "ac1", "qwk", "ac1_ci_low", "ac1_ci_high"])
        for row in flat_rows:
            writer.writerow([row["basis"], row["left"], row["right"], row["ac1"], row["qwk"], *row["ac1_bootstrap_95_ci"]])
    four = output["bases"]["four_dimension"]
    print("Four-dimension faculty means:", round(four["faculty_pair_mean_ac1"], 3), round(four["faculty_pair_mean_qwk"], 3))
    print("Four-dimension LLM-faculty means:", round(four["llm_faculty_mean_ac1"], 3), round(four["llm_faculty_mean_qwk"], 3))
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
