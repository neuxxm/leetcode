# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#23:16-23:23
def f(x, lvl, path, z):
    path[lvl] = x.val
    if x.left == None and x.right == None:
        buf = ''
        for i in xrange(lvl, -1, -1):
            buf += chr(ord('a')+path[i])
        if z[0] != '':
            if buf < z[0]:
                z[0] = buf
        else:
            z[0] = buf
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
        path = [0] * 8505
        z = ['']
        f(root, 0, path, z)
        return z[0]
