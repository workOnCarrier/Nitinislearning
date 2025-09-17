from heapq import *

class Solution:

  def __init__(self):
    self.min_heap = []
    self.max_heap = []

  def insertNum(self, num):
    if not self.max_heap or -self.max_heap[0] >= num:
        heappush(self.max_heap, -num)
    else:
        heappush(self.min_heap, num)
    if len(self.max_heap) > len(self.min_heap) + 1:
        heappush(self.min_heap, -heappop(self.max_heap))
    elif len(self.max_heap) < len(self.min_heap):
        heappush(self.max_heap, -heappop(self.min_heap))

  def findMedian(self):
    # print(f"\t {self.max_heap}")
    # print(f"\t {self.min_heap}")
    if len(self.max_heap) == len(self.min_heap):
        return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
    return -self.max_heap[0] / 1.0


def main():
  sol = Solution()
  sol.insertNum(3)
  sol.insertNum(1)
  print("The median is: " + str(sol.findMedian()))
  sol.insertNum(5)
  print("The median is: " + str(sol.findMedian()))
  sol.insertNum(4)
  print("The median is: " + str(sol.findMedian()))


main()
