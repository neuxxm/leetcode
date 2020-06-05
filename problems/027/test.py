#15:37-15:39
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return 0
        start = 0
        end = 0
        while end < n:
            if a[end] == val:
                end += 1
            else:
                a[start] = a[end]
                start += 1
                end += 1
        return start
