#15:20-15:21
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = nums
        n = len(a)
        y = target
        l = 0
        r = n-1
        while l <= r:
            m = (l+r) >> 1
            if y == a[m]:
                return m
            if y < a[m]:
                r = m-1
            else:
                l = m+1
        return -1
