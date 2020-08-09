#19:03-19:03
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for t in nums:
            if t in map:
                return True
            map[t] = 1
        return False
