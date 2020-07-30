#15:27-15:30
def f(s):
    r = 0
    for c in s:
        if c == '0':
            r += 1
    return r
def g(s):
    r = 0
    for c in s:
        if c == '1':
            r += 1
    return r
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        z = 0
        for i in xrange(1, n):
            t = f(s[:i]) + g(s[i:])
            if t > z:
                z = t
        return z
