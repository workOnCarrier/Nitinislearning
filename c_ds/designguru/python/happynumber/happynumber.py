class Solution:
  def find_square_sum(self, num):
    square_sum = 0
    while num > 0:
      digit = (int)(num % 10)
      num = (int)(num / 10)
      square_sum += digit * digit
    return square_sum

  def find(self, num):
    print(f" num:{num}")
    fast = self.find_square_sum(self.find_square_sum(num))
    slow = self.find_square_sum(num)
    print(f" slow:{slow} - fast:{fast}")
    while True:
      fast = self.find_square_sum(self.find_square_sum(fast))
      slow = self.find_square_sum(slow)
      print(f" slow:{slow} - fast:{fast}")
      if slow == fast:
        break
    return slow == 1

def main():
  sol = Solution()
  print(sol.find(23))
  print(sol.find(12))


main()
