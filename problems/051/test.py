#11:46-12:01
def judge(x, y, n, a):
    b = True
    for i in xrange(n):
        if a[x][i] == 'Q':
            return False
    for i in xrange(n):
        if a[i][y] == 'Q':
            return False
    i = x
    j = y
    while i < n and j < n:
        if a[i][j] == 'Q':
            return False
        i += 1
        j += 1
    i = x
    j = y
    while i >= 0 and j >= 0:
        if a[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i = x
    j = y
    while i >= 0 and j < n:
        if a[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    i = x
    j = y
    while i < n and j >= 0:
        if a[i][j] == 'Q':
            return False
        i += 1
        j -= 1
    return True  
def put(a, i, n, z):
    if i == n:
        l = []
        for i in xrange(n):
            l.append(''.join(a[i]))
        z.append(l)
        return
    for j in xrange(n):
        if judge(i, j, n, a):
            a[i][j] = 'Q'
            put(a, i+1, n, z)
            a[i][j] = '.'
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        a = []
        z = []
        for i in xrange(n):
            l = ['.'] * n
            a.append(l)
        put(a, 0, n, z)
        return z
