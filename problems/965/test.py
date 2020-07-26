# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#20:00-20:04
def f(x, last):
    if x == None:
        return True
    if last[0]:
        if x.val != last[0]:
            return False
    else:
        last[0] = x.val
    if not f(x.left, last):
        return False
    if not f(x.right, last):
        return False
    return True
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        last = [None]
        return f(root, last)
