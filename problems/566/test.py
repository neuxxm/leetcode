#23:23-23:26
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        a = nums
        n = len(a)
        if n == 0:
            return a
        m = len(a[0])
        if n*m != r*c:
            return a
        rs = []
        for i in xrange(r):
            l = [0] * c
            rs.append(l)
        k = 0
        for i in xrange(n):
            for j in xrange(m):
                x = k/c
                y = k%c
                rs[x][y] = a[i][j]
                k += 1
        return rs
