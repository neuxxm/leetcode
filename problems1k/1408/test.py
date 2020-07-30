#16:00-16:06
def f(s, map):
    n = len(s)
    for i in xrange(n):
        for j in xrange(i+1, n+1):
            if i==0 and j==n:
                continue
            map[s[i:j]] = 1
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        map = {}
        for w in words:
            f(w, map)
        rs = []
        for w in words:
            if w in map:
                rs.append(w)
        return rs
