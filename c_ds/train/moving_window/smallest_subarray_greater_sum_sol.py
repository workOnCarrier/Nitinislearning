import math

class Solution:
    def findMinSubArray(self, s, arr):
        window_sum = 0      # Initialize the sum of the current window
        min_length = math.inf  # Initialize the minimum length to positive infinity
        window_start = 0    # Initialize the start of the current window

        for window_end in range(0, len(arr)):
            window_sum += arr[window_end]  # Add the next element to the window sum
            # Shrink the window as small as possible until 'window_sum' is smaller than 's'
            while window_sum >= s:
                min_length = min(min_length, window_end - window_start + 1)  # Update the minimum length
                window_sum -= arr[window_start]  # Remove the element going out of the window
                window_start += 1  # Slide the window ahead
        
        if min_length == math.inf:
            return 0
        return min_length


def main():
    sol = Solution()
    print("Smallest subarray length: " + str(sol.findMinSubArray(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(sol.findMinSubArray(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(sol.findMinSubArray(8, [3, 4, 1, 1, 6])))

main()
