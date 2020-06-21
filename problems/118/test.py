#17:27AC
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n = numRows
        dp = []
        for i in xrange(n):
            l = [0] * (i+1)
            dp.append(l)
        for i in xrange(n):
            dp[i][0] = 1
            dp[i][i] = 1
        for i in xrange(2, n):
            for j in xrange(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp
