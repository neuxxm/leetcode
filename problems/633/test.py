#14:43-14:48
import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        t = int(math.sqrt(c))
        for i in xrange(t, -1, -1):
            z = i*i
            x = c-z
            tt = int(math.sqrt(x))
            if tt*tt == x:
                return True
        return False
