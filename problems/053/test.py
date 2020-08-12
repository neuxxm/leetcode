#16:04-17:45
def f(a, l, r, n):
    if l == r:
        return a[l]
    m = (l+r) >> 1
    z1 = float('-inf')
    if m >= 0:
        i = m
        t = 0
        while i >= l:
            t += a[i]
            if t > z1:
                z1 = t
            i -= 1
    z2 = float('-inf')
    if m+1 < n:
        i = m + 1
        t = 0
        while i <= r:
            t += a[i]
            if t > z2:
                z2 = t
            i += 1
    z = max([z1, z2, z1+z2])
    if l <= m-1:
        t = f(a, l, m-1, n)
        if t > z:
            z = t
    if m+1 <= r:
        t = f(a, m+1, r, n)
        if t > z:
            z = t
    return z
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return 0
        return f(a, 0, n-1, n)
