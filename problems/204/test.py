#21:15-21:20
import math
def f(x):
    t = int(math.sqrt(x))
    for i in xrange(3, t+1, 2):
        if x%i == 0:
            return False
    return True
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        r = 1
        for i in xrange(3, n, 2):
            if f(i):
                r += 1
        return r
