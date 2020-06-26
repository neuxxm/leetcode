#23:49-23:51
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        a = 0
        b = 1
        c = 0
        for i in xrange(2, n+1):
            c = (a + b)%1000000007
            a = b
            b = c
        return c
