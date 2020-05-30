#20:19fail
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
        r = 0
        for i in xrange(n):
            l = [0] * m
            dp.append(l)
        for i in xrange(m):
            dp[0][i] = 1 if a[0][i] == '1' else 0
            if a[0][i] == '1':
                r = 1
        for i in xrange(n):
            dp[i][0] = 1 if a[i][0] == '1' else 0
            if a[i][0] == '1':
                r = 1
        for i in xrange(1, n):
            for j in xrange(1, m):
                if a[i][j] == '1':
                    t = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    dp[i][j] = t
                    if t > r:
                        r = t
                else:
                    dp[i][j] = 0
        return r*r
