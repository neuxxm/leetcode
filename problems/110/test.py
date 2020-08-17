# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#12:08-12:11
def h(x):
    if x == None:
        return 0
    return max(h(x.left), h(x.right)) + 1
def f(x):
    if x == None:
        return True
    if f(x.left) == False:
        return False
    if f(x.right) == False:
        return False
    l = h(x.left)
    r = h(x.right)
    if abs(l-r) > 1:
        return False
    return True
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return f(root)
