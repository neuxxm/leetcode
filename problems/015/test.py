#12:30fail
def find(a, x, y, target, rs):
    l = x
    r = y
    while l < r:
        t = a[l] + a[r]
        if t == target:
            rs.append([a[l], a[r], -target])
            l += 1
            while l < r and a[l] == a[l-1]:
                l += 1
            r -= 1
            while l < r and a[r]==a[r+1]:
                r -= 1
        elif t < target:
            l += 1
        else:
            r -= 1
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a = sorted(nums)
        n = len(a)
        if n < 3:
            return []
        rs = []
        for i in xrange(n):
            if i > 0 and a[i] == a[i-1]:
                continue
            #find a[i]+a[j] == -a[k]
            #for j in xrange(i+1, n):
            #    if j > i+1 and a[j] == a[j-1]:
            #        continue   
            #    for k in xrange(j+1, n):
            #        if k > j+1 and a[k] == a[k-1]:
            #            continue
            #        if a[i]+a[j]+a[k] == 0:
            #            r.append([a[i], a[j], a[k]])
            find(a, i+1, n-1, -a[i], rs)
        return rs
