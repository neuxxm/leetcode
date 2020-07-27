# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#15:20-15:23
def f(x, y, lvl, path, z):
    path[lvl] = x.val
    if x.left:
        f(x.left, y, lvl+1, path, z)
    if x.right:
        f(x.right, y, lvl+1, path, z)
    if x.left == None and x.right == None:
        if sum(path[:lvl+1]) == y:
            z.append(path[:lvl+1])
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        path = [0] * 100005
        z = []
        f(root, sum, 0, path, z)
        return z
