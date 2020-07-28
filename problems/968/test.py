# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#19:59fail
def f(x, z):
    l = -1
    if x.left:
        l = f(x.left, z)
    r = -1
    if x.right:
        r = f(x.right, z)
    if x.left == None and x.right == None:
        return 0
    if l == 0 or r == 0:
        z[0] += 1
        return 1
    if l == 1 or r == 1:
        return 2
    if l == 2 or r == 2:
        return 0
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        z = [0]
        if f(root, z) == 0:
            z[0] += 1
        return z[0]
