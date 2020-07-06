#20:12fail
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        a = prices
        n = len(a)
        r = 0
        for i in xrange(1, n):
            if a[i] > a[i-1]:
                r += a[i] - a[i-1]
        return r
