# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#15:08-15:20
def visit(x, lvl, t):
    if x == None:
        return
    if x.left == None and x.right == None:
        if lvl < t[0]:
            t[0] = lvl
    else:
        visit(x.left, lvl+1, t)
        visit(x.right, lvl+1, t)
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        t = [float('inf')]
        visit(root, 1, t)
        return t[0]
