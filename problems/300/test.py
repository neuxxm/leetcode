#14:09-14:14
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = 1
        for i in xrange(1, n):
            m = 1
            for j in xrange(i):
                if a[i] > a[j]:
                    t = dp[j] + 1
                    if t > m:
                        m = t
            dp[i] = m
        return max(dp)
