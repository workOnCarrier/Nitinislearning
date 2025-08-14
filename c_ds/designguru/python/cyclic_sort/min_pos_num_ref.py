class Solution:
    def findNumber(self, nums):
        i, n = 0, len(nums)
        # Rearrange the elements to place each positive integer at its correct index.
        # Negative numbers and numbers greater than the array size are ignored.
        while i < n:
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # Swap
            else:
                i += 1

        # Find the first index where the element does not match its expected positive value.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all elements from 1 to n are present, return n + 1.
        return len(nums) + 1


def main():
    sol = Solution()
    print(sol.findNumber([-3, 1, 5, 4, 2]))
    print(sol.findNumber([3, -2, 0, 1, 2]))
    print(sol.findNumber([3, 2, 5, 1]))


main()
