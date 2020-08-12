class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        d = [0] * 2001
        a = arr
        for t in arr:
            d[t] = 1
        c = 0
        z = 0
        for i in xrange(1, 2001):
            if d[i] == 0:
                c += 1
                if c == k:
                    z = i
                    break
        return z
