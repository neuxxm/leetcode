#23:28-0:19
from collections import defaultdict
def find(u, i):
    r = u[i]
    while u[r] != r:
        r = u[r]
    z = u[i]
    while u[z] != z:
        t = u[z]
        u[z] = r
        z = t
    return r
def union(u, i, j, istr):
    ip = find(u, i)
    jp = find(u, j)
    if istr[ip] < istr[jp]:
        u[j] = ip
        u[jp] = ip
    else:
        u[i] = jp
        u[ip] = jp
class Solution(object):
    def trulyMostPopular(self, names, synonyms):
        """
        :type names: List[str]
        :type synonyms: List[str]
        :rtype: List[str]
        """
        ind = {}
        istr = {}
        ix = 0
        for s in names:
            fs = s.split('(')
            k = fs[0]
            if k not in ind:
                ind[k] = ix
                istr[ix] = k
                ix += 1
        for s in synonyms:
            fs = s.split(',')
            k = fs[0][1:]
            k2 = fs[1][:-1]
            if k not in ind:
                ind[k] = ix
                istr[ix] = k
                ix += 1
            if k2 not in ind:
                ind[k2] = ix
                istr[ix] = k2
                ix += 1
        u = [0] * ix
        for i in xrange(ix):
            u[i] = i
        for s in synonyms:
            fs = s.split(',')
            k = fs[0][1:]
            k2 = fs[1][:-1]
            i = ind[k]
            j = ind[k2]
            union(u, i, j, istr)
        cnt = defaultdict(lambda:0)
        for s in names:
            fs = s.split('(')
            k = fs[0]
            v = int(fs[1][:-1])
            k_id = find(u, ind[k])
            k = istr[k_id]
            cnt[k] += v
        rs = []
        for k,v in cnt.items():
            rs.append('%s(%d)'%(k, v))
        return rs
