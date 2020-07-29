#23:52-23:55
def f(n):
    z = n
    while n:
        t = n%10
        if t!= 0:
            if z%t != 0:
                return False
        else:
            return False
        n /= 10
    return True
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        z = 0
        rs = []
        for i in xrange(left, right+1):
            if f(i):
                rs.append(i)
        return rs
