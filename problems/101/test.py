# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#19:11-19:13
def f(p, q):
    if p==None and q!=None:
        return False
    if p!=None and q==None:
        return False
    if p == None and q == None:
        return True
    if p.val != q.val:
        return False
    return f(p.left, q.right) and f(p.right, q.left)
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return f(root.left, root.right)
