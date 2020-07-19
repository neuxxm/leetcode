# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
#1:11-1:13
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:
            m = (l+r) >> 1
            t = guess(m)
            if t == 0:
                return m
            if t < 0:
                r = m-1
            else:
                l = m+1
