#12:36-12:37
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        a = coordinates
        n = len(a)
        if n == 2:
            return True
        for i in xrange(2, n):
            x1 = a[i-2][0]
            y1 = a[i-2][1]
            x2 = a[i-1][0]
            y2 = a[i-1][1]
            x3 = a[i][0]
            y3 = a[i][1]
            if (y1-y2)*(x2-x3) == (y2-y3)*(x1-x2):
                pass
            else:
                return False
        return True
