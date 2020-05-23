# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    ma = float('-inf')
    def f(self, cur):
        if cur.left:
            if not self.f(cur.left):
                return False
        if cur.val > self.ma:
            self.ma = cur.val
        else:
            return False
        if cur.right:
            if not self.f(cur.right):
                return False
        return True
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.f(root)
        else:
            return True
