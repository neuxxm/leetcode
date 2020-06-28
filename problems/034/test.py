#22:57-23:00
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
        l = 0
        r = n - 1
        z = -1
        while l <= r:
            m = l + (r-l)/2
            if y == a[m]:
                z = m
                break
            if y < a[m]:
                r = m - 1
            else:
                l = m + 1
        l = []
        if z == -1:
            l.append(-1)
            l.append(-1)
            return l
        t = z
        while t >= 0:
            if a[t] != y:
                break
            t -= 1
        l.append(t+1)
        t = z
        while t < n:
            if a[t] != y:
                break
            t += 1
        l.append(t-1)
        return l
