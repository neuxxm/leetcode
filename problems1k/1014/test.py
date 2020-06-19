#20:23-21:31
class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = A
        n = len(a)
        a1 = [0] * n
        a2 = [0] * n
        a3 = [0] * n
        for i in xrange(n):
            a1[i] = a[i] + i
        for i in xrange(n):
            a2[i] = a[i] - i
        ma = float('-inf')
        for i in xrange(n-1, -1, -1):
            if a2[i] > ma:
                ma = a2[i]
            a3[i] = ma
        ma = float('-inf')
        for i in xrange(0, n-1):
            t = a1[i] + a3[i+1]
            if t > ma:
                ma = t
        return ma
