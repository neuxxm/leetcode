#2:56-3:12
def f(a, n, m):
    t = 0
    i = 0
    z = 0
    while i < n:
        if t + a[i] <= m:
            t += a[i]
        else:
            z += 1
            t = a[i]
        i += 1
    if t > 0:
        z += 1
    return z
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        a = weights
        d = D
        n = len(a)
        l = max(a)
        r = sum(a)
        ans = 0
        while l <= r:
            m = (l+r) >> 1
            t = f(a, n, m)
            if t <= d:
                ans = m
                r = m-1
            else:
                l = m+1
        return ans
