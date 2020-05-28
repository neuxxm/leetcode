# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#13:24-13:25
def f(x):
    if x.left == None and x.right == None:
        return
    x.left, x.right = x.right, x.left
    if x.left:
        f(x.left)
    if x.right:
        f(x.right)
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        f(root)
        return root
