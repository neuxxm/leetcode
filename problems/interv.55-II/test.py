# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:17-16:22
def h(x):
    if x == None:
        return 0
    return max(h(x.left), h(x.right)) + 1
def judge(x):
    return abs(h(x.left)-h(x.right)) <= 1
def visit(x):
    if not judge(x):
        return False
    if x.left:
        if not visit(x.left):
            return False
    if x.right:
        if not visit(x.right):
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
        return visit(root)
