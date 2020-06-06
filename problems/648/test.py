#9:55-10:08
class Trie:
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
            pass
        else:
            cur.sons[n] = Trie()
        cur = cur.sons[n]
def find(td, s, r):
    s += '#'
    cur = td
    path = [''] * 1005
    lvl = 0
    for c in s:
        n = 0
        if c != '#':
            n = ord(c)-ord('a')+1
        if cur.sons[n]:
            path[lvl] = c
            lvl += 1
            if cur.sons[n].sons[0] != None:
                r[0] = ''.join(path[:lvl])
                return
        else:
            return
        cur = cur.sons[n]
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        td = Trie()
        for s in dict:
            add(td, s)
        i = 0
        n = len(sentence)
        buf = ''
        r = ''
        while i < n:
            c = sentence[i]
            if c == ' ':
                if len(buf) > 0:
                    t = [buf]
                    find(td, buf, t)
                    r += t[0] + ' '
                buf = ''
            else:
                buf += c
            i += 1
        if len(buf) > 0:
            t = [buf]
            find(td, buf, t)
            r += t[0] + ' '
        if r.endswith(' '):
            r = r[:-1]
        return r
