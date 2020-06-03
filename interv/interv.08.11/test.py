#14:54-15:10
class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        cap = n
        a = [0, 1, 5, 10, 25]
        n = len(a) - 1
        dp = [0] * (cap+1)
        dp[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(a[i], cap+1):
                dp[j] += dp[j-a[i]]%1000000007
        return dp[cap]%1000000007
