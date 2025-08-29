class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


def main():
    s = Solution()
    print(s.climbStairs(1))
    print(s.climbStairs(2))
    print(s.climbStairs(6))


if __name__ == "__main__":
    main()