#21:28
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = nums
        map = {}
        for c in a:
            if c in map:
                return True
            else:
                map[c] = 1
        return False
