#10:52-10:53
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        r = 0
        while n != 0:
            if n&1:
                r += 1
            n >>= 1
        return r
