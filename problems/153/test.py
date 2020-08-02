#21:32-21:41
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        l = 0
        r = n - 1
        if a[l] < a[r]:
            return a[l]
        while l <= r:
            m = (l+r) >> 1
            if m == 0:
                if a[m] > a[m+1]:
                    return a[m + 1]
                l += 1
                continue
            if m == n-1:
                r -= 1
                continue
            if a[m]>a[0] and a[m]>a[m+1]:
                return a[m + 1]
            if a[m] > a[0]:
                l = m + 1
            else:
                r = m - 1
