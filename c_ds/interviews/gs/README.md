# Interview Practice Problems

Each markdown prompt under `curation/` now has a matching Python practice harness under `problems/` and an implemented reference solution under `solution/`. Every file is self-contained—run it with `python <filename>` to execute the included boundary-focused tests.

| Problem | Practice File | Reference Solution | Closest LeetCode Analog |
| --- | --- | --- | --- |
| [Transaction Segments](curation/transaction_segments.md) | `problems/transaction_segments_test.py` | `solution/transaction_segments_test.py` | [`Longest Continuous Increasing Subsequence`](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) (related counting variant) |
| [Efficient Tasks Across 3 Servers](curation/efficient_task_across_3_servers.md) | `problems/efficient_task_across_3_servers_test.py` | `solution/efficient_task_across_3_servers_test.py` | N/A – bespoke partitioning objective |
| [Execute Grid Moves](curation/execute_grid_moves.md) | `problems/execute_grid_moves_test.py` | `solution/execute_grid_moves_test.py` | [`Robot Return to Origin`](https://leetcode.com/problems/robot-return-to-origin/) (same move set, different goal) |
| [First Unique Character](curation/first_unique_char.md) | `problems/first_unique_char_test.py` | `solution/first_unique_char_test.py` | [`First Unique Character in a String`](https://leetcode.com/problems/first-unique-character-in-a-string/) |
| [Group Strings by Anagram](curation/group_strings_by_anagram.md) | `problems/group_strings_by_anagram_test.py` | `solution/group_strings_by_anagram_test.py` | [`Group Anagrams`](https://leetcode.com/problems/group-anagrams/) |
| [Highest Average Score](curation/highest_average_score.md) | `problems/highest_average_score_test.py` | `solution/highest_average_score_test.py` | N/A – closest in spirit to averaged-score interview questions |
| [Longest Non-Repeating Substring](curation/longest_non_repeating_substr.md) | `problems/longest_non_repeating_substr_test.py` | `solution/longest_non_repeating_substr_test.py` | [`Longest Substring Without Repeating Characters`](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| [Lottery Coupons: Most Popular Digit-Sum Values](curation/lottery_coupons.md) | `problems/lottery_coupons_test.py` | `solution/lottery_coupons_test.py` | [`Count Largest Group`](https://leetcode.com/problems/count-largest-group/) |

To get started on any challenge, open the corresponding `problems/…_test.py` file, fill in the stubbed function, and run the script. Compare against the implementation under `solution/` if you want a reference or to debug your approach.
