#18:02-18:18
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = nums
        n = len(a)
        if n == 1:
            return
        cnt = 0
        i = 0
        while cnt < n:
            z = a[i]
            y = i
            while True:
                t = i-(k%n)
                while t < 0:
                    t += n
                if t == y:
                    break
                a[i] = a[t]
                cnt += 1
                i = t
            a[i] = z
            cnt += 1
            i += 1
