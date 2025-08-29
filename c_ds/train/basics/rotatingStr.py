class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        slen = len(s)
        if slen == 1:
            return s == goal
        for _ in range(slen):
            s = s[1:] + (s[0])
            if s == goal:
                return True
        return False

def main():
    s = Solution()

    check_str = "abcdefg"
    goal = "defgabc"
    print(s.rotateString(check_str, goal))

    check_str = "abcdefgabcdefg"
    goal = "d"
    print(s.rotateString(check_str, goal))

if __name__ == "__main__":
    main()