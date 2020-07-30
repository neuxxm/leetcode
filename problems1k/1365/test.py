#12:20-12:21
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = nums
        n = len(a)
        r = [0] * n
        for i in xrange(n):
            z = 0
            for j in xrange(n):
                if i == j:
                    continue
                if a[j] < a[i]:
                    z += 1
            r[i] = z
        return r
