class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        a = sorted(piles)
        k = 0
        n = len(a)
        c = len(a) / 3
        r = 0
        for i in xrange(n-2, -1, -2):
            r += a[i]
            k += 1
            if k >= c:
                break
        return r
