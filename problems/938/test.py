# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def f(x, l, r, z):
    if x == None:
        return
    t = x.val
    #print t
    if t < l:
        f(x.right, l, r, z)
    elif t > r:
        f(x.left, l, r, z)
    else:
        z[0] += t
        f(x.left, l, r, z)
        f(x.right, l, r, z)
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        z = [0]
        f(root, L, R, z)
        return z[0]
