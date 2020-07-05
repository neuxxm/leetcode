#17:12-17:18
def partition(a, l, r):
    p = a[l]
    while l < r:
        while l < r and a[r] >= p:
            r -= 1
        a[l], a[r] = a[r], a[l]
        while l < r and a[l] <= p:
            l += 1
        a[l], a[r] = a[r], a[l]
    a[l] = p
    return l
def qsort(a, l, r, k):
    if l >= r:
        return
    p = partition(a, l, r)
    if p == k:
        return
    if p > k:
        qsort(a, l, p-1, k)
    else:
        qsort(a, p+1, r, k)
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        a = arr
        n = len(a)
        if n == 0:
            return []
        qsort(a, 0, n-1, k)
        return a[:k]
