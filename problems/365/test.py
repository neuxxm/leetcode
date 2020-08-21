#15:32
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
        print w
        dp = []
        for i in xrange(n+1):
            l = [float('inf')] * (cap+1)
            dp.append(l)
        dp[0][0] = 0
        for i in xrange(1, n+1):
            for j in xrange(w[i], cap+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-w[i]])
                print i, j, dp[i][j], dp[i-1][j], dp[i][j-w[i]]
        for l in dp:
            print l
        return dp[n][cap] == 0
x = 3
y = 5
z = 4
s = Solution()
print s.canMeasureWater(x, y, z)
