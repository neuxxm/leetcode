#8.14 19:57-20:01
def f(x, z):
    if x == None:
        return
    if x.left:
        f(x.left, z)
    if z[0] != None:
        t = x.val - z[0]
        if z[1] != None:
            if t < z[1]:
                z[1] = t
        else:
            z[1] = t
        z[0] = x.val
    else:
        z[0] = x.val
    if x.right:
        f(x.right, z)
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        z = [None, None]
        f(root, z)
        return z[1]
