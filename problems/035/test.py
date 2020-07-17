#11:52-11:58
class Solution(object):
    def searchInsert(self, nums, target):
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
        ans = -1
        while l <= r:
            m = (l+r)>>1
            if a[m] == y:
                return m
            if y < a[m]:
                ans = m
                r = m-1
            else:
                ans = m+1
                l = m+1
        return ans
