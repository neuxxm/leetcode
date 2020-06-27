#11:39-11:51
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[str]
        """
        dict = {}
        for w in wordList:
            dict[w] = 1
        q = []
        q.append(beginWord)
        y = endWord
        ss = ''
        for i in xrange(26):
            ss += chr(ord('a')+i)
        z = 0
        pre = {}
        find = False
        while len(q) > 0:
            l = len(q)
            while l > 0:
                l -= 1
                s = q.pop(0)
                if s == y:
                    find = True
                    break
                #print s,
                for i,c in enumerate(s):
                    for k in xrange(0, 26):
                        if ss[k] != c:
                            buf = s[:i] + ss[k] + s[i+1:]
                            if buf in dict:
                                pre[(buf,z)] = s
                                q.append(buf)
                                del dict[buf]
            if find:
                break
            z += 1
        r = []
        if find:
            r.append(y)
            while z >= 0:
                if (y,z) in pre:
                    y = pre[(y, z)]
                    r.append(y)
                z -= 1
        return r[::-1]
