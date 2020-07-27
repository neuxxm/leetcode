# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#14:24-14:28
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        x = root
        y = target
        x.left = self.removeLeafNodes(x.left, y)
        x.right = self.removeLeafNodes(x.right, y)
        if x.left == None and x.right == None:
            if x.val == y:
                x = None
                return x
            else:
                return x
        else:
            return x
