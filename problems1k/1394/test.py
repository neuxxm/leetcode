#13:12-13:14
from collections import defaultdict
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        a = arr
        n = len(a)
        map = defaultdict(lambda:0)
        for i in xrange(n):
            map[a[i]] += 1
        ma = None
        for k,v in map.items():
            if k == v:
                if ma:
                    if k > ma:
                        ma = k
                else:
                    ma = k
        return ma if ma != None else -1
