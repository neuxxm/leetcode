#14:21fail
def f(x, z):
    if x == None:
        return 0
    l = f(x.left, z)
    r = f(x.right, z)
    s = x.val
    lt = x.val
    if l > 0:
        lt = x.val + l
        s += l
    rt = x.val
    if r > 0:
        rt = x.val + r
        s += r
    if z[0] == None:
        z[0] = s
    elif s > z[0]:
        z[0] = s
    return max(lt, rt)
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        z = [None]
        f(root, z)
        return z[0]
