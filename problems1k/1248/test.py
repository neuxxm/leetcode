#13:41-13:53,15:16-15:27
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a = nums
        n = len(a)
        l = 0
        r = 0
        cnt = 0
        ls = [-1]
        rs = [-1]
        while True:
            while r < n:
                c = a[r]
                r += 1
                if c&1:
                    cnt += 1
                    if cnt == k:
                        break
            if cnt != k:
                break
            while l < n and cnt == k:
                c = a[l]
                l += 1
                if c&1:
                    cnt -= 1
                    break
            ls.append(l-1)
            rs.append(r-1)
        ls.append(n)
        rs.append(n)
        le = len(ls)
        #print ls
        #print rs
        z = 0
        for i in xrange(1, le-1):
            t = (ls[i]-ls[i-1]) * (rs[i+1]-rs[i])
            z += t
        return z
