# problem statement 
'''Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
'''

# mistakes -- use max queue instead of min queue -- gives kth min
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minh = []
        for i in range(len(nums)):
            if len(minh) < k:
                heapq.heappush(minh, nums[i])
            else:
                heapq.heappush(minh, nums[i])
                while len(minh) > k:
                    heapq.heappop(minh)
        return minh[0]
