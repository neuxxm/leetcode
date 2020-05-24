# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#9:54-10:10
def h(x):
    if x == None:
        return 0
    r = 1
    if x.left:
        r = h(x.left) + 1
    if x.right:
        t = h(x.right) + 1
        if t > r:
            r = t
    return r
def judge(root):
    return abs(h(root.left) - h(root.right)) <= 1
def f(root):
    if not judge(root):
        return False
    if root.left:
        if not f(root.left):
            return False
    if root.right:
        if not f(root.right):
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
