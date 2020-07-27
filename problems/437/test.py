# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#15:31-16:44
def dfs(x, y, s, z):
    s += x.val
    if x.left:
        dfs(x.left, y, s, z)
    if x.right:
        dfs(x.right, y, s, z)
    if s == y:
        z[0] += 1
def f(x, y, z):
    if x.left:
        f(x.left, y, z)
    if x.right:
        f(x.right, y, z)
    dfs(x, y, 0, z)
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        z = [0]
        f(root, sum, z)
        return z[0]
