#15:05-15:07
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        m = len(s)
        buf = ''
        for i in xrange(m):
            if i >= n:
                buf += s[i]
        for i in xrange(m):
            if i < n:
                buf += s[i]
            else:
                break
        return buf
