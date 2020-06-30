#14:32fail
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        t = num
        return (t&(t-1))==0 and (t&0x55555555)
