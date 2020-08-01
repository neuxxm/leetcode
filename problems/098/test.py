# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:47-16:54
def f(x, z):
    if x == None:
        return True
    if not f(x.left, z):
        return False
    if z[0] != None:
        if x.val <= z[0]:
            return False
        z[0] = x.val
    else:
        z[0] = x.val
    if not f(x.right, z):
        return False
    return True
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        z = [None]
        return f(root, z)
