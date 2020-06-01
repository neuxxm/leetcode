#11:34-11:38
def mergesort(a, l, r):
    if l >= r:
        return
    m = (l+r) / 2
    mergesort(a, l, m)
    mergesort(a, m+1, r)
    i = l
    j = m+1
    b = []
    while i <= m and j <= r:
        if a[i] < a[j]:
            b.append(a[i])
            i += 1
        elif a[i] > a[j]:
            b.append(a[j])
            j += 1
        else:
            b.append(a[i])
            b.append(a[j])
            i += 1
            j += 1
    while i <= m:
        b.append(a[i])
        i += 1
    while j <= r:
        b.append(a[j])
        j += 1
    a[l:r+1] = copy.deepcopy(b)
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = nums
        n = len(a)
        mergesort(a, 0, n-1)
        return a
