# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#23:41-23:42
def h(x):
    if x == None:
        return 0
    r = 1
    if x.left:
        r = max(h(x.left) + 1, r)
    if x.right:
        r = max(h(x.right) + 1, r)
    return r
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return h(root)
