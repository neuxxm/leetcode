#12:54-13:24
def lowbit(x):
    return x&(-x)
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.a = [0] * (n+1)
        self.n = n
        for i in xrange(n):
            self.update2(i, nums[i])
    
    def update2(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        i += 1
        while i <= self.n:
            self.a[i] += val
            i += lowbit(i)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        t = self.sum(i) - self.sum(i-1)
        self.update2(i, val-t)

    def sum(self, i):
        r = 0
        i += 1
        it = i
        while i > 0:
            r += self.a[i]
            i -= lowbit(i)
        return r

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j) - self.sum(i-1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
