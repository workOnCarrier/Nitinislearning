import math
class Solution:
  def findMaxSumSubArray(self,k, arr):
    window_end = 0
    window_start = 0
    max_sum = -math.inf
    cur_sum = 0
    while window_end < len(arr):
      cur_sum += arr[window_end]
      # if (window_end - window_start + 1 ) >= k:
      if window_end >= k - 1:
        max_sum = max(max_sum, cur_sum)
        cur_sum -= arr[window_start]
        window_start += 1
      window_end += 1
    return max_sum
    
def main():
    sol = Solution()
    print("Maximum sum of a subarray of size K: " +
        str(sol.findMaxSumSubArray(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
        str(sol.findMaxSumSubArray(2, [2, 3, 4, 1, 5])))

main()
