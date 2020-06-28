#23:12-23:13
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = [0] * len(nums)
        for t in nums:
            cnt[t] += 1
            if cnt[t] > 1:
                return t
