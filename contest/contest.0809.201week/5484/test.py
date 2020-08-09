class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return '0'
        l = 0
        r = (1<<n)-2
        k = k -1
        isleft = True
        while l <= r:
            m = (l+r) / 2
            if l+2 == r:
                if k == l:
                    return '0'
                if k == r:
                    return '1'
                if isleft:
                    return '1'
                else:
                    return '0'
            if k == m:
                if isleft:
                    return '1'
                else:
                    return '0'
            if k < m:
                isleft = True
                r = m - 1
            else:
                isleft = False
                l = m + 1
