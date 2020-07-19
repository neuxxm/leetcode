#7.18fail,7.19 19:11AC
def topsort(s2e):
    d = {}
    for x,ys in s2e.items():
        if x not in d:
            d[x] = 0
        for y in ys:
            if y not in d:
                d[y] = 0
            d[y] += 1
    q = []
    for k,v in d.items():
        if v == 0:
            q.append(k)
    rs = []
    while q:
        x = q.pop(0)
        rs.append(x)
        for y in s2e[x]:
            d[y] -= 1
            if d[y] == 0:
                q.append(y)
    return rs
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        for i in xrange(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        S2E = defaultdict(set)
        for y in xrange(n):
            yid = group[y]
            if yid not in S2E:
                S2E[yid] = set()
            for x in beforeItems[y]:
                xid = group[x]
                if xid != yid:
                    S2E[xid].add(yid)
        group_seq = topsort(S2E)
        maps = {}
        for y in xrange(n):
            yid = group[y]
            if yid not in maps:
                maps[yid] = defaultdict(list)
            if y not in maps[yid]:
                maps[yid][y] = []
            for x in beforeItems[y]:
                xid = group[x]
                if xid == yid:
                    if xid not in maps:
                        maps[xid] = defaultdict(list)
                    maps[xid][x].append(y)
        zs = []
        for gid in group_seq:
            rs = topsort(maps[gid])
            if len(rs) != len(maps[gid]):
                return []
            zs.extend(rs)
        return zs if len(zs) == n else []
