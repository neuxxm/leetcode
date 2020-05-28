# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def get_path(x, lvl, path, p, a):
    path[lvl] = x
    if x.val == p.val:
        a.append(path[:lvl+1])
        return
    if x.left:
        get_path(x.left, lvl+1, path, p, a)
    if x.right:
        get_path(x.right, lvl+1, path, p, a)
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        az = []
        path = [0] * 100005
        get_path(root, 0, path, p, az)
        a = az[0]
        bz = []
        get_path(root, 0, path, q, bz)
        b = bz[0]
        i = 0
        j = 0
        n = len(a)
        m = len(b)
        while i < n and j < m:
            if a[i].val == b[j].val:
                i += 1
                j += 1
            else:
                break
        return a[i-1]
