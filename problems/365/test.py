#14:05
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        w = set()
        w.add(0)
        w.add(x)
        w.add(y)
        w.add(abs(x-y))
        w = list(w)
        n = len(w) - 1
        cap = z
        dp = []
        for i in xrange(n+1):
            l = [float('inf')] * (cap+1)
            dp.append(l)
        dp[0][0] = 0
        for i in xrange(1, n+1):
            for j in xrange(cap+1):
                t = dp[i-1][j]
                if j >= w[i]:
                    t2 = dp[i][j-w[i]]
                    if t2 < t:
                        t = t2
                dp[i][j] = t
        for l in dp:
            print l
s = Solution()
s.canMeasureWater(3, 5, 4)
