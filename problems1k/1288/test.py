#22:21AC
class pair:
    def __init__(self, l, r):
        self.l = l
        self.r = r
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        a = sorted(intervals, key=lambda fs:int(fs[0])*10000+int(fs[1]))
        n = len(a)
        if n == 0:
            return 0
        i = 0
        r = []
        r.append((a[i][0], a[i][1]))
        z = 0
        i += 1
        while i < n:
            if a[i][0] <= r[z][0] and r[z][1] <= a[i][1]:
                r.pop()
                r.append((a[i][0], a[i][1]))
                i += 1
            elif r[z][0] <= a[i][0] and a[i][1] <= r[z][1]:
                i += 1
            else:
                r.append((a[i][0], a[i][1]))
                z += 1
                i += 1
        return z + 1
