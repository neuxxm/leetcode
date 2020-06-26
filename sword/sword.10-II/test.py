#23:57-23:59
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n < 3:
            return n
        a = 1
        b = 2
        for i in xrange(3, n+1):
            c = (a+b)%1000000007
            a = b
            b = c
        return c
