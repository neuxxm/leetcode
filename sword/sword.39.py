#16:53AC
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(nums)
        return a[len(a)/2]
