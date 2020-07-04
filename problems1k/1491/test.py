#21:24-21:26
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        a = salary
        n = len(a)
        if n == 0:
            return 0
        mi = a[0]
        ma = a[0]
        r = a[0]
        for i in xrange(1, n):
            if a[i] < mi:
                mi = a[i]
            if a[i] > ma:
                ma = a[i]
            r += a[i]
        return float(r-mi-ma)/(n-2)
