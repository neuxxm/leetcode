# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#11:09-11:15
def f(root, l, r, z):
    if root == None:
        return
    if l<=root.val and root.val<=r:
        z[0] += root.val
    if l < root.val:
        f(root.left, l, r, z)
    if r > root.val:
        f(root.right, l, r, z)
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        z = [0]
        f(root, L, R, z)
        return z[0]
