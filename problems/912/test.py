#19:47-20:09fail
def partition(a, l, r):
    p = a[l]
    while l < r:
        while l<r and a[r]>=p:
            r -= 1
        a[l], a[r] = a[r], a[l]
        while l<r and a[l]<=p:
            l += 1
        a[l], a[r] = a[r], a[l]
    return l
def qsort(a, x, y):
    if x >= y:
        return
    p = partition(a, x, y)
    qsort(a, x, p-1)
    qsort(a, p+1, y)
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = nums
        n = len(a)
        qsort(a, 0, n-1)
        return a
