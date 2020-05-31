#22:52fail
def adjust(a, n, i):
    cur = i
    l = cur*2+1
    while l < n:
        r = l+1
        ma = a[cur]
        ix = cur
        if a[l] > ma:
            ma = a[l]
            ix = l
        if r<n and a[r] > ma:
            ma = a[r]
            ix = r
        if ix == cur:
            break
        a[cur], a[ix] = a[ix], a[cur]
        cur = ix
        l = cur*2 + 1
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = nums
        n = len(a)
        for i in xrange((n-1)/2, -1, -1):
            adjust(a, n, i)
        for i in xrange(n-1, 0, -1):
            a[i], a[0] = a[0], a[i]
            adjust(a, i, 0)
        return a
