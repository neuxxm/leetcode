#23:14-23:21
class Trie:
    def __init__(self):
        self.sons = [None] * 27
def add(s, x, b, z):
    s += '#'
    cur = x
    cnt = 0
    path = [''] * len(s)
    lvl = 0
    for c in s:
        n = 0
        if c != '#':
            n = ord(c)-ord('a')+1
        if cur.sons[n]:
            cnt += 1
            if b:
                path[lvl] = c
                lvl += 1
            pass
        else:
            if b and cnt == 0:
                return False
            cur.sons[n] = Trie()
        cur = cur.sons[n]
    r = ''.join(path)
    if r.endswith('#'):
        r = r[:-1]
    if z[0] == '':
        z[0] = r
    elif len(r) < len(z[0]):
        z[0] = r
    return True
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        x = Trie()
        n = len(strs)
        if n == 0:
            return ''
        if n == 1:
            return strs[0]
        z = ['']
        add(strs[0], x, False, z)
        for i in xrange(1, n):
            if add(strs[i], x, True, z) == False:
                return ""
        return z[0]
