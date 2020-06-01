#17:09
import bisect
class bit:
    def __init__(self, n):
        self.a = [0] * (n+1)
        self.n = n
    def f(self, x):
        return x & -x
    def update(self, i, val):
        while i <= self.n: # !!!
            self.a[i] += val
            i += self.f(i)
    def sum(self, i):
        r = 0
        while i > 0:
            r += self.a[i]
            i -= self.f(i)
        return r
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        sa = []
        map = {}
        for t in a:
            if t in map:
                continue
            map[t] = 1
            sa.append(t*2)
        sa.sort()
        b = bit(n)
        z = 0
        for i in xrange(n-1, -1, -1):
            ix = bisect.bisect_left(sa, a[i]) + 1
            if ix > 0:
                z += b.sum(ix-1)
                ix2 = bisect.bisect_left(sa, a[i]*2) + 1
                b.update(ix2, 1)
        return z
