# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#14:25-14:33
def f(x, lvl, path, z):
    path[lvl] = chr(x.val + ord('a'))
    if x.left == None and x.right == None:
        t = ''.join(path[:lvl+1][::-1])
        if z[0] != None:
            if t < z[0]:
                z[0] = t
        else:
            z[0] = t
        return
    if x.left:
        f(x.left, lvl+1, path, z)
    if x.right:
        f(x.right, lvl+1, path, z)
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ''
        path = [None] * 8505
        z = [None]
        f(root, 0, path, z)
        return z[0]
