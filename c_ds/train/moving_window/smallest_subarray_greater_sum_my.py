import math

class Solution:
  def findMinSubArray(self, s, arr):
    print(f"\t\t {arr} +++ for {s}")
    win_sum, min_len = 0, len(arr)
    win_start = 0
    for win_end in range(len(arr)):
      win_sum += arr[win_end]
      while win_sum >= s:
        min_len = min(min_len, win_end - win_start + 1)
        print(f"\t win_sum:{win_sum} >=s:{s} === win_start:{win_start} win_end:{win_end} -- min_len{min_len}")
        win_sum -= arr[win_start]
        win_start += 1
    return min_len   

def main():
    sol = Solution()
    print("Smallest subarray length: " + str(sol.findMinSubArray(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(sol.findMinSubArray(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(sol.findMinSubArray(8, [3, 4, 1, 1, 6])))

main()
