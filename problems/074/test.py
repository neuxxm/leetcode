#23:00-23:19
def f(a, l, r, y):
    while l <= r:
        m = (l+r) >> 1
        if y == a[m]:
            return True
        if y < a[m]:
            r = m-1
        else:
            l = m+1
    return False
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        a = matrix
        n = len(a)
        if n == 0:
            return False
        y = target
        m = len(a[0])
        if m == 0:
            return False
        for i in xrange(n):
            if y < a[i][0]:
                continue
            if y > a[i][m-1]:
                continue
            if f(a[i], 0, m-1, y):
                return True
        return False
