#20:53-21:02
def f(a, n, d):
    if d[n] != None:
        return d[n]
    if n == 0:
        return a[0]
    d[n] = a[n] * f(a, n-1, d)
    return d[n]
def g(a, i, n, d):
    if d[i] != None:
        return d[i]
    if i == n-1:
        return a[i]
    d[i] = a[i] * g(a, i+1, n, d)
    return d[i]
class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        n = len(a)
        b = []
        d = [None] * n
        d2 = [None] * n
        for i in xrange(n):
            t = 1
            if i-1 >= 0:
                t *= f(a, i-1, d)
            if i+1 < n:
                t *= g(a, i+1, n, d2)
            b.append(t)
        return b
