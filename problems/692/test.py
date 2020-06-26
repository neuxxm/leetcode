#23:23-23:41
class Trie():
    def __init__(self, val):
        self.sons = [None] * 27
        self.val = val
def add(td, s, cnt):
    cur = td
    maf = 0
    for c in s:
        n = 0
        if c != '#':
            n = ord(c)-ord('a')+1
            if cur.sons[n]:
                pass
            else:
                cur.sons[n] = Trie(1)
        else:
            if cur.sons[n]:
                cur.sons[n].val += 1
            else:
                cur.sons[n] = Trie(1)
        cur = cur.sons[n]
        cnt[cur.val] = 1
def dfs(td, lvl, path, maf, z, k):
    for i in xrange(27):
        if td.sons[i]:
            if i == 0:
                if td.sons[i].val == maf:
                    if len(z) < k:
                        z.append(''.join(path[:lvl]))
            else:
                path[lvl] = chr(ord('a')+i-1)
                dfs(td.sons[i], lvl+1, path, maf, z, k)
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        td = Trie(0)
        ma = 0
        maf = 0
        cnt = {}
        for w in words:
            w += '#'
            add(td, w, cnt)
            if len(w) > ma:
                ma = len(w)
        path = [''] * (ma+1)
        z = []
        for maf in sorted(cnt.keys(), reverse=True):
            dfs(td, 0, path, maf, z, k)
        return z
