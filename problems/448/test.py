#16:17-16:43
def f(a, i):
    while True:
        t = a[i]-1
        if t == i:
            return
        if a[t] != t+1:
            a[i], a[t] = a[t], a[i]
            if a[i] == 0:
                return
        else:
            a[i] = 0
            return
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = nums
        n = len(a)
        for i in xrange(n):
            f(a, i)
        r = []
        for i in xrange(n):
            if a[i] == 0:
                r.append(i+1)
        return r
