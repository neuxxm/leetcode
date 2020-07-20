#23:51-0:03
def f(a, i, j, n, m, b):
    dx = [0, 0, 1, 1, 1, 0, -1, -1, -1]
    dy = [0, 1, 1, 0, -1, -1, -1, 0, 1]
    cnt = 0
    su = 0
    for k in xrange(9):
        x = i+dx[k]
        y = j+dy[k]
        if x>=0 and x<n and y>=0 and y<m:
            cnt += 1
            su += a[x][y]
    b[i][j] = su / cnt
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        a = M
        n = len(a)
        if n == 0:
            return []
        m = len(a[0])
        b = []
        for i in xrange(n):
            l = [0] * m
            b.append(l)
        for i in xrange(n):
            for j in xrange(m):
                f(a, i, j, n, m, b)
        return b
