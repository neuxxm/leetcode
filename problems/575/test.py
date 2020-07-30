#16:50-16:54
from collections import defaultdict
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        a = candies
        n = len(a)
        n2 = n / 2
        cnt = defaultdict(lambda:0)
        for i in xrange(n):
            cnt[a[i]] += 1
        if len(cnt) >= n2:
            return n2
        else:
            return len(cnt)
