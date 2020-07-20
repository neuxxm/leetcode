#11:28-11:32
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = numbers
        y = target
        n = len(a)
        l = 0
        r = n-1
        rs = []
        while l < r:
            z = a[l] + a[r]
            if z == y:
                rs.append(l+1)
                rs.append(r+1)
                return rs
            if z < y:
                l += 1
            else:
                r -= 1
