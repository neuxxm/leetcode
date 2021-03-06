#16:51-17:00
import bisect
def lowbit(x):
    return x&-x
class bit_t:
    def __init__(self, n):
        self.a = [0] * (n+1)
        self.n = n
    def update(self, i, v):
        while i <= self.n:
            self.a[i] += v
            i += lowbit(i)
    def query(self, i):
        r = 0
        while i >= 1:
            r += self.a[i]
            i -= lowbit(i)
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
        b = bit_t(n)
        rs = []
        for i in xrange(n-1, -1, -1):
            t = b.query(a[i]-1)
            rs.append(t)
            b.update(a[i], 1)
        return rs[::-1]
