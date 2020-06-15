#15:49-16:19
def adjust(a, n, i):
    cur = i
    while cur < n:
        l = cur*2+1
        r = cur*2+2
        m = a[cur]
        mi = cur
        if l<n and a[l] > m:
            m = a[l]
            mi = l
        if r<n and a[r] > m:
            m = a[r]
            mi = r
        if cur == mi:
            break
        a[cur], a[mi] = a[mi], a[cur]
        cur = mi
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a = nums
        n = len(a)
        for i in xrange((n-1)/2, -1, -1):
            adjust(a, n, i)
        j = n-1
        while True:
            a[0], a[j] = a[j], a[0]
            adjust(a, j, 0)
            k -= 1
            if k == 0:
                break
            j -= 1
        return a[j]
