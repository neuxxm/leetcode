#20:15-20:18
def f(s):
    cnt = [0] * 26
    for c in s:
        cnt[ord(c)-ord('a')] += 1
    r = ''
    for i in xrange(26):
        r += '%d.'%(cnt[i])
    return r
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for s in strs:
            n = f(s)
            if n in map:
                map[n].append(s)
            else:
                map[n] = []
                map[n].append(s)
        r = []
        for v in map.values():
            r.append(v)
        return r
