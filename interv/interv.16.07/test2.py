#15:30
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
        if (y2-y1)*(x4-x3) == (y4-y3)*(x2-x1):
            return []
