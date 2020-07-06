#23:30-00:00
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False
        a = nums
        n = len(a)
        map = {}
        list = []
        for i in xrange(n):
            t = a[i]
            if t in map:
                return True
            if len(map) < k:
                map[t] = 1
                list.append(t)
            else:
                x = list.pop(0)
                del map[x]
                map[t] = 1
                list.append(t)
        return False
