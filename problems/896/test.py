#19:39-19:40
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        a = A
        n = len(a)
        b = True
        for i in xrange(1, n):
            if a[i] < a[i-1]:
                b = False
                break
        b2 = True
        for i in xrange(1, n):
            if a[i] > a[i-1]:
                b2 = False
                break
        return b or b2
