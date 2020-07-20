#19:49-20:01
def partition(a, l, r):
    p = a[l]
    while l < r:
        while l < r and a[r] >= p:
            r -= 1
        a[l], a[r] = a[r], a[l]
        while l < r and a[l] <= p:
            l += 1
        a[l], a[r] = a[r], a[l]
    return l
def qsort(a, x, y):
    if x >= y:
        return
    m = partition(a, x, y)
    qsort(a, x, m-1)
    qsort(a, m+1, y)
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        a = arr
        n = len(a)
        if n == 0:
            return []
        qsort(a, 0, n-1)
        mi = float('inf')
        for i in xrange(1, n):
            t = abs(a[i]-a[i-1])
            if t < mi:
                mi = t
        rs = []
        for i in xrange(1, n):
            t = abs(a[i]-a[i-1])
            if t == mi:
                rs.append([a[i-1], a[i]])
        return rs
