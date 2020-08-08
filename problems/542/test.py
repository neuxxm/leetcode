#19:56-20:04
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        a = matrix
        n = len(a)
        if n == 0:
            return []
        m = len(a[0])
        r = []
        for i in xrange(n):
            l = [0] * m
            r.append(l)
        visit = []
        for i in xrange(n):
            l = [0] * m
            visit.append(l)
        q = []
        for i in xrange(n):
            for j in xrange(m):
                if a[i][j] == 0:
                    visit[i][j] = 1
                    q.append((i,j))
        z = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        while q:
            xs = []
            while q:
                x,y = q.pop(0)
                r[x][y] = z
                xs.append((x,y))
            for x,y in xs:
                for k in xrange(4):
                    x2 = x+dx[k]
                    y2 = y+dy[k]
                    if x2>=0 and x2<n and y2>=0 and y2<m:
                        if visit[x2][y2] == 0:
                            visit[x2][y2] = 1
                            q.append((x2,y2))
            z += 1
        return r
