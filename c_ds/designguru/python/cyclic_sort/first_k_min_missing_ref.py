class Solution:
  def findNumbers(self, nums, k):
    n = len(nums)
    i = 0
    while i < len(nums):
      j = nums[i] - 1
      if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
        print(f"\t expected:{j}, currend:{i}, in {nums}")
        nums[i], nums[j] = nums[j], nums[i]  # Swap the current element with its correct position.
      else:
        i += 1

    missingNumbers = []
    extraNumbers = set()
    for i in range(n):
      if len(missingNumbers) < k:
        if nums[i] != i + 1:
          print(f"\t adding {i} as {nums[i]} does not match")
          missingNumbers.append(i + 1)  # Add the missing number to the result list.
          extraNumbers.add(nums[i])     # Keep track of extra numbers encountered.

    # Add the remaining missing numbers
    i = 1
    while len(missingNumbers) < k:
      candidateNumber = i + n
      # Ignore if the array contains the candidate number
      if candidateNumber not in extraNumbers:
        missingNumbers.append(candidateNumber)  # Add remaining missing numbers to the result list.
      i += 1

    return missingNumbers


def main():
  sol = Solution()
  print(sol.findNumbers([3, -1, 4, 5, 5], 3))
  print(sol.findNumbers([2, 3, 4], 3))
  print(sol.findNumbers([-2, -3, 4], 2))
  print(sol.findNumbers([2, 3, -7, 6, 8, 1, -10, 15], 3))

main()
