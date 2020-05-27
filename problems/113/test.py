# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#22:55-23:00
def f(x, lvl, path, z, rs):
    path[lvl] = x.val
    if x.left == None and x.right == None:
        t = path[:lvl+1]
        if sum(t) == z:
            rs.append(t)
        return
    if x.left:
        f(x.left, lvl+1, path, z, rs)
    if x.right:
        f(x.right, lvl+1, path, z, rs)
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
        rs = []
        f(root, 0, path, sum, rs)
        return rs
