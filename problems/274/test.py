#20:59-21:03
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        a = sorted(citations, reverse=True)
        n = len(a)
        i = 0
        while i < n:
            if a[i] >= i+1:
                i += 1
            else:
                break
        return i
