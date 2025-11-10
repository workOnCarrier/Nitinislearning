from typing import List

nums1 = [-12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0]
m = 1
nums2 = [-49, -45, -42, -41, -40, -39, -39, -39, -38, -36, -34, -34, -33, -33, -32, -31, -29, -28,
         -26, -26, -24, -21, -20, -20, -18, -16, -16, -14, -11, -7, -6, -5, -4, -4, -3, -3, -2, -2,
         -1, 0, 0, 0, 2, 2, 6, 7, 7, 8, 10, 10, 13, 13, 15, 15, 16, 17, 17, 19, 19, 20, 20, 20, 21,
         21, 22, 22, 24, 24, 25, 26, 27, 29, 30, 30, 30, 35, 36, 36, 36, 37, 39, 40, 41, 42, 45, 46,
         46, 46, 47, 48]
n = 90

expected = [-49, -45, -42, -41, -40, -39, -39, -39, -38, -36, -34, -34, -33, -33, -32, -31, -29,
            -28, -26, -26, -24, -21, -20, -20, -18, -16, -16, -14, -12, -11, -7, -6, -5, -4, -4, -3,
            -3, -2, -2, -1, 0, 0, 0, 2, 2, 6, 7, 7, 8, 10, 10, 13, 13, 15, 15, 16, 17, 17, 19, 19,
            20, 20, 20, 21, 21, 22, 22, 24, 24, 25, 26, 27, 29, 30, 30, 30, 35, 36, 36, 36, 37, 39,
            40, 41, 42, 45, 46, 46, 46, 47, 48]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos_1 = 0
        pos_2 = 0
        r_pos = 0
        result = list()
        while r_pos < m + n :
            if pos_2 >= n:
                result.append(nums1[pos_1])
                pos_1 += 1
                r_pos += 1
            elif nums1[pos_1] < nums2[pos_2] and pos_1 < m:
                result.append(nums1[pos_1])
                pos_1 += 1
                r_pos += 1
            elif nums1[pos_1] == nums2[pos_2] and pos_1 < m:
                result.append(nums1[pos_1])
                result.append(nums1[pos_1])
                pos_1 += 1
                pos_2 += 1
                r_pos += 2
            else:
                result.append(nums2[pos_2])
                pos_2 += 1
                r_pos += 1
        pos_1 = 0
        for item in result:
            nums1[pos_1] = item
            pos_1 += 1


if __name__ == '__main__':
    obj = Solution()
    obj.merge(nums1, m, nums2, n)
    print(nums1)
