#11:06-11:10
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        y = s
        a = nums
        n = len(a)
        l = 0
        r = 0
        z = 0
        zz = n + 1
        while r < n:
            while r < n:
                z += a[r]
                r += 1
                if z >= y:
                    break
            while l < n:
                if z >= y:
                    t = r-l
                    if t < zz:
                        zz = t
                z -= a[l]
                l += 1
                if z < y:
                    break
        return zz if zz != n+1 else 0
