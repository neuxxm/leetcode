#15:24-16:07
def find(x, u):
    r = x
    while u[r] != r:
        r = u[r]
    t = x
    while u[t] != t:
        l = t
        t = u[t]
        u[l] = r
    return r
def merge(x, y, num, u):
    x = find(x, u)
    y = find(y, u)
    if num[x] >= num[y]: 
        u[y] = x
        num[x] += num[y]
    else:
        u[x] = y
        num[y] += num[x]
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        map = {}
        rmap = {}
        umap = {}
        ix = 0
        num = [0] * 10005
        u = [0] * 10005
        al = len(accounts)
        for k in xrange(al):
            a = accounts[k]
            n = len(a)
            last = -1
            for i in xrange(1, n):
                if a[i] not in map:
                    map[a[i]] = ix
                    rmap[ix] = a[i]
                    umap[ix] = k
                    u[ix] = ix
                    ix += 1
                aid = map[a[i]]
                if last != -1:
                    merge(aid, last, num, u)
                    last = aid
                else:
                    last = aid
        for i in xrange(ix):
            find(i, u)
        dict = {}
        for i in xrange(ix):
            z = u[i]
            v = rmap[i]
            if z in dict:
                dict[z].append(v)
            else:
                dict[z] = []
                dict[z].append(v)
        r = []
        for z in dict.keys():
            dict[z].sort()
            l = []
            k = accounts[umap[z]][0]
            l.append(k)
            for v in dict[z]:
                l.append(v)
            r.append(l)
        return r
