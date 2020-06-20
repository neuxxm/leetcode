#11:15
def f(i, j, s, p, n, m):
    if i >= n:
        return j == m
    if j >= m:
        return i == n
    if p[j] == '.':
        return f(i+1, j+1, s, p, n, m)
    if p[j] == '*':
        if j == 0:
            return False
        last = p[j-1]
        if last == '.':
            while i < n:
                if f(i, j+1, s, p, n, m):
                    return True
                i += 1
            return False
        else:
            while i < n:
                if s[i] == last:
                    if f(i, j, s, p, n, m):
                        return True
                    i += 1
                else:
                    break
            return f(i, j+1, s, p, n, m)    
        return False
    if p[j] == s[i]:
        return f(i+1, j+1, s, p, n, m)
    if j+1 < m and p[j+1] == '*':
        return f(i, j+2, s, p, n, m)
    return False
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return f(0, 0, s, p, len(s), len(p))
