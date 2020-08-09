#2:54-3:01
class Solution(object):
    def exchangeBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = num
        if n == 0:
            return 0
        rs = []
        while n:
            rs.append(n&1)
            n >>= 1
        while len(rs) < 32:
            rs.append(0)
        n = len(rs)
        z = 0
        l = 2
        for i in xrange(0, n, 2):
            z += rs[i] * l
            l <<= 2
        l = 1
        for i in xrange(1, n, 2):
            z += rs[i] * l
            l <<= 2
        return z
