#19:19-19:22
class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l = 1
        while n > 0:
            l *= 10
            n -= 1
        rs = []
        for i in xrange(1, l):
            rs.append(i)
        return rs
