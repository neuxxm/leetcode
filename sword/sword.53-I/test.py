#22:25-22:34
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
        r = n - 1
        ans = -1
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
            return 0
        l = ans-1
        r = ans+1
        z = 1
        while l >= 0:
            if a[l] == y:
                l -= 1
                z += 1
            else:
                break
        while r < n:
            if a[r] == y:
                r += 1
                z += 1
            else:
                break
        return z
