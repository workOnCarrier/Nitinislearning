"""Reference solution for Problem 1: Transaction Segments."""
from typing import List


def count_increasing_segments(transaction_values: List[int], k: int) -> int:
    """Return the number of length-k windows that are strictly increasing."""
    n = len(transaction_values)
    if k <= 0 or k > n:
        return 0
    if k == 1:
        return n

    count = 0
    run_length = 1  # length of current strictly increasing streak ending at i
    for i in range(1, n):
        if transaction_values[i] > transaction_values[i - 1]:
            run_length += 1
        else:
            run_length = 1
        if run_length >= k:
            count += 1
    return count


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
