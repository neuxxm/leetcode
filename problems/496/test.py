#18:05-18:08
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        for i,t in enumerate(nums2):
            map[t] = i
        a = nums1
        n = len(a)
        b = nums2
        m = len(b)
        rs = []
        for i in xrange(n):
            if a[i] in map:
                z = True
                for j in xrange(map[a[i]]+1, m):
                    if b[j] > a[i]:
                        rs.append(b[j])
                        z = False
                        break
                if z:
                    rs.append(-1)
            else:
                rs.append(-1)
        return rs
