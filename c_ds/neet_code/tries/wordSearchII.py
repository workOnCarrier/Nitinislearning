class Trie:
    def __init__(self):
        self.children = {}
        self.isLast = False
    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isLast = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        visited, result = set(), set()
        cw = ''
        isValid = lambda r, c: r < len(board) and r >= 0 and c >= 0 and c < len(board[0]) and (r,c) not in visited

        def dfs(row, col, node, cur_word):
            curval = board[row][col]
            if curval not in node.children:
                return
            next_node = node.children[curval]
            visited.add( (row, col) )
            cur_word += curval
            if next_node.isLast:
                result.add(cur_word)
            candidates = [ (row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]
            valcan = [(nr, nc) for nr, nc in candidates if isValid(nr, nc)]
            for nr, nc in valcan:
                dfs(nr, nc, next_node, cur_word)
            visited.remove( (row, col) )

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, trie, cw)
        return list(result)


        