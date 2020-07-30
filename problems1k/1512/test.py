#12:50-12:51
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        z = 0
        for i in xrange(n):
            for j in xrange(i+1, n):
                if a[i] == a[j]:
                    z += 1
        return z
