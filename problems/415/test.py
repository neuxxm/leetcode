#11:26-11:36
def f(a, b, tag):
    t = int(a) + int(b) + tag
    if t >= 10:
        t -= 10
        tag = 1
    else:
        tag = 0
    return t, tag
def f2(a, tag):
    t = int(a) + tag
    if t >= 10:
        t -= 10
        tag = 1
    else:
        tag = 0
    return t, tag
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
        tag = 0
        z = []
        while i>=0 and j>=0:
            t, tag = f(a[i], b[j], tag)
            z.append(t)
            i -= 1
            j -= 1
        while i>=0:
            t, tag = f2(a[i], tag)
            z.append(t)
            i -= 1
        while j>=0:
            t, tag = f2(b[j], tag)
            z.append(t)
            j -= 1
        if tag:
            z.append(tag)
        s = ''
        for t in z[::-1]:
            s += '%d'%t
        return s
