#23:25-23:31
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        x = N
        if x == 0:
            return 1
        r = []
        while x:
            r.append(x&1)
            x >>= 1
        n = len(r)
        l = 1
        z = 0
        for i in xrange(n):
            if r[i] == 0:
                z += l
            l <<= 1
        return z
