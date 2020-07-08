#22:28fail
def f(a, x, y, n, m):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    i = 0
    for k in xrange(8):
        x2 = x + dx[k]
        y2 = y + dy[k]
        if x2>=0 and x2<n and y2>=0 and y2<m:
            if a[x2][y2]&1:
                i += 1
    if a[x][y]&1:
        if i < 2:
            a[x][y] |= 2
            a[x][y] &= 0xd
        elif i < 4:
            a[x][y] |= 2
        else:
            a[x][y] |= 2
            a[x][y] &= 0xd
    else:
        if i == 3:
            a[x][y] |= 2
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        a = board
        n = len(a)
        if n == 0:
            return
        m = len(a[0])
        for i in xrange(n):
            for j in xrange(m):
                f(a, i, j, n, m)
        for i in xrange(n):
            for j in xrange(m):
                a[i][j] = 1 if a[i][j]&2 else 0
