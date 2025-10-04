# https://leetcode.com/problems/surrounded-regions/
from collections import deque

class Solution:
    def print_board(self):
        for row in range(self.row_max):
            print("\t[", end="")
            for col in range(self.col_max):
                print(f"{self.board[row][col]}", end=", ")
            print("]")
        print(f"{'-'*30}")
 
    def dfs_operate(self, row: int, col: int, operate: callable):
        if self.visited[row][col] == True:
            return
        self.visited[row][col] = True
        if row == 0 or col == 0 or row == self.row_max - 1 or col == self.col_max - 1:
            self.backtrack = True
        else:
            if self.backtrack == False:
                operate(row, col)
        candidates = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for new_row, new_col in candidates:
            if new_row < 0 or new_col < 0 or new_row > self.row_max - 1 or new_col > self.col_max - 1:
                continue
            if self.visited[new_row][new_col] == True or self.board[new_row][new_col] == "X":
                continue
            if new_row == 0 or new_col == 0 or new_row == self.row_max - 1 or new_col == self.col_max - 1:
                # cannot be surrounded
                self.backtrack = True
            else:
                self.dfs_operate(new_row, new_col, operate)

    def solve(self, board: list[list[str]]) -> None:
        self.row_max, self.col_max = len(board), len(board[0])
        # establish visited
        self.board, self.visited = board, []
        self.print_board()

        # find all 0s
        pq = deque()
        for row in range(self.row_max):
            self.visited.append([])
            for col in range(self.col_max):
                self.visited[row].append(False)
                if board[row][col] == "O":
                    pq.append((row, col))
                else:
                    self.visited[row][col] = True
       # dfs on each 0 
        while pq:
            row, col = pq.popleft()
            set_val_list = []
            self.backtrack = False
            if self.visited[row][col] == True:
                continue
            add_set_val_list = lambda row, col: set_val_list.append((row, col))

            self.dfs_operate( row, col, add_set_val_list)
            if self.backtrack == False:
                for row, col in set_val_list:
                    board[row][col] = "X"
        self.print_board()
        

def test():
    s = Solution()
    input = [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
    s.solve(input)
    expected = [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","O"],["O","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","X"],["O","X","X","X","X","X","X","X","X","O"],["O","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
    if expected != input:
        print(" -- expected did not match output --")
    else:
        print(" -- SUCCESS -- ")



if __name__ == "__main__":
    test()

