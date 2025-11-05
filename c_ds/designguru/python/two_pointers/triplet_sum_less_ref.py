class Solution:
  def searchTriplets(self, arr, target):
    if len(arr) < 3:
      return 0
      
    arr.sort()
    count = 0
    for i in range(len(arr)-2):
      count += self.searchPair(arr, target - arr[i], i)
    return count


  def searchPair(self, arr, target_sum, first):
    count = 0
    left, right = first + 1, len(arr) - 1
    while (left < right):
      if arr[left] + arr[right] < target_sum:  # found the triplet
        # since arr[right] >= arr[left], therefore, we can replace arr[right] by any 
        # number between left and right to get a sum less than the target sum
        count += right - left
        left += 1
      else:
        right -= 1  # we need a pair with a smaller sum
    return count


def main():
  sol = Solution()
  print(sol.searchTriplets([-1, 0, 2, 3], 3))
  print(sol.searchTriplets([-1, 4, 2, 1, 3], 5))


main()
