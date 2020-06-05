#23:54-23:57
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n > 0:
            if n&1:
                break
            n >>= 1
        return n == 1
