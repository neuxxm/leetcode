# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#20:17-20:20
def h(x):
    if x == None:
        return 0
    r = 1
    if x.left:
        r = max(r, h(x.left) + 1)
    if x.right:
        r = max(r, h(x.right) + 1)
    return r
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return h(root)
