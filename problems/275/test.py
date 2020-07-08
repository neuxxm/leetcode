#21:07-21:26
def f(a, l, r, n):
    ans = -1
    while l <= r:
        m = (l+r) >> 1
        if a[m] >= n-m:
            ans = m
            r = m-1
        else:
            l = m+1
    if ans == -1:
        return 0
    return n-ans
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        a = citations
        n = len(a)
        if n == 0:
            return 0
        return f(a, 0, n-1, n)
