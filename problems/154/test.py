#15:50-16:34
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
            if m > 0:
                if a[m] < a[m-1]:
                    return a[m]
            else:
                if a[m] > a[m+1]:
                    l = m + 1
                    continue
            if a[m] > a[0]:
                l = m + 1
            elif a[m] < a[n-1]:
                r = m - 1
            else:
                if a[r] == a[n-1]:
                    r = r - 1
                else:
                    l = l + 1
        return a[l]
