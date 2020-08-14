#20:15-20:19
def f(s):
    map = {}
    s1 = '0125689'
    s2 = '0152986'
    for i,c in enumerate(s1):
        map[c] = s2[i]
    buf = ''
    for c in s:
        if c not in map:
            return False
        buf += map[c]
    return buf != s
class Solution(object):
    def __init__(self):
        self.vmap = {}
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        vmap = self.vmap
        r = 0
        for i in xrange(1, N+1):
            if i in vmap:
                r += vmap[i]
            else:
                if f('%d'%i):
                    vmap[i] = 1
                    r += 1
                else:
                    vmap[i] = 0
        return r
