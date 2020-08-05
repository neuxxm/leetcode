class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        buf = ''
        l = len(s)
        for i in xrange(n, l):
            buf += s[i]
        for i in xrange(0, n):
            buf += s[i]
        return buf
