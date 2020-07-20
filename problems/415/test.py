#20:23-20:27
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = num1
        b = num2
        n = len(a)
        m = len(b)
        i = n-1
        j = m-1
        r = []
        tag = 0
        while i>=0 and j>=0:
            t = int(a[i]) + int(b[j]) + tag
            if t >= 10:
                t -= 10
                tag = 1
            else:
                tag = 0
            r.append(t)
            i -= 1
            j -= 1
        while i>=0:
            t = int(a[i]) + tag
            if t >= 10:
                t -= 10
                tag = 1
            else:
                tag = 0
            r.append(t)
            i -= 1
        while j>=0:
            t = int(b[j]) + tag
            if t >= 10:
                t -= 10
                tag = 1
            else:
                tag = 0
            r.append(t)
            j -= 1
        if tag > 0:
            r.append(tag)
        buf = ''
        for i in xrange(len(r)-1, -1, -1):
            buf += '%d'%(r[i])
        return buf
