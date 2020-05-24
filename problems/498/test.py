#17:32-17:49
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        a = matrix
        n = len(a)
        if n == 0:
            return []
        m = len(a[0])
        i,j = 0,0
        d = 1
        cnt = 0
        up_size = n*m
        r = []
        while cnt < up_size:
            r.append(a[i][j])
            cnt += 1
            if d:
                i -= 1
                j += 1
                if i<0 or j>=m:
                    j += 1
                    while i<0 or j>=m:
                        i += 1
                        j -= 1
                    d = 0
            else:
                i += 1
                j -= 1
                if i>=n or j<0:
                    i += 1
                    while i>=n or j<0:
                        i -= 1
                        j += 1
                    d = 1
        return r
