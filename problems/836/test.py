#11:12
def f(x, y, b):
    i1 = b[0]
    j1 = b[1]
    i2 = b[2]
    j2 = b[3]
	return x>i1 and x<i2 and y>j1 and y<j2
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        a = rec1
        x1 = a[0]
        y1 = a[1]
        x2 = a[2]
        y2 = a[3]
        return f(x1, y1, b) or f(x1,y2, b) or f(x2,y1,b) or f(x2,y2,b)
