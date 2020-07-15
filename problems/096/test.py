#14:27fail
def f(n, dp):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n in dp:
        return dp[n]
    r = 0
    for i in xrange(1, n+1):
        r += f(i-1, dp)*f(n-i, dp)
    dp[n] = r
    return r
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        return f(n, dp)
