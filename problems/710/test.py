#19:20fail
import random
def bisearch(a, x):
    l = 0
    r = len(a) - 1
    ans = -1
    while l <= r:
        m = (l+r) >> 1
        t = a[m] - m
        if x < t:
            ans = m - 1
            r = m - 1
        else:
            ans = m
            l = m + 1
    return ans
class Solution(object):
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.m = N - len(blacklist)
        self.a = sorted(blacklist)
    def pick(self):
        """
        :rtype: int
        """
        x = random.randint(0, self.m-1)
        loc = bisearch(self.a, x)
        if loc == -1:
            r = x
        else:
            r = x+loc+1
        return r
