#13:48fail
import bisect
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return 0
        sum = [0] * n
        sum[0] = a[0]
        for i in xrange(1, n):
            sum[i] = sum[i-1] + a[i]
        ssum = sorted(sum)
        r = 0
        for i in xrange(n):
            y = 0
            if i > 0:
                y = sum[i-1]
            a1 = bisect.bisect_left(ssum, y+lower)
            a2 = bisect.bisect_right(ssum, y+upper)
            if a2 >= a1:
                r += (a2-a1)
            ssum.remove(sum[i])
        return r
