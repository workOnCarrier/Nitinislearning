class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(nums:list[int], permute_res:list[int], result):
            print(f"\t permute_res:{permute_res} - sub_list:{nums}")
            if len(nums) > 0:
                for num in nums:
                    new_nums = nums.copy()
                    new_nums.remove(num)
                    permute_res.append(num)
                    dfs(new_nums, permute_res, result)
                    permute_res.remove(num)
            else:
                print(f"\t\t -- finally adding:{permute_res}")
                # permute_res_copy = permute_res.copy()
                result.append(permute_res[:])

        result = []
        for num in nums:
            permute_res = []
            new_nums = nums.copy()
            new_nums.remove(num)
            permute_res.append(num)
            dfs(new_nums, permute_res, result)
        return result
        

def test():
    nums = [1,2,3]
    s = Solution()
    longest_str = s.permute(nums)
    print(f"\t result:{longest_str}")

if __name__ == "__main__":
    test()