#22:01AC
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
        while l < r:
            t = a[l] + a[r]
            if t == y:
                return [l+1, r+1]
            elif t < y:
                l += 1
            else:
                r -= 1
        return []
