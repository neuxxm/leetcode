#0:02AC
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a = A
        b = [0] * 1001
        for t in a:
            b[t] += 1
        i = 0
        j = 1
        for k in xrange(0, 1001, 2):
            while b[k] > 0:
                b[k] -= 1
                a[i] = k
                i += 2
        for k in xrange(1, 1001, 2):
            while b[k] > 0:
                b[k] -= 1
                a[j] = k
                j += 2
        return a
