"""Practice tests for Task 1: First Unique Character."""

def first_unique_char(s: str) -> int:
    """Return the index of the first non-repeating character or -1 if none exist."""
    raise NotImplementedError("Count occurrences and track the earliest index")


def _run_tests() -> None:
    tests = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("z", 0),
        ("aabbccd", 6),
    ]

    for idx, (s, expected) in enumerate(tests, 1):
        result = first_unique_char(s)
        assert result == expected, f"Test {idx} failed: expected {expected}, got {result}"
    print("All First Unique Character tests passed.")


if __name__ == "__main__":
    _run_tests()
