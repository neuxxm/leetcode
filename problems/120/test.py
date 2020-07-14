#13:57-14:15
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        a = triangle
        n = len(a)
        if n == 0:
            return 0
        dp = [0] * n
        dp2 = [0] * n
        dp[0] = a[0][0]
        for i in xrange(1, n):
            dp2[0] = dp[0] + a[i][0]
            for j in xrange(1, i):
                dp2[j] = min(dp[j-1], dp[j]) + a[i][j]
            dp2[i] = dp[i-1] + a[i][i]
            dp = dp2[:]
        return min(dp)
