# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#19:22-19:23
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
