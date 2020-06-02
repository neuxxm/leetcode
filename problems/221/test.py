#12:47-12:50
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        a = matrix
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        dp = []
        z = 0
        for i in xrange(n):
            l = [0] * m
            dp.append(l)
        for i in xrange(m):
            if a[0][i] == '1':
                dp[0][i] = 1
            else:
                dp[0][i] = 0
            if dp[0][i] > z:
                z = dp[0][i]
        for i in xrange(n):
            if a[i][0] == '1':
                dp[i][0] = 1
            else:
                dp[i][0] = 0
            if dp[i][0] > z:
                z = dp[i][0]
        for i in xrange(1, n):
            for j in xrange(1, m):
                if a[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = 0
                if dp[i][j] > z:
                    z = dp[i][j]
        return z*z
