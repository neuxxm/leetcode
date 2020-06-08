#00:34-00:37
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0] * max(3, n+1)
        a[1] = 1
        a[2] = 2
        for i in xrange(3, n+1):
            a[i] = a[i-2] + a[i-1]
        return a[n]
