#0:06-0:07
def f(b, a):
    if a == 1:
        return b
    return b + f(b, a-1)
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        if B < A:
            A, B = B, A
        return f(B, A)
