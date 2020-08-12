#15:29-16:00
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        a = arr
        n = len(a)
        d = difference
        if d == 0:
            map = {}
            for t in a:
                if t in map:
                    map[t] += 1
                else:
                    map[t] = 1
            m = 0
            for v in map.values():
                if v > m:
                    m = v
            return m
        dp = [0] * n
        map = {}
        dp[0] = 1
        map[a[0]] = 1 
        map[a[0]+d] = 2
        for i in xrange(1, n):
            if a[i] in map:
                dp[i] = map[a[i]]
                map[a[i]] = dp[i]
                map[a[i]+d] = dp[i] + 1
            else:
                dp[i] = 1
                map[a[i]] = 1
                map[a[i]+d] = 2
        return max(dp)
