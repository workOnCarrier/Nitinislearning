
class Solution:
  def findNumbers(self, nums, k):
    missingNumbers = []
    extra_numbers = set()
    cur_index, length = 0, len(nums)
    while cur_index < length:
      expected_index = nums[cur_index] - 1
      if expected_index  >= 0 and expected_index < length and nums[expected_index] != nums[cur_index]:
        print(f"\t expected:{expected_index}, currend:{cur_index}, in {nums}")
        nums[expected_index], nums[cur_index] =   nums[cur_index], nums[expected_index]
      else:
        cur_index += 1
    for index in range(length):
      if len(missingNumbers) == k:
        break
      else:
        if nums[index] != index + 1:
          print(f"\t adding {index + 1} as {nums[index]} does not match")
          missingNumbers.append( index + 1)
          extra_numbers.add(nums[index])
    offset = 1
    while len(missingNumbers) < k:
      next_ = offset + length
      if next_ not in extra_numbers:
        missingNumbers.append(next_)
      offset += 1

    return missingNumbers

def main():
  sol = Solution()
  print(sol.findNumbers([3, -1, 4, 5, 5], 3))
  print(sol.findNumbers([2, 3, 4], 3))
  print(sol.findNumbers([-2, -3, 4], 2))
  print(sol.findNumbers([2, 3, -7, 6, 8, 1, -10, 15], 3))


main()
