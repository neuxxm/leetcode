#13:54AC
import bisect
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        n = len(w)
        self.a = [0] * (n+1)
        for i in xrange(1, n+1):
            self.a[i] = self.a[i-1] + w[i-1]
        self.n = self.a[i]

    def pickIndex(self):
        """
        :rtype: int
        """
        t = random.randint(1, self.n)
        return bisect.bisect_left(self.a, t) - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
