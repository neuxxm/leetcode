#11:28fail
def f(s, i, n, map, d):
    if d[i] != -1:
        return d[i]
    if i == n:
        return True
    for j in xrange(i+1, n+1):
        if s[i:j] in map:
            if f(s, j, n, map, d):
                return True
    d[i] = False
    return False
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        map = {}
        for w in wordDict:
            map[w] = 1
        d = [-1] * (len(s) + 1)
        return f(s, 0, len(s), map, d)
