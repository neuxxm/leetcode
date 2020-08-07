#coding:utf8
class Trie:
    def __init__(self, val):
        self.val = val
        self.sons = [None] * 27
def add(td, s, ix):
    cur = td
    s += '#'
    for c in s:
        n = 0
        if c != '#':
            n = ord(c)-ord('a')+1
        if cur.sons[n]:
            if n == 0:
                cur.sons[n].val = ix
        else:
            if n != 0:
                cur.sons[n] = Trie(0)
            else:
                cur.sons[n] = Trie(ix)
        cur = cur.sons[n]
def visit(cur, path, lvl, z, z2):
    for i in xrange(27):
        if cur.sons[i] != None:
            if i == 0:
                z.append(path[:lvl])
                z2.append(cur.sons[i].val)
            else:
                path[lvl] = chr(ord('a') + i-1)
                visit(cur.sons[i], path, lvl+1, z, z2)
def dfs(cur, s, n, i, path, z, z2):
    if i == n:
        visit(cur, path, i, z, z2)
        return
    ix = ord(s[i]) - ord('a') + 1
    if cur.sons[ix] != None:
        path[i] = s[i]
        dfs(cur.sons[ix], s, n, i+1, path, z, z2)
    else:
        return
def is_aba(s):
    n = len(s)
    for i in xrange(n/2):
        if s[i] != s[n-1-i]:
            return False
    return True
def deal(i, w, z, z2, rs, map):
    for j,ts in enumerate(z):
        t = ''.join(ts)
        t2 = t[::-1]
        p = (w,t2)
        if p in map:
            continue
        map[p] = 1
        if w != t2:
            tt = w + t2
            if is_aba(tt):
                rs.append([i, z2[j]])
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        td = Trie(0)
        for i,w in enumerate(words):
            add(td, w[::-1], i)
        path = [0] * 1000
        z = []
        z2 = []
        '''visit(td, path, 0, z, z2)
        for ts in z:
            t = ''.join(ts)
            print t
        print '==='''
        rs = []
        map = {}
        for i,w in enumerate(words):
            wl = len(w)
            if wl >= 2 and w[wl-1]==w[wl-2]:
                for j in xrange(len(w)+1):
                    path = [0] * 1000
                    z = []
                    z2 = []
                    w2 = w[:j]
                    dfs(td, w2, len(w2), 0, path, z, z2)
                    deal(i, w, z, z2, rs, map)
            else:
                for j in xrange(wl-1, wl+1):
                    path = [0] * 1000
                    z = []
                    z2 = []
                    w2 = w[:j]
                    dfs(td, w2, len(w2), 0, path, z, z2)
                    deal(i, w, z, z2, rs, map)
        return rs
ws = []
s = Solution()
s.palindromePairs(ws)
