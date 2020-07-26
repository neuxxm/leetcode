# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#19:29-19:31
def h(x):
    if x == None:
        return 0
    return max(h(x.left), h(x.right)) + 1
def f(x):
    if x == None:
        return True
    l = h(x.left) + 1
    r = h(x.right) + 1
    if abs(l-r) > 1:
        return False
    return f(x.left) and f(x.right)
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return f(root)
