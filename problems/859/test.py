#0:19-0:24
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a = A
        n = len(a)
        b = B
        m = len(b)
        if n != m:
            return False
        cnt = 0
        zs = []
        zcnt = [0] * 26
        for i in xrange(n):
            if a[i] != b[i]:
                cnt += 1
                zs.append(i)
            else:
                zcnt[ord(a[i])-ord('a')] += 1
        if cnt == 0:
            r = 0
            for i in xrange(26):
                if zcnt[i] >= 2:
                    return True
            return False
        if cnt != 2:
            return False
        return a[zs[1]] == b[zs[0]] and a[zs[0]] == b[zs[1]]
