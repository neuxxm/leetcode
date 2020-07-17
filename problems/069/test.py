#12:27AC
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x
        y = x
        ans = 0
        while l <= r:
            m = (l+r) >> 1
            t = m*m
            if y == t:
                return m
            if y < t:
                ans = m-1
                r = m-1
            else:
                ans = m
                l = m+1
        return ans
