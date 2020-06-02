#10:41-10:44
def f(n):
    if n == 1:
        return 1
    return f(n-1) + n
class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return f(n)
