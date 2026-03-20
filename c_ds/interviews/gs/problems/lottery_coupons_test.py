"""Practice tests for Lottery Coupons: Most Popular Digit-Sum Values."""

def lottery_coupons(n: int) -> int:
    """Return how many distinct digit sums 1..9*d achieve the maximum winner count for 1..n."""
    raise NotImplementedError("Use digit DP or optimized counting to avoid iterating through all coupons")


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
