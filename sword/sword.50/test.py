class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0] * 26
        m = len(s)
        r = [' '] * 26
        for i,c in enumerate(s):
            n = ord(c)-ord('a')
            cnt[n] += 1
            if cnt[n] == 1:
                r[n] = i
            else:
                r[n] = m
        z = m
        zz = ' '
        for i in xrange(26):
            if r[i] < z:
                z = r[i]
                zz = chr(ord('a')+i)
        return zz
