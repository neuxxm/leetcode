#13:20fail
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        ps = prerequisites
        ind = {}
        for i in xrange(0, n):
            ind[i] = 0
        for b,a in ps:
            ind[b] += 1
        q = []
        for k,v in ind.items():
            if v == 0:
                q.append(k)
        r = []
        while len(q) > 0:
            t = q.pop(0)
            r.append(t)
            for b,a in ps:
                if a == t:
                    ind[b] -= 1
                    if ind[b] == 0:
                        q.append(b)
        return r if len(r) == n else []
