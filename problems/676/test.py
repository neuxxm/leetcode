#20:58AC
class Trie():
    def __init__(self):
        self.sons = [None] * 27
def add(td, s):
    s += '#'
    cur = td
    for c in s:
        n = 0
        if c != '#':
            n = ord(c)-ord('a')+1
        if cur.sons[n]:
            cur = cur.sons[n]
        else:
            cur.sons[n] = Trie()
            cur = cur.sons[n]
def f(x, s, i, n, z, loc):
    if s[i] == '.':
        if z[0] > 0:
            return False
        for k in xrange(27):
            if x.sons[k] and k != loc:
                z[0] = 1
                if f(x.sons[k], s, i+1, n, z, loc):
                    return True
        return False 
    elif s[i] != '#':
        n = ord(s[i])-ord('a')+1
        if x.sons[n]:
            return f(x.sons[n], s, i+1, n, z, loc)
        else:
            return False
    else:
        if x.sons[0]:
            return z[0] == 1
        else:
            return False
class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.td = Trie()
    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for s in dict:
            add(self.td, s)
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        n = len(word)
        w = word + '#'
        #if g(self.td, w, 0, n+1):
        #    return False
        for i in xrange(n):
            loc = ord(word[i]) - ord('a') + 1
            w = word[:i] + '.' + word[i+1:] + '#'
            z = [0]
            if f(self.td, w, 0, n+1, z, loc):
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
