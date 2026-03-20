"""Reference solution for Lottery Coupons: Most Popular Digit-Sum Values."""
from functools import lru_cache
from typing import Tuple


def lottery_coupons(n: int) -> int:
    """Return how many distinct digit sums achieve the maximum winner count for 1..n."""
    if n <= 0:
        raise ValueError("n must be >= 1")

    digits = list(map(int, str(n)))
    max_sum = 9 * len(digits)

    @lru_cache(maxsize=None)
    def dfs(pos: int, tight: bool) -> Tuple[int, ...]:
        if pos == len(digits):
            counts = [0] * (max_sum + 1)
            counts[0] = 1
            return tuple(counts)

        limit = digits[pos] if tight else 9
        total = [0] * (max_sum + 1)
        for digit in range(limit + 1):
            suffix_counts = dfs(pos + 1, tight and digit == limit)
            for digit_sum, cnt in enumerate(suffix_counts):
                if cnt and digit_sum + digit <= max_sum:
                    total[digit_sum + digit] += cnt
        return tuple(total)

    counts = list(dfs(0, True))
    counts[0] -= 1  # exclude the number 0

    max_frequency = 0
    winners = 0
    for digit_sum in range(1, len(counts)):
        freq = counts[digit_sum]
        if freq > max_frequency:
            max_frequency = freq
            winners = 1
        elif freq == max_frequency and freq > 0:
            winners += 1
    return winners


def _run_tests() -> None:
    tests = [
        (1, 1),  # only digit sum 1 appears
        (9, 9),  # each sum 1..9 appears exactly once
        (19, 9),  # sums 1..9 all tie with two winners each
        (100, 1),  # sum=9 wins alone
        (1000, 2),  # sums 13 and 14 tie for the largest group
    ]

    for idx, (n, expected) in enumerate(tests, 1):
        result = lottery_coupons(n)
        assert result == expected, f"Test {idx} failed: expected {expected}, got {result}"
    print("All Lottery Coupons tests passed.")


if __name__ == "__main__":
    _run_tests()
