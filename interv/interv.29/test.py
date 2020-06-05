#11:10AC
def f(x, y, n, m):
    return x>=0 and x<n and y>=0 and y<m
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        a = matrix
        n = len(a)
        if n == 0:
            return []
        m = len(a[0])
        x = 0
        y = 0
        cnt = 0
        up = n*m
        d = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        r = []
        visit = {}
        while cnt < up:
            r.append(a[x][y])
            visit[(x,y)] = 1
            cnt += 1
            t = x + dx[d]
            t2 = y + dy[d]
            if (t,t2) not in visit and f(t, t2, n, m):
                x = t
                y = t2
            else:
                d = d + 1
                if d == 4:
                    d = 0
                t = x + dx[d]
                t2 = y + dy[d]
                if (t,t2) not in visit and f(t, t2, n, m):
                    x = t
                    y = t2
        return r
