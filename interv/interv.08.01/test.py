#18:00AC
class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0] * max(4, n+1)
        a[1] = 1
        a[2] = 2
        a[3] = 4
        # 1,1,1
        # 1, 2
        # 2, 1
        # 3
        for i in xrange(4, n+1):
            a[i] = a[i-3] + a[i-2] + a[i-1]
            a[i] %= 1000000007
        return a[n]
