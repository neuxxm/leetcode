#23:13-23:24
class Trie:
    def __init__(self, val):
        self.sons = [None] * 27
        self.val = val
def dfs(x, r):
    for i in xrange(27):
        if x.sons[i]:
            if i != 26:
                dfs(x.sons[i], r)
            else:
                r[0] += x.sons[i].val
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.td = Trie(0)
        self.map = {}
        for i in xrange(0, 26):
            t = chr(i + ord('a'))
            self.map[t] = i
        self.map['#'] = 26

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        cur = self.td
        key += '#'
        for c in key:
            n = self.map[c]
            if cur.sons[n]:
                pass
            else:
                cur.sons[n] = Trie(val)
            cur = cur.sons[n]
        cur.val = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.td
        for c in prefix:
            n = self.map[c]
            if cur.sons[n]:
                cur = cur.sons[n]
            else:
                return 0
        if cur:
            r = [0]
            dfs(cur, r)
            return r[0]
        else:
            return 0
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
