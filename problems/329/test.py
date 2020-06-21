#11:09-12:36
def f(a, x, y, n, m, dp, visit):
    if dp[x][y] != -1:
        return dp[x][y]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    r = 1
    for i in xrange(4):
        x2 = x + dx[i]
        y2 = y + dy[i]
        if x2>=0 and x2<n and y2>=0 and y2<m:
            if visit[x2][y2] == 0:
                if a[x2][y2] < a[x][y]:
                    visit[x2][y2] = 1
                    t = f(a, x2, y2, n, m, dp, visit)+1
                    if t > r:
                        r = t
                    visit[x2][y2] = 0
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
        visit = []
        for i in xrange(n):
            l = [-1] * m
            dp.append(l)
            l = [0] * m
            visit.append(l)
        r = 0
        for i in xrange(n):
            for j in xrange(m):
                visit[i][j] = 1
                dp[i][j] = f(a, i, j, n, m, dp, visit)
                visit[i][j] = 0
        for i in xrange(n):
            for j in xrange(m):
                if dp[i][j] > r:
                    r = dp[i][j]
        return r