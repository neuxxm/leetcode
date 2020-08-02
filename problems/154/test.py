#21:55-22:09
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
        t = a[l]
        if l+1<n and a[l+1] == t:
            while l<r and a[l]==t:
                l += 1
            if a[l] != t:
                l -= 1
        t = a[r]
        if r-1>=0 and a[r-1] == t:
            while l<r and a[r]==t:
                r -= 1
            if a[r] != t:
                r += 1
        if l == r:
            return a[l]
        while l <= r:
            m = (l+r) >> 1
            if m == 0:
                if a[m] > a[m+1]:
                    return a[m+1]
                l += 1
                continue
            if m == n-1:
                r -= 1
                continue
            if a[m]>=a[0] and a[m]>a[m+1]:
                return a[m+1]
            if a[m] >= a[0]:
                l = m+1
            else:
                r = m-1
