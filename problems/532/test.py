#22:37-22:40
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        z = set()
        a = nums
        n = len(a)
        map = {}
        for i in xrange(n):
            map[a[i]] = i
        for i in xrange(n):
            t = a[i]
            if t+k in map:
                if i != map[t+k]:
                    z.add((t,t+k))
            if t-k in map:
                if i != map[t-k]:
                    z.add((t-k,t))
        return len(z)
