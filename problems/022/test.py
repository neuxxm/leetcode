#21:39-21:43
def f(left, right, n, path, z):
    if left == n and right == n:
        z.append(path)
        return
    if left < n:
        f(left+1, right, n, path+'(', z)
    if right < left:
        f(left, right+1, n, path+')', z)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        z = []
        f(0, 0, n, '', z)
        return z
