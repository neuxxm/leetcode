#11:27fail
from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a = nums
        n = len(a)
        dp = [0] * (n+1)
        dp[0] = 0
        for i in xrange(0, n):
            dp[i+1] = dp[i] + a[i]
        r = 0
        map = defaultdict(lambda:0)
        for i in xrange(n+1):
            t = dp[i] - k
            if t in map:
                r += map[t]
            map[dp[i]] += 1
        return r
