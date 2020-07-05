#11:16fail
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        dp = []
        for i in xrange(n+1):
            l = [False] * (m+1)
            dp.append(l)
        dp[0][0] = True
        #i=0
        j = 1
        while j <= m:
            if p[j-1] == '*':
                dp[0][j] = True
                j += 1
            else:
                break
        while j <= m:
            dp[0][j] = False
            j += 1
        #j=0
        for i in xrange(1, n+1):
            dp[i][0] = False
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                if p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    if s[i-1] == p[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False
        return dp[n][m]
