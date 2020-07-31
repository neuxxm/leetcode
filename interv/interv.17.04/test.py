#23:59-0:21
def f(a, ix, z):
    while True:
        if a[ix-1] == ix:
            return
        t = a[ix-1]
        if t == 0:
            return
        a[ix-1], a[t-1] = a[t-1], a[ix-1]
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        z = [-1]
        for i in xrange(1, n+1):
            f(a, i, z)
        for i in xrange(0, n):
            if a[i] == 0:
                return i+1
        return 0
