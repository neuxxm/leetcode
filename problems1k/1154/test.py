#20:49-20:52
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ts = date.split('-')
        y = int(ts[0])
        if y%4 == 0 and y%100 != 0:
            days[2] = 29
        m = int(ts[1])
        d = int(ts[2])
        z = d
        for i in xrange(1, m):
            z += days[i]
        return z
