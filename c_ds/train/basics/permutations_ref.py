class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans


def test():
    nums = [1,2,3]
    s = Solution()
    longest_str = s.permute(nums)
    print(f"\t result:{longest_str}")

if __name__ == "__main__":
    test()