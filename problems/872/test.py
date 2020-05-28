# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#11:42-11:44
def f(x, z):
    if x.left == None and x.right == None:
        z.append(x.val)
        return
    if x.left:
        f(x.left, z)
    if x.right:
        f(x.right, z)
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        z = []
        f(root1, z)
        z2 = []
        f(root2, z2)
        b = True
        if len(z) != len(z2):
            b = False
        else:
            for i in xrange(len(z)):
                if z[i] != z2[i]:
                    b = False
                    break
        return b
