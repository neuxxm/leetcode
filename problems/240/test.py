#20:45fail
def bisearch(a, l, r, y):
    while l <= r:
        m = (l+r) >> 1
        if y == a[m]:
            return True
        if y < a[m]:
            r = m-1
        else:
            l = m+1
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        a = matrix
        y = target
        n = len(a)
        if n == 0:
            return False
        m = len(a[0])
        if m == 0:
            return False
        for i in xrange(n):
            if y < a[i][0]:
                continue
            if y > a[i][m-1]:
                continue
            if bisearch(a[i], 0, m-1, y):
                return True
        return False
