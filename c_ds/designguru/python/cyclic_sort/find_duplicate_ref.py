class Solution:
  def find_duplicate(self, nums):
    i = 0
    while i < len(nums):
      if nums[i] != i + 1:  # Check if the current element is in its correct position
        j = nums[i] - 1  # Calculate the correct index for the current element
        if nums[i] != nums[j]:  # Check if the current element is not equal to the element at its correct index
          nums[i], nums[j] = nums[j], nums[i]  # Swap the elements to their correct positions
        else:  # We have found the duplicate
          return nums[i]
      else:
        i += 1  # Move to the next element

    return -1  # No duplicate found

def main():
  sol = Solution()
  print(sol.find_duplicate([1, 4, 4, 3, 2]))
  print(sol.find_duplicate([2, 1, 3, 3, 5, 4]))
  print(sol.find_duplicate([2, 4, 1, 4, 4]))

main()
