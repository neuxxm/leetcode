#11:54fail
import random
def bisearch(a, x):
    n = len(a)
    l = 0
    r = n - 1
    ans = -1
    while l < r:
        print x, l, r
        m = l + (r-l)/2
        #t = a[m] - m
        t = a[m]
        if x <= t:
            ans = m
            r = m-1
        else:
            l = m+1
    print 'final', x, ans
class Solution(object):
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.m = N - len(blacklist)
        self.bl = sorted(blacklist)
    def pick(self):
        """
        :rtype: int
        """
        x = random.randint(0, m-1)
        bisearch(self.bl, x)
a = [2,3,7,8]
bisearch(a, 1)
