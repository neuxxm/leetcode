# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#20:18-20:21
def f(x, lvl, path, z):
    path[lvl] = x.val
    if x.left:
        f(x.left, lvl+1, path, z)
    if x.right:
        f(x.right, lvl+1, path, z)
    if x.left == None and x.right == None:
        t = '%d'%path[0]
        for i in xrange(1, lvl+1):
            t += '->%d'%path[i]
        z.append(t)
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        path = [0] * 10005
        z = []
        f(root, 0, path, z)
        return z
