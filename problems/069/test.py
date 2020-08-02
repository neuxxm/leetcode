#22:45-22:50
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 1
        r = x
        ans = 0
        while l <= r:
            m = (l+r) >> 1
            t = m*m
            if t == x:
                return m
            if t < x:
                ans = m
                l = m+1
            else:
                ans = m-1
                r = m-1
        return ans
