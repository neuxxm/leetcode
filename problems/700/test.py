# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#17:16-17:17
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        x = root
        if x == None:
            return None
        if x.val == val:
            return x
        if val < x.val:
            return self.searchBST(x.left, val)
        else:
            return self.searchBST(x.right, val)
