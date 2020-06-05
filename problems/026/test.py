#15:10-15:25
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return 0
        last = a[0]
        start = 0
        i = 1
        while i < n:
            if a[i] != last:
                a[start+1] = a[i]
                last = a[i]
                start += 1
            else:
                pass
            i += 1
        return start + 1
