# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#23:41-23:45
def f(x, lvl, path, z):
    path[lvl] = x.val
    if x.left == None and x.right == None:
        if sum(path[:lvl+1]) == z:
            return True
        return False
    if x.left:
        if f(x.left, lvl+1, path, z):
            return True
    if x.right:
        if f(x.right, lvl+1, path, z):
            return True
    return False
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        path = [0] * 100005
        return f(root, 0, path, sum)
