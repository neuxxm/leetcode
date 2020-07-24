#13:42-13:43
def f(s, map):
    n = len(s)
    t = map[s[0]]
    for i in xrange(1, n):
        if map[s[i]] != t:
            return False
    return True
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r = []
        map = {}
        s1 = 'qwertyuiop'
        s2 = 'asdfghjkl'
        s3 = 'zxcvbnm'
        for c in s1:
            map[c] = 1
            map[chr(ord(c)-ord('a')+ord('A'))] = 1
        for c in s2:
            map[c] = 2
            map[chr(ord(c)-ord('a')+ord('A'))] = 2
        for c in s3:
            map[c] = 3
            map[chr(ord(c)-ord('a')+ord('A'))] = 3
        for w in words:
            if f(w, map):
                r.append(w)
        return r
