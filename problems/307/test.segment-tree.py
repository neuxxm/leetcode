#15:26-15:51
def build(a, l, r, ix, nums):
    if l == r:
        a[ix] = nums[l]
        return
    m = (l+r) >> 1
    build(a, l, m, ix*2+1, nums)
    build(a, m+1, r, ix*2+2, nums)
    a[ix] = a[ix*2+1] + a[ix*2+2]
def upd(a, l, r, ix, x, val):
    if l==x and r==x:
        a[ix] = val
        return
    m = (l+r) >> 1
    if x <= m:
        upd(a, l, m, ix*2+1, x, val)
    else:
        upd(a, m+1, r, ix*2+2, x, val)
    a[ix] = a[ix*2+1] + a[ix*2+2]
def query(a, l, r, ix, x, y):
    if x<=l and r<=y:
        return a[ix]
    m = (l+r) >> 1
    ans = 0
    if x <= m:
        ans += query(a, l, m, ix*2+1, x, y)
    if y > m:
        ans += query(a, m+1, r, ix*2+2, x, y)
    return ans
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.a = [0] * (n*4)
        self.n = n
        if self.n == 0:
            return
        build(self.a, 0, n-1, 0, nums)
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        if self.n == 0:
            return
        upd(self.a, 0, self.n-1, 0, i, val)      
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.n == 0:
            return 0
        return query(self.a, 0, self.n-1, 0, i, j)
