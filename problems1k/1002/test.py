#23:24-23:40
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        zcnt = [0] * 26
        n = len(A)
        uniq = [0] * 26
        for c in A[0]:
            zcnt[ord(c)-ord('a')] += 1
        for i in xrange(26):
            if zcnt[i] > 0:
                uniq[i] += 1
        for k in xrange(1, n):
            cnt = [0] * 26
            for c in A[k]:
                cnt[ord(c)-ord('a')] += 1
            for i in xrange(26):
                if cnt[i] > 0:
                    uniq[i] += 1
                    if zcnt[i] > 0:
                        zcnt[i] = min(zcnt[i], cnt[i])
        rs = []
        for i in xrange(26):
            if uniq[i] < n:
                continue
            for k in xrange(zcnt[i]):
                rs.append(chr(ord('a')+i))
        return rs
