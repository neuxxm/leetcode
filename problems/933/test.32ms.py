#12:54AC
class RecentCounter(object):
    def __init__(self):
        self.q = []
        self.n = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if self.n > 0:
            while self.n > 0 and t - self.q[0] > 3000:
                self.q.pop(0)
                self.n -= 1
            self.q.append(t)
            self.n += 1
            return self.n
        else:
            self.q.append(t)
            self.n += 1
            return self.n

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
