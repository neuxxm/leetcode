#18:34-18:48
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        s1 = word1
        s2 = word2
        n = len(s1)
        m = len(s2)
        dp = []
        for i in xrange(n+1):
            l = [0] * (m+1)
            dp.append(l)
        for i in xrange(m+1):
            dp[0][i] = i
        for i in xrange(n+1):
            dp[i][0] = i 
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] 
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[n][m]
