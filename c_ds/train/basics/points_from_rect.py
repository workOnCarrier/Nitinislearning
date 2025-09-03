# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/editorial/?envType=daily-question&envId=2025-09-02

class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
       
        points.sort(key=lambda x: (x[0], -x[1]))
        pairs = set()
        processed = [point for point in points[0:1]]
        print(f"\t sorted:{points}")
        for point in points:
            if point in processed:
                continue
            for prev_proc in processed[-1:]:
                if prev_proc[1] >= point[1]:
                    if (prev_proc[0], point[0]) not in pairs:
                        pairs.add((prev_proc[0], point[0]))
        return len(pairs)

def test():
    # points = [[1,1],[2,2],[3,3]]
    points = [[0,1],[0,2],[0,4]]
    s = Solution()
    no_of_rectangles = s.numberOfPairs(points)
    print(no_of_rectangles )

if __name__ == "__main__":
    test()