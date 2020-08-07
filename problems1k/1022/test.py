# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#11:59-12:05
def f(x, lvl, path, z):
    if x == None:
        return
    path[lvl] = x.val
    if x.left == None and x.right == None:
        t = 0
        l = 1
        for i in xrange(lvl, -1, -1):
            t += path[i] * l
            l <<= 1
        z[0] += t
        return
    f(x.left, lvl+1, path, z)
    f(x.right, lvl+1, path, z)
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path = [0] * 1005
        z = [0]
        f(root, 0, path, z)
        return z[0]
