# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:18-16:21
def f(x, z):
    if x == None:
        return 0
    l = f(x.left, z)
    r = f(x.right, z)
    t = l + r
    if t > z[0]:
        z[0] = t
    return max(l, r) + 1
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        z = [0]
        f(root, z)
        return z[0]
