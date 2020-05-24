# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:49-16:51
def f(x, last):
    if x.val != last:
        return False
    if x.left:
        if not f(x.left, last):
            return False
    if x.right:
        if not f(x.right, last):
            return False
    return True
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        last = root.val
        return f(root, last)
