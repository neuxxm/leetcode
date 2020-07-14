class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        s = sentence + ' '
        n = len(s)
        buf = ''
        cnt = 0
        for i in xrange(n):
            c = s[i]
            if c == ' ':
                cnt += 1
                if buf.startswith(searchWord):
                    return cnt
                buf = ''
            else:
                buf += c
        return -1
