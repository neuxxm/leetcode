#23:47AC
def adjust(a, i, n):
    #print 'bef', a
    cur = i
    while cur < n:
        l = cur*2+1
        r = cur*2+2
        t = cur
        if l < n and a[l] < a[t]:
            t = l
        if r < n and a[r] < a[t]:
            t = r
        if t == cur:
            break
        #print 'swap', a[cur], a[t]
        a[cur], a[t] = a[t], a[cur]
        cur = t
    #print 'aft', a
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.a = [0] * k
        self.ix = 0
        self.k = k
        if len(nums) >= k:
            for i in xrange(0, k):
                self.a[i] = nums[i]
            self.ix = k
            for i in xrange((self.k-1)/2, -1, -1):
                adjust(self.a, i, self.k)
            for i in xrange(k, len(nums)):
                self.add(nums[i])
        else:
            for t in nums:
                self.a[self.ix] = t
                self.ix += 1
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.ix < self.k:
            self.a[self.ix] = val
            self.ix += 1
            if self.ix == self.k:
                for i in xrange((self.k-1)/2, -1, -1):
                    adjust(self.a, i, self.k)
                #print 'after k', self.a
        else:
            a = self.a
            if val > a[0]:
                a[0] = val
                adjust(self.a, 0, self.k)
        return self.a[0]
