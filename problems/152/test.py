#11:37AC
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return 0
        dp = [0] * n
        dp2 = [0] * n
        dp[0] = a[0]
        dp2[0] = a[0]
        for i in xrange(1, n):
            dp[i] = max(a[i], dp[i-1]*a[i], dp2[i-1]*a[i])
            dp2[i] = min(a[i], dp[i-1]*a[i], dp2[i-1]*a[i])
        return max(dp)
