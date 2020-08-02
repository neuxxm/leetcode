#22:36-22:40
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = A
        n = len(a)
        if n == 0:
            return 0
        l = 0
        r = n-1
        while l <= r:
            m = (l+r) >> 1
            if m == 0:
                l += 1
                continue
            if m == n-1:
                r -= 1
                continue
            if a[m]>a[m-1] and a[m]>a[m+1]:
                return m
            if a[m] > a[m-1]:
                l = m+1
            else:
                r = m-1
