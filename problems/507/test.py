#14:58-15:05
import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        n = num
        t = int(math.sqrt(n))
        r = 0
        for i in xrange(t, 0, -1):
            if n%i == 0:
                tt = n/i
                if i != tt:
                    if i != 1:
                        r += i + tt
                    else:
                        r += i
                else:
                    r += i
        return r == n
