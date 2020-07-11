#20:19-20:37
import bisect
def lowbit(x):
    return x&-x
class bit_t:
    def __init__(self, n):
        self.a = [0] * (n+1)
        self.n = n
    def update(self, i, val):
        while i <= self.n:
            self.a[i] += val
            i += lowbit(i)
    def sum(self, i):
        r = 0
        while i >= 1:
            r += self.a[i]
            i -= lowbit(i)
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
        sa2 = []
        if n == 0:
            return 0
        sa2.append(sa[0])
        last = sa[0]
        for i in xrange(1, n):
            if sa[i] == last:
                pass
            else:
                sa2.append(sa[i])
                last = sa[i]
        r = 0
        sa2_len = len(sa2)
        b = bit_t(sa2_len)
        for i in xrange(n-1, -1, -1):
            t = bisect.bisect_left(sa2, a[i]/2)
            if t >= sa2_len:
                r += b.sum(t)
            elif t>=0 and a[i] > sa2[t]*2:
                r += b.sum(t+1)
            elif t>0 and a[i] > sa2[t-1]*2:
                r += b.sum(t)
            t = bisect.bisect_left(sa2, a[i]) + 1
            b.update(t, 1)
        return r
