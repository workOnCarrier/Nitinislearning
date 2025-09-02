class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x : x[0])
        result = [intervals[0]]
        for item in intervals[1:]:
            merged_item = result[-1]
            if  merged_item[1] < item[0]:
                result.append(item)
            else:
                merged_item[1] = max(merged_item[1], item[1])
        return result




def test():
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[2,6],[1,3],[1,4],[8,10],[15,18]]
    s = Solution()
    final_list = s.merge(intervals)
    print(f"\t for input:{intervals} \n\t merged:{final_list}")



if __name__ == "__main__":
    test()