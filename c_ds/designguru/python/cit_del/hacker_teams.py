##
# # problem = ``` A cyber security firm is building a team of hackers to take down a network of cybercriminals. The skill level of the ith hacker of team A is team_a[i] and of team B is team_b[i].
# A team is considered strong if for each index i a hacker is selected either from team A or team B, and the skill levels of the selected team are non-decreasing.
# Given two arrays team_a and team_b of n integers each, choose two indices i and j such that the subarrays [team_a[i], team_a[i + 1]... team_[j]] and [team_b[i], team_b[i + 1] ... team_b[j]] can form a strong team.
# Find the maximum possible value of [i , j] i.e. the length of the chosen subarray.  ```
##

import math

class Solution:
    def max_sub_array_of_hackers(teamA, teamB):
        max_len = 0
        win_start, win_end = 0, 0
        if (len(teamA) != len(teamB)):
            return 1
        sol_len = len(teamB)
        prev_val = -1
        while True:
            if teamA[win_end] >= prev_val and teamB[win_end] >= prev_val:
                prev_val = min(teamB[win_end], teamA[win_end])
                win_end += 1
            elif max(teamA[win_end], teamB[win_end]) < prev_val:
                sub_len = win_end - win_start
                max_len = max(sub_len, max_len)
                win_start += 1
                win_end == win_start
                prev_val = min(teamB[win_end], teamA[win_end])
            else:
                prev_val = max(teamA[win_end], teamB[win_end])
                win_end += 1
            if win_start > sol_len - 1 or win_end > sol_len - 1:
                sub_len = win_end - win_start
                max_len = max(sub_len, max_len)
                break
        return max_len

def test(teamA, teamB):
    max_len = Solution.max_sub_array_of_hackers(teamA, teamB)
    return max_len
    
def test_1():
    teamA = [5, 2, 4, 1]
    teamB = [3, 6, 2, 2]
    result = test(teamA, teamB)
    print(result)

if __name__ == "__main__":
    test_1()

