#11:51
import math
from collections import defaultdict
def g(x):
    return x*x
def f(p, p2):
    return g(p[0]-p2[0]) + g(p[1]-p2[1])
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        a = points
        n = len(a)
        map = {}
        r = 0
        for i in xrange(n):
            for j in xrange(i+1, n):
                t = f(a[i], a[j])
                if t in map:
                    r += map[t]
                    map[t] += 1
                else:
                    map[t] = 1
        return r*2
