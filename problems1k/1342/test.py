#12:15-12:16
class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        x = num
        r = 0
        while x != 0:
            if x&1:
                x -= 1
            else:
                x >>= 1
            r += 1
        return r
