#13:22-13:59
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = nums
        y = target
        l = 0
        r = len(a) - 1
        ans = 0
        while l <= r:
            m = (l+r) >> 1
            if y == a[m]:
                ans = m
                break
            if y < a[m]:
                ans = m
                r = m - 1
            else:
                ans = m + 1
                l = m + 1
        return ans
