#18:22fail
class pair:
    def __init__(self, fir, sec):
        self.fir = fir
        self.sec = sec
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        a = piles
        n = len(a)
        dp = []
        for i in xrange(n):
            l = []
            for j in xrange(n):
                t = pair(0, 0)
                l.append(t)
            dp.append(l)
        for i in xrange(n):
            dp[i][i].fir = a[i]
            dp[i][i].sec = 0
        for l in xrange(1, n):
            for i in xrange(0, n):
                j = i + l
                if j >= n:
                    continue
                left = dp[i+1][j].sec + a[i]
                right = dp[i][j-1].sec + a[j]
                if left > right:
                    dp[i][j].fir = left
                    dp[i][j].sec = dp[i+1][j].fir
                else:
                    dp[i][j].fir = right
                    dp[i][j].sec = dp[i][j-1].fir
        return dp[0][n-1].fir - dp[0][n-1].sec > 0
