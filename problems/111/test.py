#8.21 11:20-11:24
def f(x, lvl, z):
    if x == None:
        return 0
    f(x.left, lvl+1, z)
    f(x.right, lvl+1, z)
    if x.left == None and x.right == None:
        t = lvl + 1
        if z[0] != None:
            if t < z[0]:
                z[0] = t
        else:
            z[0] = t
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        z = [None]
        f(root, 0, z)
        return z[0] if z[0] != None else 0
