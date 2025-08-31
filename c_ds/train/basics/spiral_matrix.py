class Solution:
    def __init__(self):
        self.direction_order = ['r', 'd', 'l', 'u']
        self.operation_order = [    lambda row, col : (row, col + 1),
                                    lambda row, col : (row + 1, col),
                                    lambda row, col : (row, col - 1),
                                    lambda row, col : (row - 1, col) ]

        self.undo_operation= [      lambda row, col : (row, col - 1),
                                    lambda row, col : (row - 1, col),
                                    lambda row, col : (row, col + 1),
                                    lambda row, col : (row + 1, col) ]
        self.result_set = list()
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row_max = len(matrix)
        col_max = len(matrix[0])
        full_len = row_max * col_max
        row, col = 0, 0 
        order_offset = 0
        cur_len = len(self.result_set)
        while cur_len < full_len :
            cur_len = len(self.result_set)
            if (row, col) not in self.result_set and row < row_max and col < col_max and row >= 0 and col >= 0:
                self.result_set.append((row, col))
                row, col = self.operation_order[order_offset](row, col)
                print(f" after update: row({row}), col({col})")
            else:
                row, col = self.undo_operation[order_offset](row, col)
                order_offset = (order_offset + 1) % len(self.direction_order)
                row, col = self.operation_order[order_offset](row, col)
                print(f" after undo: row({row}), col({col}) _____ order_offset:{order_offset} going:{self.direction_order[order_offset]}")
        result = []
        print(f"\t result set:{self.result_set}")
        for row, col in self.result_set:
            result.append(matrix[row][col])
        return result


def test():
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    s = Solution()
    result = s.spiralOrder(matrix)
    print(f"\tfor matrix:{matrix}\n\t spiral result:{result }")

if __name__ == "__main__":
    test()

        