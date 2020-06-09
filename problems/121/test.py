#14:35fail
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mi = float('inf')
        a = prices
        n = len(a)
        z = 0
        for i in xrange(n):
            t = a[i] - mi
            if t > z:
                z = t
            if a[i] < mi:
                mi = a[i]
        return z
