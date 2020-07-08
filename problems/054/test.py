#20:24
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        a = matrix
        n = len(a)
        if n == 0:
            return
		m = len(a[0])
