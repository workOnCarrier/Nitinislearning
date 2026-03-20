"""Reference solution for Group Strings by Anagram."""
from collections import defaultdict
from typing import List


def group_strings_by_anagram(strs: List[str]) -> List[List[str]]:
    """Group strings that are anagrams; return order does not matter."""
    buckets: dict[tuple[int, ...], List[str]] = defaultdict(list)
    for word in strs:
        signature = tuple(sorted(word))
        buckets[signature].append(word)
    return list(buckets.values())


def _normalize(groups: List[List[str]]) -> List[List[str]]:
    return sorted(sorted(group) for group in groups)


def _run_tests() -> None:
    tests = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]],
        ),
        ([], []),
        ([""], [[""]]),
    ]

    for idx, (strings, expected) in enumerate(tests, 1):
        result = group_strings_by_anagram(strings)
        assert _normalize(result) == _normalize(expected), (
            f"Test {idx} failed: expected {_normalize(expected)}, got {_normalize(result)}"
        )
    print("All Group Anagrams tests passed.")


if __name__ == "__main__":
    _run_tests()
