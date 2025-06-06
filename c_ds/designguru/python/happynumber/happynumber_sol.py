class Solution:
  def find(self, num):
    slow, fast = num, num
    while True:
      slow = self.find_square_sum(slow)  # move one step
      fast = self.find_square_sum(self.find_square_sum(fast))  # move two steps
      if slow == fast:  # found the cycle
        break
    return slow == 1  # see if the cycle is stuck on the number '1'


  def find_square_sum(self, num):
    _sum = 0
    while (num > 0):
      digit = num % 10
      _sum += digit * digit
      num //= 10
    return _sum


def main():
  sol = Solution()
  print(sol.find(23))
  print(sol.find(12))


main()
