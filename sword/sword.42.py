#18:58fail
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        dp = [0] * n
        dp[0] = a[0]
        for i in xrange(1, n):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + a[i]
            else:
                dp[i] = a[i]
        ma = dp[0]
        for i in xrange(1, n):
            if dp[i] > ma:
                ma = dp[i]
        return ma
