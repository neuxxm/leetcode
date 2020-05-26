# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#19:45-19:53
def f(p, q):
    if p == None and q == None:
        return True
    if p == None and q:
        return False
    if p and q == None:
        return False
    if p.val != q.val:
        return False
    if not f(p.left, q.left):
        return False
    return f(p.right, q.right)
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return f(p, q)
