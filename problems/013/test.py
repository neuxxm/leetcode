#13:55AC
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = []
        cstr = 'IVXLCDM'
        a = [1, 5, 10, 50, 100, 500, 1000]
        map = {}
        for i in xrange(len(cstr)):
            map[cstr[i]] = i
        r = 0
        for c in s:
            ix = map[c]
            l = len(q)
            if l > 0:
                if ix <= q[l-1]:
                    t = q.pop()
                    q.append(ix)
                    r += a[t]
                else:
                    t = q.pop()
                    r += a[ix] - a[t]
            else:
                q.append(ix)
        while len(q) > 0:
            t = q.pop()
            r += a[t]
        return r
