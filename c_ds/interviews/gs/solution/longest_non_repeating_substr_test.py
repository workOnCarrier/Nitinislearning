"""Reference solution for Longest Non-Repeating Substring."""
from typing import Tuple


def longest_non_repeating_substr(s: str) -> Tuple[int, str]:
    """Return (length, substring) for the longest substring without repeating chars."""
    last_seen: dict[str, int] = {}
    start = 0
    best_len = 0
    best_substring = ""

    for idx, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = idx
        window_len = idx - start + 1
        if window_len > best_len:
            best_len = window_len
            best_substring = s[start : idx + 1]

    return best_len, best_substring


def _is_valid_substring(source: str, candidate: str) -> bool:
    return candidate in source and len(candidate) == len(set(candidate))


def _run_tests() -> None:
    tests = [
        ("abcabcbb", 3, {"abc", "bca", "cab"}),
        ("", 0, {""}),
        ("bbbbb", 1, {"b"}),
        ("pwwkew", 3, {"wke", "kew"}),
        ("dvdf", 3, {"vdf"}),
    ]

    for idx, (s, expected_len, valid_substrings) in enumerate(tests, 1):
        length, substring = longest_non_repeating_substr(s)
        assert length == expected_len, f"Test {idx} failed: expected length {expected_len}, got {length}"
        assert substring in valid_substrings, (
            f"Test {idx} failed: substring {substring!r} not in acceptable set {valid_substrings}"
        )
        assert _is_valid_substring(s, substring), f"Test {idx} failed: substring {substring!r} invalid"
    print("All Longest Non-Repeating Substring tests passed.")


if __name__ == "__main__":
    _run_tests()
