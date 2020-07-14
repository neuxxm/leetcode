#15:25-15:29
def f(a, i, y, path, map):
    if i == 0:
        if y == a[i]:
            ts = sorted(path + [a[i]])
            buf = ''
            for t in ts:
                buf += '%d.'%t
            map[buf[:-1]] = 1
        return
    if y >= a[i]:
        if y == a[i]:
            ts = sorted(path + [a[i]])
            buf = ''
            for t in ts:
                buf += '%d.'%t
            map[buf[:-1]] = 1
        f(a, i-1, y-a[i], path+[a[i]], map)
    f(a, i-1, y, path, map)
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        a = candidates
        y = target
        n = len(a)
        if n == 0:
            return []
        path = []
        map = {}
        f(a, n-1, y, path, map)
        z = []
        for k in map.keys():
            rs = k.split('.')
            r = []
            for t in rs:
                r.append(int(t))
            z.append(r)
        return z
