class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        r = float('-inf')
        for i in xrange(n):
            for j in xrange(i+1, n):
                t = (a[i]-1) * (a[j]-1)
                if t > r:
                    r = t
        return r
