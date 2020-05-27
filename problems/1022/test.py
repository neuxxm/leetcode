# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#23:06-23:10
def f(x, lvl, path, z):
    path[lvl] = x.val
    if x.left == None and x.right == None:
        l = 1
        t = 0
        for i in xrange(lvl, -1, -1):
            t += path[i] * l
            l <<= 1
        z[0] += t
        z[0] %= 1000000007
        return
    if x.left:
        f(x.left, lvl+1, path, z)
    if x.right:
        f(x.right, lvl+1, path, z)
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        path = [0] * 1005
        z = [0]
        f(root, 0, path, z)
        return z[0]
