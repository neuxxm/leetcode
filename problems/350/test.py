#15:08-15:10
from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = defaultdict(lambda:0)
        for t in nums1:
            map[t] += 1
        map2 = defaultdict(lambda:0)
        for t in nums2:
            if t in map:
                map2[t] += 1
        rs = []
        for t in map.keys():
            m = min(map[t], map2[t])
            for i in xrange(m):
                rs.append(t)
        return rs
