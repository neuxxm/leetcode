#23:40-23:42
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        map = {}
        for i in xrange(26):
            v = chr(ord('a')+i)
            map[chr(ord('A')+i)] = v
            map[v] = v
        r = ''
        for c in str:
            if c in map:
                r += map[c]
            else:
                r += c
        return r
