#23:10-23:18
def dfs(a, x, y, z, visit, n, m):
    t = a[x][y]
    a[x][y] = z
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for k in xrange(4):
        x2 = x + dx[k]
        y2 = y + dy[k]
        if x2>=0 and x2<n and y2>=0 and y2<m and visit[x2][y2] == 0:
            if a[x2][y2] == t:
                visit[x2][y2] = 1
                dfs(a, x2, y2, z, visit, n, m)
                visit[x2][y2] = 0
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # 1 1 1
        # 1 1 0
        # 1 0 1
        a = image
        n = len(a)
        if n == 0:
            return []
        m = len(a[0])
        visit = []
        for i in xrange(n):
            l = [0] * m
            visit.append(l)
        visit[sr][sc] = 1
        dfs(a, sr, sc, newColor, visit, n, m)
        visit[sr][sc] = 0
        return a
