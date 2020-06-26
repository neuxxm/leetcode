# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
#6.26 20:12-20:18
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        ans = 1
        while l <= r:
            m = l + ((r-l)>>1)
            b = isBadVersion(m)
            if b:
                ans = m
                r = m - 1
            else:
                ans = m + 1
                l = m + 1
        return ans
