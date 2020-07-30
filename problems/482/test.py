#17:37-17:41
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S
        k = K
        buf = ''
        map = {}
        for i in xrange(26):
            map[chr(ord('a')+i)] = chr(ord('A')+i)
        for c in s:
            if c != '-':
                if c in map:
                    buf += map[c]
                else:
                    buf += c
        n = len(buf)
        t = n%k
        out = ''
        for i in xrange(t):
            out += buf[i]
        if len(out) > 0:
            out += '-'
        for i in xrange(t, n, k):
            for j in xrange(i, i+k):
                out += buf[j]
            out += '-'
        if out.endswith('-'):
            out = out[:-1]
        return out
