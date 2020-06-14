#23:01AC
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 1:
            if a[0] == 0:
                return 1
            else:
                return 0
        l = 0
        r = n-1
        ans = -1
        while l <= r:
            m = (l+r)/2
            if a[m] == m:
                ans = m+1
                l = m+1
            else:
                ans = m
                r = m-1
        return ans
