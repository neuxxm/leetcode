#14:57-15:33
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        zero = []
        one = []
        for s in strs:
            l = len(s)
            t = s.count('0')
            zero.append(t)
            one.append(l-t)
        an = len(strs)
        dp = []
        for j in xrange(m+1):
            l = [0] * (n+1)
            dp.append(l)
        for j in xrange(m+1):
            for k in xrange(n+1):
                if j>=zero[0] and k>=one[0]:
                    dp[j][k] = 1
        for i in xrange(1, an):
            for j in xrange(m, -1, -1):
                for k in xrange(n, -1, -1):
                    if j>=zero[i] and k>=one[i]:
                        dp[j][k] = max(dp[j][k], dp[j-zero[i]][k-one[i]] + 1)
        return dp[m][n]
