class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        end = len(height) - 1
        max_vol = 0
        while start < end:
            # print(f" \t\t start:{start}({height[start]}) - end:{end}({height[end]})")
            max_vol = max(max_vol, (end - start) * min(height[start], height[end]))
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return max_vol


def test():
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    max_area = s.maxArea(height)
    print(f"\t max area:{max_area}")


if __name__ == "__main__":
    test()
