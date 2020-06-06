#13:22-13:31
class Trie():
    def __init__(self):
        self.sons = [None] * 27
def add(td, s):
    s += '#'
    cur = td
    for c in s:
        n = 0
        if c != '#':
            n = ord(c) - ord('a') + 1
        if cur.sons[n]:
            cur = cur.sons[n]
        else:
            cur.sons[n] = Trie()
            cur = cur.sons[n]
def dfs(x, path, lvl, rs):
    for i in xrange(27):
        if x.sons[i]:
            if i > 0:
                if x.sons[0]:
                    path[lvl] = chr(i-1+ord('a'))
                    dfs(x.sons[i], path, lvl+1, rs)
            else:
                buf = ''.join(path[:lvl])
                if len(buf) > len(rs[0]):
                    rs[0] = buf
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        td = Trie()
        td.sons[0] = Trie()
        for s in words:
            add(td, s)
        path = [''] * 35
        rs = ['']
        dfs(td, path, 0, rs)
        return rs[0]
