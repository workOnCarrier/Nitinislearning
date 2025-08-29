
class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        fibos = [0 for _ in range(n+1)]
        fibos[1] = 1
        for index in range(2, n+1):
            fibos[index] = fibos[index - 1] + fibos[index - 2]
        return fibos[n]


def main():
    s = Solution()
    print(s.fib(5))
    print(s.fib(-1))
    print(s.fib(1))
    print(s.fib(100))


if __name__ == "__main__":
    main()
