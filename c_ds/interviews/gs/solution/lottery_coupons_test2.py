"""Alternate reference solution for Lottery Coupons without recursion memoization."""
from collections import defaultdict
from typing import Dict


def lottery_coupons(n: int) -> int:
    """Return how many digit sums appear most often among coupons 1..n."""
    if n <= 0:
        raise ValueError("n must be >= 1")

    digits = list(map(int, str(n)))
    max_sum = 9 * len(digits)

    states: Dict[bool, Dict[int, int]] = {True: {0: 1}, False: {}}
    for pos, limit_digit in enumerate(digits):
        new_states = {True: defaultdict(int), False: defaultdict(int)}
        for tight, sum_counts in states.items():
            if not sum_counts:
                continue
            limit = limit_digit if tight else 9
            for digit_sum, ways in sum_counts.items():
                for digit in range(limit + 1):
                    new_tight = tight and digit == limit
                    new_states[new_tight][digit_sum + digit] += ways
        states = {True: dict(new_states[True]), False: dict(new_states[False])}

    total_counts = [0] * (max_sum + 1)
    for tight in (True, False):
        for digit_sum, ways in states[tight].items():
            total_counts[digit_sum] += ways

    total_counts[0] -= 1  # exclude coupon "0"

    max_freq = 0
    winners = 0
    for digit_sum in range(1, len(total_counts)):
        freq = total_counts[digit_sum]
        if freq > max_freq:
            max_freq = freq
            winners = 1
        elif freq == max_freq and freq > 0:
            winners += 1
    return winners


def _run_tests() -> None:
    tests = [
        (1, 1),
        (9, 9),
        (19, 9),
        (100, 1),
        (1000, 2),
    ]

    for idx, (n, expected) in enumerate(tests, 1):
        result = lottery_coupons(n)
        assert result == expected, f"Test {idx} failed: expected {expected}, got {result}"
    print("All Lottery Coupons (iterative) tests passed.")


if __name__ == "__main__":
    _run_tests()
