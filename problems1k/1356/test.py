#11:45fail
def g(x):
    r = 0
    while x != 0:
        if x&1:
            r += 1
        x >>= 1
    return r
def f(x, y):
    #return x - y
    t = g(x) - g(y)
    if t > 0:
        return 1
    elif t < 0:
        return -1
    else:
        t = x - y
        if t > 0:
            return 1
        elif t < 0:
            return -1
        else:
            return 0
def partition(a, i, j):
    p = a[i]
    while i < j:
        while i < j and f(a[j],p) >= 0:
            j -= 1
        a[i], a[j]  = a[j], a[i]
        while i < j and f(a[i],p) <= 0:
            i += 1
        a[i], a[j] = a[j], a[i]
    return i
def qsort(a, i, j):
    if i >= j:
        return
    m = partition(a, i, j)
    qsort(a, i, m-1)
    qsort(a, m+1, j)
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        a = arr
        qsort(a, 0, len(a)-1)
        return a
