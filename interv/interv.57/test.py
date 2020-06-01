#23:43-23:51
def f(a, l, r, z, zz):
    if z < a[l]:
        return
    if z > a[r]:
        return
    while l <= r:
        m = (l+r) / 2
        if a[m] == z:
            zz.append(a[m])
            return
        if z < a[m]:
            r = m-1
        else:
            l = m+1
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = nums
        n = len(a)
        zz = []
        for i in xrange(0, n-1):
            f(a, i+1, n-1, target-a[i], zz)
            if len(zz) > 0:
                break
        zz.append(a[i])
        return zz
