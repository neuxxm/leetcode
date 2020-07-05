#15:54fail
def update(s, i, j, r):
    t = j-i+1
    if t > r[0]:
        r[0] = t
        r[1] = s[i:j+1]
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = []
        for i in xrange(n):
            l = [0] * n
            dp.append(l)
        r = [0, '']
        for l in xrange(0, n):
            for i in xrange(0, n):
                j = i+l
                if j >= n:
                    continue
                if l == 0:
                    dp[i][j] = 1
                    update(s, i, j, r)
                elif l == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                        update(s, i, j, r)
                else:
                    if dp[i+1][j-1] > 0 and s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                        update(s, i, j, r)
        return r[1]
