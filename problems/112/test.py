# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#14:34-14:41
def f(x, lvl, y, z):
    z += x.val
    if x.left:
        if f(x.left, lvl+1, y, z):
            return True
    if x.right:
        if f(x.right, lvl+1, y, z):
            return True
    if x.left == None and x.right == None:
        return y == z
    return False
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        return f(root, 0, sum, 0)
