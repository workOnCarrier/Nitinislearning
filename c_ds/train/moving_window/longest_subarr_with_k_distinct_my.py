class Solution:
  def findLength(self, str1, k):
      max_length = 0
      win_start = 0
      distinct_dict = {}
      for win_end in range(len(str1)):
        key = str1[win_end]
        if key not in distinct_dict.keys():
          distinct_dict[key] = 0
        distinct_dict[key] += 1
        while len(distinct_dict.keys()) > k:
          old_key = str1[win_start]
          distinct_dict[old_key] -= 1
          win_start += 1
          if distinct_dict[old_key] == 0:
            del distinct_dict[old_key]
        length = win_end - win_start + 1
        max_length = max ( max_length, length)
      return max_length

def main():
    sol = Solution()
    print("Length of the longest substring: "
          + str(sol.findLength("araaci", 2)))
    print("Length of the longest substring: "
          + str(sol.findLength("araaci", 1)))
    print("Length of the longest substring: "
          + str(sol.findLength("cbbebi", 3)))


main()
