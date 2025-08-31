class Solution:
    def countAndSay(self, n: int) -> str:
        cs = "1"
        for _ in range(n-1):
            ns = ""
            j, k = 0, 0
            while k < len(cs):
                while k < len(cs) and cs[j] == cs[k]:
                    k += 1
                ns += str(k-j) + cs[j]
                j = k
            cs = ns
        return cs


def test():
    s = Solution()
    for input in range(3, 10):
        print(f"cas for {input}: {s.countAndSay(input)}")


if __name__ == "__main__":
    test()