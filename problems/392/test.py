#23:20-23:23
def f(s, t, i, j):
    if i == -1:
        return True
    if j == -1:
        return False
    if s[i] == t[j]:
        return f(s, t, i-1, j-1)
    else:
        return f(s, t, i, j-1)
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        if n == 0:
            return True
        if m < n:
            return False    
        return f(s, t, n-1, m-1)
