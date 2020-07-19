#1:22-1:27
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = [0] * 26
        ans = [-1] * 26
        m = len(s)
        for i in xrange(m):
            n = ord(s[i]) - ord('a')
            cnt[n] += 1
            if cnt[n] == 1:
                ans[n] = i
            else:
                ans[n] = -1
        mi = m
        for i in xrange(26):
            if ans[i] != -1:
                if ans[i] < mi:
                    mi = ans[i]
        return mi if mi != m else -1
