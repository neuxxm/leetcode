#2:16fail
def myabs(x):
    return int(sqrt(x*x))
class Solution(object):
    def maximum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return (myabs(a-b) + a + b) >> 1
