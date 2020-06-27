#11:23AC
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        a = arr
        n = len(a)/2
        cnt = {}
        for t in a:
            if t in cnt:
                cnt[t] += 1
            else:
                cnt[t] = 1
        z = 0
        r = 0
        for v in sorted(cnt.values(), reverse=True):
            z += v
            r += 1
            if z >= n:
                break
        return r
