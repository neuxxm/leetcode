#12:02AC
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        for i in xrange(26):
            c = chr(ord('A')+i)
            map[c] = i+1
        n = 0
        l = 1
        for c in s[::-1]:
            n += map[c] * l
            l *= 26
        return n
