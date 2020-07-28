# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#12:23-12:24
def f(x):
    if x == None:
        return 0
    return max(f(x.left), f(x.right)) + 1
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return f(root)
