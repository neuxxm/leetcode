#23:13AC
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        a = sorted(g)
        b = sorted(s)
        n = len(a)
        m = len(b)
        i = 0
        j = 0
        r = 0
        while i < n and j < m:
            if b[j] >= a[i]:
                j += 1
                i += 1
                r += 1
            else:
                j += 1
        return r
