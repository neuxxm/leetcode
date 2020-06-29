#11:02-11:11
def adjust(a, n, i):
    cur = i
    while cur < n:
        left = cur*2+1
        right = cur*2+2
        t = cur
        if left < n and a[left] > a[t]:
            t = left
        if right < n and a[right] > a[t]:
            t = right
        if t == cur:
            break
        a[cur], a[t] = a[t], a[cur]
        cur = t
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a = nums
        n = len(a)
        for i in xrange((n-1)/2, -1, -1):
            adjust(a, n, i)
        cnt = 0
        z = 0
        for i in xrange(n-1, -1, -1):
            a[0], a[i] = a[i], a[0]
            z = a[i]
            cnt += 1
            if cnt >= k:
                break
            adjust(a, i, 0)
        return z
