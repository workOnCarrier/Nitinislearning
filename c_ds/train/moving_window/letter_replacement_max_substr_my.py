def get_max_len(distinct_dict:dict):
  max_len = 0
  for key, value in distinct_dict.items():
    max_len = max(value, max_len)
  return max_len

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
        length = win_end - win_start + 1
        max_len_key = get_max_len(distinct_dict)
        while length - max_len_key > k:
          start_key = str1[win_start]
          distinct_dict[start_key] -= 1
          win_start += 1
          max_len_key = get_max_len(distinct_dict)
          length = win_end - win_start + 1
        max_length = max (max_length, length)
      return max_length

def main():
    sol = Solution()
    print(sol.findLength("aabccbb", 2))
    print(sol.findLength("abbcb", 1))
    print(sol.findLength("abccde", 1))


main()
