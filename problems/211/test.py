#11:09-11:25
class Trie():
    def __init__(self):
        self.sons = [None] * 27
def dfs(x, s, i, l):
    c = s[i]
    if c == '#':
        return x.sons[0] != None
    elif c == '.':
        for k in xrange(1, 27):
            if x.sons[k]:
                if dfs(x.sons[k], s, i+1, l):
                    return True
        return False
    else:
        n = ord(c) - ord('a') + 1
        if x.sons[n]:
            return dfs(x.sons[n], s, i+1, l)
        else:
            return False
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.td = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        word += '#'
        cur = self.td
        for c in word:
            n = 0
            if c != '#':
                n = ord(c) - ord('a') + 1
            if cur.sons[n]:
                cur = cur.sons[n]
            else:
                cur.sons[n] = Trie()
                cur = cur.sons[n]


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        word += '#'
        l = len(word)
        return dfs(self.td, word, 0, l)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
