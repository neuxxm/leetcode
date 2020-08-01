# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#22:10-22:12
def f(x, z):
    if x == None:
        return
    f(x.left, z)
    z.append(x.val)
    f(x.right, z)
def build(a):
    n = len(a)
    if n == 0:
        return None
    ix = n / 2
    x = TreeNode(a[ix])
    x.left = build(a[:ix])
    x.right = build(a[ix+1:])
    return x
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        z = []
        f(root, z)
        return build(z)
