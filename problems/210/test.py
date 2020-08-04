#11:23-11:26
from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        ps = prerequisites
        rs = []
        ind = [0] * n
        for y,x in ps:
            ind[y] += 1
        q = deque()
        for i in xrange(n):
            if ind[i] == 0:
                q.append(i)
        while q:
            t = q.popleft()
            rs.append(t)
            for y,x in ps:
                if t == x:
                    ind[y] -= 1
                    if ind[y] == 0:
                        q.append(y)
        return rs if len(rs) == n else []
