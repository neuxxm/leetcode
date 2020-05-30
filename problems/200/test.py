#17:54-18:12
def f(x, y, n, m, visit, a, r):
    q = []
    q.append((x, y))
    visit[x][y] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    r[0] += 1
    while len(q) > 0:
        x, y = q.pop(0)
        for i in xrange(4):
            x2 = x + dx[i]
            y2 = y + dy[i]
            if x2 < 0 or x2 >= n:
                continue
            if y2 < 0 or y2 >= m:
                continue
            if visit[x2][y2] == 0 and a[x2][y2] == '1':
                visit[x2][y2] = 1
                q.append((x2,y2))
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
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
        r = [0]
        for i in xrange(n):
            for j in xrange(m):
                if a[i][j] == '1' and visit[i][j] == 0:
                    f(i, j, n, m, visit, a, r)
        return r[0]
