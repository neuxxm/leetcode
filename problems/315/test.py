#15:14-15:24
import bisect
class bit():
    def __init__(self, n):
        self.a = [0] * (n+1)
        self.n = n
    def lowbit(self, x):
        return x&-x
    def update(self, i, val):
        while i <= self.n:
            self.a[i] += val
            i += self.lowbit(i)
    def sum(self, i):
        r = 0
        while i > 0:
            r += self.a[i]
            i -= self.lowbit(i)
        return r
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = nums
        sa = sorted(a)
        n = len(a)
        for i in xrange(n):
            a[i] = bisect.bisect_left(sa, a[i]) + 1
        b = bit(n)
        r = [0] * n
        for i in xrange(n-1, -1, -1):
            r[i] = b.sum(a[i]-1)
            b.update(a[i], 1)
        return r
