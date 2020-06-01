#20:55-21:05
def g(x):
    if x == 1:
        return False
    t = int(sqrt(x))
    for i in xrange(2, t+1):
        if x%i == 0:
            return False
    return True
def f(x):
    z = 0
    while x > 0:
        if x&1:
            z += 1
        x >>= 1
    return g(z)
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        z = 0
        for x in xrange(L, R+1):
            if f(x):
                z += 1
        return z
