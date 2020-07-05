#20:38-20:40
def f(x):
    if x%2 == 0:
        return f(x/2)
    if x%3 == 0:
        return f(x/3)
    if x%5 == 0:
        return f(x/5)
    return x == 1
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        return f(num)
