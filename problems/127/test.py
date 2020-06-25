#12:22-12:36fail
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        d = {}
        for w in wordList:
            d[w] = 1
        q = []
        q.append(beginWord)
        estr = ''
        for i in xrange(26):
            estr += chr(ord('a')+i)
        r = 0
        b = False
        while len(q) > 0 and b == False:
            qlen = len(q)
            #print q
            r += 1
            for k in xrange(qlen):
                s = q.pop(0)
                if s == endWord:
                    b = True
                    break
                l = len(s)
                for i in xrange(l):
                    for j in xrange(26):
                        if estr[j] != s[i]:
                            buf = s[:i] + estr[j] + s[i+1:]
                            if buf in d:
                                #print buf
                                del d[buf]
                                q.append(buf)
        return r if b else 0
