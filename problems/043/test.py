#20:45-21:18
def f(a, b, tag):
    t = a*b+tag
    if t >= 10:
        tag = int(t)/10
        t %= 10
    else:
        tag = 0
    return t, tag
def multi(a, n, c, r, k):
    tag = 0
    i = n-1
    while i >= 0:
        r[k], tag = f(int(a[i]), int(c), tag)
        k += 1
        i -= 1
    if tag > 0:
        r[k] = tag
def add(a, b, n):
    tag = 0
    for i in xrange(n):
        t = a[i]+b[i]+tag
        if t >= 10:
            a[i] = t-10
            tag = 1
        else:
            a[i] = t
            tag = 0
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = num1
        b = num2
        n = len(a)
        m = len(b)
        if a == '0' or b == '0':
            return '0'
        z = [0] * (n+m+1)
        k = 0
        for j in xrange(m-1, -1, -1):
            r = [0] * (n+m+1)
            multi(a, n, b[j], r, k)
            k += 1
            add(z, r, n+m+1)
        j = n+m
        while j >= 0:
            if z[j] == 0:
                j -= 1
            else:
                break
        zz = []
        for i in xrange(j, -1, -1):
            zz.append(z[i])
        return ''.join(str(t) for t in zz)
