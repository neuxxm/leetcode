#22:42-22:44
def f(buf, rs):
    if len(buf) > 0:
        rs.append(buf)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        buf = ''
        rs = []
        for c in s:
            if c == ' ':
                f(buf, rs)
                buf = ''
            else:
                buf += c
        f(buf, rs)
        return ' '.join(rs[::-1])
