#22:50-23:01
def f(s):
    cnt = [0] * 26
    for c in s:
        cnt[ord(c)-ord('a')] += 1
    for i in xrange(26):
        if cnt[i]:
            return cnt[i]
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        a = [0] * n
        for i,w in enumerate(words):
            a[i] = f(w)
        m = len(queries)
        rs = [0] * m
        map = [0] * 2001
        for i in xrange(n):
            for j in xrange(1, a[i]):
                map[j] += 1
        for i,q in enumerate(queries):
            t = f(q)
            #z = 0
            #for j in xrange(n):
            #    if t < a[j]:
            #        z += 1
            rs[i] = map[t]
        return rs
