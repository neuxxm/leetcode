#19:28-19:30
class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        r = 1
        ma = 1
        for i in xrange(1, n):
            if s[i] == s[i-1]:
                r += 1
                if r > ma:
                    ma = r
            else:
                r = 1
                if r > ma:
                    ma = r
        return ma
