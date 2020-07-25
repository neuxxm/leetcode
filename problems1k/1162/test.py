#15:32-15:40
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a = grid
        n = len(a)
        q = []
        for i in xrange(n):
            for j in xrange(n):
                if a[i][j] == 1:
                    q.append((i,j))
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        visit = []
        for i in xrange(n):
            l = [0] * n
            visit.append(l)
        lvl = 0
        b = False
        while q:
            xs = []
            while q:
                xs.append(q.pop())
            lvl += 1
            for x in xs:
                for k in xrange(4):
                    x2 = x[0] + dx[k]
                    y2 = x[1] + dy[k]
                    if x2>=0 and x2<n and y2>=0 and y2<n:
                        if a[x2][y2] == 0 and visit[x2][y2] == 0:
                            visit[x2][y2] = 1
                            q.append((x2,y2))
                            b = True
        return lvl-1 if b else -1
