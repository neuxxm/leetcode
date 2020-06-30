#13:46-13:48
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = 0
        while x > 0 and y > 0:
            t = x&1
            t2 = y&1
            if t != t2:
                r += 1
            x >>= 1
            y >>= 1
        while x > 0:
            if x&1:
                r += 1
            x >>= 1
        while y > 0:
            if y&1:
                r += 1
            y >>= 1
        return r
