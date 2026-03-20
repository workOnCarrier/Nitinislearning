"""Practice tests for Problem 1: Transaction Segments."""
from typing import List


def count_increasing_segments(transaction_values: List[int], k: int) -> int:
    """Return the number of length-k windows that are strictly increasing."""
    raise NotImplementedError("Implement the sliding-window counting logic")


def _run_tests() -> None:
    tests = [
        (([1, 2, 3, 4], 3), 2),  # every window of length 3 increases
        (([1, 1, 2, 3], 2), 2),  # equal neighbors break strictness
        (([5, 4, 3, 2], 2), 0),  # strictly decreasing array
        (([2, 3, 5, 4, 6, 7], 3), 2),  # only windows [2,3,5] and [4,6,7]
        (([1, 3, 2, 4, 5], 1), 5),  # every length-1 segment counts
    ]

    for idx, (args, expected) in enumerate(tests, 1):
        result = count_increasing_segments(*args)
        assert result == expected, f"Test {idx} failed: expected {expected}, got {result}"
    print("All Transaction Segments tests passed.")


if __name__ == "__main__":
    _run_tests()
