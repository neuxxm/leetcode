# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#14:00-14:14
class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        x = root
        left = self.trimBST(x.left, L, R)
        right = self.trimBST(x.right, L, R)
        if L<=x.val and x.val<=R:
            x.left = left
            x.right = right
            return x
        else:
            if x.val < L:
                x = right
            else:
                x = left
            return x
