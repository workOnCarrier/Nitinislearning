"""Reference solution for Problem 2: Efficient Tasks Across 3 Servers."""
from typing import List


def efficient_task_across_3_servers(difficulty: List[int]) -> int:
    """Return the maximum possible minimal |d1-d2|+|d2-d3| achievable."""
    if len(difficulty) < 3:
        raise ValueError("At least three modules are required")
    minimum = min(difficulty)
    maximum = max(difficulty)
    return maximum - minimum


def _run_tests() -> None:
    tests = [
        ([1, 2, 10, 20], 19),  # isolate min and max on different servers
        ([4, 4, 4], 0),  # all modules have same difficulty
        ([1, 100, 50], 99),  # every assignment must include min and max
        ([5, 5, 9, 11], 6),  # duplicates should not reduce achievable range
        ([7, 3, 3, 7, 14], 11),  # extra middle values still bounded by extremes
    ]

    for idx, (difficulty, expected) in enumerate(tests, 1):
        result = efficient_task_across_3_servers(difficulty)
        assert result == expected, f"Test {idx} failed: expected {expected}, got {result}"
    print("All Efficient Tasks tests passed.")


if __name__ == "__main__":
    _run_tests()
