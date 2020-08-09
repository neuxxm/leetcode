#18:53-18:57
def f(s):
    c = [0] * 26
    for t in s:
        n = ord(t)-ord('a')
        c[n] += 1
    return c
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        c = f(chars)
        z = 0
        for w in words:
            c2 = f(w)
            b = True
            for k in xrange(26):
                if c2[k] > c[k]:
                    b = False
                    break
            if b:
                z += len(w)
        return z
