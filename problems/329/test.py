#14:03-14:25
def dfs(a, x, y, n, m, dp):
    if dp[x][y] != 0:
        return dp[x][y]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    r = 1
    for k in xrange(4):
        x2 = x + dx[k]
        y2 = y + dy[k]
        if x2>=0 and x2<n and y2>=0 and y2<m:
            if a[x2][y2] < a[x][y]:
                t = dfs(a, x2, y2, n, m, dp) + 1
                if t > r:
                    r = t
    dp[x][y] = r
    return r
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        a = matrix
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        dp = []
        for i in xrange(n):
            l2 = [0] * m
            dp.append(l2)
        for i in xrange(n):
            for j in xrange(m):
                dfs(a, i, j, n, m, dp)
        r = 0
        for i in xrange(n):
            for j in xrange(m):
                if dp[i][j] > r:
                    r = dp[i][j]
        return r
