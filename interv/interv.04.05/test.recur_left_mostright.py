# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:04fail
def is_bst(x):
    if x.left:
        p = x.left
        while p.right:
            p = p.right
        if p.val >= x.val:
            return False
        if not is_bst(x.left):
            return False
    if x.right:
        p = x.right
        while p.left:
            p = p.left
        if p.val <= x.val:
            return False
        if not is_bst(x.right):
            return False
    return True
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return is_bst(root)
