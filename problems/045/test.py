#23:10
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        if n <= 1:
            return 0
        q = []
        q.append((0, 0))
        obj = n-1
        while len(q) > 0:
            x, lvl = q.pop(0)
            if x + a[x] >= obj:
                return lvl + 1
            ma = 0
            ma_i = 0
            for i in xrange(1, a[x]+1):
                x2 = x + i
                t = x2 + a[x2]
                if t > ma:
                    ma = t
                    ma_i = i
            if ma > 0:
                q.append((x + ma_i, lvl+1))
