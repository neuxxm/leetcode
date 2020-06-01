#23:19-23:22
class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        a = A
        b = B
        k = n+m - 1
        i = m-1
        j = n-1
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
