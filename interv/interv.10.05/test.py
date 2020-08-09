#2:30-2:35
class Solution(object):
    def findString(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        a = words
        n = len(a)
        l = 0
        r = n - 1
        while l <= r:
            m = (l+r) >> 1
            if s == a[m]:
                return m
            z = m
            while z>=0 and a[z] == '':
                z -= 1
            if z < 0:
                return -1
            if s == a[z]:
                return z
            if s < a[z]:
                r = z - 1
            else:
                l = m + 1
        return -1
