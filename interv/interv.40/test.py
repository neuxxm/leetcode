#11:22AC
def partition(a, x, y):
    p = a[x]
    while x < y:
        while x<y and a[y]>=p:
            y -= 1
        a[x], a[y] = a[y], a[x]
        while x<y and a[x]<=p:
            x += 1
        a[x], a[y] = a[y], a[x]
    return x
def qsort(a, x, y, k):
    if x >= y:
        return
    m = partition(a, x, y)
    if m == k:
        return
    if m > k:
        qsort(a, x, m-1, k)
    else:
        qsort(a, m+1, y, k)
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        qsort(arr, 0, len(arr)-1, k)
        return arr[:k]
