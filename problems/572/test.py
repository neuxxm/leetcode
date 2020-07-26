# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#19:45-19:52
def check(p, q):
    if p==None and q==None:
        return True
    if p!=None and q==None:
        return False
    if p==None and q!=None:
        return False
    if p.val != q.val:
        return False
    return check(p.left, q.left) and check(p.right, q.right)
def f(s, t):
    if s == None:
        return False
    if check(s, t):
        return True
    if f(s.left, t):
        return True
    if f(s.right, t):
        return True
    return False
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t == None:
            return True
        return f(s, t)
