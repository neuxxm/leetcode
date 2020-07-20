#13:10-13:12
def f(s):
    cnt = [0] * 26
    for c in s:
        n = ord(c)-ord('a')
        cnt[n] += 1
    return cnt
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c = f(s)
        c2 = f(t)
        for i in xrange(26):
            if c[i] != c2[i]:
                return chr(ord('a')+i)
