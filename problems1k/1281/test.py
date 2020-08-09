#1:37-1:38
def f(n):
    rs = []
    while n != 0:
        rs.append(n%10)
        n /= 10
    t = 1
    t2 = 0
    for r in rs:
        t *= r
        t2 += r
    return t - t2
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        return f(n)
