#23:22-23:23
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(nums)
        n = len(a)
        r = 0
        for i in xrange(0, n, 2):
            r += a[i]
        return r
