#22:32fail
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        a = nums
        l = n
        for i in xrange(0, n):
            l ^= i^a[i]
        return l
