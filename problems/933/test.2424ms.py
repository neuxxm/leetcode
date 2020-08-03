#14:51-15:09
class RecentCounter(object):
    def __init__(self):
        self.q = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        q = self.q
        q.append(t)
        l = len(q)
        mi = t - 3000
        z = 0
        for i in xrange(l-1, -1, -1):
            if q[i] >= mi:
                z += 1
            else:
                break
        return z
