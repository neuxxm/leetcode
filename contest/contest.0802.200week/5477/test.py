def f(a, x, loc, m):
    n = len(a)
    if n == 0:
        return 0
    #print a, x, loc, 'n', n
    b = True
    for j in xrange(loc, m):
        if a[0][j] != 0:
            b = False
            break
    #print 'b', b
    if b:
        return f(a[x+1:], 0, loc+1, m)
    else:
        z = 0
        i = 1
        while i < n:
            b = True
            for j in xrange(loc, m):
                if a[i][j] != 0:
                    b = False
                    break
            if b:
                z = i
                break
            else:
                i += 1
        if i == n:
            return -1
        #print 'i', i
        t = f(a[:i]+a[i+1:], 0, loc+1, m)
        if t == -1:
            return -1
        return z + t
class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a = grid
        if len(a) == 0:
            return 0
        return f(a, 0, 1, len(a[0]))
