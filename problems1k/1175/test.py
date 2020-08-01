#23:08-23:15
def prime(x):
    t = int(sqrt(x))
    for i in xrange(2, t+1):
        if x%i == 0:
            return False
    return True
def f(n):
    z = 0
    for i in xrange(2, n+1):
        if prime(i):
            z += 1
    return z
def a(n):
    if n == 0:
        return 1
    return (n*a(n-1))%1000000007
class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        pcnt = f(n)
        left = n - pcnt
        return (a(left) * a(pcnt))%1000000007
