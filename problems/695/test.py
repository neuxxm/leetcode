#19:30-19:49
def f(a, x, y, n, m, visit, z):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []
    q.append((x,y))
    t = 0
    while q:
        x,y = q.pop(0)
        t += 1
        for k in xrange(4):
            x2 = x+dx[k]
            y2 = y+dy[k]
            if x2>=0 and x2<n and y2>=0 and y2<m:
                if a[x2][y2] == 1 and visit[x2][y2] == 0:
                    visit[x2][y2] = 1
                    q.append((x2,y2))
    if t > z[0]:
        z[0] = t
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
        z = [0]
        for i in xrange(n):
            for j in xrange(m):
                if a[i][j] == 1 and visit[i][j] == 0:
                    visit[i][j] = 1
                    f(a, i, j, n, m, visit, z)
        return z[0]
