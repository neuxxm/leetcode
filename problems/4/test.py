class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def f(a, b, n, m, k):
            if n > m:
                return f(b, a, m, n, k)
            i, j = 0, 0
            while True:
                if i == n:
                    return b[j+k-1]
                if j == m:
                    return a[i+k-1]
                if k == 1:
                    return min(a[i], b[j])
                new_i = min(i + (k/2-1), n-1)
                new_j = min(j + (k/2-1), m-1)
                if a[new_i] <= b[new_j]:
                    k -= (new_i-i+1)
                    i = new_i + 1
                else:
                    k -= (new_j-j+1)
                    j = new_j + 1
        a = nums1
        b = nums2
        n = len(a)
        m = len(b)
        if (n+m)&1:
            return f(a, b, n, m, (n+m)/2+1)
        else:
            return (f(a, b, n, m, (n+m)/2) + f(a, b, n, m, (n+m)/2+1)) / 2.0
