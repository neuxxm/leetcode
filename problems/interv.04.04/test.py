# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:01-16:17
def h(x):
    if x == None:
        return 0
    r = 1
    if x.left:
        r = max(r, h(x.left)+1)
    if x.right:
        r = max(r, h(x.right)+1)
    return r
def judge(x):
    return abs(h(x.left) - h(x.right)) <= 1
def f(x):
    if not judge(x):
        return False
    if x.left and not f(x.left):
        return False
    if x.right and not f(x.right):
        return False
    return True
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return f(root)
