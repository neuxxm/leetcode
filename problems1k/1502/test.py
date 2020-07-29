#23:16-23:19
def partition(a, l, r):
    p = a[l]
    while l < r:
        while l < r and a[r]>=p:
            r -= 1
        a[l], a[r] = a[r], a[l]
        while l < r and a[l]<=p:
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
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        a = arr
        n = len(a)
        qsort(a, 0, n-1)
        t = a[1] - a[0]
        for i in xrange(2, n):
            if a[i] - a[i-1] != t:
                return False
        return True
