# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#10:15-10:25
def f(t1, t2):
    r = None
    if t1 != None and t2 != None:
        t = t1.val + t2.val
        r = TreeNode(t)
        r.left = f(t1.left, t2.left)
        r.right = f(t1.right, t2.right)
    elif t1 != None and t2 == None:
        t = t1.val
        r = TreeNode(t)
        r.left = f(t1.left, None)
        r.right = f(t1.right, None)
    elif t2 != None and t1 == None:
        t = t2.val
        r = TreeNode(t)
        r.left = f(t2.left, None)
        r.right = f(t2.right, None)
    return r       
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        r = f(t1, t2)
        return r
