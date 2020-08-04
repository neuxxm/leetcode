#11:05-11:12
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses
        ps = prerequisites
        ind = [0] * n
        for xs in ps:
            y = xs[0]
            x = xs[1]
            ind[y] += 1
        q = []
        for i in xrange(n):
            if ind[i] == 0:
                q.append(i)
        z = 0
        while q:
            t = q.pop(0)
            z += 1
            for xs in ps:
                y = xs[0]
                x = xs[1]
                if x == t:
                    ind[y] -= 1
                    if ind[y] == 0:
                        q.append(y)
        return z == n
