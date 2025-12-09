class Solution:
    def letterCombinations(self, digits: str) -> list:
        dcmap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res, part = [], []
        def dfs(i):
            if i >= len(digits):
                res.append("".join(part))
                return
            vals = dcmap[digits[i]]
            for val in vals:
                part.append(val)
                dfs(i + 1)
                part.pop()
        if digits:
            dfs(0)
        else:
            return []
        return res

def test():
    sol = Solution()
    assert sorted(sol.letterCombinations("23")) == sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])
    assert sol.letterCombinations("") == []
    assert sol.letterCombinations("2") == ["a","b","c"]

if __name__ == "__main__":
    test()