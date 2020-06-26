# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#6.26 20:36-20:44
def f(x, z):
    left = 0
    right = 0
    if x.left:
        left = f(x.left, z)
    if x.right:
        right = f(x.right, z)
    h = 0
    if x.left or x.right:
        h = max(left, right) + 1
        if x.left and x.right:
            t = left + right + 2
        elif x.left:
            t = left + 1
        else:
            t = right + 1
        if t > z[0]:
            z[0] = t
    #print x.val, h, z[0]
    return h
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        z = [0]
        f(root, z)
        return z[0]
