#2:27-2:30
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        s = text1
        s2 = text2
        n = len(s)
        m = len(s2)
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
                if s[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]
