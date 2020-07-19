#1:03-1:06
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        y = num
        l = 1
        r = y
        while l <= r:
            m = (l+r) >> 1
            t = m*m
            if t == y:
                return True
            if y < t:
                r = m-1
            else:
                l = m+1
        return False
