from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1 = nums1 if len(nums1) < len(nums2) else nums2
        a2 = nums1 if a1 == nums2 else nums2
        map_min = dict()
        for value in a1:
            if value not in map_min.keys():
                map_min[value] = (1,0)
            else:
                map_min[value] = (map_min[value][0]+1, 0)
        for cvalue in a2:
            if cvalue in map_min.keys():
                map_min[cvalue] = (map_min[cvalue][0],  map_min[cvalue][1]+1)
        final_list = list()
        for key, value in map_min.items():
            if value[1] > 0:
                for count in range(min(value[0], value[1])):
                    final_list.append(key)
        return final_list