# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#19:37-19:43
def f(p1, p2):
    if p1 == None and p2 != None:
        return False
    if p1 != None and p2 == None:
        return False
    if p1 == None and p2 == None:
        return True
    if p1.val != p2.val:
        return False
    if not f(p1.left, p2.right):
        return False
    if not f(p1.right, p2.left):
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
