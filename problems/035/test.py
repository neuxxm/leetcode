#00:03-00:26
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = nums
        z = target
        n = len(a)
        l = 0
        r = n-1
        ans = -1
        while l <= r:
            print l, r
            m = (l+r) / 2
            if z == a[m]:
                return m
            elif z < a[m]:
                ans = m
                r = m-1
            else:
                ans = m+1
                l = m+1
        return ans
