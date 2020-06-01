def find(x, y, map, dp):
    if dp[x][y] != 0:
        return dp[x][y] > 0
    if x == y:
        dp[x][y] = 1
        return True
    if x in map:
        b = False
        for nex in map[x]:
            if find(nex, y, map, dp):
                b = True
                break
        if b:
            dp[x][y] = 1
        else:
            dp[x][y] = -1
        return b
    else:
        dp[x][y] = -1
        return False
class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        dp = []
        for i in xrange(101):
            l = [0] * 101
            dp.append(l)
        par = {}
        for a,b in prerequisites:
            if a in par:
                par[a].append(b)
            else:
                par[a] = []
                par[a].append(b)
        r = []
        for a,b in queries:
            t = find(a, b, par, dp)
            r.append(t)
        return r
