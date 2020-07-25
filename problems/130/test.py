#0:03-0:19
def bfs(a, x, y, n, m, visit):
    q = []
    q.append((x,y))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    b = True
    map = {}
    map[(x,y)] = 1
    while q:
        xs = []
        while q:
            xs.append(q.pop())
        for x in xs:
            for k in xrange(4):
                x2 = x[0] + dx[k]
                y2 = x[1] + dy[k]
                if x2>=0 and x2<n and y2>=0 and y2<m:
                    if a[x2][y2] == 'O' and visit[x2][y2] == 0:
                        visit[x2][y2] = 1
                        q.append((x2,y2))
                        map[(x2,y2)] = 1
                else:
                    b = False
    if b:
        for k in map.keys():
            a[k[0]][k[1]] = 'X'
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        a = board
        n = len(a)
        if n == 0:
            return
        m = len(a[0])
        visit = []
        for i in xrange(n):
            l = [0] * m
            visit.append(l)
        for i in xrange(n):
            for j in xrange(m):
                if a[i][j] == 'O' and visit[i][j] == 0:
                    visit[i][j] = 1
                    bfs(a, i, j, n, m, visit)
