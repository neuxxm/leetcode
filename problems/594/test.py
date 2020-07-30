#16:31-16:34
from collections import defaultdict
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        cnt = defaultdict(lambda:0)
        for i in xrange(n):
            cnt[a[i]] += 1
        ma = 0
        for k,v in cnt.items():
            if k+1 in cnt:
                v += cnt[k+1]
                if v > ma:
                    ma = v
            elif k-1 in cnt:
                v += cnt[k-1]
                if v > ma:
                    ma = v
        return ma
