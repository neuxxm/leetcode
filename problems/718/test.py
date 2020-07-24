#14:08
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        a = A
        b = B
        n = len(a)
        m = len(b)
        dp = []
        for i in xrange(n+1):
            l = [0] * (m+1)
            dp.append(l)
        for j in xrange(m+1):
            dp[0][j] = 0
        for i in xrange(n+1):
            dp[i][0] = 0
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]
