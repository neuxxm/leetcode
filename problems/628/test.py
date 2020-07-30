#23:56-23:58
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # + + +
        # + - -
        n = len(nums)
        c = [0] * 2001
        for i in xrange(n):
            t = nums[i] + 1000
            c[t] += 1
        a = []
        for i in xrange(1000, 0, -1):
            k = c[i+1000]
            while k > 0:
                k -= 1
                a.append(i)
                if len(a) >= 3:
                    break
        b = []
        b2 = []
        for i in xrange(-1000, 0, 1):
            k = c[i+1000]
            while k > 0:
                k -= 1
                b.append(i)
                if len(b) >= 2:
                    break
            if len(b) >= 2:
                break
        for i in xrange(-1, -1001, -1):
            k = c[i+1000]
            while k > 0:
                k -= 1
                b2.append(i)
                if len(b2) >= 3:
                    break
            if len(b2) >= 3:
                break
        z = c[1000]
        if len(a) >= 3:
            if len(b) >= 2:
                return max(a[0]*a[1]*a[2], a[0]*b[0]*b[1])
            else:
                return a[0]*a[1]*a[2]
        elif len(a) >= 1:
            if len(b) >= 2:
                return a[0]*b[0]*b[1]
            else: # len(b)==1
                if len(a) == 1:
                    return 0
                elif len(a) == 2:
                    return 0
        else:
            if z > 0:
                return 0
            else:
                return b2[0]*b2[1]*b2[2]
