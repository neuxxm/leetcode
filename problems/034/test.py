#15:12-15:14
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = nums
        n = len(a)
        y = target
        ans = -1
        l = 0
        r = n - 1
        while l <= r:
            m = (l+r) >> 1
            if y == a[m]:
                ans = m
                break
            if y < a[m]:
                r = m - 1
            else:
                l = m + 1
        if ans == -1:
            return [-1, -1]
        i = ans
        while i >= 0:
            if a[i] == y:
                i -= 1
            else:
                break
        r = [i+1]
        j = ans
        while j < n:
            if a[j] == y:
                j += 1
            else:
                break
        r.append(j-1)
        return r
