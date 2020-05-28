# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#11:08-11:11
def f(x, lvl, path, z, r):
    path[lvl] = x.val
    if x.left == None and x.right == None:
        if sum(path[:lvl+1]) == z:
            r.append(path[:lvl+1])
    if x.left:
        f(x.left, lvl+1, path, z, r)
    if x.right:
        f(x.right, lvl+1, path, z, r)
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        path = [0] * 10005
        r = []
        f(root, 0, path, sum, r)
        return r
