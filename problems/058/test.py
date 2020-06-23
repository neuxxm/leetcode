#12:38-12:39
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        l = 0
        map = {}
        for i in xrange(26):
            map[chr(ord('a')+i)] = 1
            map[chr(ord('A')+i)] = 1
        b = True
        for i in xrange(n-1, -1, -1):
            if b and s[i] == ' ':
                continue
            elif s[i] in map:
                b = False
                l += 1
            else:
                break
        return l
