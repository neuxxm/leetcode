#14:26-14:47
class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        a = nums1
        b = nums2
        n = len(a)
        m = len(b)
        dp = []
        for i in xrange(n):
            l = [0] * m
            dp.append(l)
        dp[0][0] = a[0] * b[0]
        for j in xrange(1, m):
            dp[0][j] = max(dp[0][j-1], a[0]*b[j])
        for i in xrange(1, n):
            dp[i][0] = max(dp[i-1][0], a[i]*b[0])
        for i in xrange(1, n):
            for j in xrange(1, m):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+a[i]*b[j], a[i]*b[j])
        return dp[n-1][m-1]
