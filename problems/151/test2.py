#12:10-12:12
def f(q, buf):
    if buf == '':
        return
    q.append(buf)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        q = []
        buf = ''
        for c in s:
            if c == ' ':
                f(q, buf)
                buf = ''
            else:
                buf += c
        f(q, buf)
        return ' '.join(q[::-1])
