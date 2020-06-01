#16:35
import bisect
class bit:
    def __init__(self, n):
        self.a = [0] * (n+1)
        self.n = n
    def f(self, x):
        return x & -x
    def update(self, i, val):
        while i < self.n:
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
        sa = sorted(a)
        for i in xrange(n):
            a[i] = bisect.bisect_left(sa, a[i]) + 1
        b = bit(n)
        z = 0
        for i in xrange(n-1, -1, -1):
            t = a[i]
            z += b.sum(t-1)
            b.update(t, 1)
        return z
s = Solution()
print s.reversePairs([7,6,5,4])
