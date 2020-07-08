#16:56
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
		a = matrix
        n = len(a)
        if n == 0:
            return
        m = len(a[0])
        for i in xrange(n):
            for j in xrange(0, m/2):
                a[i][j], a[i][m-1-j] = a[i][m-1-j], a[i][j]
        for i in xrange(n):
            for j in xrange(n-1-i):
                a[i][j], a[m-1-j][n-1-i] = a[m-1-j][n-1-i], a[i][j]
