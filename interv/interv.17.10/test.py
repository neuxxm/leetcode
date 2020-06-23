#17:26fail
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        major = a[0]
        cnt = 1
        for i in xrange(1, n):
            if a[i] == major:
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                major = a[i]
                cnt = 1
        r = 0
        for i in xrange(0, n):
            if a[i] == major:
                r += 1
        if r > n/2:
            return major
        else:
            return -1
