#11:26-13:44
def clear(a, n, m):
    for i in xrange(n):
        for j in xrange(m):
            a[i][j] = -1
def f(a, x, y, n, m, visit, dp):
    if dp[x][y] != -1:
        return dp[x][y]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    r = 1
    for k in xrange(4):
        x2 = x + dx[k]
        y2 = y + dy[k]
        if x2>=0 and x2<n and y2>=0 and y2<m and a[x2][y2]>a[x][y]:
            if visit[x2][y2] == 0:
                visit[x2][y2] = 1
                t = f(a, x2, y2, n, m, visit, dp) + 1
                if t > r:
                    r = t
                visit[x2][y2] = 0
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
        visit = []
        dp = []
        for i in xrange(n):
            l2 = [0] * m
            visit.append(l2)
            l = [-1] * m
            dp.append(l)
        r = 0
        for i in xrange(n):
            for j in xrange(m):
                visit[i][j] = 1
                #clear(dp, n, m)
                z = f(a, i, j, n, m, visit, dp)
                visit[i][j] = 0
                if z > r:
                    r = z
        return r
