#12:48AC
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = len(a)
        m = len(b)
        i = n-1
        j = m-1
        r = ''
        tag = 0
        while i>=0 and j>=0:
            t = int(a[i]) + int(b[j]) + tag
            if t >= 2:
                t -= 2
                tag = 1
            else:
                tag = 0
            r += '%d'%t
            i -= 1
            j -= 1
        while i>=0:
            t = int(a[i]) + tag
            if t >= 2:
                t -= 2
                tag = 1
            else:
                tag = 0
            r += '%d'%t
            i -= 1
        while j>=0:
            t = int(b[j]) + tag
            if t >= 2:
                t -= 2
                tag = 1
            else:
                tag = 0
            r += '%d'%t
            j -= 1
        if tag > 0:
            r += '%d'%tag
        return r[::-1]
