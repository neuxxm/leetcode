# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#19:02-19:15
def f(x, y):
    if y == x.val:
        return True
    if y < x.val:
        if x.left and f(x.left, y):
            return True
    else:
        if x.right and f(x.right, y):
            return True
    return False
def visit(x, root, y):
    if x.val*2!= y and f(root, y - x.val):
        return True
    if x.left:
        if visit(x.left, root, y):
            return True
    if x.right:
        if visit(x.right, root, y):
            return True
    return False
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None:
            return False
        return visit(root, root, k)
