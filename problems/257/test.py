# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#10:39-10:44
def f(x, lvl, path, rs):
    if x == None:
        return
    path[lvl] = x.val
    if x.left == None and x.right == None:
        buf = ''
        for i in xrange(0, lvl+1):
            if i != 0:
                buf += '->'
            buf += '%d'%(path[i])
        rs.append(buf)
        return
    f(x.left, lvl+1, path, rs)
    f(x.right, lvl+1, path, rs)
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        rs = []
        path = [0] * 100005
        f(root, 0, path, rs)
        return rs
