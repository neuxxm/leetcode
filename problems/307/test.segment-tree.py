#18:41fail
def build(a, l, r, ix, d):
    if l == r:
        a[ix] = d[l]
        return
    m = (l+r)>>1
    build(a, l, m, ix*2+1, d)
    build(a, m+1, r, ix*2+2, d)
    a[ix] = a[ix*2+1] + a[ix*2+2]
def update2(a, l, r, ix, dx, val):
    if l == r:
        #print 'hit', l
        #print 'a[%d]=%d'%(ix, val)
        a[ix] = val
        return
    m = (l+r)>>1
    if dx <= m:
        #print 'find in', l, m
        update2(a, l, m, ix*2+1, dx, val)
    else:
        #print 'find in', m+1, r
        update2(a, m+1, r, ix*2+2, dx, val)
    a[ix] = a[ix*2+1] + a[ix*2+2]
    #print 'a[%d]=a[%d]+a[%d]=%d+%d=%d'%(ix, ix*2+1, ix*2+2, a[ix*2+1], a[ix*2+2], a[ix])
def query(a, l, r, ix, x, y):
    if x<=l and r<=y:
        return a[ix]
    m = (l+r) >> 1
    ans = 0
    if x <= m:
        ans += query(a, l, m, ix*2+1, x, y)
    if y >= m+1:
        ans += query(a, m+1, r, ix*2+2, x, y)
    return ans
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        if self.n == 0:
            return
        self.a = [0] * (self.n*4)
        build(self.a, 0, self.n-1, 0, nums)
        #print self.n, self.a

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        if self.n == 0:
            return
        update2(self.a, 0, self.n-1, 0, i, val)
        #print self.a

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.n == 0:
            return 0
        return query(self.a, 0, self.n-1, 0, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
