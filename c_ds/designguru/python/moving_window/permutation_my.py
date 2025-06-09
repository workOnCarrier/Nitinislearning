import math

class Solution:
  def findPermutation(self, str1, pattern):
      
    return False

def main():
    sol = Solution()
    print('Permutation exist: ' + str(sol.findPermutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(sol.findPermutation("odicf", "dc")))
    print('Permutation exist: ' + str(sol.findPermutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(sol.findPermutation("aaacb", "abc")))


main()
