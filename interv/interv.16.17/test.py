#17:04AC
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        d = [0] * n
        d[0] = a[0]
        r = a[0]
        for i in xrange(1, n):
            d[i] = a[i] if d[i-1] < 0 else d[i-1]+a[i]
            if d[i] > r:
                r = d[i]
        return r
