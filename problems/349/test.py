#23:38AC
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        map2 = {}
        for a in nums1:
            map[a] = 1
        r = []
        for a in nums2:
            if a in map:
                if a not in map2:
                    map2[a] = 1
                    r.append(a)
        return r
