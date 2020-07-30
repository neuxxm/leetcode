#17:45-17:58
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        n = area
        t = int(sqrt(n))
        for i in xrange(t, 0, -1):
            if n%i == 0:
                return sorted([n/i, i], reverse=True)
