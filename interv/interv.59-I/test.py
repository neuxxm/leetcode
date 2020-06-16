#11:34-11:37
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        a = nums
        n = len(a)
        if n == 0:
            return []
        l = 0
        r = 0
        cnt = 0
        s = 0
        rs = []
        while True:
            while r < n and cnt < k:
                s += a[r]
                r += 1
                cnt += 1
            if cnt == k:
                t = max(a[l:r])
                rs.append(t)
            else:
                break
            s -= a[l]
            cnt -= 1
            l += 1
        return rs
