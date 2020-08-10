#3:25-3:31
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        a = cost
        n = len(a)
        dp = [0] * (n+1)
        dp[0] = a[0]
        dp[1] = a[1]
        if n <= 2:
            return dp[n-1]
        for i in xrange(2, n+1):
            dp[i] = min(dp[i-1], dp[i-2])
            if i < n:
                dp[i] += a[i]
        return dp[n]
