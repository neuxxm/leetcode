#13:00AC
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        a = []
        a.append(0)
        for c in coins:
            a.append(c)
        cap = amount
        n = len(a)-1
        dp = []
        for i in xrange(n+1):
            l = [float('inf')] * (cap+1)
            dp.append(l)
        for i in xrange(n+1):
            dp[i][0] = 0
        for j in xrange(cap+1):
            dp[1][j] = j/a[1] if j%a[1] == 0 else float('inf')
        for i in xrange(2, n+1):
            for j in xrange(1, cap+1):
                dp[i][j] = dp[i-1][j]
                if j >= a[i]:
                    dp[i][j] = min(dp[i][j], dp[i][j-a[i]]+1)
                #print i,j, dp[i][j]
        return dp[n][cap] if dp[n][cap] < float('inf') else -1
