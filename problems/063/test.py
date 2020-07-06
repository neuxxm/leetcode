#11:07-11:19
def f(a, x, y, n, m, dp):
    if dp[x][y] != -1:
        return dp[x][y]
    if x == n-1 and y == m-1:
        dp[x][y] = 1
        return 1
    dx = [0, 1]
    dy = [1, 0]
    r = 0
    for k in xrange(2):
        x2 = x + dx[k]
        y2 = y + dy[k]
        if x2>=0 and x2<n and y2>=0 and y2<m and a[x2][y2] == 0:
            r += f(a, x2, y2, n, m, dp)
    dp[x][y] = r
    return r
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        a = obstacleGrid
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        z = [0]
        if a[0][0] == 0:
            dp = []
            for i in xrange(n):
                l = [-1] * m
                dp.append(l)
            z[0] = f(a, 0, 0, n, m, dp)
        return z[0]
