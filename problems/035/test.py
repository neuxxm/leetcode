#14:58-15:02
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return 0
        y = target
        l = 0
        r = n - 1
        ans = 0
        # 5
        # 4, 0
        # 6, 1
        while l <= r:
            m = (l+r) >> 1
            if y == a[m]:
                return m
            if y < a[m]:
                ans = m
                r = m - 1
            else:
                ans = m + 1
                l = m + 1
        return ans
