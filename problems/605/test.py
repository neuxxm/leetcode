#16:58-17:06
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        m = n
        a = flowerbed
        n = len(a)
        if n == 0:
            return False
        if n == 1:
            if a[0] == 0:
                return m <= 1
            else:
                return m == 0
        z = 0
        if a[0] == 0:
            if a[1] == 0:
                a[0] = 1
                z += 1
        if a[n-1] == 0:
            if a[n-2] == 0:
                a[n-1] = 1
                z += 1
        for i in xrange(1, n-1):
            if a[i] == 0:
                if a[i-1]==0 and a[i+1] == 0:
                    a[i] = 1
                    z += 1
        return z >= m
