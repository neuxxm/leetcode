#0:07-0:12
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = A
        n = len(a)
        l = 0
        r = n - 1
        while l <= r:
            m = (l+r) >> 1
            if m == 0:
                l = m + 1
                continue
            if m == n-1:
                r = m - 1
                continue
            if a[m]>a[m-1] and a[m]>a[m+1]:
                return m
            if a[m] > a[m-1]:
                l = m + 1
            else:
                r = m - 1
