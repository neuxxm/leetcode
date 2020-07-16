#7.16 16:41-16:46
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = nums
        n = len(a)
        q = []
        q.append(0)
        while len(q) > 0:
            list = []
            while len(q) > 0:
                t = q.pop(0)
                if t >= n-1:
                    return True
                list.append(t)
            for x in list:
                u = a[x]
                ma = x
                ma_ix = -1
                for k in xrange(1, u+1):
                    y = x+k
                    if y >= n-1:
                        return True
                    t = y+a[y]
                    if t > ma:
                        ma = t
                        ma_ix = k
                if ma != x:
                    q.append(x+ma_ix)
        return False
