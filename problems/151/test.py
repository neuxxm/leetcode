#14:31-14:35
def f(buf, q):
    if len(buf) > 0:
        q.append(buf)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        buf = ''
        q = []
        for i in xrange(n):
            c = s[i]
            if c == ' ':
                f(buf, q)
                buf = ''
            else:
                buf += c
        f(buf, q)
        return ' '.join(q[::-1])
