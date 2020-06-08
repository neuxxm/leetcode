#11:32-11:43
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        # (a + a+n-1) * n / 2 = t
        # (2a + n-1) * n  = 2t
        # n*n < 2t
        # n < sqrt(2t)
        t2 = target * 2
        n2 = int(math.sqrt(t2))
        r = []
        for n in xrange(n2, 1, -1):
            z = (t2 / n - n + 1) / 2
            if (2*z + n-1)*n == t2:
                l = []
                for i in xrange(z, z+n):
                    l.append(i)
                r.append(l)
        return r
