#22:48AC
class Trie():
    def __init__(self):
        self.sons = [None] * 27
def add(td, s):
    s += '#'
    x = td
    for c in s:
        n = 0
        if c != '#':
            n = ord(c) - ord('a') + 1
        if x.sons[n]:
            pass
        else:
            x.sons[n] = Trie()
        x = x.sons[n]
def dfs(a, x, y, n, m, td, visit, path, lvl, z, map):
    if td.sons[0]:
        t = ''.join(path[:lvl])
        if t not in map:
            map[t] = 1
            z.append(t)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in xrange(4):
        x2 = x+dx[i]
        y2 = y+dy[i]
        if x2>=0 and x2<n and y2>=0 and y2<m:
            t = ord(a[x2][y2]) - ord('a') + 1
            if td.sons[t] and visit[(x2,y2)] == 0:
                path[lvl] = a[x2][y2]
                visit[(x2,y2)] = 1
                dfs(a, x2, y2, n, m, td.sons[t], visit, path, lvl+1, z, map)
                visit[(x2,y2)] = 0
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        a = board
        n = len(a)
        if n == 0:
            return []
        m = len(a[0])
        td = Trie()
        for w in words:
            add(td, w)
        map = {}
        visit = {}
        for i in xrange(n):
            for j in xrange(m):
                visit[(i,j)] = 0
        z = []
        for i in xrange(n):
            for j in xrange(m):
                t = ord(a[i][j]) - ord('a') + 1
                if td.sons[t]:
                    visit[(i,j)] = 1
                    path = [''] * (n*m)
                    path[0] = a[i][j]
                    dfs(a, i, j, n, m, td.sons[t], visit, path, 1, z, map)
                    visit[(i,j)] = 0
        return z
