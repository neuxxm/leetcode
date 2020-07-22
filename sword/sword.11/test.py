#10:49-11:06
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        a = numbers
        n = len(a)
        for i in xrange(1, n):
            if a[i] < a[i-1]:
                return a[i]
        return a[0]
