class Trie:
    def __init__(self, val):
        self.sons = [None] * 27
        self.val = val
def add(td, s):
    s += '#'
    n = len(s)
    cur = td
    i = 0
    while i < n:
        c = s[i]
        z = 26 
        if c != '#':
            z = ord(c)-ord('a')
        if cur.sons[z] != None:
            cur = cur.sons[z]
            cur.val += 1
        else:
            cur.sons[z] = Trie(1)
            cur = cur.sons[z]
        i += 1
def dfs(x, lvl, path, r, n):
    if x.val == n:
        t = path[:lvl]
        if len(t) > len(r[0]):
            r[0] = t
    for i in xrange(27):
        if x.sons[i] != None:
            if i != 26:
                path[lvl] = chr(ord('a') + i)
            else:
                path[lvl] = '#'
            dfs(x.sons[i], lvl+1, path, r, n)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        td = Trie(0)
        n = len(strs)
        for s in strs:
			add(td, s)
        path = [0] * 100005
        r = ['']
        dfs(td, 0, path, r, n)
        z = ''.join(r[0])
        if z.endswith('#'):
            z = z[:-1]
        return z
a = ["flower","flow","flight"]
a = ["dog","racecar","car"]
a = ["a","a","a"]
s = Solution()
print s.longestCommonPrefix(a)
