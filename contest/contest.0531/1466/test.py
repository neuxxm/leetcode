class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        pairs = connections
        q = []
        q.append(0)
        visit = {}
        visit[0] = 1
        map = {}
        map2 = {}
        for x,y in pairs:
            if y == 0:
                q.append(x)
                visit[x] = 1
            else:
                if x in map:
                    map[x].append(y)
                else:
                    map[x] = []
                    map[x].append(y)
            if y in map2:
                map2[y].append(x)
            else:
                map2[y] = []
                map2[y].append(x)
        #print q
        cnt = 0
        while len(q) > 0:
            #print q
            t = q.pop(0)
            #for x,y in pairs:
            #    if x not in visit:
            #        if y == t:
            if t in map2:
                for nex in map2[t]:
                    if nex not in visit:
                        q.append(nex)
                        visit[nex] = 1
            if t in map:
                for nex in map[t]:
                    if nex not in visit:
                        #print t, nex
                        cnt += 1
                        q.append(nex)
                        visit[nex] = 1
        return cnt
