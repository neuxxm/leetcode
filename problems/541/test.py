#22:46-22:57
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        k2 = k<<1
        i = 0
        buf = ''
        while i+k2 < n:
            for z in xrange(i+k-1, i-1, -1):
                buf += s[z]
            buf += s[i+k:i+k2]
            i += k2
        if i+k < n:
            for z in xrange(i+k-1, i-1, -1):
                buf += s[z]
            buf += s[i+k:]
        else:
            for z in xrange(n-1, i-1, -1):
                buf += s[z]
        return buf
