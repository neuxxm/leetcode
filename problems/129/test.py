# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#23:31-23:34
def f(x, lvl, path, z):
    path[lvl] = x.val
    if x.left == None and x.right == None:
        t = 0
        l = 1
        for i in xrange(lvl, -1, -1):
            t += path[i] * l
            l *= 10
        z[0] += t
        return
    if x.left:
        f(x.left, lvl+1, path, z)
    if x.right:
        f(x.right, lvl+1, path, z)
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        path = [0] * 100005
        z = [0]
        f(root, 0, path, z)
        return z[0]
