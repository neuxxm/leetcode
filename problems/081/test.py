#19:41-21:17
def f(a, l, r, y):
    while l <= r:
        m = (l+r) >> 1
        if y == a[m]:
            return True
        if y < a[m]:
            r = m - 1
        else:
            l = m + 1
    return False
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        a = nums
        n = len(a)
        if n == 0:
            return False
        y = target
        l = 0
        r = n-1
        if a[l] < a[r]:
            return f(a, l, r, y)
        if a[l] == a[r]:
            if y == a[l]:
                return True
            t = a[l]
            while l<r and a[l] == t:
                l += 1
            while l<r and a[r] == t:
                r -= 1
            if l == r:
                return y == a[l]
        peak = -1
        while l <= r:
            m = (l+r) >> 1
            if m == 0:
                if a[m] > a[m+1]:
                    peak = m
                    break
                l += 1
                continue
            if m == n-1:
                r -= 1
                continue
            if a[m]>=a[0] and a[m]>a[m+1]:
                peak = m
                break
            if a[m]>=a[0]:
                l = m + 1
            else:
                r = m - 1
        if f(a, 0, peak, y):
            return True
        return f(a, peak+1, n-1, y)
