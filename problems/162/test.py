#22:17-22:31
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return 0
        if n == 1:
            return 0
        l = 0
        r = n - 1
        while l <= r:
            m = (l+r) >> 1
            if m == 0:
                if a[m] > a[m+1]:
                    return m
                l += 1
                continue
            if m == n-1:
                if a[m] > a[m-1]:
                    return m
                r -= 1
                continue
            if a[m]>a[m-1] and a[m]>a[m+1]:
                return m
            if a[m]>a[m-1]:
                l = m+1
            else:
                r = m-1
