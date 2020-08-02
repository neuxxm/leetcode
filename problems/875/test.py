#23:25-23:38
def f(a, n, m):
    z = 0
    for i in xrange(n):
        if a[i]%m == 0:
            z += a[i]/m
        else:
            z += a[i]/m + 1
    return z
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        a = piles
        n = len(a)
        h = H
        l = 1
        r = max(a)
        ans = -1
        while l <= r:
            m = (l+r) >> 1
            t = f(a, n, m)
            if t == h:
                return m
            if t > h:
                ans = m+1
                l = m+1
            else:
                ans = m
                r = m-1
        return ans
