"""Reference solution for Task 2: Highest Average Score."""
from typing import List, Tuple


Record = Tuple[str, int]


def highest_average_score(records: List[Record]) -> float:
    """Return the maximum average score among the provided student records."""
    if not records:
        raise ValueError("records must be non-empty")

    totals: dict[str, int] = {}
    counts: dict[str, int] = {}
    for student, score in records:
        totals[student] = totals.get(student, 0) + score
        counts[student] = counts.get(student, 0) + 1

    max_average = float("-inf")
    for student in totals:
        average = totals[student] / counts[student]
        if average > max_average:
            max_average = average
    return max_average


def _run_tests() -> None:
    tests = [
        ([("a", 80), ("b", 90), ("a", 100)], 90.0),
        ([("alice", 100)], 100.0),
        ([("x", 0), ("y", -10), ("y", 10)], 0.0),
        ([("a", 95), ("a", 96)], 95.5),
    ]

    for idx, (records, expected) in enumerate(tests, 1):
        result = highest_average_score(records)
        assert abs(result - expected) < 1e-9, (
            f"Test {idx} failed: expected {expected}, got {result}"
        )
    print("All Highest Average Score tests passed.")


if __name__ == "__main__":
    _run_tests()
