#11:06AC
class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = sorted(nums, reverse=True)
        s = sum(a) / 2
        n = len(a)
        t = 0
        r = []
        for i in xrange(0, n):
            t += a[i]
            if t > s:
                r = a[:i+1]
                break
        return r
