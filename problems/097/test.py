#20:46-21:01
def f(s1, s2, s3, i, j, k, n, m, l, dp):
    if (i,j,k) in dp:
        return dp[(i,j,k)]
    if i == n:
        if j==m and k==l:
            dp[(i,j,k)] = True
            return True
        if s2[j] == s3[k]:
            dp[(i,j,k)] = f(s1, s2, s3, i, j+1, k+1, n, m, l, dp)
            return dp[(i,j,k)]
        dp[(i,j,k)] = False
        return False
    if j == m:
        if i==n and k==l:
            dp[(i,j,k)] = True
            return True
        if s1[i] == s3[k]:
            dp[(i,j,k)] = f(s1, s2, s3, i+1, j, k+1, n, m, l, dp)
            return dp[(i,j,k)]
        dp[(i,j,k)] = False
        return False
    if k == l:
        dp[(i,j,k)] = i==n and j==m
        return dp[(i,j,k)]
    if s1[i] == s2[j]:
        if s1[i] == s3[k]:
            dp[(i,j,k)] = f(s1, s2, s3, i+1, j, k+1, n, m, l, dp) or f(s1, s2, s3, i, j+1, k+1, n, m, l, dp)
        else:
            dp[(i,j,k)] = False
        return dp[(i,j,k)]
    else:
        if s1[i] == s3[k]:
            dp[(i,j,k)] = f(s1, s2, s3, i+1, j, k+1, n, m, l, dp)
        elif s2[j] == s3[k]:
            dp[(i,j,k)] = f(s1, s2, s3, i, j+1, k+1, n, m, l, dp)
        else:
            dp[(i,j,k)] = False
        return dp[(i,j,k)]
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n = len(s1)
        m = len(s2)
        l = len(s3)
        if n+m != l:
            return False
        dp = {}
        return f(s1, s2, s3, 0, 0, 0, n, m, l, dp)
