#23:45fail
def f(left, right, path, z):
    if left == 0 and right == 0:
        z.append(path)
        return
    if left > 0:
        f(left-1, right, path+'(', z)
    if left < right:
        f(left, right-1, path+')', z)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        z = []
        f(n, n, '', z)
        return z
