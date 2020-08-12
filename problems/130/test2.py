#11:24
def f(a, i, j, n, m, visit):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []
    q.append((i,j))
    while q:
        x,y = q.pop(0)
        for k in xrange(4):
            x2 = x+dx[k]
            y2 = y+dy[k]
            if x2<0 or x2>=n or y2<0 or y2>=m:
                return
            if a[x2][y2] == 'O' and visit[x2][y2] == 0:
                visit[x2][y2] = 1
                q.append((x2,y2))
    q = []
    q.append((i,j))
    while q:
        x,y = q.pop(0)
        for k in xrange(4):
            x2 = x+dx[k]
            y2 = y+dy[k]
            if a[x2][y2] == 'O':
                a[x2][y2] = 'X'
                q.append((x2,y2))
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
                    f(a, i, j, n, m, visit)
a = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s = Solution()
s.solve(a)
for l in a:
    print l
