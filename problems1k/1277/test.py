#21:33-21:38
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        a = matrix
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        dp = []
        for i in xrange(n):
            l = [0] * m
            dp.append(l)
        for i in xrange(m):
            dp[0][i] = a[0][i]
        for i in xrange(n):
            dp[i][0] = a[i][0]
        for i in xrange(1, n):
            for j in xrange(1, m):
                if a[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = 0
        r = 0
        for i in xrange(0, n):
            r += sum(dp[i])
        return r
