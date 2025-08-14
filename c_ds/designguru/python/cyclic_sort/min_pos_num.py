class Solution:
  def findNumber(self, nums):
    curr_index, length = 0, len(nums)
    while curr_index < length:
      expected_index = nums[curr_index] - 1
      if nums[curr_index] > 0 and nums[curr_index] < length and nums[curr_index] != nums[expected_index]:
        nums[curr_index], nums[expected_index] =  nums[expected_index], nums[curr_index]
      else:
        curr_index += 1

    for index in range(length):
      if nums[index] != index + 1:
        return index + 1
    return len(nums) + 1


def main():
    sol = Solution()
    print(sol.findNumber([-3, 1, 5, 4, 2]))
    print(sol.findNumber([3, -2, 0, 1, 2]))
    print(sol.findNumber([3, 2, 5, 1]))


main()
