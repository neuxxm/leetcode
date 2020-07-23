#16:07-16:14
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a = word1
        b = word2
        n = len(a)
        m = len(b)
        dp = []
        for i in xrange(n+1):
            l = [0] * (m+1)
            dp.append(l)
        for j in xrange(m+1):
            dp[0][j] = j
        for i in xrange(n+1):
            dp[i][0] = i
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        return dp[n][m]
