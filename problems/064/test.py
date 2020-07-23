#15:47-15:54
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a = grid
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        dp = []
        for i in xrange(n):
            l = [0] * m
            dp.append(l)
        dp[0][0] = a[0][0]
        for j in xrange(1, m):
            dp[0][j] = dp[0][j-1] + a[0][j]
        for i in xrange(1, n):
            dp[i][0] = dp[i-1][0] + a[i][0]
        for i in xrange(1, n):
            for j in xrange(1, m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + a[i][j]
        return dp[n-1][m-1]
