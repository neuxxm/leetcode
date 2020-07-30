#19:13-19:20
def partition(a, l, r):
    p = a[l]
    while l < r:
        while l < r and a[r] <= p:
            r -= 1
        a[l], a[r] = a[r], a[l]
        while l < r and a[l] >= p:
            l += 1
        a[l], a[r] = a[r], a[l]
    return l
def qsort(a, x, y):
    if x >= y:
        return
    m = partition(a, x, y)
    qsort(a, x, m-1)
    qsort(a, m+1, y)
def bisearch(a, n, x):
    l = 0
    r = n-1
    while l <= r:
        m = (l+r) >> 1
        if a[m] == x:
            return m
        if x > a[m]:
            r = m - 1
        else:
            l = m + 1
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        a = nums
        n = len(a)
        if n == 0:
            return []
        sa = a[:]
        qsort(sa, 0, n-1)
        map = {}
        map[1] = 'Gold Medal'
        map[2] = 'Silver Medal'
        map[3] = 'Bronze Medal'
        for i in xrange(n):
            t = bisearch(sa, n, a[i]) + 1
            if t in map:
                a[i] = map[t]
            else:
                a[i] = '%d'%t
        return a
