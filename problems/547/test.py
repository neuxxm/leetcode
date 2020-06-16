def find(x, u):
    while u[x] != x:
        x = u[x]
    return x
def merge(x, y, u):
    x = find(x, u)
    y = find(y, u)
    if x == y:
        return
    if x < y:
        u[y] = x
    else:
        u[x] = y
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        a = M
        n = len(a)
        if n == 0:
            return 0
        u = [0] * n
        for i in xrange(n):
            u[i] = i
        for i in xrange(0, n):
            for j in xrange(i+1, n):
                if a[i][j] > 0:
                    merge(i, j, u)
        print u
        map = {}
        for i in xrange(0, n):
            map[u[i]] = 1
        return len(map)
a = [[1,1,0],
 [1,1,0],
  [0,0,1]]
s = Solution()
print s.findCircleNum(a)
