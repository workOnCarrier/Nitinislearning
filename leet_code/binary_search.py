from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found_index = -1
        start_index = 0
        end_index = len(nums)
        while start_index < end_index:
            mid_index = int((end_index + start_index - 1 ) / 2)
            if nums[mid_index] == target:
                found_index = mid_index
                break
            elif nums[mid_index] > target:
                if mid_index == end_index:
                    end_index -= 1
                    continue
                end_index = mid_index
            else:
                if start_index == mid_index:
                    start_index += 1
                    continue
                start_index = mid_index
        return found_index


def try_solution ():
    nums = [-1, 0, 3, 5, 9, 12]
    # nums = [-1, 0, 3, 5, 9 ]
    target = 9
    sol = Solution()
    result = sol.search(nums, target)
    print(f'found result {result}')

if __name__ == '__main__':
    try_solution()