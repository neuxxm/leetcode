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
        r = float('-inf')
        for i in xrange(n):
            list = [float('-inf')] * m
            dp.append(list)
        #return calc(a, b, n, m, dp)
        for j in xrange(0, m):
            ma = a[0] * b[j]
            for k in xrange(j-1, -1, -1):
                t = a[0] * b[k]
                if t > ma:
                    ma = t
            dp[0][j] = ma
            if ma > r:
                r = ma
        for i in xrange(0, n):
            ma = a[i] * b[0]
            for k in xrange(i-1, -1, -1):
                t = a[k] * b[0]
                if t > ma:
                    ma = t
            dp[i][0] = ma
            if ma > r:
                r = ma
        for i in xrange(1, n):
            for j in xrange(1, m):
                ma = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1], dp[i-1][j-1] + a[i] * b[j], a[i] * b[j])
                dp[i][j] = ma
                if ma > r:
                    r = ma
        return r
