class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def swap(matrix: list, p1: list, p2: list):
            print(f"\t -- swapping:{p1} with {p2}")
            tmp = matrix[p1[0]][p1[1]]
            matrix[p1[0]][p1[1]] = matrix[p2[0]][p2[1]]
            matrix[p2[0]][p2[1]] = tmp

        start, end = 0, len(matrix)-1
        x_max, y_max = len(matrix), len(matrix[0])
        if x_max != y_max:
            raise Exception("invalid matrix")
        while start < end:
            print(f"\t\t rotating circle start:{start}, end:{end}")
            g1p = lambda offset, start, end: (start, end - offset)
            g2p = lambda offset, start, end: (offset, start)
            g3p = lambda offset, start, end: (end, offset)
            g4p = lambda offset, start, end: (end - offset, end)
            offset = start
            while offset < end:
                p1 = g1p(offset - start, start, end)
                p2 = g2p(offset, start, end)
                p3 = g3p(offset, start, end)
                p4 = g4p(offset - start , start, end)
                print(f"\t p1:{p1}, p2:{p2}, p3:{p3}, p4:{p4}")
                swap(matrix, p1, p2)
                swap(matrix, p2, p3)
                swap(matrix, p3, p4)
                offset += 1
            start += 1
            end -= 1

def test():
    # matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    s = Solution()
    s.rotate(matrix)
    print(f"\t result:{matrix}")

if __name__ == "__main__":
    test()