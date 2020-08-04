#11:55fail
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        a = A
        n = len(a)
        s = sum(a)
        if s%3 != 0:
            return False
        s /= 3
        t = 0
        z = 0
        for i in xrange(n):
            t += a[i]
            if t == s:
                z += 1
                t = 0
        return z >= 3
