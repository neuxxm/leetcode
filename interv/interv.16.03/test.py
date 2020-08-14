#16:23fail
import math
def get_abc(x1, y1, x2, y2):
    a = y2 - y1
    b = x1 - x2
    c = x2*y1 - x1*y2
    return a, b, c
def dis(x1, y1, x2, y2):
    t = x1-x2
    t2 = y1-y2
    r = math.sqrt(t*t + t2*t2)
    return r
def f(x, y, x1, y1, x2, y2):
    return abs(dis(x,y,x1,y1) + dis(x,y,x2,y2) - dis(x1,y1,x2,y2)) < 1e-7
class Solution(object):
    def intersection(self, start1, end1, start2, end2):
        """
        :type start1: List[int]
        :type end1: List[int]
        :type start2: List[int]
        :type end2: List[int]
        :rtype: List[float]
        """
        x1 = start1[0]
        y1 = start1[1]
        x2 = end1[0]
        y2 = end1[1]
        x3 = start2[0]
        y3 = start2[1]
        x4 = end2[0]
        y4 = end2[1]
        a1, b1, c1 = get_abc(x1, y1, x2, y2)
        a2, b2, c2 = get_abc(x3, y3, x4, y4)
        if a1*b2 == a2*b1:
            if f(x1, y1, x3, y3, x4, y4):
                return [x1, y1]
            if f(x2, y2, x3, y3, x4, y4):
                return [x2, y2]
            if f(x3, y3, x1, y1, x2, y2):
                return [x3, y3]
            if f(x4, y4, x1, y1, x2, y2):
                return [x4, y4]
            return []
        x = float(c2*b1-c1*b2) / float(a1*b2 - a2*b1)
        y = float(c1*a2-c2*a1) / float(a1*b2 - a2*b1)
        if f(x, y, x1, y1, x2, y2) and f(x, y, x3, y3, x4, y4):
            return [x, y]
        return []
