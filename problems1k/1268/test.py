#23:28-23:45
class Trie():
    def __init__(self):
        self.sons = [None] * 27
def add(s, td):
    cur = td
    s += '#'
    for c in s:
        n = 0
        if c != '#':
            n = ord(c) - ord('a') + 1
        if cur.sons[n]:
            pass
        else:
            cur.sons[n] = Trie()
        cur = cur.sons[n]
def dfs(x, lvl, path, r):
    for i in xrange(0, 27):
        if x.sons[i]:
            if i != 0:
                path[lvl] = chr(i + ord('a') - 1)
                if dfs(x.sons[i], lvl+1, path, r):
                    return True
            else:
                r.append(''.join(path[:lvl]))
                if len(r) >= 3:
                    return True
    return False
def find(s, td):
    cur = td
    lvl = 0
    path = [0] * 10005
    for c in s:
        n = 0
        if c != '#':
            n = ord(c) - ord('a') + 1
            path[lvl] = c
            lvl += 1
        if cur.sons[n]:
            pass
        else:
            return []
        cur = cur.sons[n]
    r = []
    dfs(cur, lvl, path, r)
    return r
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        td = Trie()
        for s in products:
            add(s, td)
        n = len(searchWord)
        rs = []
        for i in xrange(1, n+1):
            r = find(searchWord[:i], td)
            rs.append(r)
        return rs
