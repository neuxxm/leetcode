#12:07-12:11
def f(n, dp):
    if n in dp:
        return dp[n]
    t = f(n-1, dp) + f(n-2, dp) + f(n-3, dp)
    dp[n] = t
    return t
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        return f(n, dp)
