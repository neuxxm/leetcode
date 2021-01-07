#16:24-16:34
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        a = isConnected
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        visit = {}
        cnt = 0
        for i in xrange(n):
            if i in visit:
                continue
            q = []
            q.append(i)
            visit[i] = 1
            while q:
                x = q.pop(0)
                for j in xrange(m):
                    if x == j:
                        continue
                    if a[x][j] == 1 and j not in visit:
                        q.append(j)
                        visit[j] = 1
            cnt += 1
        return cnt
