#13:30-13:42
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        k = rowIndex
        if k == 0:
            return [1]
        dp = [0] * (k+1)
        dp2 = [0] * (k+1)
        dp[0] = 1
        dp[1] = 1
        dp2[0] = 1
        for i in xrange(2, k+1):
            for j in xrange(1, i):
                dp2[j] = dp[j-1] + dp[j]
            dp2[i] = 1
            dp = dp2[:]
        return dp
