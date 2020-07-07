# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#11:04-11:08
def f(root, y, lvl, path):
    path[lvl] = root.val
    if root.left == None and root.right == None:
        if sum(path[:lvl+1]) == y:
            return True
        return False
    if root.left:
        if f(root.left, y, lvl+1, path):
            return True
    if root.right:
        if f(root.right, y, lvl+1, path):
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
        path = [0] * 100000
        return f(root, sum, 0, path)
