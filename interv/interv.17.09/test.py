#14:08fail
class Solution(object):
    def getKthMagicNumber(self, k):
        """
        :type k: int
        :rtype: int
        """
        n = k
        dp = [0] * (1+n)
        dp[1] = 1
        z = 2
        i = 1
        j = 1
        k = 1
        while z <= n:
            a = dp[i]*3
            b = dp[j]*5
            c = dp[k]*7
            m = min(a, b, c)
            dp[z] = m
            z += 1
            if m == a:
                i += 1
            if m == b:
                j += 1
            if m == c:
                k += 1
        return dp[n]
