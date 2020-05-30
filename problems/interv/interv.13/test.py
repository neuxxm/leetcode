#17:28-17:45
def f(x, y, k):
    xt = x
    yt = y
    r = 0
    while x > 0:
        r += x%10
        x /= 10
    while y > 0:
        r += y%10
        y /= 10
    return r <= k
def move(x, y, n, m, q, visit, k):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    for i in xrange(4):
        x2 = x + dx[i]
        y2 = y + dy[i]
        if x2 < 0 or x2 >= n:
            continue
        if y2 < 0 or y2 >= m:
            continue
        if (x2,y2) not in visit and f(x2, y2, k):
            q.append((x2, y2))
            visit[(x2,y2)] = 1
class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        q = []
        r = 0
        visit = {}
        q.append((0, 0))
        visit[(0,0)] = 1
        while len(q) > 0:
            x, y = q.pop()
            r += 1
            move(x, y, m, n, q, visit, k)
        return r
