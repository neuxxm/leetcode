def f(n, m):
    x = ord(n)-ord('a')+1
    y = ord(m)-ord('a')+1
    if x < y:
        return y - x
    return 26-x+y
class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        if n != m:
            return False
        c = [0] * 26
        map = {}
        z = 0
        for i in xrange(n):
            if s[i] != t[i]:
                x = f(s[i], t[i])
                c[x] += 1
        cnt = k / 26
        left = k%26
        c2 = [cnt] * 26
        for i in xrange(1, left+1):
            c2[i] += 1
        for i in xrange(1, 26):
            if c[i] > c2[i]:
                return False
        return True
