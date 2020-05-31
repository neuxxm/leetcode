# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#18:33-18:40
def f(x, y):
    if x == None and y == None:
        return True
    if x and y == None:
        return False
    if x == None and y:
        return False
    if x.val != y.val:
        return False
    if not f(x.left, y.right):
        return False
    if not f(x.right, y.left):
        return False
    return True
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return f(root.left, root.right)
