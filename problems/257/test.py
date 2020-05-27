# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#18:28-18:33
def f(x, lvl, path, r):
    path[lvl] = x.val
    if x.left == None and x.right == None:
        buf = '%d'%path[0]
        for i in xrange(1, lvl+1):
            buf += '->%d'%path[i]
        r.append(buf)
        return
    if x.left:
        f(x.left, lvl+1, path, r)
    if x.right:
        f(x.right, lvl+1, path, r)
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        r = []
        path = [0] * 100005
        f(root, 0, path, r)
        return r
