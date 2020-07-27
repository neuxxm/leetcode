# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#19:02-19:14
def visit(x):
    if x.left:
        x.left = visit(x.left)
    if x.right:
        x.right = visit(x.right)
    if x.left == None and x.right == None:
        if x.val == 0:
            x = None
    return x
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        root = visit(root)
        return root
