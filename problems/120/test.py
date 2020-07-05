#17:32-17:50
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        a = triangle
        n = len(a)
        dp = [float('inf')] * n
        dp2 = [float('inf')] * n
        for i in xrange(n):
            t = a[i][0]
            if i > 0:
                t += dp2[0]
            dp[0] = t
            t = a[i][i]
            if i > 0:
                t += dp2[i-1]
            dp[i] = t
            for j in xrange(1, i):
                dp[j] = min(dp2[j-1], dp2[j]) + a[i][j]
            dp2 = dp[:]
        return min(dp)
