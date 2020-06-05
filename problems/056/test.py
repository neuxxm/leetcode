#12:37-12:54
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        x = sorted(intervals, key=lambda fs:fs[0])
        n = len(x)
        if n == 0:
            return []
        i = 0
        a = x[i][0]
        b = x[i][1]
        r = []
        while i < n-1:
            c = x[i+1][0]
            d = x[i+1][1]
            if b < c:
                r.append((a, b))
                a = c
                b = d
                i += 1
            elif b == c:
                b = d
                i += 1
            elif b < d:
                if a < c:
                    b = d
                    i += 1
                else:
                    a = c
                    b = d
                    i += 1
            else:
                i += 1
        if len(r) > 0 and a != r[len(r)-1][0]:
            r.append((a, b))
        else:
            r.append((a, b))
        return r
