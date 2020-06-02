#18:14-18:30
def f(x, y, n, m):
    return x>=0 and x<n and y>=0 and y<m
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a = grid
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        q = []
        visit = []
        for i in xrange(n):
            l = [0] * m
            visit.append(l)
        for i in xrange(n):
            for j in xrange(m):
                if a[i][j] == 2:
                    q.append((i, j, 0))
                    visit[i][j] = 1
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        last_l = 0
        while len(q) > 0:
            x,y,lvl = q.pop(0)
            #print x, y, lvl
            a[x][y] = 2
            last_l = lvl
            for k in xrange(4):
                x2 = x + dx[k]
                y2 = y + dy[k]
                if f(x2, y2, n, m) and visit[x2][y2] == 0:
                    if a[x2][y2] == 1:
                        q.append((x2, y2, lvl+1))
                        visit[x2][y2] = 1
        for i in xrange(n):
            for j in xrange(m):
                if a[i][j] == 1:
                    return -1
        return last_l
