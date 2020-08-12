#15:15-15:21
def lowbit(x):
    return x&-x
class bit:
    def __init__(self, nums):
        self.n = len(nums)
        self.a = [0] * (self.n+1)
        for i in xrange(self.n):
            self.update(i+1, nums[i])
    def update(self, i, val):
        while i <= self.n:
            self.a[i] += val
            i += lowbit(i)
    def sum(self, i):
        r = 0
        while i >= 1:
            r += self.a[i]
            i -= lowbit(i)
        return r
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.b = bit(nums)
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        b = self.b
        i += 1
        j += 1
        return b.sum(j) - b.sum(i-1)
