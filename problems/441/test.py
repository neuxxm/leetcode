#11:45-11:47
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        while True:
            t = (k+1)*(k+2)/2
            if t > n:
                return k
            k += 1
