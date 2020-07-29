#11:11-11:19
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        p = a[0]
        cnt = 1
        for i in xrange(1, n):
            if cnt == 0:
                p = a[i]
                cnt = 1
            elif a[i] == p:
                cnt += 1
            else:
                cnt -= 1
        return p
