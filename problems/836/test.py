#12:29fail
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1 = rec1[0]
        y1 = rec1[1]
        x2 = rec1[2]
        y2 = rec1[3]
        x3 = rec2[0]
        y3 = rec2[1]
        x4 = rec2[2]
        y4 = rec2[3]
        if x3 >= x2:
            return False
        if x4 <= x1:
            return False
        if y3 >= y2:
            return False
        if y4 <= y1:
            return False
        return True
