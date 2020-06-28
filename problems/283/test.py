#22:43-22:44
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = nums
        n = len(a)
        cnt = 0
        for i,t in enumerate(a):
            if t == 0:
                cnt += 1
            else:
                a[i-cnt] = a[i]
        for i in xrange(n-cnt, n):
            a[i] = 0
