#11:02-11:54
def f(s):
    ts = s.split('-')
    return int(ts[0]), int(ts[1]), int(ts[2])
def isleap(y):
    if y%100 == 0:
        return y%400 == 0
    else:
        return y%4 == 0
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        ms = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = f(date1)
        y2, m2, d2 = f(date2)
        if y > y2:
            y, y2 = y2, y
            m, m2 = m2, m
            d, d2 = d2, d
        elif y == y2:
            if m > m2:
                m, m2 = m2, m
                d, d2 = d2, d
            elif m == m2:
                if d > d2:
                    d, d2 = d2, d
                elif d == d2:
                    return 0
                return d2 - d
            if isleap(y):
                ms[2] = 29
            else:
                ms[2] = 28
            r = ms[m] - d
            for i in xrange(m+1, m2):
                r += ms[i]
            r += d2
            return r
        if isleap(y):
            ms[2] = 29
        else:
            ms[2] = 28
        r = ms[m] - d
        for i in xrange(m+1, 13):
            r += ms[i]
        for i in xrange(y+1, y2):
            if isleap(i):
                r += 366
            else:
                r += 365
        if isleap(y2):
            ms[2] = 29
        else:
            ms[2] = 28
        for i in xrange(1, m2):
            r += ms[i]
        r += d2
        return r
