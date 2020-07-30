#13:00-13:01
class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n&1:
            r = ''
            for i in xrange(n):
                r += 'a'
            return r
        else:
            r = 'a'
            for i in xrange(1, n):
                r += 'b'
            return r
