#19:38fail
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return 0
        dp = [0] * n
        dp[0] = 0
        if s[1] == ')' and s[0] == '(':
            dp[1] = 2
        for i in xrange(2, n):
            if s[i] == '(':
                dp[i] = 0
            else:
                # "(())),())("
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                else:
                    t = i - dp[i-1] - 1
                    if t>=0 and s[t] == '(':
                        dp[i] = dp[i-1] + 2
                        if t-1 >= 0:
                            dp[i] += dp[t-1]
                    else:
                        dp[i] = 0
        return max(dp)
