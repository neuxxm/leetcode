#18:35-20:55
def add1(s):
    i = len(s) - 1
    tag = 1
    r = []
    while i >= 0:
        t = int(s[i]) + tag
        if t >= 2:
            t -= 2
            r.append('%d'%t)
            tag = 1
        else:
            r.append('%d'%t)
            tag = 0
        i -= 1
    if tag > 0:
        r.append('%d'%tag)
    return ''.join(r[::-1])
class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        while s != "1":
            n = len(s)
            if s[n-1] == '0':
                s = s[:n-1]
            else:
                s = add1(s)
            r += 1
        return r
