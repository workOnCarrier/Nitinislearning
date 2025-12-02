class Solution:
    def exist(self, board: list, word: str) -> bool:
        rows, cols = len(board), len(board[0])
        print(f"\t input {rows},{cols} for {word}")
        visited = set()
        def nav(row, col, index):
            print(f"\t checking {row},{col} for {index}")
            if board[row][col] != word[index]:
                return False
            if index + 1 == len(word):
                return True
            visited.add((row, col))
            cands = [(row + 1, col), (row -1, col), (row, col -1), (row, col + 1)]
            print(f"\t candidates {cands}")
            vcand = [(row, col) for row, col in cands if (row,col) not in visited and row >= 0 and row < rows and col >= 0 and col < cols]
            print(f"\t valid candidates {vcand}")
            for nrow, ncol in vcand:
                status = nav(nrow, ncol, index + 1)
                if status == True:
                    return True
            visited.remove((row, col))
            return False
        for crow in range(rows):
            for ccol in range(cols):
                status = nav(crow,ccol, 0)
                if status == True:
                    return True
        return False
       

def test():
    input = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    input = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    s = Solution()
    status = s.exist(input, word)
    print(status)

if __name__ == "__main__":
    test()