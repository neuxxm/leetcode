# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#17:07-17:09
def f(x, z):
    if x == None:
        return
    f(x.left, z)
    if z[0] != None:
        t = x.val - z[0]
        if t < z[1]:
            z[1] = t
        z[0] = x.val
    else:
        z[0] = x.val
    f(x.right, z)
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        z = [None, float('inf')]
        f(root, z)
        return z[1]
