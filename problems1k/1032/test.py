#10:46-10:55
class Trie:
    def __init__(self):
        self.sons = [None] * 27
def add(td, s):
    s += '#'
    cur = td
    for c in s:
        n = 0
        if c != '#':
            n = ord(c) - ord('a') + 1
        if cur.sons[n]:
            cur = cur.sons[n]
        else:
            cur.sons[n] = Trie()
            cur = cur.sons[n]
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.td = Trie()
        for s in words:
            add(self.td, s[::-1])
        self.buf = ''
        self.n = 0

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.buf += letter
        self.n += 1
        i = self.n-1
        cur = self.td
        while i >= 0:
            c = self.buf[i]
            n = ord(c) - ord('a') + 1
            if cur.sons[n]:
                cur = cur.sons[n]
                if cur.sons[0] != None:
                    return True
            else:
                return False
            i -= 1
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
