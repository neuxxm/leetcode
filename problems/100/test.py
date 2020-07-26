# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#18:57-18:59
def f(p, q):
    if p==None and q!=None:
        return False
    if p!=None and q==None:
        return False
    if p==None and q==None:
        return True
    if p.val != q.val:
        return False
    return f(p.left, q.left) and f(p.right, q.right)
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return f(p, q)
