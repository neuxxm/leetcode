#22:28-22:33
from collections import defaultdict
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        cnt = defaultdict(lambda:0)
        for t in arr1:
            cnt[t] += 1
        r = []
        for t in arr2:
            if t in cnt:
                for k in xrange(cnt[t]):
                    r.append(t)
                del cnt[t]
        for k,v in sorted(cnt.items(),key=lambda fs:fs[0]):
            for x in xrange(v):
                r.append(k)
        return r
