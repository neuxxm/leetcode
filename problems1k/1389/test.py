#13:05-13:09
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        a = nums
        n = len(nums)
        r = [0] * n
        m = 0
        for i in xrange(n):
            t = a[i]
            loc = index[i]
            for j in xrange(m+1, loc-1, -1):
                if j >= n:
                    continue
                r[j] = r[j-1]
            r[loc] = t
            m += 1
        return r
