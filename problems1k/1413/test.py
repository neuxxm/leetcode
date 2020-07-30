#15:17-15:19
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        mi = a[0]
        t = a[0]
        for i in xrange(1, n):
            t += a[i]
            if t < mi:
                mi = t
        return (-mi+1) if mi < 0 else 1
