#14:07-14:43
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    return gcd(b, a%b) if b != 0 else a
def is_sub(a, b):
    #print a, b
    i = 0
    n = len(a)
    j = 0
    m = len(b)
    if m%n != 0:
        return False
    while i < n and j < m:
        #print i, j
        if a[i] == b[j]:
            i += 1
            j += 1
            if i == n:
                i = 0
        else:
            return False
    return i==0 and j==m
def f(a, b):
    cnt = [0] * 26
    for c in a:
        tn = ord(c)-ord('A')
        cnt[tn] += 1
    #for i in xrange(26):
    #    if cnt[i]:
    #        print chr(i+ord('A')), cnt[i]
    last = None
    z = len(a)
    for i in xrange(26):
        if cnt[i] > 0:
            z = gcd(z, cnt[i])
    n = len(a)
    if z > 1:
        for i in xrange(1, n+1):
            #print n, i
            if n%i == 0:
                k = n/i
                t = a[:k]
                #print t
                if is_sub(t, a) and is_sub(t, b):
                    return t
        return ''
    else:
        if is_sub(a, b):
            return a
        else:
            return ''
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        a = str1
        b = str2
        n = len(a)
        m = len(b)
        if n < m:
            return f(a, b)
        else:
            return f(b, a)
