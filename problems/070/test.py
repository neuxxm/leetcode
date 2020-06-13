class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * max(n+1, 3)
        dp[1] = 1
        dp[2] = 2
        for i in xrange(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
