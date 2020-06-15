#15:37AC
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        a = rooms
        n = len(a)
        r = 0
        q = []
        q.append(0)
        visit = {}
        visit[0] = 1
        while len(q) > 0:
            t = q.pop(0)
            r += 1
            for v in a[t]:
                if v not in visit:
                    q.append(v)
                    visit[v] = 1
        return r == n
