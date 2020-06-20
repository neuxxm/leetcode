#23:24-23:26
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        m = numCourses
        ps = prerequisites
        c = [0] * m
        for b,a in ps:
            c[b] += 1
        q = []
        for i in xrange(m):
            if c[i] == 0:
                q.append(i)
        r = 0
        while len(q) > 0:
            t = q.pop(0)
            r += 1
            for b,a in ps:
                if a == t:
                    c[b] -= 1
                    if c[b] == 0:
                        q.append(b)
        return r == m
