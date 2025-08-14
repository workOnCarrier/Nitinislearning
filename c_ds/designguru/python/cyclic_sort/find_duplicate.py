class Solution:
  def find_duplicate(self, nums):
    cur_index, n = 0, len(nums)
    while cur_index < n:
      cur_val = nums[cur_index]
      expected_index = cur_val -1
      print(f"\t value:{cur_val}, expected_index:{expected_index}, cur_index:{cur_index} in {nums}")
      if nums[expected_index] != nums[cur_index]:
        nums[expected_index], nums[cur_index] = nums[cur_index], nums[expected_index], 
      else:
        cur_index += 1
    return nums[-1]

def main():
  sol = Solution()
  print(sol.find_duplicate([1, 4, 4, 3, 2]))
  print(sol.find_duplicate([2, 1, 3, 3, 5, 4]))
  print(sol.find_duplicate([2, 4, 1, 4, 4]))
  print(sol.find_duplicate([2, 3, 4, 4, 1]))

main()
