#14:12-14:37
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a = nums1
        b = nums2
        i = m-1
        j = n-1
        k = len(a) - 1
        while i>=0 and j>=0:
            if a[i] >= b[j]:
                a[k] = a[i]
                i -= 1
                k -= 1
            else:
                a[k] = b[j]
                j -= 1
                k -= 1
        while i>=0:
            a[k] = a[i]
            i -= 1
            k -= 1
        while j>=0:
            a[k] = b[j]
            j -= 1
            k -= 1
