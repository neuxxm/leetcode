def get_max(a, n, x):
    ma = a[0] - 0
    t = x - a[n-1]
    if t > ma:
        ma = t
    for i in xrange(1, n):
        t = a[i] - a[i-1]
        if t > ma:
            ma = t
    return ma
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        a = horizontalCuts
        b = verticalCuts
        a.sort()
        b.sort()
        n = len(a)
        m = len(b)
        ma = get_max(a, n, h)%(1000000007)
        ma2 = get_max(b, m, w)%(1000000007)
        return (ma * ma2)%(1000000007)
