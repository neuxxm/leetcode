#21:32-21:35
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        a = nums
        n = len(a)
        if n == 0:
            return []
        start = a[0]
        i = 1
        r = []
        while i < n:
            if a[i] == a[i-1]+1:
                i += 1
            else:
                end = a[i-1]
                if start != end:
                    r.append('%d->%d'%(start, end))
                else:
                    r.append('%d'%start)
                start = a[i]
                i += 1
        end = a[i-1]
        if start != end:
            r.append('%d->%d'%(start, end))
        else:
            r.append('%d'%start)
        return r
