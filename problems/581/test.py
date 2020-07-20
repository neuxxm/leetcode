#23:33-23:37
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
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[:]
        n = len(a)
        qsort(a, 0, n-1)
        l = 0
        r = n-1
        while l < n and a[l] == nums[l]:
            l += 1
        while r >= 0 and a[r] == nums[r]:
            r -= 1
        if l >= r:
            return 0
        return r-l+1
