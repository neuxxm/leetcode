#1:16-1:18
def f(s, cnt):
    for c in s:
        n = ord(c)-ord('a')
        cnt[n] += 1
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c = [0] * 26
        c2 = [0] * 26
        f(ransomNote, c)
        f(magazine, c2)
        for i in xrange(26):
            if c[i] > c2[i]:
                return False
        return True
