#11:33-11:42
def f(i, j, a, n):
    r = 0
    x = i
    y = j
    while x >= 0:
        c = a[x][y]
        if c == 'B':
            break
        if c == 'p':
            r += 1
            break
        x -= 1
    x = i
    y = j
    while x < n:
        c = a[x][y]
        if c == 'B':
            break
        if c == 'p':
            r += 1
            break
        x += 1
    x = i
    y = j
    while y >= 0:
        c = a[x][y]
        if c == 'B':
            break
        if c == 'p':
            r += 1
            break
        y -= 1
    x = i
    y = j
    while y < n:
        c = a[x][y]
        if c == 'B':
            break
        if c == 'p':
            r += 1
            break
        y += 1
    return r      
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        a = board
        n = len(a)
        for i in xrange(n):
            for j in xrange(n):
                if a[i][j] == 'R':
                    return f(i, j, a, n)
