#23:14-23:45
def adjust(a, n, i):
    cur = i
    while cur < n:
        l = cur*2+1
        r = l+1
        ma_ix = cur
        if l < n and a[l] > a[ma_ix]:
            ma_ix = l
        if r < n and a[r] > a[ma_ix]:
            ma_ix = r
        if ma_ix == cur:
            return
        a[cur], a[ma_ix] = a[ma_ix], a[cur]
        cur = ma_ix
#    5
#  4   3
# 2 1
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        a = stones
        n = len(a)
        if n < 2:
            return a[0]
        for i in xrange(n/2, -1, -1):
            adjust(a, n, i)
        i = n - 1
        while True:
            x = a[0]
            a[0] = a[i]
            adjust(a, i, 0)
            i -= 1
            if i == -1:
                return a[0]
            y = a[0]
            #print x, y
            if x == y:
                a[0] = a[i]
                adjust(a, i, 0)
                i -= 1
                if i == -1:
                    return 0
            else:
                a[0] = abs(x-y)
                adjust(a, i+1, 0)
            #print a[:i+1]
