#21:23-21:25
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        a = arr
        n = len(a)
        m = None
        rs = []
        for i in xrange(n-1, -1, -1):
            if m:
                rs.append(m)
                if a[i] > m:
                    m = a[i]
            else:
                m = a[i]
                rs.append(-1)
        return rs[::-1]
