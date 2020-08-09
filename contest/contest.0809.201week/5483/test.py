def f(s):
    n = len(s)
    buf = ''
    i = 0
    while i < n-1:
        x = ord(s[i])-ord('a')
        y = ord(s[i+1])-ord('A')
        if x == y:
            i += 2
        else:
            x = ord(s[i])-ord('A')
            y = ord(s[i+1])-ord('a')
            if x == y:
                i += 2
            else:
                buf += s[i]
                i += 1
    if i == n-1:
        buf += s[i]
    return buf
class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        while True:
            s2 = f(s)
            if s == s2:
                break
            s = s2
        return s
