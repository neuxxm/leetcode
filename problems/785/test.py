#11:02fail
def bfs(a, n, i, color):
    if color[i] != -1:
        return
    q = []
    q.append(i)
    c = 0
    while len(q) > 0:
        list = []
        while len(q) > 0:
            x = q.pop(0)
            list.append(x)
        for x in list:
            color[x] = c
            for y in a[x]:
                if color[y] == -1:
                    q.append(y)
        c = 1-c
def bfs_judge(a, n, i, color):
    visit = [0] * n
    q = []
    q.append(i)
    visit[i] = 1
    c = 0
    while len(q) > 0:
        list = []
        while len(q) > 0:
            x = q.pop(0)
            list.append(x)
        for x in list:
            visit[x] = 1
            for y in a[x]:
                if color[x] + color[y] != 1:
                    return False
                if visit[i] == 0:
                    q.append(y)
    return True
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        a = graph
        n = len(a)
        color = [-1] * n
        for i in xrange(n):
            bfs(a, n, i, color)
        for i in xrange(n):
            if not bfs_judge(a, n, i, color):
                return False
        return True
