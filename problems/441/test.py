#11:29-11:31
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        while True:
            t = k*(k+1)/2
            if t > n:
                break
            k += 1
        return k-1
