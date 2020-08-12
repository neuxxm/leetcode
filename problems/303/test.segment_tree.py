#13:33AC
def build(a, l, r, ix, nums):
    if l == r:
        a[ix] = nums[l]
        return a[ix]
    m = (l+r) >> 1
    ans = build(a, l, m, ix*2+1, nums)
    ans += build(a, m+1, r, ix*2+2, nums)
    a[ix] = ans
    return a[ix]
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
        n = len(nums)
        if n == 0:
            return
        self.a = [0] * (n<<2)
        build(self.a, 0, n-1, 0, nums)
        self.n = n
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.n == 0:
            return 0
        return query(self.a, 0, self.n-1, 0, i, j)
