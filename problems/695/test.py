#15:59
def dfs(a, x, y, visit, n, m, lvl):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    b = False
    for k in xrange(4):
        x2 = x + dx[k]
        y2 = y + dy[k]
        if x2>=0 and x2<n and y2>=0 and y2<m:
            b = True
            visit[x2][y2] = 1
            dfs(a, x2, y2, visit, n, m, lvl+1)
            visit[x2][y2] = 0
    if b == False:
        print lvl
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
		a = grid
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        visit = []
        for i in xrange(n):
            l = [0] * m
            visit.append(l)
        for i in xrange(n):
            for j in xrange(m):
                visit[i][j] = 1
                dfs(a, i, j, visit, n, m, 0)
                visit[i][j] = 0
