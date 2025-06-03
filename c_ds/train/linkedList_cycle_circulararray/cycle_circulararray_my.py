
problem = '''We are given an array containing positive and negative numbers. Suppose the array contains a number 'M' at a particular index. Now, if 'M' is positive we will move forward 'M' indices and if 'M' is negative move backwards 'M' indices. You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
Write a method to determine if the array has a cycle.

The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

'''
from enum import Enum
class Direction(Enum):
    Forward = 1
    Backward = 2

class Solution:
  def loopExists(self, arr):
    for i in range(len(arr)):
        fast, slow = i, i
        direction = Direction.Backward if arr[i] < 0 else Direction.Forward
        while True:
          fast = self.next_offset (arr, direction, fast, 'fast')
          slow = self.next_offset (arr, direction, slow, 'slow')
          if fast != -1:
            fast = self.next_offset (arr, direction, fast, 'fast 2')
          if fast == -1 or slow == -1 or fast == slow:
            break
        if fast == slow and fast != -1:
            return True
    return False
  def next_offset(self, arr, direction: Direction, offset, tag = ''):
    if direction == Direction.Forward and arr[offset] < 0:
      print(f"\t {tag} {direction} changing direction for {direction}: {arr[offset]} ({arr[offset]})")
      return -1
    elif direction == Direction.Backward and arr[offset] >= 0:
      print(f"\t {tag} {direction} changing direction for {direction}: {arr[offset]} ({arr[offset]})")
      return -1
    
    new_offset = (arr[offset]  + offset )% len(arr)
    print(f" {tag} {direction} new offset -- old offset {new_offset}: {offset} ({arr[offset]})")
    # same element loop -- can happen if the arr[offset] value is 0
    if new_offset == offset: 
      print(f"\t {tag} {direction} new offset == old offset {new_offset}: {offset} ({arr[offset]})")
      return -1
    return new_offset

def test():
  sol = Solution()
  # print(sol.loopExists([1, 2, -1, 2, 2]))
  print(sol.loopExists([2, 2, -1, 2]))
  # print(sol.loopExists([2, 1, -1, -2]))


if __name__ == "__main__":
  test()

