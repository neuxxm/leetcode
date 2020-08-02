#17:37-18:08
def f(a, l, r, y):
    while l <= r:
        m = (l+r) >> 1
        if y == a[m]:
            return m
        if y < a[m]:
            r = m - 1
        else:
            l = m + 1
    return -1
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return -1
        y = target
        if n == 1:
            if a[0] == y:
                return 0
            return -1
        if n == 2:
            for i in xrange(2):
                if a[i] == y:
                    return i
            return -1
        l = 0
        r = n-1
        if a[0] < a[n-1]:
            return f(a, 0, n-1, y)
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
            if a[m]>a[0] and a[m]>a[m+1]:
                peak = m
                break
            if a[m] > a[0]:
                l = m + 1
            else:
                r = m - 1
        if peak == -1:
            return -1
        t = f(a, 0, peak, y)
        if t != -1:
            return t
        return f(a, peak+1, n-1, y)
