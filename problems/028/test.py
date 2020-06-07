#17:26-17:42
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = haystack
        b = needle
        n = len(a)
        m = len(b)
        if m == 0:
            return 0
        if m > n:
            return -1
        z = -1
        for i in xrange(n):
            if i+m > n:
                continue
            r = True
            for j in xrange(m):
                if a[i+j] != b[j]:
                    r = False
                    break
            if r:
                z = i
                break
        return z
