#13:05-13:24
import copy
def mergesort(a, l, r, z):
    if l >= r:
        return
    #print a[l:r+1]
    m = (l+r) / 2
    mergesort(a, l, m, z)
    mergesort(a, m+1, r, z)
    i = l
    j = m+1
    b = []
    #print 'merge', a[l:m+1], a[m+1:r+1]
    while i <= m and j <= r:
        if a[i] < a[j]:
            b.append(a[i])
            i += 1
        elif a[i] > a[j]:
            b.append(a[j])
            j += 1
            z[0] += (m-i+1)
        else:
            b.append(a[i])
            i += 1
    while i <= m:
        b.append(a[i])
        i += 1
    while j <= r:
        b.append(a[j])
        j += 1
    a[l:r+1] = copy.deepcopy(b)
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        z = [0]
        mergesort(a, 0, n-1, z)
        return z[0]
