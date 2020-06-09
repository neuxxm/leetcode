#11:29-11:45
def f(s, i, n, two2, dp):
    if i in dp:
        return dp[i]
    if i == n:
        dp[i] = 1
        return 1
    if s[i] == '1':
        if i+1 < n:
            dp[i] = f(s, i+1, n, two2, dp) + f(s, i+2, n, two2, dp)
            return dp[i]
        else:
            dp[i] = f(s, i+1, n, two2, dp)
            return dp[i]
    if s[i] == '2':
        if i+1 < n and s[i+1] in two2:
            dp[i] = f(s, i+1, n, two2, dp) + f(s, i+2, n, two2, dp)
            return dp[i]
        else:
            dp[i] = f(s, i+1, n, two2, dp)
            return dp[i]
    else:
        dp[i] = f(s, i+1, n, two2, dp)
        return dp[i]
class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = '%d'%num
        n = len(s)
        two2 = {}
        for i in xrange(6):
            two2['%d'%i] = 1
        dp = {}
        return f(s, 0, n, two2, dp)
