#14:48-15:12
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = nums
        n = len(a)
        s = sum(a)
        if s%2 != 0:
            return False
        cap = s / 2
        dp = []
        for i in xrange(n+1):
            l = [0] * (cap+1)
            dp.append(l)
        dp[0][0] = 1
        for i in xrange(1, n+1):
            for j in xrange(0, a[i-1]):
                if j > cap:
                    continue
                dp[i][j] = dp[i-1][j]
            for j in xrange(a[i-1], cap+1):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-a[i-1]])
        return dp[n][cap] == 1
