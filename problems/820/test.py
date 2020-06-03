#18:31-19:00
class Trie:
    def __init__(self):
        self.sons = [None] * 28
def add(word, td):
    cur = td
    da = ord('a') - 2
    word = '#' + word[::-1] + '^'
    #print word
    for c in word:
        n = ord(c) - da
        if c == '#':
            n = 1
        elif c == '^':
            n = 0
        #print c, n
        if cur.sons[n] == None:
            cur.sons[n] = Trie()
        cur = cur.sons[n]
def dfs(td, z, lvl):
    for i in xrange(28):
        if td.sons[i] != None:
            if i != 0:
                dfs(td.sons[i], z, lvl+1)
            else:
                b = True
                for k in xrange(1, 28):
                    if td.sons[k] != None:
                        b = False
                if b:
                    z[0] += lvl
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        td = Trie()
        for word in words:
            add(word, td)
        z = [0]
        dfs(td, z, 0)
        return z[0]
