#17:11-17:15
def proc(buf, list, bi, rs):
    list.append(buf)
    l = len(list)
    if l >= 3:
        k = list[l-3] + '\t' + list[l-2]
        if k == bi:
            rs.append(buf)
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        s = text
        n = len(s)
        buf = ''
        list = []
        bi = first + '\t' + second
        rs = []
        for i in xrange(n):
            c = s[i]
            if c == ' ':
                if len(buf) > 0:
                    proc(buf, list, bi, rs)
                buf = ''
            else:
                buf += c
        if len(buf) > 0:
            proc(buf, list, bi, rs)
        return rs
